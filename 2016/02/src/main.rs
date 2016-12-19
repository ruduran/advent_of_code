use std::process;
use std::env;
use std::fs::File;
use std::io::Read;

#[derive(Clone, Debug, PartialEq, Eq)]
struct Location {
    x: usize,
    y: usize
}

#[derive(Clone, Debug, PartialEq, Eq)]
struct Board {
    elems: Vec<Vec<char>>,
    pos: Location
}

impl Board {
    fn new(file: &String) -> Board {
        let elems = get_board(file);
        let mut x: usize = 0;
        let mut y: usize = 0;
        for (row, item) in elems.iter().enumerate() {
            let ret = item.iter().position(|x| *x == '5');
            match ret {
                Some(col) => {x = col; y = row;},
                None => {}
            }
        }
        Board{elems: elems, pos: Location{x: x, y: y}}
    }

    fn something_in(&self, x: &usize, y: &usize) -> bool {
        *y < self.elems.len() &&
        self.elems[*y].len() > *x &&
        self.elems[*y][*x] != ' '
    }

    fn move_up(&mut self) {
        let first_line = self.pos.y == 0;
        if !first_line && self.something_in(&(self.pos.y -1), &self.pos.x) {
            self.pos.y -= 1;
        }
    }

    fn move_down(&mut self) {
        if self.something_in(&(self.pos.y + 1), &self.pos.x) {
            self.pos.y += 1;
        }
    }

    fn move_left(&mut self) {
        let first_col = self.pos.x == 0;
        if !first_col && self.something_in(&self.pos.y, &(self.pos.x - 1)) {
            self.pos.x -= 1;
        }
    }

    fn move_right(&mut self) {
        if self.something_in(&self.pos.y, &(self.pos.x + 1)) {
            self.pos.x += 1;
        }
    }

    fn next_key(&mut self, movement: &char) {
        match *movement {
            'U' => {self.move_up()},
            'D' => {self.move_down()},
            'L' => {self.move_left()},
            'R' => {self.move_right()}
            _ => {}
        }
    }

    fn current_key(&self) -> char {
        self.elems[self.pos.y][self.pos.x]
    }
}

fn get_board(file: &String) -> Vec<Vec<char>> {
    let mut f = File::open(file).unwrap();
    let mut s = String::new();
    f.read_to_string(&mut s);

    let mut v = Vec::<Vec<char>>::new();
    for l in s.lines() {
        let mut vl = Vec::<char>::new();
        for (i,elem) in l.chars().enumerate() {
            if i % 2 == 0 {
                vl.push(elem);
            }
        }
        v.push(vl.clone())
    }
    v
}

fn get_instructions(file: & String) -> Vec<String> {
    let mut f = File::open(file).unwrap();
    let mut s = String::new();
    f.read_to_string(&mut s);
    s.lines().map(String::from).collect()
}

fn main() {
    let mut code = Vec::<char>::new();
    let args: Vec<_> = env::args().collect();
    if args.len() != 3 {
        println!("Usage: {} board input", args[0]);
        process::exit(0);
    }

    let board_file = &args[1];
    let mut board = Board::new(board_file);
    let input_file = &args[2];
    for movement in get_instructions(input_file) {
        for c in movement.chars() {
            board.next_key(&c);
        }
        code.push(board.current_key());
    }

    let str_code: String = code.iter().cloned().collect();
    println!("{}", str_code);
}
