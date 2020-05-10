use std::io;

fn read_unsigned_integer() -> u32 {
    let mut integer = String::new();
    io::stdin().read_line(&mut integer).unwrap();
    integer.trim().parse().unwrap()
}

fn main() {
    let amount = read_unsigned_integer();
    for _i in 0..amount {
        let n = read_unsigned_integer();

        let mut sum = 0;
        
        for c in 1..(n+1) {
            sum += c.pow(3);
        }
        
        println!("{}", sum);
    }
}