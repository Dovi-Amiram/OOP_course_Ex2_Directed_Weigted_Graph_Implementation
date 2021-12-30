# Project - Directed Weighted Graphs:
**Written in: Python.**
## About:
This project deals with the Abstraction, Design and Implementation of a Directed Weighted Graph.  
This specific Implementation of a Directed Weighted Graph is revolved around the abstraction of road-maps and the way SAT-NAV's typically represent the world around us. each Node may refer to a city or a junction, and Edge may refer to a road between two places, and the Egde's weight may refer to the distance or time to be travelled via said road.  
The same project has already been written in Java by my partner and I. This project however, is also meant for testing performance differences between the 2 different Implementations (Java VS Python): [Wiki](https://github.com/shlomoPearl/OOP-Ex3/wiki/ "Comparing our Java program's performance to our Python program's performance")

### UML Diagram:

![UML](https://user-images.githubusercontent.com/73857923/147769542-f42b5408-17b9-457c-bf92-5c0f3256f12d.png)

  
  
  
  
### Data Structures:
#### Each graph is defined by:
1.	A collection of Nodes implemented by a dictionary, which maps the Node's Integer ID (key) to the corresponding Node object (value).  
An example of a key-value pair in said dictionary: 23: <Node Object>

2.	A collection of directed edges implemented by a dictionary, which maps a tuple of an ordered pair (a, b) of two integer Node ID's, to the corresponding edge's weight.  
  An example of a key-value pair in said dictionary: **(3, 4): 23.456**  
  
#### Extra data structures designed to help with algorithms' implementations:  
  
3.	Each Node Object contains a collection of his out-going edges implemented by a dictionary which maps the Integer ID of the destination Node of the edge, to the edge's weight.
4.	Each Node Object also contains a collection of his in-going edges implemented by a dictionary which maps the Integer ID of the source Node of the edge, to the edge's weight.  
### Algorithms and Functions:
#### Actions to perform on a graph object:
1. **Add Node** –  Adds a node to the graph with an integer ID and a Location (x, y, z coordinates) given by the user.
2. **Remove Node** – Removes from the graph, the Node with the given integer ID. This method also automatically removes all in-going and out-going Edges connected to the removed node.
3. **Add Edge** – Adds an Edge to the graph between user-specified source an destination Nodes, with a user-specified weight.
4. **Remove Edge** – Removes an Edge from the graph, between user-specified source an destination Nodes.
5. **Get All 'V'**: Returns a dictionary which maps all of the graph's Nodes' Integer ID's (key) to the corresponding Node object (value)
6. **Get All 'E'**: Returns a dictionary which maps all the tuples, (ordered pairs - (a, b)) of 2 integer Node ID's, each representing an edge from the graph, to the corresponding edge's weight.
#### Algorithms to be perform on a graph object:
7. **Shortest Path** – Input: 2 integers Node ID's.  
Returns: a tuple object: pair s.t:  
pair[0] = Shortest path distance between the 2 Nodes.  
pair[1] = A list of the Nodes that form the path in the correct order.
(based on the famous Dijkstra algorithm).
8. **Center** - Returns the Node which has the smallest maximum distance from all other Nodes, assuming the graph is connected.
9. **TSP** – Algorithm designed to solve a lenient version of the well known problem from the fields of mathematics and computer sciences: The Travelling Salesman Problem. This is a recursive greedy algorithm which calculates the shortest ("cheapest") route, which passes through user-specified cities (vertices on the graph, and travelling through "other" cities (which are not in the original given collection) is permitted.
10. **Save** – Saves the graph in a JSON file in a "pretty-printing" JSON format.
11. **Load** – Loads and creates a graph from a JSON file.
12. **PlotGraph** – Plots a representation of the graph on a graphical window.  
  
  #### Example:  
  
  ![WhatsApp Image 2021-12-30 at 01 01 23](https://user-images.githubusercontent.com/73857923/147785358-eb00a191-7aa5-4e18-925c-7e7e0a0d4975.jpeg)
  
### Running the program from your command line:  
  
We designed a way to load a graph from a Json file, and plot its representation in a graphical window, using this simple command:  
  
1. For plotting the graphs from our project's files:  
  **python Ex3.py data/\<json file name\>**  
  
2. For plotting any graphs from your device, represented in our json format:  
  **python Ex3.py \<your json file path\>**
  
