use cryptopals::{
    hex_to_b64,
    hex_to_str,
    xor_two_str,
    str_to_hex
};

#[test]
fn test_hex_to_b64() {
    let input = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d";
    let output = hex_to_b64(input);
    assert!(output == "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t");
}

#[test]
fn test_hex_to_str() {
    let input = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d";
    let output = hex_to_str(input);
    assert!(output == "I'm killing your brain like a poisonous mushroom");
}

#[test]
fn test_hex_two_str() {
    let xored_str = xor_two_str(
        "1c0111001f010100061a024b53535009181c",
        "686974207468652062756c6c277320657965"
    );

    assert!(xored_str == "the kid don't play");
}
#[test]
fn test_str_to_hex() {
    let hex_str = str_to_hex("the kid don't play");

    assert!(hex_str == "746865206b696420646f6e277420706c6179");
}

