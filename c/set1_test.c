#include "set1.c"
#include <assert.h>
#include <stdio.h>

void test_challange1(){
	printf("Testing the first challange : ");
	assert(hex_to_b64("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d") == "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t");
	printf(" Pass !\n");
}

int main(){

	test_challange1();

    return 0;
}
