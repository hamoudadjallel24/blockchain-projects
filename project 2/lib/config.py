from bitcoin import SelectParams
from bitcoin.wallet import CBitcoinSecret, CBitcoinAddress, P2PKHBitcoinAddress
SelectParams('testnet')
network_type = 'btc-test4'
faucet_address = CBitcoinAddress('tb1qerzrlxcfu24davlur5sqmgzzgsal6wusda40er')
# PUBLIC DEMO KEYS: for offline testing only. Replace my_private_key with
# a fresh lib/keygen.py key before requesting coins for Q1-Q3.
# Alice/Bob need no funded keys for the required offline Q4.
my_private_key = CBitcoinSecret.from_secret_bytes((1).to_bytes(32, "big"))
alice_secret_key_BTC = CBitcoinSecret.from_secret_bytes((2).to_bytes(32, "big"))
bob_secret_key_BTC = CBitcoinSecret.from_secret_bytes((3).to_bytes(32, "big"))
alice_secret_key_BCY = CBitcoinSecret.from_secret_bytes((4).to_bytes(32, "big"))
bob_secret_key_BCY = CBitcoinSecret.from_secret_bytes((5).to_bytes(32, "big"))
my_public_key = my_private_key.pub
my_address = P2PKHBitcoinAddress.from_pubkey(my_public_key)
alice_public_key_BTC = alice_secret_key_BTC.pub
alice_address_BTC = P2PKHBitcoinAddress.from_pubkey(alice_public_key_BTC)
bob_public_key_BTC = bob_secret_key_BTC.pub
bob_address_BTC = P2PKHBitcoinAddress.from_pubkey(bob_public_key_BTC)
alice_public_key_BCY = alice_secret_key_BCY.pub
alice_address_BCY = P2PKHBitcoinAddress.from_pubkey(alice_public_key_BCY)
bob_public_key_BCY = bob_secret_key_BCY.pub
bob_address_BCY = P2PKHBitcoinAddress.from_pubkey(bob_public_key_BCY)
