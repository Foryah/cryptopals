package main

import (
	"testing"
)

func TestChall1(t *testing.T) {
	if HTo64("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d") != "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t" {
		t.Error("YOU SHALL NOT PASS !")
	}
}

func TestChall2(t *testing.T) {
	if HeXor("1c0111001f010100061a024b53535009181c", "686974207468652062756c6c277320657965") != "746865206b696420646f6e277420706c6179" {
		t.Error("YOU SHALL NOT PASS !")
	}
}

func TestChall3(t *testing.T) {
	if GetBestEnglishMatch(GetAllOneLetterHexXor("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736")) != "Cooking MC's like a pound of bacon" {
		t.Error("YOU SHALL NOT PASS !")
	}

}
