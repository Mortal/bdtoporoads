import json

from osgeo import ogr


def main() -> None:
    ds = ogr.Open("/home/rav/t/BDTOPO_3-0_TOUSTHEMES_GPKG_LAMB93_D075_2022-09-15/BDTOPO/1_DONNEES_LIVRAISON_2022-10-00024/BDT_3-0_GPKG_LAMB93_D075-ED2022-09-15/BDT_3-0_GPKG_LAMB93_D075-ED2022-09-15.gpkg")
    layer = ds.GetLayer("troncon_de_route")
    layer_defn = layer.GetLayerDefn()
    i_sens_de_circulation = layer_defn.GetFieldIndex("sens_de_circulation")
    node_id = {}
    edge_lists = []

    def lookup_node(p):
        try:
            return node_id[p]
        except KeyError:
            edge_lists.append([])
            return node_id.setdefault(p, len(node_id))

    for f in layer:
        circ = f.GetFieldAsString(i_sens_de_circulation)
        if circ == "Sans objet":
            continue
        g = f.GetGeometryRef()
        u = lookup_node(g.GetPoint(0)[:2])
        v = lookup_node(g.GetPoint(g.GetPointCount() - 1)[:2])
        if u == v:
            continue
        if circ != "Sens direct":
            edge_lists[v].append(u)
        if circ != "Sens inverse":
            edge_lists[u].append(v)
        del g

    with open("roads1.json", "w") as ofp:
        ofp.write(json.dumps({"nodes": list(node_id.keys()), "edge_lists": edge_lists}))


if __name__ == "__main__":
    main()
