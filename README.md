# lifePy
An implementation of Conway's Game of Life in Python (with matplotlib)

## Usage

To run this code, you will need `matplotlib` and `numpy`.

To run the code, do the following:

```
python main.py [-s N] [-t T] [-i INIT]
        -s : size of the (square) board (integer only)
	      -t : time period of simulation
	      -i : initial state, the available options are:
	           - block
	           - glider
	           - blinker
	      Example:
					    python main.py -s 10 -t 10 -i GLIDER
```

The boundaries are not periodic, and therefore the _objects_ would die upon touching the border.

Also, this is like version -1. This shouldn't be up yet. But I want to put it up. Sue me.
