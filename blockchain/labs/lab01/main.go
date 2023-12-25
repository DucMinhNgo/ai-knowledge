package main

import (
	bc "lab01/blockchain"
)

func main() {
	// Create a new blockchain
	blockchain := bc.NewBlockchain()

	// Add some transactions
	transactions1 := []*bc.Transaction{
		{Data: []byte("Transaction 1")},
		{Data: []byte("Transaction 2")},
	}
	blockchain.AddBlock(transactions1)

	transactions2 := []*bc.Transaction{
		{Data: []byte("Transaction 3")},
		{Data: []byte("Transaction 4")},
	}
	blockchain.AddBlock(transactions2)

	// Print the blockchain
	blockchain.PrintBlockchain()
}
