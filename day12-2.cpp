#include "bits/stdc++.h"

using namespace std;

static unordered_map<int, vector<int>> graph;
static set<int> small_nodes;

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

static void dfs(unordered_map<int, int>& node_counts, int& res_paths, int last_node) {
    if (last_node == end_hash) {
        res_paths++;
        if (res_paths % 1000 == 0) {
            //cout << res_paths << '\n';
        }
        return;
    }

    for (auto next : graph[last_node]) {
        if (next == start_hash) {
            continue;
        }

        bool used2 = false;
        bool bad = false;
        for (auto& [node, ct] : node_counts) {
            if (!small_nodes.count(node)) {
                continue;
            }

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
            unordered_map<int, int> new_counts = node_counts;
            new_counts[next] += 1;
            dfs(new_counts, res_paths, next);
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
    unordered_map<int, int> start_counts;
    for (auto& [node, neighbors] : graph) {
        start_counts[node] = 0;
    }
    dfs(start_counts, res_paths, start_hash);

    cout << '\n' << res_paths << '\n';
    return 0;
}
