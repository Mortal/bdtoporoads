import collections
import json
import random


def main() -> None:
    with open("roads5.json") as fp:
        roads = json.load(fp)
    n = len(roads["nodes"])
    edge_lists = roads["edge_lists"]
    edge_count = sum(len(e) for e in edge_lists)
    color = roads["final_color"]
    print(n, edge_count)
    for i in range(n):
        for j in edge_lists[i]:
            if color[i] == color[j]:
                print(i, j, 0)
            elif color[i]:
                print(i, j, 1)
            else:
                print(i, j, 2)


if __name__ == "__main__":
    main()
