# Structural
I designed a strategy board game for two players adn implemented it using tkinter.

The game is played starting with a rectangular grid made of dots, with a red dot and a blue dot at the ends of the grid called "bases".
![new board](https://github.com/curlhairedude/Python-Project-Structural/blob/main/Pics/New%20board.JPG?raw=true)
In the middle of the grid is a yellow colored dot called the "game dot".
The starting player can choose 1 out of eight directions to join the join the starting yellow dot with an adjacent dot with a horizontal,vertical or diagonal line.
The newly connected dot then turns into the game dot.
![Turn1](https://github.com/curlhairedude/Python-Project-Structural/blob/main/Pics/Turn%201.JPG?raw=true)
The players take turns choosing directions and try to direct the gamedot to the opponent's base.
![Turn2](https://github.com/curlhairedude/Python-Project-Structural/blob/main/Pics/Turn%202.JPG?raw=true)
There are two ways of winning.

If a player connects into the opponent's base, the player wins.
![Win way 1](https://github.com/curlhairedude/Python-Project-Structural/blob/main/Pics/Win1.JPG?raw=true)
However, if the player connects into the player's own base, the game goes on. In doing this, the player seals an entrance to his own base.
![Seal](https://github.com/curlhairedude/Python-Project-Structural/blob/main/Pics/Win2.JPG?raw=true)
If the player successfully seals all 5 directions into his own base, the player also wins.
![Win way 2](https://github.com/curlhairedude/Python-Project-Structural/blob/main/Pics/Win3.JPG?raw=true)
The game is more complex than it initially appears, there are certain tactics that resembles "structures"
that will force the opponent into drawing a direction the player wants, henc the name "structural".
