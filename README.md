<div align="center">
    <img src="assets/images/tic-tac-toe.png" align="center" width="200px">
</div>

<h1 align="center">
    Tic-Tac-Toe
</h1>

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
[![wakatime](https://wakatime.com/badge/user/018cee13-789a-4312-ba87-bff7005ff31b/project/0cc27a01-c405-41dd-917b-ddfe552a2ca8.svg)](https://wakatime.com/badge/user/018cee13-789a-4312-ba87-bff7005ff31b/project/0cc27a01-c405-41dd-917b-ddfe552a2ca8)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

Classic user vs computer Tic-Tac-Toe game on CLI

</div>

## Getting Started

This project is a simple implementation of the classic Tic-Tac-Toe game where the user plays against the computer. The computer makes random moves, and the game continues until there is a winner or a draw.

## Game Rules

- The computer plays using 'X's.
- The user plays using 'O's.
- The computer always makes the first move by placing an 'X' in the middle of the board.
- The board squares are numbered from 1 to 9, starting from the top-left corner and moving row by row.
- The user inputs their move by entering the number of the square they choose.
- The game ends when there is a winner or a draw.

## Example Session

```md
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

## How to Run

1. Ensure you have Python installed on your machine.
2. Clone this repository.
3. Navigate to the project directory.
4. Run the game using the following command:
    ```sh
    python main.py
    ```

## Project Structure

- [`assesment.md`](/assesment.md): Contains the project description and instructions.
- [`main.py`](/main.py): The main Python script that implements the game logic.
- [`README.md`](/README.md): This file, providing an overview of the project.

## Functions

- `display_board`: Displays the current state of the board.
- `enter_move`: Handles the user's move.
- `make_list_of_free_fields`: Generates a list of free fields on the board.
- `victory_for`: Checks if there is a winner.
- `draw_move`: Handles the computer's move.

## License
This project is licensed under the [MIT License](LICENSE).
