use cryptopals::{hex_to_b64, hex_to_str};

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
