package main

import (
	"bytes"
	"crypto/sha256"
	"fmt"
	"time"
)

func Str2Bytes(str string) []byte {
	return []byte(str)
}

func Bytes2Str(b []byte) string {
	return string(b)
}

func ByteFunS2() {
	data := [][]byte{[]byte("an"), []byte("old"), []byte("wolf")}
	joined := bytes.Join(data, []byte(" "))

	fmt.Println(data)
	fmt.Println(joined)
	fmt.Println(string(joined))

	fmt.Println("--------------------------")

	data2 := []byte{102, 97, 108, 99, 111, 110, 32}
	fmt.Println(data2)
	fmt.Println(string(data2))
	fmt.Println(string(bytes.Repeat(data2, 5)))

	fmt.Println("--------------------------")
	data4 := []byte{32, 32, 102, 97, 108, 99, 111, 110, 32, 32, 32}
	fmt.Println(string(data4))
	fmt.Println(string(bytes.Trim(data4, " ")))
}

func BufferFunc() {
	var buf bytes.Buffer

	buf.Write([]byte("a old"))
	buf.WriteByte(32)
	buf.Write([]byte(" a"))
	buf.WriteString(" Dustin ")
	buf.Write([]byte("Dustin "))
	buf.WriteRune('🌵')
	fmt.Println(buf.String())
}

type Block struct {
	ID   int
	Data string
}

func BlockAndBlockStar() {
	// Using []*Block (slice of pointers to Block)
	blocksWithPointers := []*Block{
		{ID: 1, Data: "Block 1"},
		{ID: 2, Data: "Block 2"},
	}

	blockPointer := blocksWithPointers[0]
	blockPointer.Data = "Modified Block 1"
	for _, data := range blocksWithPointers {
		fmt.Println(data.Data)
	}

	blocksWithoutPointers := []Block{
		{ID: 1, Data: "Block 1"},
		{ID: 2, Data: "Block 2"},
	}
	blockWithoutPointer := blocksWithoutPointers[0]
	blockWithoutPointer.Data = "Modified Block 1"

	fmt.Println(blockWithoutPointer)
	for _, data := range blocksWithoutPointers {
		fmt.Println(data.Data)
	}
}

func main() {
	// b := Str2Bytes("Welcome to")
	// fmt.Println(b)
	// fmt.Println(Bytes2Str(b))
	// fmt.Println(string([]byte{87, 101, 108, 99, 111, 109, 101, 32, 116, 111}))

	// ByteFunS2()

	// BufferFunc()
	// BlockAndBlockStar()

	hash := sha256.Sum256([]byte("hello world\n"))
	// Print hash
	fmt.Printf("hash: %x\n", hash)

	// Print hash[:] (slice representation)
	fmt.Printf("hash[:]: %x\n", hash[:])

	// primes := [][]byte{[]byte("1"), []byte("2"), []byte("3"), []byte("4"), []byte("5"), []byte("6")}
	// a := [][]byte{}

	// append(a, primes[1]...)

	// Create two slices
	slice1 := []byte{1, 2, 3}
	slice2 := []byte{4, 5, 6}

	// Combine the slices into a new slice
	combinedSlice := append(slice1, slice2...)

	// Print the result
	fmt.Println(combinedSlice) // Output: [1 2 3 4 5 6]
	fmt.Println(time.Now().Unix())
}
