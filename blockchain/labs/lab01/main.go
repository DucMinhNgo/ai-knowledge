package main

import (
	"encoding/json"
	"fmt"
	bc "lab01/blockchain"
	"time"
)

func main() {
	firstBlock := bc.Block{
		Timestamp:     time.Now().Unix(),
		Transactions:  []*bc.Transaction{{Data: []byte("Genesis Transaction")}},
		PrevBlockHash: []byte{},
		Hash:          []byte{},
	}
	firstBlock.Hash = bc.CalculateHash(firstBlock.Timestamp, firstBlock.Transactions, firstBlock.PrevBlockHash)

	var Blockchain []bc.Block
	Blockchain = append(Blockchain, firstBlock)

	for i := 1; i < 5; i++ {
		newTransactions := []*bc.Transaction{{Data: []byte(fmt.Sprintf("Transaction #%d", i))}}
		newBlock := bc.GenerateBlock(Blockchain[len(Blockchain)-1], newTransactions)
		if bc.IsBlockValid(newBlock, Blockchain[len(Blockchain)-1]) {
			Blockchain = append(Blockchain, newBlock)
			fmt.Printf("Block #%d has been added to the Blockchain!\n", newBlock.Timestamp)
		}
	}

	blockchainJSON, _ := json.MarshalIndent(Blockchain, "", "  ")
	fmt.Printf("Blockchain:\n%s\n", blockchainJSON)
}
