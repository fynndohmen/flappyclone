# Flappy Clone

A simple Flappy Bird–style game written in Python with Pygame.  
Fly the bird through an endless field of pipes while a parallax background scrolls by.

---

## Features

- Start screen with **“Start Game”** button
- Smooth **parallax scrolling** background with multiple layers
- **Gravity & jump**: bird falls down and flaps up with spacebar
- Procedurally generated **top & bottom pipe pairs** with a gap
- Endless scrolling pipes from right to left
- **Collision reset**: on collision, the game returns to the start screen

---

## Requirements

- Python 3.10+ (earlier 3.x versions will probably work too)
- [Pygame](https://www.pygame.org/news)

Install Pygame with:

pip install pygame
How to Run
Clone the repository:

git clone https://github.com/fynndohmen/flappyclone.git
cd flappyclone
Make sure the assets/ folder (bird sprite, pipe sprite, background layers, etc.) is in the project directory.

Run the game:

python game.py
(or whatever your main file is named, e.g. main.py if you split it later)

Controls
Mouse Left Click – click “Start Game” on the start screen to begin.

Spacebar – flap the bird upwards.

Window close button (X) – quit the game.

If the bird collides with a pipe, the game resets back to the start screen.

Project Structure (typical)

flappyclone/
├─ assets/
│  ├─ bird.png
│  ├─ pipe.png
│  ├─ layer-1.png
│  ├─ layer-2.png
│  ├─ layer-3.png
│  ├─ layer-4.png
│  └─ start_background.jpg
├─ game.py
└─ README.md
game.py – main game loop, states (start / play), background, bird, pipes.

assets/ – sprites and background images.

Game States
The game uses a simple state system:

start – shows the start screen, background image, and “Start Game” button.

play – runs the actual game:

parallax background layers scrolling

bird affected by gravity and jumps on space

pipes spawning at intervals with random vertical gap positions

collision with a pipe returns to start
