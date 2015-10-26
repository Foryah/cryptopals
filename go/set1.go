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

// paddKey Used internaly to expand a key so it can have the same len
// 		   as the string with which it will be xor'ed
func paddKey(key string, val int) string {
	if len(key) == val {
		return key
	}

	paddedKey := []byte{}
	i := 0
	for len(paddedKey) < val {
		paddedKey = append(paddedKey, key[i])

		if i < len(key)-1 {
			i++
		} else {
			i = 0
		}
	}

	return string(paddedKey)
}

// GetAllOneLetterHexXor will return an array with all xor's between the
// 						 encodedString and all the utf-8 characters
func GetAllOneLetterHexXor(encodedString string) []string {
	result := []string{}

	for i := 0; i < 256; i++ {
		result = append(result, HToS(HeXor(encodedString, paddKey(SToH(string(i)), len(encodedString)))))
	}

	return result
}

// GetScore returns an "score" based on the probability of the english language
// 13 9 8 8 7 7 7 6 6 4 4 3 3 3 3 2 2 2 1 1 1 - - - - -
//  E T A O N I R S H L D C U P F M W Y B G V K Q X J Z
func GetScore(str string) int {
	probTable := map[uint8]int{
		"e"[0]: 13, "E"[0]: 13,
		"t"[0]: 9, "T"[0]: 9,
		"a"[0]: 8, "A"[0]: 8,
		"o"[0]: 8, "O"[0]: 8,
		"n"[0]: 7, "N"[0]: 7,
		"i"[0]: 7, "I"[0]: 7,
		"r"[0]: 7, "R"[0]: 7,
		"s"[0]: 6, "S"[0]: 6,
		"h"[0]: 6, "H"[0]: 6,
		"l"[0]: 4, "L"[0]: 4,
		"d"[0]: 4, "D"[0]: 4,
		"c"[0]: 3, "C"[0]: 3,
		"u"[0]: 3, "U"[0]: 3,
		"p"[0]: 3, "P"[0]: 3,
		"f"[0]: 3, "F"[0]: 3,
		"m"[0]: 2, "M"[0]: 2,
		"w"[0]: 2, "W"[0]: 2,
		"y"[0]: 2, "Y"[0]: 2,
		"b"[0]: 1, "B"[0]: 1,
		"g"[0]: 1, "G"[0]: 1,
		"v"[0]: 1, "V"[0]: 1,
		" "[0]: 4,
	}

	score := 0
	for i := range str {
		score += probTable[str[i]]
	}

	return score
}

// GetBestEnglishMatch will return the best match based on a probability
func GetBestEnglishMatch(results []string) string {
	max := 0
	str := ""
	score := 0

	for _, result := range results {
		score = GetScore(result)

		if score > max {
			max = score
			str = result
		}
	}

	return str
}
