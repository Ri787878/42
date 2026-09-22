*This project has been created as part of the 42 curriculum by ridias.*

# Fly-in

## Description
Fly-in is a project that combines a custom configuration interpreter with a pathfinding and simulation system. It reads a scenario file describing the environment, then validates and parses the data to reconstruct a graph-like maze composed of hubs, connections, restrictions, and drone assignments.

The program’s goal is to coordinate several drones so they can move through the network while respecting the constraints defined in the input file. It does so by:
- parsing and validating the layout and rules provided by the user
- building the internal representation of the map and its restrictions
- computing a path for each drone individually
- reserving the next step for each drone to avoid conflicts
- dispatching the first valid movement at each simulation step
- logging each movement
- checking whether all drones have reached their final destination

A graphical interface built with Pygame is also started alongside the simulation to visualize the execution step by step and make the behavior easier to understand and debug.

### Algorithm Choices && implementation
The algorithm used is "A*". A algorithm that uses a normal BFS algorithm and gives it an incentive to search in the right direction inthe form of a heuristic. A heuristic is a function that rewards the algorithm if, for example, approaches the goal by calculating the distatnce between the point and the goal, so it incentivises the algorithm to approach the goal no matter what.
Regarding the implementation of the algorithm the algorithm is a somewhat simple pathfinder to implement needing only the map itself and a few helper functions that for example provide the heuristic calculation.

### Visual Representation Features
The visual representation of the project is quite simple in terms of features, having no buttons to interact with it mid simulation. However it does have a few features worht mentioning:
- "WASD" keys control to look around the map
- Zoom using the mouse wheel to better see each zoom
- Dinamic color interpretation depending on provided color in the map file
- A simple step counter
- Capabilitie to receive every valid single-word strings for a color, including "rainbow" that cycles through a HUE of colors

### Example Input
Example map file to provide the program:
```bash
# Easy Level 1: Simple linear path

nb_drones: 4

start_hub: start 0 0 [color=green]
hub: waypoint1 1 0 [color=blue]
hub: waypoint2 2 0 [color=blue]
end_hub: goal 3 0 [color=red]

connection: start-waypoint1
connection: waypoint1-waypoint2
connection: waypoint2-goal
```

### Expected Output
Possible expected path taken by the program:
```bash
D1-waypoint1
D1-waypoint2 D2-waypoint1
D1-goal D2-waypoint2 D3-waypoint1
D2-goal D3-waypoint2 D4-waypoint1
D3-goal D4-waypoint2
D4-goal
```

### Features

- Validation of the input file format and rules
- Parsing of hubs, connections, and restrictions
- Multi-drone pathfinding
- Conflict prevention through reserved next moves
- Step-by-step simulation loop
- Real-time visualization with Pygame
- Creation of output on a file "output.txt"

## Instructions

### Installation
```bash
make install
```

### Execution
```bash
make run
```


The project expects a valid map/configuration file as input. Once launched, it will parse the file, build the simulation environment, and start the drone movement loop while displaying the state in the graphical interface.


## Resources

- https://en.wikipedia.org/wiki/A*_search_algorithm
- https://www.geeksforgeeks.org/dsa/a-search-algorithm/
- https://www.pygame.org/docs/
- https://www.datacamp.com/tutorial/a-star-algorithm
- https://pydantic.dev/docs/validation/dev/get-started/


### AI usage
AI was used as a support tool during the development of this project for:
- drafting and improving the README structure and project description
- explaining pathfinding concepts and comparing algorithm choices
- helping review simulation edge cases and input validation scenarios
- suggesting debugging ideas and clarifying implementation details

AI was mainly used to accelerate understanding, documentation, and validation work rather than replace the project’s actual reasoning and coding.