from bitcoin import SelectParams
from bitcoin.wallet import CBitcoinSecret, CBitcoinAddress
from bitcoin.core import CTransaction, CScript, Hash, b2x, CTxIn, CTxOut, COutPoint
from bitcoin.core.script import SIGHASH_ALL
from binascii import unhexlify

# Initialize Bitcoin parameters
SelectParams('testnet')

def create_signed_transaction(txins, txouts, private_keys):
    """Creates a signed Bitcoin transaction."""

    # Create the unsigned transaction
    tx = CTransaction()
    tx.vin = txins
    tx.vout = txouts

    # Sign each input
    for i, txin in enumerate(txins):
        # Get the private key for this input
        private_key = CBitcoinSecret(private_keys[i])

        # Create a signature hash for this input
        sighash = tx.signature_hash(i, private_key.pub, SIGHASH_ALL)

        # Sign the hash using the private key
        signature = private_key.sign(sighash) + bytes([SIGHASH_ALL])

        # Create a new CTxIn object with the updated scriptSig
        new_txin = CTxIn(
            prevout=txin.prevout,
            scriptSig=CScript([signature, private_key.pub]),
            sequence=txin.sequence
        )

        # Create a new CTransaction object with the modified vin list
        new_tx = CTransaction(tx.vin[:i] + [new_txin] + tx.vin[i+1:], tx.vout)
        tx = new_tx  # Replace the existing tx with the new one

    # Serialize the transaction
    return b2x(tx.serialize())

# Define the UTXO information
utxo_txid = 'a319b44c6f2dd88f1f4acc5670762f9c5ec65dc45f223f4a40ca23657b73756e'
utxo_index = 0
utxo_value = 500000000  # Value of the UTXO in satoshis

# Create a transaction input (UTXO)
txin = CTxIn(COutPoint(Hash(unhexlify(utxo_txid))[::-1], utxo_index))

# Specify the recipient's Bitcoin address and the amount to send
recipient_address = 'mv4rnyY3Su5gjcDNzbMLKBQkBicCtHUtFB'
amount_to_send = 0.00395847  # Amount to send in satoshis

# Create a transaction output (TxOut)
txout = CTxOut(amount_to_send, CBitcoinAddress(recipient_address).to_scriptPubKey())

# Specify the private key corresponding to the UTXO
private_key = 'cSz37ppyonDHANjpv6pziLPKYEKXEiGrCLKRyqwLqkiTs2aZQKgx'

# Create and sign the transaction
signed_transaction = create_signed_transaction([txin], [txout], [private_key])

# Print the raw serialized signed transaction
print("Signed Transaction:")
print(b2x(signed_transaction))  # Directly serialize the returned tx object
