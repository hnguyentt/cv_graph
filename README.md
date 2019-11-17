# GENERATION OF RESUME GRAPH

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

I have embedded the my graph into my blog [here](https://nguyenhoa93.github.io/about/)

{::nomarkdown}

<html>
<head>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/vis/4.16.1/vis.css" type="text/css" />
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/vis/4.16.1/vis-network.min.js"> </script>

<!-- <link rel="stylesheet" href="../node_modules/vis/dist/vis.min.css" type="text/css" />
<script type="text/javascript" src="../node_modules/vis/dist/vis.js"> </script>-->

<style type="text/css">

        #mynetwork {
            width: 100%;
            height: 750px;
            background-color: #ffffff;
            border: 1px solid lightgray;
            position: relative;
            float: left;
        }

        

        

        
</style>

</head>

<body>
<div id = "mynetwork"></div>


<script type="text/javascript">

    // initialize global variables.
    var edges;
    var nodes;
    var network; 
    var container;
    var options, data;

    
    // This method is responsible for drawing the graph, returns the drawn network
    function drawGraph() {
        var container = document.getElementById('mynetwork');
        
        

        // parsing and collecting nodes and edges from the python
        nodes = new vis.DataSet([{"id": "Hoa Nguyen", "image": "https://raw.githubusercontent.com/nguyenhoa93/cv_graph/master/images/Gau.jpg", "label": "Hoa Nguyen", "shape": "circularImage", "size": 50}, {"id": "Education", "image": "https://raw.githubusercontent.com/nguyenhoa93/cv_graph/master/images/education.png", "label": "Education", "shape": "circularImage"}, {"id": "Luong The Vinh high school for the gifted", "image": "https://raw.githubusercontent.com/nguyenhoa93/cv_graph/master/images/LTV.jpg", "label": "Luong The Vinh high school for the gifted", "shape": "circularImage"}, {"id": "University of Medicine and Pharmacy, Ho Chi Minh city", "image": "https://raw.githubusercontent.com/nguyenhoa93/cv_graph/master/images/UMPHCM.png", "label": "University of Medicine and Pharmacy, Ho Chi Minh city", "shape": "circularImage"}, {"id": "VietAI", "image": "https://raw.githubusercontent.com/nguyenhoa93/cv_graph/master/images/VietAI.png", "label": "VietAI", "shape": "circularImage"}, {"id": "Research Experience", "image": "https://raw.githubusercontent.com/nguyenhoa93/cv_graph/master/images/research.png", "label": "Research Experience", "shape": "circularImage"}, {"id": "Online Research Club", "image": "https://raw.githubusercontent.com/nguyenhoa93/cv_graph/master/images/ORC.png", "label": "Online Research Club", "shape": "circularImage"}, {"id": "Working Experience", "image": "https://raw.githubusercontent.com/nguyenhoa93/cv_graph/master/images/working.png", "label": "Working Experience", "shape": "circularImage"}, {"id": "Cao Thang Eye Hospital", "image": "https://raw.githubusercontent.com/nguyenhoa93/cv_graph/master/images/CTEH.png", "label": "Cao Thang Eye Hospital", "shape": "circularImage"}, {"id": "Hobbies", "image": "https://raw.githubusercontent.com/nguyenhoa93/cv_graph/master/images/hobby.jpg", "label": "Hobbies", "shape": "circularImage"}, {"id": "Playing musical instruments", "image": "https://raw.githubusercontent.com/nguyenhoa93/cv_graph/master/images/piano.jpg", "label": "Playing musical instruments", "shape": "circularImage"}, {"id": "Cycling", "image": "https://raw.githubusercontent.com/nguyenhoa93/cv_graph/master/images/cycling.jpg", "label": "Cycling", "shape": "circularImage"}, {"id": "Drawing", "image": "https://raw.githubusercontent.com/nguyenhoa93/cv_graph/master/images/drawing.png", "label": "Drawing", "shape": "circularImage"}, {"id": "Reading", "image": "https://raw.githubusercontent.com/nguyenhoa93/cv_graph/master/images/reading.png", "label": "Reading", "shape": "circularImage"}]);
        edges = new vis.DataSet([{"color": "#0B806C", "from": "Hoa Nguyen", "to": "Education"}, {"color": "#0B806C", "from": "Education", "to": "Luong The Vinh high school for the gifted"}, {"color": "#0B806C", "from": "Education", "to": "University of Medicine and Pharmacy, Ho Chi Minh city"}, {"color": "#0B806C", "from": "Education", "to": "VietAI"}, {"color": "#0B3080", "from": "Hoa Nguyen", "to": "Research Experience"}, {"color": "#0B3080", "from": "Research Experience", "to": "University of Medicine and Pharmacy, Ho Chi Minh city"}, {"color": "#0B3080", "from": "Research Experience", "to": "Online Research Club"}, {"color": "#805B0B", "from": "Hoa Nguyen", "to": "Working Experience"}, {"color": "#805B0B", "from": "Working Experience", "to": "VietAI"}, {"color": "#805B0B", "from": "Working Experience", "to": "Cao Thang Eye Hospital"}, {"color": "#800B64", "from": "Hoa Nguyen", "to": "Hobbies"}, {"color": "#800B64", "from": "Hobbies", "to": "Playing musical instruments"}, {"color": "#800B64", "from": "Hobbies", "to": "Cycling"}, {"color": "#800B64", "from": "Hobbies", "to": "Drawing"}, {"color": "#800B64", "from": "Hobbies", "to": "Reading"}]);

        // adding nodes and edges to the graph
        data = {nodes: nodes, edges: edges};

        var options = {"nodes": {"color": {"background": "rgba(255,253,248,1)"}}, "edges": {"color": {"inherit": true}, "smooth": false}, "physics": {"minVelocity": 0.75}};
        
        

        

        network = new vis.Network(container, data, options);

        


        

        return network;

    }

    drawGraph();

</script>
</body>
</html>

{:/}