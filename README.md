<div align="center">
    <img src="assets/images/tic-tac-toe.png" align="center" width="200px">
</div>

<h1 align="center">
    Tic-Tac-Toe CLI
</h1>

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
[![wakatime](https://wakatime.com/badge/user/018cee13-789a-4312-ba87-bff7005ff31b/project/0cc27a01-c405-41dd-917b-ddfe552a2ca8.svg)](https://wakatime.com/badge/user/018cee13-789a-4312-ba87-bff7005ff31b/project/0cc27a01-c405-41dd-917b-ddfe552a2ca8)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

Classic user vs computer Tic-Tac-Toe game on CLI

</div>

## Overview

This project is a simple implementation of the classic Tic-Tac-Toe game where the user plays against the computer. The computer makes random moves, and the game continues until there is a winner or a draw.

### Game Rules

- The computer plays using 'X's.
- The user plays using 'O's.
- The computer always makes the first move by placing an 'X' in the middle of the board.
- The board squares are numbered from 1 to 9, starting from the top-left corner and moving row by row.
- The user inputs their move by entering the number of the square they choose.
- The game ends when there is a winner or a draw.

## How to Run

1. Ensure you have Python 3.x or higher installed on your machine.
2. Clone this repository.
3. Navigate to the project directory.
4. Run the game using the following command:

    ```sh
    python main.py
    ```

## How It Works

1. **Initialization**:
   - The board is initialized as a 3x3 grid with numbers 1 to 9.
   - Flags and dictionaries are set up to track the game state, including whether the game is a draw and whether a player has won.

2. **Main Game Loop**:
   - The game continues while there are free fields and no player has won.
   - The computer makes a move by placing 'X' on the board.
   - The game checks if the computer has won.
   - If there are still free fields and the computer hasn't won, the player makes a move by placing 'O' on the board.
   - The game checks if the player has won.
   - If either player has won, the game ends and the result is displayed.

3. **Functions**:
   - `display_board(board)`: Displays the current state of the board.
   - `enter_move(board)`: Allows the player to enter their move and updates the board accordingly.
   - `make_list_of_free_fields(board)`: Returns a list of coordinates of the free cells on the board.
   - `victory_for(board, sign)`: Checks if the specified player has won the game.
   - `draw_move(board)`: Makes a move for the computer and updates the board accordingly.

### Example Session

<details>
<summary> Clik to expand </summary>

```md
...
+-------+-------+-------+
|       |       |       |
|   1   |   2   |   3   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   4   |   X   |   6   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   8   |   9   |
|       |       |       |
+-------+-------+-------+
Enter your move: 1
+-------+-------+-------+
|       |       |       |
|   O   |   2   |   3   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   4   |   X   |   6   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   8   |   9   |
|       |       |       |
+-------+-------+-------+
+-------+-------+-------+
|       |       |       |
|   O   |   X   |   3   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   4   |   X   |   6   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   8   |   9   |
|       |       |       |
+-------+-------+-------+
...


Enter your move: 7
+-------+-------+-------+
|       |       |       |
|   O   |   X   |   X   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   O   |   X   |   X   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   O   |   O   |   9   |
|       |       |       |
+-------+-------+-------+
You won!
```

</details>

### UML Sequence Diagram

Below is a UML sequence diagram that illustrates the interaction between the main components of the game.

<details>

<summary>
    Click to view diagram
</summary>

<div style="text-align: center;">

![sequence-diagram](/assets/docs/sequence-diagram/Tic%20Tac%20Toe%20Sequence%20Diagram.png)

</div>

</details>


## Project Structure

- [`main.py`](/main.py): The main Python script that implements the game logic.
- [`README.md`](/README.md): This file, providing an overview of the project.
- [`assesment.md`](/assesment.md): Contains the project description and instructions.

## License

This project is licensed under the [MIT License](LICENSE).
