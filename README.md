# 🐍 Python Mini-Games Collection

A collection of simple games built with Python. This project explores how games can be created using basic programming concepts and libraries like `turtle` and `arcade`.

## 🎮 Games Included

### 1. Turtle Race
A fun race between turtles of different colors! The player bets on which turtle will win.

<div style="text-align: center;">
<img src=".\images\turtle_game.png" alt="Turtle Race" width="300"/>
</div>

- **Technologies**: `turtle`, `random`
- **How to Play**:
  1. Run the script.
  2. Enter your bet (choose a turtle color).
  3. Watch the turtles race!
  4. Find out if you win based on your bet.

### 2. Snake Game
A classic Snake game where you control the snake to collect food and avoid hitting the walls or yourself.

- **Technologies**: `turtle`
- **Game Features:**
  -  Move the snake using arrow keys: **Up**, **Down**, **Left**, and **Right**
  - Eat food to grow the snake
  - Score increases with each food item eaten
  - Game ends when the snake hits the wall or itself
  - Score is displayed and game over message shown when game ends

### 3. Pong Game
A simple recreation of the classic **Pong** arcade game using Python's `turtle` module. Two players control paddles to keep the ball in play and score points!

<div style="text-align: center;">
<img src=".\images\us_states_game.jpg" alt="US States Game" width="300"/>
</div>

- **Technologies**: `turtle`
- **Game Features**
  - Two-player game:
    - **Right Paddle**: Controlled with **Up** and **Down** arrow keys
    - **Left Paddle**: Controlled with **W** and **S** keys
  - Ball bounces off walls and paddles
  - Scoreboard updates when a player scores
  - Game ends when you close the window
 
### 4. U.S. States Guessing Game
This is a simple interactive Python game that challenges users to name all 50 U.S. states. When a correct state is guessed, its name appears on the map. The game ends when all states are guessed or the user exits.

- **Technologies**: `turtle`, `pandas`
- **Game Features:**
  - A blank U.S. map appears.
  - The player is prompted to guess state names.
  - If the answer is correct:
    - The name appears on the correct location of the map.
    - The score increases.
  - Typing **Exit** ends the game early and creates a CSV file with the missing states.
---

## 🛠️ Requirements

Make sure you have Python 3 installed.
