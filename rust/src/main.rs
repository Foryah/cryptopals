mod lib;

use lib::{hex_to_b64, hex_to_str};

fn main() {
    let b64_str = hex_to_b64("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d");
    let ascii_str = hex_to_str("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d");
    println!("b64\t{}", b64_str);
    println!("ascii\t{}", ascii_str);
}
