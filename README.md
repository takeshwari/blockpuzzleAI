# blockpuzzleAI

Solving a block-puzzle by implementing the A* algorithm. 

The puzzle contains 3 black tiles and 3 white tiles which can slide or hop within a row of 7 spaces. The initial puzzle configuration is:

![alt text](https://github.com/takeshwari/blockpuzzleAI/blob/master/state1.JPG)

The goal (or "solved") configuration is to have all of the white tiles to the left of all the black tiles. Note that there are several possible puzzle configurations that qualify as "solved"; for example, both of these are "solved" configurations:

![alt text](https://github.com/takeshwari/blockpuzzleAI/blob/master/state2.JPG)

There are two possible moves:

1. Slide a tile into an adjacent empty square. This move has cost 1.
2. Hop a tile over 1 or 2 adjacent tiles, landing in an empty square. The cost of this move is the number of tiles hopped.
