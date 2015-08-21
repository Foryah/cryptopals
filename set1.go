package main

import (
	"encoding/base64"
	"encoding/hex"
	"fmt"
)

// HToS Converts a hexa string to a utf-8 string
func HToS(hexString string) string {
	bytes, err := hex.DecodeString(hexString)
	if err != nil {
		fmt.Println(err.Error())
	}

	return string(bytes)
}

// STo64 Converts a uft-8 string to a base64 string
func STo64(utfString string) string {
	return base64.StdEncoding.EncodeToString([]byte(utfString))
}

// SToH Converts a utf-8 string to a hexa string
func SToH(utfString string) string {
	return hex.EncodeToString([]byte(utfString))
}

// HTo64 Converts a hexa string to a base64 string
func HTo64(hexString string) string {
	return STo64(HToS(hexString))
}

// HeXor Returnes the xor between two hexa strings as a hexa string
func HeXor(first, second string) string {
	result := []byte{}
	first = HToS(first)
	second = HToS(second)

	for i := range first {
		result = append(result, first[i]^second[i])
	}

	return SToH(string(result))
}
