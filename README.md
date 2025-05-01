# Blackjack Game 🃏

A simple console-based Blackjack card game implemented in Python 💻. The game allows a player to compete against a computer dealer, with features like random card dealing, ace value adjustment (1 or 11), and standard Blackjack rules 🎲.

## Features ✨
- 🕹️ Play Blackjack against a computer dealer.
- ♠️ Automatic ace value adjustment to prevent busting.
- 🖥️ Clear console interface with game status updates.
- 🃟 Option to hit or stand during your turn.
- 🤖 Computer follows standard dealer rules (hits until score is at least 17).

## Prerequisites 📋
- 🐍 Python 3.x installed on your system.

## Installation ⚙️
1. Clone the repository:
   ```bash
   git clone https://github.com/yukamenes/BlackjackGame.git
   ```
2. Navigate to the project directory:
   ```bash
   cd BlackjackGame
   ```

## Usage 🎮
1. Run the game by executing the main script:
   ```bash
   python main.py
   ```
2. Follow the prompts:
   - Type `y` to start a new game or `n` to exit.
   - During the game, type `y` to hit (draw another card) or `n` to stand (pass).
3. The game will display your cards, score, and the computer's first card. After the round, it shows the final hands and declares the winner 🏆.

## Project Structure 📂
- `main.py`: The main Python script containing the game logic 🐍.
- `.gitignore`: Ignores Python cache files and bytecode 🗑️.
- `README.md`: This file, providing project documentation 📝.
- `LICENSE`: CC0 1.0 Universal Public Domain Dedication license 📜.

## Rules 🎰
- 🎯 The goal is to get a hand value as close to 21 as possible without going over.
- 🔢 Number cards (2-10) are worth their face value.
- 👑 Face cards (Jack, Queen, King) are worth 10.
- 🅰️ Aces are worth 1 or 11, automatically adjusted to avoid busting.
- 🤖 The computer dealer must hit until their score is at least 17.
- 💥 If you or the dealer exceeds 21, that player loses.
- 🤝 If both have the same score, it's a draw.

## Contributing 🤝
Contributions are welcome! Feel free to open an issue or submit a pull request with improvements or bug fixes 🚀.

## License 📄
This project is released under the [CC0 1.0 Universal (CC0 1.0) Public Domain Dedication](https://creativecommons.org/publicdomain/zero/1.0/) 🌍. You are free to use, modify, and distribute this project without any restrictions. See the `LICENSE` file for details.
