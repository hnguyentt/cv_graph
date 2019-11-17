# SIMPLE INTERACTIVE RESUME GRAPH
![cv_graph](images/graph.png)

**Package requirements**
```bash
pip install pyvis
```

To generate a resume graph, these materials are required:

(1) Images for the graph that are stored in the `images` folder.<br>
(2) `cv.txt` in this format:
- List all nodes first:
```text
N#  \<node name\>   \<img name (without extension)\>
```
- List all edges:
```text
E#    \<N# of node 1\>    \<N# of node 2\>    \<HTML color code (without #)\>
```
Then, run:
```bash
python generate_graph_cv.py
```
The file `cv.html` file is generated.

I have embedded the my graph into my blog [here](https://nguyenhoa93.github.io/about/)<br>
*This graph is interactive that means you can drag, zoom in, zoom out, change the position of nodes, etc.*