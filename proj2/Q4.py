from bitcoin.core.script import *

######################################################################
# These functions will be used by Alice and Bob to send their respective
# coins to a utxo that is redeemable either of two cases:
# 1) Recipient provides x such that hash(x) = hash of secret
#    and recipient signs the transaction.
# 2) Sender and recipient both sign transaction
#
# TODO: Fill these in to create scripts that are redeemable by both
#       of the above conditions.
# See this page for opcode documentation: https://en.bitcoin.it/wiki/Script

# This is the ScriptPubKey for the swap transaction
def coinExchangeScript(public_key_sender, public_key_recipient, hash_of_secret):
    raise NotImplementedError("TODO: atomic swap script")

# This is the ScriptSig that the receiver will use to redeem coins
def coinExchangeScriptSig1(sig_recipient, secret):
    raise NotImplementedError("TODO: atomic swap script")

# This is the ScriptSig for sending coins back to the sender if unredeemed
def coinExchangeScriptSig2(sig_sender, sig_recipient):
    raise NotImplementedError("TODO: atomic swap script")
######################################################################

######################################################################
#
# Configured for your addresses
#
# TODO: Fill in all of these fields
#

alice_txid_to_spend     = "0000000000000000000000000000000000000000000000000000000000000000"
alice_utxo_index        = 0
alice_amount_to_send    = 0.00166892

bob_txid_to_spend       = "0000000000000000000000000000000000000000000000000000000000000000"
bob_utxo_index          = 0
bob_amount_to_send      = 0.00124875

# Get current block height (for locktime) in 'height' parameter for each blockchain (will be used in swap.py):
#  curl https://mempool.space/testnet4/api/blocks/tip/height
btc_chain_height  = 1835704

#  curl https://api.blockcypher.com/v1/bcy/test
bcy_test_chain_height   = 3056145

# Parameter for how long Alice/Bob should have to wait before they can take back their coins
# alice_locktime MUST be > bob_locktime
alice_locktime = 5
bob_locktime = 3

tx_fee = 0.00001

# While testing your code, you can edit these variables to see if your
# transaction can be broadcasted succesfully.
broadcast_transactions = False
alice_redeems = False

######################################################################
