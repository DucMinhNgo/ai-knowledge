# Spend Locked Funds
from bitcoin import *
from bitcoin.wallet import CBitcoinSecret, P2PKHBitcoinAddress
from binascii import unhexlify

bitcoin.SelectParams('testnet')

def create_signed_transaction(txins, txouts, private_keys):
    """Creates a signed Bitcoin transaction.

    Args:
        txins: A list of transaction inputs (CTxIn objects).
        txouts: A list of transaction outputs (CTxOut objects).
        private_keys: A list of private keys corresponding to the input addresses.

    Returns:
        The raw serialized signed transaction as a bytes object.
    """

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

        # Set the scriptSig for this input
        txin.scriptSig = CScript([signature, private_key.pub])

    # Serialize the transaction
    return b2x(tx.serialize())

# Private key and Bitcoin address from the previous step
private_key = 'cSz37ppyonDHANjpv6pziLPKYEKXEiGrCLKRyqwLqkiTs2aZQKgx'
address = 'mjMtakiboBU17oVbvqFEmu6A1Vxq5AvELi'
# Create a transaction input (UTXO)
txid = 'a319b44c6f2dd88f1f4acc5670762f9c5ec65dc45f223f4a40ca23657b73756e'  # Transaction ID of the UTXO you want to spend
output_index = 0  # Index of the output in the transaction

def create_txin(utxo_txid, utxo_index):
    # Create a transaction input (TxIn) using the UTXO information
    txin = {
        "txid": unhexlify(utxo_txid)[::-1],  # Convert the hex string to bytes and reverse the byte order
        "vout": utxo_index,
        "scriptSig": "",  # Placeholder for the unlocking script (signature)
        "sequence": 0xFFFFFFFF,  # Use 0xFFFFFFFF for the default sequence number
    }
    return txin

def create_txout(amount_to_send, destination_address):
    # Create a transaction output (TxOut)
    txout = {
        "scriptPubKey": P2PKHBitcoinAddress(destination_address).to_scriptPubKey(),
        "value": amount_to_send,
    } 
    return txout
txin = create_txin(txid, output_index)
# Create a transaction output to the desired destination
destination_address = 'mv4rnyY3Su5gjcDNzbMLKBQkBicCtHUtFB'  # Recipient’s address
amount_to_send = 0.00395847  # Amount to send in satoshis
txout = create_txout(amount_to_send, destination_address)

print (txin)
print (txout)
print (private_key)

# Create the transaction
tx = create_signed_transaction([txin], [txout], [private_key])
# Broadcast the transaction
# broadcast_tx(tx)