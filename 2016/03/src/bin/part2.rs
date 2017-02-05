use std::process;
use std::env;
use std::fs::File;
use std::io::Read;

fn is_a_triangle(x: u32, y: u32, z: u32) -> bool {
    x + y > z && x + z > y && y + z > x
}

fn number_of_triangles(file: &str) -> u32 {
    let mut f = File::open(file).unwrap();
    let mut s = String::new();
    f.read_to_string(&mut s);

    let mut num_triangles: u32 = 0;
    let mut i: usize = 0;
    let mut multiline: Vec<Vec<u32>> = vec![Vec::new(); 3];
    for l in s.lines().map(|x| x.trim()) {
        let str_numbers = l.split_whitespace();
        let numbers: Vec<u32> = str_numbers.map(|x| x.parse::<u32>().unwrap()).collect();
        if numbers.len() == 3 {
            multiline[i] = numbers;
            if i == 2 {
                i = 0;
                for tri in 0..3 {
                    if is_a_triangle(multiline[0][tri], multiline[1][tri], multiline[2][tri]) {
                        num_triangles += 1;
                    }
                }
            } else {
                i += 1;
            }
        }
    }
    num_triangles
}

fn main() {
    let args: Vec<_> = env::args().collect();
    if args.len() != 2 {
        println!("Usage: {} input", args[0]);
        process::exit(0);
    }

    let input_file = &args[1];
    let num_triangles = number_of_triangles(input_file);
    println!("{}", num_triangles);
}
