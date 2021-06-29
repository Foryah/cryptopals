extern crate rustc_serialize as serialize;

use std::str;
use serialize::base64::{self, ToBase64};
use serialize::hex::FromHex;

pub fn hex_to_b64(hex_str: &str) -> String {
    hex_str.from_hex().unwrap().to_base64(base64::STANDARD)
}

pub fn hex_to_str(hex_str: &str) -> String {
    let str_bytes = hex_str.from_hex().unwrap();
    str::from_utf8(&str_bytes).unwrap().to_string()
}
