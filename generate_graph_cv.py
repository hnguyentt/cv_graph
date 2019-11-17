"""
Purpose: Convert information from csv.txt file into graph network
Format of cv.txt file:
Nodes: N#   <Node name> <Image name without extension>
Edges: E#   <N#>    <N#>    <Color code>
"""

# DEPENDENCIES
import re
import os
from pyvis.network import Network

# CONSTANTS
IMG = "https://raw.githubusercontent.com/nguyenhoa93/cv_graph/master/images/"

if __name__=="__main__":
    # Load cv
    f = open("cv.txt", "r")
    # Create an empty graph
    G = Network(height="750px", width="100%")

    node_dict = {}
    exts = ["jpg", "png", "jpeg"]
    for line in f:
        sep = line.strip("\n").split("\t")
        if len(sep) == 3:
            node_dict[sep[0]] = sep[1]
            for ext in exts:
                if os.path.isfile("images/%s.%s" % (sep[2], ext)):
                    im = sep[2] + "." + ext
                    break
            if sep[0] == "N1":
                G.add_node(sep[1], shape="circularImage", size=50, image=IMG + im)
            else:
                G.add_node(sep[1], shape="circularImage", image=IMG + im)
        else:
            G.add_edge(node_dict[sep[1]], node_dict[sep[2]], color="#%s" % sep[3])

    G.set_options("""
    var options = {
      "nodes": {
        "color": {
          "background": "rgba(255,253,248,1)"
        }
      },
      "edges": {
        "color": {
          "inherit": true
        },
        "smooth": false
      },
      "physics": {
        "minVelocity": 0.75
      }
    }
    """)
    G.show("cv.html")