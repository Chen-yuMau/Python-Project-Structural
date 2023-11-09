# Structural

## Overview:

Structural is a pencil-and-paper game for two players 

## Requirements:

* Python 3.5 or up.

## Running the game:

For the first time only, clone the git repository.
```
$ git clone https://github.com/Chen-yuMau/Python-Project-Structural
```

Execute the following command.
```
$ cd Python-Project-Structural
$ python Structural.py
```

> For Linux, use the `python3` command instead of the `python` command,  
> or install the `python-is-python3` package.  
> ```
> $ sudo apt install python-is-python3
> ```
## Development:
The current version of the game is meant for offline play. The file "Structural.py" is sufficient for online play. 
An online connection version is currently in development. 
## Rules of the game:
I designed a strategy board game for two players and implemented it using tkinter.

The game is played starting with a rectangular grid made of dots, with a red dot and a blue dot at the ends of the grid called "bases".

![new board](https://github.com/curlhairedude/Python-Project-Structural/blob/main/Pics/New%20board.JPG?raw=true)

In the middle of the grid is a yellow colored dot called the "game dot".
The starting player can choose 1 out of eight directions to join the starting yellow dot with an adjacent dot with a horizontal,vertical or diagonal line.
The newly connected dot then turns into the game dot.

![Turn1](https://github.com/curlhairedude/Python-Project-Structural/blob/main/Pics/Turn%201.JPG?raw=true)

The players take turns choosing directions and try to direct the gamedot to the opponent's base.

![Turn2](https://github.com/curlhairedude/Python-Project-Structural/blob/main/Pics/Turn%202.JPG?raw=true)

There are two ways of winning.

If a player connects to the opponent's base, the player wins.

![Win way 1](https://github.com/curlhairedude/Python-Project-Structural/blob/main/Pics/Win1.JPG?raw=true)

However, if the player connects to the player's own base, the game goes on. In doing this, the player seals an entrance to his own base.

![Seal](https://github.com/curlhairedude/Python-Project-Structural/blob/main/Pics/Win2.JPG?raw=true)

If the player successfully seals all 5 directions into his own base, the player also wins.

![Win way 2](https://github.com/curlhairedude/Python-Project-Structural/blob/main/Pics/Win3.JPG?raw=true)

The game is more complex than it initially appears, there are certain tactics that resembles "structures"
that will force the opponent into drawing a direction the player wants, hence the name "structural".
