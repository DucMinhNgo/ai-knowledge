package blockchain

import (
	"bytes"
	"crypto/sha256"
	"fmt"
	"time"
)

type Transaction struct {
	Data []byte
}

type Block struct {
	Timestamp     int64
	Transactions  []*Transaction
	PrevBlockHash []byte
	Hash          []byte
}

func CalculateHash(timestamp int64, transactions []*Transaction, prevBlockHash []byte) []byte {
	value := fmt.Sprintf("%d%v%x", timestamp, transactions, prevBlockHash)
	hashInBytes := sha256.Sum256([]byte(value))
	return hashInBytes[:]
}

func GenerateBlock(oldBlock Block, transactions []*Transaction) Block {
	var newBlock Block

	newBlock.Timestamp = time.Now().Unix()
	newBlock.Transactions = transactions
	newBlock.PrevBlockHash = oldBlock.Hash
	newBlock.Hash = CalculateHash(newBlock.Timestamp, newBlock.Transactions, newBlock.PrevBlockHash)

	return newBlock
}

func IsBlockValid(newBlock, oldBlock Block) bool {
	if oldBlock.Timestamp > newBlock.Timestamp {
		return false
	}

	if !bytes.Equal(oldBlock.Hash, newBlock.PrevBlockHash) {
		return false
	}

	if !bytes.Equal(CalculateHash(newBlock.Timestamp, newBlock.Transactions, newBlock.PrevBlockHash), newBlock.Hash) {
		return false
	}

	return true
}
