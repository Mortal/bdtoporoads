import json


def main() -> None:
    with open("roads1.json") as fp:
        roads = json.load(fp)
    n = len(roads["nodes"])

    edge_lists = roads["edge_lists"]
    reverse_edge_lists = [[] for _ in range(n)]
    for i in range(n):
        for j in edge_lists[i]:
            reverse_edge_lists[j].append(i)

    seen = [0]*n
    dfs = []
    ccs = [0]
    cc_id = 0
    for i in range(n):
        if seen[i]:
            continue
        size = 0
        cc_id += 1
        seen[i] = cc_id
        dfs.append(i)
        while dfs:
            i = dfs.pop()
            size += 1
            for j in edge_lists[i] + reverse_edge_lists[i]:
                if seen[j]:
                    assert seen[j] == cc_id
                    continue
                seen[j] = cc_id
                dfs.append(j)
        ccs.append(size)
    largest = max(range(len(ccs)), key=lambda i: ccs[i])
    new_name = dict(zip((i for i in range(n) if seen[i] == largest), range(ccs[largest])))
    print(list(new_name.keys())[:10])
    print(list(new_name.values())[:10])
    new_nodes = [roads["nodes"][i] for i in new_name.keys()]
    new_edge_lists = [[new_name[j] for j in edge_lists[i]] for i in new_name.keys()]
    print(ccs[largest])
    ccs.sort()
    print(ccs[-100:])
    print(len(ccs))
    print(n)
    print(largest)
    with open("roads2.json", "w") as ofp:
        ofp.write(json.dumps({"nodes": new_nodes, "edge_lists": new_edge_lists}) + "\n")


if __name__ == "__main__":
    main()
