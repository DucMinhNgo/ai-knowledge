package main

import (
	"bytes"
	"crypto/sha256"
	"encoding/json"
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

func calculateHash(timestamp int64, transactions []*Transaction, prevBlockHash []byte) []byte {
	value := fmt.Sprintf("%d%v%x", timestamp, transactions, prevBlockHash)
	hashInBytes := sha256.Sum256([]byte(value))
	return hashInBytes[:]
}

func generateBlock(oldBlock Block, transactions []*Transaction) Block {
	var newBlock Block

	newBlock.Timestamp = time.Now().Unix()
	newBlock.Transactions = transactions
	newBlock.PrevBlockHash = oldBlock.Hash
	newBlock.Hash = calculateHash(newBlock.Timestamp, newBlock.Transactions, newBlock.PrevBlockHash)

	return newBlock
}

func isBlockValid(newBlock, oldBlock Block) bool {
	if oldBlock.Timestamp > newBlock.Timestamp {
		return false
	}

	if !bytes.Equal(oldBlock.Hash, newBlock.PrevBlockHash) {
		return false
	}

	if !bytes.Equal(calculateHash(newBlock.Timestamp, newBlock.Transactions, newBlock.PrevBlockHash), newBlock.Hash) {
		return false
	}

	return true
}

func main() {
	firstBlock := Block{
		Timestamp:     time.Now().Unix(),
		Transactions:  []*Transaction{{Data: []byte("Genesis Transaction")}},
		PrevBlockHash: []byte{},
		Hash:          []byte{},
	}
	firstBlock.Hash = calculateHash(firstBlock.Timestamp, firstBlock.Transactions, firstBlock.PrevBlockHash)

	var Blockchain []Block
	Blockchain = append(Blockchain, firstBlock)

	for i := 1; i < 5; i++ {
		newTransactions := []*Transaction{{Data: []byte(fmt.Sprintf("Transaction #%d", i))}}
		newBlock := generateBlock(Blockchain[len(Blockchain)-1], newTransactions)
		if isBlockValid(newBlock, Blockchain[len(Blockchain)-1]) {
			Blockchain = append(Blockchain, newBlock)
			fmt.Printf("Block #%d has been added to the Blockchain!\n", newBlock.Timestamp)
		}
	}

	blockchainJSON, _ := json.MarshalIndent(Blockchain, "", "  ")
	fmt.Printf("Blockchain:\n%s\n", blockchainJSON)
}
