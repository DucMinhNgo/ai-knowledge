package blockchain

import (
	"bytes"
	"crypto/sha256"
	"fmt"
	"time"
)

// Transaction represents a transaction in the blockchain.
type Transaction struct {
	ID   string
	Data []byte
}

// Block represents a block in the blockchain.
type Block struct {
	Timestamp     int64
	Transactions  []*Transaction
	PrevBlockHash []byte
	MerkleRoot    []byte
	Hash          []byte
}

// Blockchain represents the entire blockchain.
// []*Block allow modified data
type Blockchain struct {
	blocks []*Block
}

// CalculateHash calculates the hash of a block.
// %d: base 10 (integer)
// %x: base 16, with lower-case letters for a-f (integer)
// ----------------------------------------------------------------
// hash[:]: hash[:] is a slice of bytes ([]byte) created from the array hash.
// It represents the same data as the original array, but in a more flexible slice form.
// This is often more convenient for passing around and working with in Go, especially when interacting with other functions or libraries
func (b *Block) CalculateHash() []byte {
	data := fmt.Sprintf("%d%x%x%x", b.Timestamp, b.Transactions, b.PrevBlockHash, b.MerkleRoot)
	hash := sha256.Sum256([]byte(data))
	return hash[:]
}

// CalculateMerkleRoot calculates the Merkle root of a list of transactions.
func CalculateMerkleRoot(transactions []*Transaction) []byte {
	var hashes [][]byte

	// Convert transactions into hash bytes
	for _, tx := range transactions {
		hash := sha256.Sum256(tx.Data)
		hashes = append(hashes, hash[:])
	}

	// Build the Merkle tree
	for len(hashes) > 1 {
		var levelHashes [][]byte

		// Combine adjacent hashes
		for i := 0; i < len(hashes); i += 2 {
			var hashPair []byte
			if i+1 < len(hashes) {
				hashPair = append(hashes[i], hashes[i+1]...)
			} else {
				hashPair = append(hashes[i], hashes[i]...)
			}
			hash := sha256.Sum256(hashPair)
			levelHashes = append(levelHashes, hash[:])
		}

		hashes = levelHashes
	}

	if len(hashes) == 1 {
		return hashes[0]
	}

	return nil
}

// NewBlock creates a new block in the blockchain.
func NewBlock(transactions []*Transaction, prevHash []byte) *Block {
	merkleRoot := CalculateMerkleRoot(transactions)
	block := &Block{
		Timestamp:     time.Now().Unix(),
		Transactions:  transactions,
		PrevBlockHash: prevHash,
		MerkleRoot:    merkleRoot,
	}
	block.Hash = block.CalculateHash()
	return block
}

// NewBlockchain creates a new blockchain with a genesis block.
func NewBlockchain() *Blockchain {
	genesisBlock := NewBlock([]*Transaction{{Data: []byte("Block")}}, nil)
	return &Blockchain{blocks: []*Block{genesisBlock}}
}

// AddBlock adds a new block to the blockchain.
func (bc *Blockchain) AddBlock(transactions []*Transaction) {
	prevBlock := bc.blocks[len(bc.blocks)-1]
	newBlock := NewBlock(transactions, prevBlock.Hash)
	bc.blocks = append(bc.blocks, newBlock)
}

// PrintBlockchain prints the blocks in the blockchain.
func (bc *Blockchain) PrintBlockchain() {
	for _, block := range bc.blocks {
		fmt.Printf("Timestamp: %d\n", block.Timestamp)
		fmt.Printf("Prev BlockHash: %x\n", block.PrevBlockHash)
		fmt.Printf("Merkle Root: %x\n", block.MerkleRoot)
		fmt.Printf("Hash: %x\n", block.Hash)
		fmt.Println("Transactions:")
		for _, tx := range block.Transactions {
			fmt.Printf("ID: %s, Data: %s\n", tx.ID, string(tx.Data))
		}
		fmt.Println()
	}
}

// VerifyTransactionInMerkleTree checks if a transaction with a given ID is included in the Merkle tree.
func VerifyTransactionInMerkleTree(merkleRoot []byte, transactions []*Transaction) bool {
	// Convert the transaction ID to bytes
	// txIDBytes := []byte(txID)

	// Calculate the Merkle root of the transactions
	calculatedMerkleRoot := CalculateMerkleRoot(transactions)

	fmt.Println(calculatedMerkleRoot)
	fmt.Println(merkleRoot)

	// Check if the calculated Merkle root matches the expected Merkle root
	return bytes.Equal(calculatedMerkleRoot, merkleRoot)
}

// TransactionExists checks whether a transaction with a given ID exists in the block.
func (b *Block) TransactionExists(txID string) bool {
	// Calculate the Merkle root of the block's transactions
	merkleRoot := CalculateMerkleRoot(b.Transactions)

	// Iterate through each transaction in the block
	for _, tx := range b.Transactions {
		// Check if the transaction ID matches the target ID
		if tx.ID == txID {
			// Verify the transaction's inclusion in the Merkle tree
			return VerifyTransactionInMerkleTree(merkleRoot, b.Transactions)
		}
	}

	return false
}

// TransactionExists checks whether a transaction with a given ID exists in the blockchain.
func (bc *Blockchain) TransactionExists(txID string) bool {
	// Iterate through each block in the blockchain
	for _, block := range bc.blocks {
		// Check if the transaction ID exists in the current block's transactions
		if txExists := block.TransactionExists(txID); txExists {
			return true
		}
	}
	return false
}
