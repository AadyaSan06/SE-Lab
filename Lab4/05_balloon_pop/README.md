# Balloon Pop Lab

## Overview

Balloon Pop is a single-player game developed using Python and Pygame. The objective is to pop falling balloons to earn points while avoiding missed balloons and managing the available lives within a limited time.

This project was completed as part of the Balloon Pop Lab to practice debugging, object-oriented programming, collision detection, game-state management, and timer implementation.

## Features Implemented

### 1. Fixed Click-Detection Bug

* Fixed the click-detection logic in `game/click_detection.py`.
* Updated the distance comparison so that clicks are correctly detected anywhere within a balloon's visible circular boundary.
* Balloons can now be popped without requiring pixel-perfect clicks near their centers.

### 2. Different Balloon Types

Implemented three types of balloons, each with a distinct color and scoring effect:

* **Normal Balloon:** Awards regular points.
* **Bonus Balloon:** Awards additional points.
* **Penalty Balloon:** Reduces the player's score or applies the defined penalty.

### 3. Lives and Miss System

* The player starts with 3 lives.
* Missing a balloon and allowing it to fall past the bottom of the screen costs one life.
* Popping a balloon does not cost a life, regardless of its type.
* The game ends when all lives are lost.

### 4. Timed Round

* Each round lasts 30 seconds.
* The remaining time is displayed on the screen.
* The game ends when the timer reaches zero or the player loses all lives.
* The final score is displayed when the round ends.
* Players can start a new round, resetting the score, lives, timer, and game state.

## Technologies Used

* **Python 3.10+**
* **Pygame**

## Installation and Execution

### Prerequisites

* Python 3.10 or later
* pip package manager

### Steps

1. Clone or download this repository.

2. Open a terminal in the project directory.

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the game:

   ```bash
   python main.py
   ```

## Controls

* **Left Mouse Click:** Pop a balloon.
* **Restart Option:** Start a new round after the current round ends, using the in-game restart control.

## Project Structure

```text
balloon-pop/
├── main.py
├── requirements.txt
├── README.md
└── game/
    ├── game_engine.py
    ├── balloon.py
    ├── click_detection.py
    └── renderer.py
```

## Testing and Verification

The completed game was tested to verify the following:

* Balloon clicks register correctly across the visible balloon area.
* Each balloon type applies its corresponding scoring effect.
* Missed balloons reduce the remaining lives.
* Popping balloons does not reduce lives.
* The round ends when the timer expires or all lives are lost.
* The final score is displayed, and a new round can be started with the game state reset.


**ChatGPT Conversation Link:** https://chatgpt.com/c/6abc79de-1cc0-83ee-b7cf-fd8607031f9f

## Conclusion

The Balloon Pop Lab was completed by fixing the click-detection bug and implementing different balloon types, a lives and miss system, and a timed round with restart functionality. The project demonstrates the use of Python and Pygame to build an interactive game with collision detection, scoring, and game-state management.
