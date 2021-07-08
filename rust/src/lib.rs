extern crate rustc_serialize as serialize;

use std::ops::BitXor;
use serialize::base64::{self, ToBase64};
use serialize::hex::{FromHex, ToHex};

pub fn hex_to_b64(hex_str: &str) -> String {
    hex_str.from_hex().unwrap().to_base64(base64::STANDARD)
}

pub fn hex_to_str(hex_str: &str) -> String {
    let str_bytes = hex_str.from_hex().unwrap();
    String::from_utf8(str_bytes).unwrap()
}

pub fn str_to_hex(ascii_str: &str) -> String {
    ascii_str.as_bytes().to_hex()
}

pub fn xor_two_str(base_str: &str, xor_str: &str) -> String {
    if base_str.len() != xor_str.len() {
        panic!("The two &str have to be the same length!")
    }

    let mut result: Vec<u8> = Vec::new();
    let base_str_bytes = base_str.from_hex().unwrap();
    let xor_str_bytes = xor_str.from_hex().unwrap();
    for i in 0..base_str_bytes.len() {
        result.push(base_str_bytes[i].bitxor(xor_str_bytes[i]));
    }

    String::from_utf8(result).unwrap()
}
