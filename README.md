# Blockchain
Simple Blockchain Creation.

This Python script creates a Blockchain of the length that the user desires. 
Each block in the blockchain consists of the following:
- Previous hash
- Current hash
- Data
- Nonce

I created hashes using the sha256 Python package, and the blockchain runs a validation method to ensure that the entire chain is valid.
The difficulty of the blockchain is adjustable (higher difficulty --> more difficult to mine a new block).
