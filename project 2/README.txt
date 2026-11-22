Due November 22, 2026.

Use Python 3.10+ and a virtual environment:
  python3 -m venv .venv
  source .venv/bin/activate
  python -m pip install -r requirements.txt
On Windows activate .venv\Scripts\activate instead.

Read proj2.pdf before starting. Q1–Q3 use Bitcoin Testnet4 only.
Explorer: https://mempool.space/testnet4/
Faucet: https://coinfaucet.eu/en/btc-testnet4/
Broadcasting: https://mempool.space/testnet4/api/tx
python-bitcoinlib SelectParams('testnet') supplies the shared test-network
key/address encoding. The broadcast endpoint selects Testnet4.

Replace the public demo funding/customer keys with fresh keys before
requesting test coins. Replace all synthetic funding transaction IDs,
indices and example amounts with YOUR verified UTXO details.
Q2/Q3 puzzle scripts are wrapped in P2SH by the supplied infrastructure.

Q4 is offline only, with public demo keys and synthetic funding references.
It needs no faucet, API account, or token. Implement Q4 plus Q1 (which Q4
uses), then run python swap.py with each value of alice_redeems.
broadcast_transactions must stay False.

Submit your code, five transaction IDs in docs/transactions.py, and
completed docs/Q4design_doc.txt. Do not include .venv or caches.
