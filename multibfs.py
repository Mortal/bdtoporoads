import json


def main() -> None:
    with open("roads3.json") as fp:
        roads = json.load(fp)
    n = len(roads["nodes"])
    edge_lists = roads["edge_lists"]

    self_dist = []
    seen = [-1] * n
    bfs = []
    no_loop = 0
    maxsofar = 0
    for i in range(n):
        front = 0
        del bfs[:]
        curdist = 0
        nextdist = 0
        for j in edge_lists[i]:
            seen[j] = i
            bfs.append(j)
        while front < len(bfs):
            if front == nextdist:
                curdist += 1
                nextdist = len(bfs)
            if bfs[front] == i:
                break
            for j in edge_lists[bfs[front]]:
                if seen[j] == i:
                    continue
                seen[j] = i
                bfs.append(j)
            front += 1
        if front == len(bfs):
            self_dist.append(-1)
            no_loop += 1
        else:
            self_dist.append(curdist)
            if curdist > maxsofar:
                maxsofar = curdist
                print(curdist, i)

    print(no_loop)
    import collections
    print(collections.Counter(self_dist))

    new_name = {i: j for j, i in enumerate(sorted((i for i in range(n) if self_dist[i] >= 0), key=lambda i: self_dist[i]))}
    print(list(new_name.keys())[:10])
    print(list(new_name.values())[:10])
    new_nodes = [roads["nodes"][i] for i in new_name.keys()]
    new_edge_lists = [[new_name[j] for j in edge_lists[i] if j in new_name] for i in new_name.keys()]

    with open("roads4.json", "w") as ofp:
        ofp.write(json.dumps({"nodes": new_nodes, "edge_lists": new_edge_lists}) + "\n")


if __name__ == "__main__":
    main()
