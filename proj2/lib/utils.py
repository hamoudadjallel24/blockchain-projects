import requests
from decimal import Decimal, ROUND_HALF_UP

from bitcoin.core import b2x, lx, COIN, COutPoint, CMutableTxOut, CMutableTxIn, CMutableTransaction, Hash160
from bitcoin.core.script import CScript, SignatureHash, SIGHASH_ALL, OP_HASH160, OP_EQUAL
from bitcoin.core.scripteval import VerifyScript, SCRIPT_VERIFY_P2SH

def send_from_custom_transaction(
        amount_to_send, txid_to_spend, utxo_index,
        txin_scriptPubKey, txin_scriptSig, txout_scriptPubKey, network):
    txout = create_txout(amount_to_send, txout_scriptPubKey)
    txin = create_txin(txid_to_spend, utxo_index)
    new_tx = create_signed_transaction(txin, txout, txin_scriptPubKey,
                                       txin_scriptSig, p2sh=True)
    return broadcast_transaction(new_tx, network)

def create_txin(txid, utxo_index):
    return CMutableTxIn(COutPoint(lx(txid), utxo_index))

def to_satoshis(amount):
    # Round float subtraction artifacts; never truncate a satoshi.
    value = Decimal(str(amount)) * COIN
    if not value.is_finite() or value <= 0:
        raise ValueError("Amount must be positive and finite")
    nearest = value.to_integral_value(rounding=ROUND_HALF_UP)
    if abs(value - nearest) > Decimal("0.000001"):
        raise ValueError("Amount must be a whole number of satoshis")
    return int(nearest)

def create_txout(amount, scriptPubKey):
    return CMutableTxOut(to_satoshis(amount), CScript(scriptPubKey))

def create_OP_CHECKSIG_signature(txin, txout, txin_scriptPubKey, seckey):
    tx = CMutableTransaction([txin], [txout])
    sighash = SignatureHash(CScript(txin_scriptPubKey), tx,
                            0, SIGHASH_ALL)
    sig = seckey.sign(sighash) + bytes([SIGHASH_ALL])
    return sig

def P2SH_scriptPubKey(redeem_script):
    script = CScript(redeem_script)
    if not script:
        raise ValueError("Complete the redeem script before funding it")
    return [OP_HASH160, Hash160(script), OP_EQUAL]

def create_signed_transaction(txin, txout, txin_scriptPubKey,
                              txin_scriptSig, p2sh=False):
    tx = CMutableTransaction([txin], [txout])
    if p2sh:
        txin.scriptSig = CScript(list(txin_scriptSig) + [bytes(CScript(txin_scriptPubKey))])
        locking_script = CScript(P2SH_scriptPubKey(txin_scriptPubKey))
    else:
        txin.scriptSig = CScript(txin_scriptSig)
        locking_script = CScript(txin_scriptPubKey)
    VerifyScript(txin.scriptSig, locking_script,
                 tx, 0, (SCRIPT_VERIFY_P2SH,))
    return tx

def broadcast_transaction(tx, network):
    if network == 'btc-test4':
        url = 'https://mempool.space/testnet4/api/tx'
    elif network == 'bcy-test':
        url = 'https://api.blockcypher.com/v1/bcy/test/txs/push'
    else:
      raise ValueError("Network must be one of either 'btc-test4', 'bcy-test'")

    raw_transaction = b2x(tx.serialize())
    if network == "btc-test4":
        response = requests.post(url, data=raw_transaction,
                                 headers={"Content-Type": "text/plain"}, timeout=30)
    else:
        response = requests.post(url, json={"tx": raw_transaction}, timeout=30)
    response.raise_for_status()
    if network == "bcy-test" and "error" in response.json():
        raise ValueError(response.json()["error"])
    return response
