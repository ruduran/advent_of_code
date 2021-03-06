use std::process;
use std::env;

extern crate day01;
use day01::movements::{Point, Direction};
use day01::input;

fn main() {
    let mut loc = Point::new();
    let mut direction: Direction = Direction::North;
    let args: Vec<_> = env::args().collect();
    if args.len() != 2 {
        println!("Usage: {} input", args[0]);
        process::exit(0);
    }

    let input_file = &args[1];
    for movement in input::get_instructions(input_file) {
        match movement.chars().nth(0).unwrap() {
            'R' => direction.turn_right(),
            'L' => direction.turn_left(),
            _ => {}
        }

        let str_steps = &movement[1..];
        let steps = str_steps.parse::<i32>().unwrap();
        loc.walk(&direction, &steps);
    }

    println!("{} blocks away", loc.distance());
}
