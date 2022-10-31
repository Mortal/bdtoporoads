import collections
import json
import random


def main() -> None:
    with open("roads4.json") as fp:
        roads = json.load(fp)
    n = len(roads["nodes"])
    edge_lists = roads["edge_lists"]

    colors = [-1] * n

    rng = random.Random(17)
    seeds = [n-1, n-100]
    for _ in range(10):
        s = rng.randrange(n)
        assert s not in seeds
        seeds.append(s)
    next_list = []
    for i, s in enumerate(seeds):
        colors[s] = i
        next_list.append(s)
    component_edges = []
    color_counts = [1] * len(seeds)
    while next_list:
        i = rng.randrange(len(next_list))
        u = next_list[i]
        next_list[i] = next_list[-1]
        next_list.pop()
        c = colors[u]
        neighbors = []
        for v in edge_lists[u]:
            if colors[v] not in (-1, c):
                neighbors.append((colors[u], colors[v]))
        if neighbors:
            component_edges += neighbors
            continue
        for v in edge_lists[u]:
            if colors[v] == c:
                continue
            colors[v] = c
            color_counts[c] += 1
            next_list.append(v)
    print(color_counts)
    colors_to_merge = list(range(len(seeds)))
    repr = list(range(len(seeds)))
    while len(colors_to_merge) > 2:
        min_c = min(colors_to_merge, key=lambda c: color_counts[c])
        colors_to_merge.remove(min_c)
        repr[min_c] = min(colors_to_merge, key=lambda c: color_counts[c])
        color_counts[repr[min_c]] += color_counts[min_c]
    final_color = []
    for i in range(n):
        c = colors[i]
        if c == -1:
            final_color.append(0)
            continue
        while c != repr[c]:
            repr[c] = c = repr[repr[c]]
        if c == colors_to_merge[0]:
            final_color.append(1)
        else:
            final_color.append(0)
    print(sum(final_color), n)

    with open("roads5.json", "w") as ofp:
        ofp.write(json.dumps({"nodes": roads["nodes"], "edge_lists": edge_lists, "colors": colors, "final_color": final_color}) + "\n")


if __name__ == "__main__":
    main()
