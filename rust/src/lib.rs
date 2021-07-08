extern crate rustc_serialize as serialize;

use std::fs;
use std::ops::BitXor;
use std::collections::HashMap;

use serialize::base64::{self, ToBase64};
use serialize::hex::{FromHex, ToHex};

use serde_json::{Value, Map};


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

pub fn xor_str_with_byte_cypher(base_str: &str, xor_byte: u8) -> String {
    let mut result: Vec<u8> = Vec::new();
    let base_str_bytes = base_str.from_hex().unwrap();
    for i in 0..base_str_bytes.len() {
        result.push(base_str_bytes[i].bitxor(xor_byte));
    }

    String::from_utf8(result).unwrap()
}

pub fn freq_score(base_str: &str, freq_map: &HashMap<char, f64>) -> f64 {
    let mut score: f64 = 0.0;
    for c in base_str.chars() {
        let lower_char = c.to_lowercase().to_string().chars().nth(0).unwrap();
        if freq_map.contains_key(&lower_char) {
            score += freq_map.get(&lower_char).unwrap();
        } else {
            score -= 1.0;
        }
    }

    score
}

pub fn load_map(path: &str) -> HashMap<char, f64> {
    let f_map_file = fs::read_to_string(path).unwrap();
    let f_map_json: Value = serde_json::from_str(&f_map_file).unwrap();
    let f_map_obj: &Map<String, Value> = f_map_json.as_object().unwrap();

    let mut f_map: HashMap<char, f64> = HashMap::new();
    for (k, v) in f_map_obj {
        f_map.insert(k.chars().nth(0).unwrap(), v.as_f64().unwrap());
    }

    f_map
}

pub fn find_one_byte_cypher(base_str: &str) -> (u8, String) {
    let freq_map = load_map("/home/foryah/Projects/cryptopals/rust/data/en.json");

    let mut top_result: String = xor_str_with_byte_cypher(base_str, 0);
    let mut top_score: f64 = freq_score(&top_result[..], &freq_map);
    let mut top_cypher: u8 = 0;
    for i in 41..127 {
        let result = xor_str_with_byte_cypher(base_str, i);
        let result_score = freq_score(&result[..], &freq_map);
        if result_score > top_score {
            top_score = result_score;
            top_result = result;
            top_cypher = i;
        }
    }

    (top_cypher, top_result)
}

