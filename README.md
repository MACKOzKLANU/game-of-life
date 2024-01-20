# Conway's Game of Life

This Python code implements Conway's Game of Life, a cellular automaton devised by the British mathematician John Conway. The game consists of a grid of cells, each of which can be in one of two states: alive or dead. The state of each cell evolves over time based on a set of rules.

## Cell Class

The `Cell` class represents an individual cell in the game. It has the following methods:

### `__init__(self) -> None`

Constructor method that initializes a cell with the `isAlive` attribute set to `False` (dead).

### `Switch(self)`

Method to toggle the state of the cell between alive and dead.

## Map Class

The `Map` class represents the game board and contains a 2D grid of cells. It has the following methods:

### `__init__(self) -> None`

Constructor method that initializes a map with a default size of 20x20, filling it with dead cells.

### `Display(self)`

Method to display the current state of the game board, where alive cells are represented by "X" and dead cells by empty spaces.

### `Set(self, i, j, status)`

Method to set the state of a specific cell at position `(i, j)` to either alive (`True`) or dead (`False`).

### `Fill(self, filename)`

Method to fill the game board based on the contents of a text file. The file should contain a list of coordinates representing alive cells.

## Game Class

The `Game` class orchestrates the execution of the Game of Life. It has the following methods:

### `__init__(self)`

Constructor method that initializes a game with an associated map.

### `Play(self, times)`

Method to play the Game of Life for a specified number of iterations. The state of the board is updated and displayed at regular intervals.

### `get_alive_neighbors(self, i, j)`

Helper method to calculate the number of alive neighbors for a given cell position.

## Usage

```python
from Game import *

# Create a game instance
g = Game()

# Load a specific pattern into the game board
g.map.Fill("save5")

# Play the game with a specified time interval between iterations
g.Play(1)
```

