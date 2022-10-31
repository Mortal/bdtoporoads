import json


def main() -> None:
    with open("roads2.json") as fp:
        roads = json.load(fp)
    n = len(roads["nodes"])
    edge_lists = roads["edge_lists"]
    new_edge_lists = [sorted(set(edge_lists[i])) for i in range(n)]
    with open("roads3.json", "w") as ofp:
        ofp.write(json.dumps({"nodes": roads["nodes"], "edge_lists": new_edge_lists}) + "\n")


if __name__ == "__main__":
    main()
