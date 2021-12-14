#include "bits/stdc++.h"

using namespace std;

static void print_grid(int width, int height, const vector<pair<int, int>>& points) {
    vector<vector<bool>> grid(height);
    for (auto& row : grid) {
        row.resize(width);
    }
    for (const auto& [x, y] : points) {
        grid[y][x] = true;
    }

    for (int y = 0; y < height; y++) {
        for (int x = 0; x < width; x++) {
            cout << (grid[y][x] ? '#' : ' ');
        }
        cout << '\n';
    }
}

int main(int argc, char **argv) {
    freopen(argv[1], "r", stdin);

    vector<pair<int, int>> points;
    vector<pair<char, int>> folds;

    int width = 0;
    int height = 0;
    while (!cin.eof()) {
        string line;
        cin >> line;

        if (line.empty()) {
            continue;
        } else if (line == "fold") {
            cin >> line >> line;
            auto axis = line[0];

            auto pos = stoi(line.substr(2));
            folds.emplace_back(axis, pos);
        } else {
            auto x = stoi(line.substr(0, line.find(",")));
            auto y = stoi(line.substr(line.find(",") + 1, line.length()));
            points.emplace_back(x, y);

            if (x + 1 > width) {
                width = x + 1;
            }
            if (y + 1 > height) {
                height = y + 1;
            }
        }
    }

    for (const auto& [axis, fold_pos] : folds) {
        vector<pair<int, int>> new_points;
        new_points.reserve(points.size());

        if (axis == 'x') {
            for (auto [x, y] : points) {
                if (x > fold_pos) {
                    x = fold_pos - (x - fold_pos);
                    width = fold_pos + 1;
                }

                new_points.emplace_back(x, y);
            }
        } else {
            for (auto [x, y] : points) {
                if (y > fold_pos) {
                    y = fold_pos - (y - fold_pos);
                    height = fold_pos + 1;
                }

                new_points.emplace_back(x, y);
            }
        }

        points = std::move(new_points);
    }

    print_grid(width, height, points);

    return 0;
}
