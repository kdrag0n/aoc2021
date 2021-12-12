#include "bits/stdc++.h"

using namespace std;

static vector<vector<int>> graph;
static vector<bool> small_nodes;
static vector<int> node_counts;

static constexpr int start_node = 0;
static constexpr int end_node = 1;

static inline bool is_small(const string& node) {
    return islower(node[0]) && node != "start" && node != "end";
}

static void dfs(int& res_paths, int last_node = start_node, bool used2 = false) {
    for (auto next : graph[last_node]) {
        auto next_used2 = used2;
        if (next == start_node) {
            continue;
        } else if (next == end_node) {
            res_paths++;
            if (res_paths % 1000 == 0) {
                //cout << res_paths << '\n';
            }
            continue;
        } else if (small_nodes[next] && node_counts[next] >= 1) {
            if (!next_used2) {
                next_used2 = true;
            } else {
                continue;
            }
        }

        node_counts[next]++;
        dfs(res_paths, next, next_used2);
        node_counts[next]--;
    }
}

int main(int argc, char **argv) {
    freopen(argv[1], "r", stdin);

    unordered_map<string, int> node_map;
    node_map["start"] = start_node;
    node_map["end"] = end_node;

    while (!cin.eof()) {
        string line;
        cin >> line;
        if (line.empty()) {
            continue;
        }

        auto frm = line.substr(0, line.find("-"));
        auto to = line.substr(line.find("-") + 1, line.length());
        //cout << frm << ' ' << to << '\n';

        auto from_node = node_map.count(frm) ? node_map[frm] : node_map[frm] = node_map.size();
        auto to_node = node_map.count(to) ? node_map[to] : node_map[to] = node_map.size();
        graph.resize(node_map.size());
        small_nodes.resize(node_map.size());

        graph[from_node].push_back(to_node);
        graph[to_node].push_back(from_node);

        if (is_small(frm)) {
            small_nodes[from_node] = true;
        }
        if (is_small(to)) {
            small_nodes[to_node] = true;
        }
    }

    int res_paths = 0;
    node_counts.resize(node_map.size());
    node_counts[start_node] = 1;
    dfs(res_paths);

    cout << '\n' << res_paths << '\n';
    return 0;
}
