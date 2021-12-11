use std::env;
use std::fs;

fn main() {
    let args: Vec<String> = env::args().collect();

    let file_text = fs::read_to_string(&args[1]).unwrap();
    let file_lines: Vec<&str> = file_text.split('\n').collect();

    let mut grid: Vec<Vec<u32>> = Vec::new();
    for line in file_lines {
        if line.is_empty() {
            continue;
        }

        grid.push(Vec::<u32>::new());

        let row = &mut grid.last_mut().unwrap();
        for ch in String::from(line).chars() {
            let digit = ch.to_digit(10).unwrap();
            row.push(digit);
        }
    }

    for row in &grid {
        println!("{:?}", row);
    }
    let mut flashes = 0;
    let mut flashed = Vec::<Vec<bool>>::new();
    for _ in 0..grid.len() {
        let row: Vec<bool> = vec![false; grid[0].len()];
        flashed.push(row);
    }

    let mut pending: Vec<(usize, usize)> = Vec::new();
    for step in 0..1_000_000 {
        if step % 10 == 0 {
            println!("{}", step);
        }

        for row in grid.iter_mut() {
            for cell in row.iter_mut() {
                *cell += 1;
            }
        }

        let mut new_flashes = 0;
        loop {
            let mut incd = 0;
            for (y, row) in grid.iter().enumerate() {
                for (x, cell) in row.iter().enumerate() {
                    if *cell > 9 && !flashed[y][x] {
                        new_flashes += 1;
                        flashed[y][x] = true;

                        for xoff in -1..=1 {
                            for yoff in -1..=1 {
                                if xoff == 0 && yoff == 0 {
                                    continue;
                                }

                                let px = x as i32 + xoff;
                                let py = y as i32 + yoff;
                                if px >= 0 && px < row.len() as i32 && py >= 0 && py < grid.len() as i32 {
                                    let px = px as usize;
                                    let py = py as usize;

                                    pending.push((px, py));
                                    if grid[py][px] > 8 {
                                        incd += 1;
                                    }
                                }
                            }
                        }
                    }
                }
            }

            for (px, py) in &pending {
                grid[*py][*px] += 1;
            }
            pending.clear();

            if incd == 0 {
                break;
            }
        }

        flashes += new_flashes;
        if new_flashes == grid.len() * grid[0].len() {
            println!("ANS: {}", step + 1);
            break;
        }

        for row in grid.iter_mut() {
            for cell in row.iter_mut() {
                if *cell > 9 {
                    *cell = 0;
                }
            }
        }
        for row in flashed.iter_mut() {
            row.clear();
            row.resize(grid[0].len(), false);
        }
    }

    println!("{}", flashes);
}
