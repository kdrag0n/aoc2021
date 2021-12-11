#include "bits/stdc++.h"

using namespace std;

int main(int argc, char **argv) {
    freopen(argv[1], "r", stdin);

    vector<vector<int>> grid;
    while (!cin.eof()) {
        string line;
        cin >> line;
        if (line.length() != 0) {
            grid.emplace_back();
            auto& row = grid.back();

            for (char c : line) {
                row.push_back(c - '0');
            }
        }
    }

    int flashes = 0;
    vector<vector<bool>> flashed(grid.size());
    for (auto& row : flashed) {
        row.resize(grid[0].size());
    }

    for (int step = 0; step < 10000000; step++) {
        if (step % 10 == 0) {
            cout << step << '\n';
        }

        for (auto& row : grid) {
            for (auto& cell : row) {
                cell += 1;
            }
        }

        int new_flashes = 0;
        while (true) {
            int incd = 0;
            for (int y = 0; y < grid.size(); y++) {
                auto& row = grid[y];
                for (int x = 0; x < row.size(); x++) {
                    auto cell = row[x];
                    if (cell > 9 && !flashed[y][x]) {
                        new_flashes++;

                        for (int xoff = -1; xoff <= 1; xoff++) {
                            for (int yoff = -1; yoff <= 1; yoff++) {
                                if (xoff == 0 && yoff == 0) {
                                    continue;
                                }

                                auto px = x + xoff;
                                auto py = y + yoff;
                                if (px >= 0 && px < row.size() && py >= 0 && py < grid.size()) {
                                    grid[py][px] += 1;
                                    if (grid[py][px] > 9) {
                                        incd += 1;
                                    }
                                    flashed[y][x] = true;
                                }
                            }
                        }
                    }
                }
            }

            if (!incd) {
                break;
            }
        }

        flashes += new_flashes;
        if (new_flashes == grid.size() * grid[0].size()) {
            cout << "ANS " << step+1 << '\n';
            break;
        }

        for (auto& row : grid) {
            for (auto& cell : row) {
                if (cell > 9) {
                    cell = 0;
                }
            }
        }
        for (auto& row : flashed) {
            std::fill(row.begin(), row.end(), false);
        }
    }

    cout << flashes << '\n';
    return 0;
}
