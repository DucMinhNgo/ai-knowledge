package main

import (
	"fmt"
	bc "lab01/blockchain"
)

func main() {
	// Create a new blockchain
	blockchain := bc.NewBlockchain()

	// Add some transactions
	transactions1 := []*bc.Transaction{
		{ID: "1", Data: []byte("Transaction 1")},
		{ID: "2", Data: []byte("Transaction 2")},
	}
	blockchain.AddBlock(transactions1)

	transactions2 := []*bc.Transaction{
		{ID: "3", Data: []byte("Transaction 3")},
		{ID: "4", Data: []byte("Transaction 4")},
	}
	blockchain.AddBlock(transactions2)

	// Print the blockchain
	blockchain.PrintBlockchain()

	txIDToCheck := "1"
	if blockchain.TransactionExists(txIDToCheck) {
		fmt.Printf("Transaction with ID %s exists in the blockchain.\n", txIDToCheck)
	} else {
		fmt.Printf("Transaction with ID %s does not exist in the blockchain.\n", txIDToCheck)
	}
}
