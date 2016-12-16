use std::fs::File;
use std::io::Read;

pub fn get_instructions(file: & String) -> Vec<String> {
    println!("Reading {}", file);

    let mut f = File::open(file).unwrap();
    let mut s = String::new();
    f.read_to_string(&mut s);
    let split = s.trim().split(", ");
    let v = split.map(String::from).collect();
    v
}
