package blockchain

import (
	"crypto/sha256"
	"fmt"
	"time"
)

// Transaction represents a transaction in the blockchain.
type Transaction struct {
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
type Blockchain struct {
	blocks []*Block
}

// CalculateHash calculates the hash of a block.
func (b *Block) CalculateHash() []byte {
	data := fmt.Sprintf("%d%d%x%x%x", b.Timestamp, b.Transactions, b.PrevBlockHash, b.MerkleRoot)
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
			fmt.Printf("Data: %s\n", string(tx.Data))
		}
		fmt.Println()
	}
}
