mod lib;

use lib::{
    hex_to_b64,
    hex_to_str,
    xor_two_str,
    str_to_hex
};

fn chal1() {
    println!("\nChallenge 1");
    println!("------------------------------------");
    let b64_str = hex_to_b64("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d");
    let ascii_str = hex_to_str("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d");
    println!("B64\t\t{}", b64_str);
    println!("Ascii\t\t{}", ascii_str);
    println!("------------------------------------");
}

fn chal2() {
    println!("\nChallenge 2");
    println!("------------------------------------");
    let xored_str = xor_two_str("1c0111001f010100061a024b53535009181c", "686974207468652062756c6c277320657965");
    let hex_str = str_to_hex(&xored_str[..]);
    println!("Xor ascii\t{}", xored_str);
    println!("Xor hex\t\t{}", hex_str);
    println!("------------------------------------");
}

fn main() {
    println!("Set 1");
    println!("====================================");
    chal1();
    chal2();
}
