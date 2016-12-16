pub enum Direction {
    North,
    East,
    South,
    West
}

impl Direction {
    pub fn turn_right(&mut self) {
        use self::Direction::*;
        *self = match *self {
            North => East,
            South => West,
            East => South,
            West => North,
        }
    }
    pub fn turn_left(&mut self) {
        use self::Direction::*;
        *self = match *self {
            North => West,
            South => East,
            East => North,
            West => South,
        }
    }
}

#[derive(Clone, Debug, PartialEq, Eq)]
pub struct Point {
    x: i32,
    y: i32
}

impl Point {
    pub fn new() -> Point {
        Point{x: 0, y: 0}
    }

    pub fn walk(&mut self, direction: &Direction, distance: &i32) {
        match *direction {
            Direction::North => self.y += *distance,
            Direction::East => self.x += *distance,
            Direction::South => self.y -= *distance,
            Direction::West => self.x -= *distance
        }
    }

    pub fn distance(&self) -> i32 {
        return self.x.abs() + self.y.abs();
    }
}
