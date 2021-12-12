#include "bits/stdc++.h"

using namespace std;

static unordered_map<int, vector<int>> graph;
static set<int> small_nodes;
static unordered_map<int, int> small_counts;

static inline int hash_node(const string& node) {
    int hash = 17;
    for (char ch : node) {
        hash *= 31;
        hash += ch;
    }
    return hash;
}

static auto start_hash = hash_node("start");
static auto end_hash = hash_node("end");

static inline bool is_small(const string& node) {
    return islower(node[0]) && node != "start" && node != "end";
}

static inline void add_counts(unordered_map<int, int>& counts, const set<int>& nodes, int node) {
    if (!nodes.count(node)) {
        return;
    }

    if (counts.count(node) == 0) {
        counts.emplace(node, 0);
    }

    counts[node] += 1;
}

static void dfs(vector<int>& path, int& res_paths) {
    auto last_node = path.back();

    if (last_node == end_hash) {
        res_paths++;
        if (res_paths % 1000 == 0) {
            cout << res_paths << '\n';
        }
        return;
    }

    for (auto next : graph[last_node]) {
        if (next == start_hash) {
            continue;
        }

        small_counts.clear();
        for (auto node : path) {
            add_counts(small_counts, small_nodes, node);
        }
        add_counts(small_counts, small_nodes, next);

        bool used2 = false;
        bool bad = false;
        for (auto& [node, ct] : small_counts) {
            if (ct <= 1) {
                continue;
            } else if (ct == 2 && !used2) {
                used2 = true;
            } else {
                bad = true;
                break;
            }
        }

        if (!bad) {
            vector<int> new_path = path;
            new_path.push_back(next);
            dfs(new_path, res_paths);
        }
    }
}

int main(int argc, char **argv) {
    freopen(argv[1], "r", stdin);

    while (!cin.eof()) {
        string line;
        cin >> line;
        if (line.empty()) {
            continue;
        }

        auto frm = line.substr(0, line.find("-"));
        auto to = line.substr(line.find("-") + 1, line.length());
        cout << frm << ' ' << to << '\n';

        auto frm_hash = hash_node(frm);
        auto to_hash = hash_node(to);
        if (graph.count(frm_hash) == 0) {
            graph.emplace(frm_hash, vector<int>{});
        }
        graph[frm_hash].push_back(to_hash);
        if (graph.count(to_hash) == 0) {
            graph.emplace(to_hash, vector<int>{});
        }
        graph[to_hash].push_back(frm_hash);

        if (is_small(frm)) {
            small_nodes.insert(frm_hash);
        }
        if (is_small(to)) {
            small_nodes.insert(to_hash);
        }
    }

    int res_paths = 0;
    vector<int> start_path{start_hash};
    dfs(start_path, res_paths);

    cout << '\n' << res_paths << '\n';
    return 0;
}
