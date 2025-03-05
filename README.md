# ♟️ Terminal Chess

**Terminal Chess** is a simple chess game playable in the command line. It allows two players to compete using UCI notation for moves. The game supports basic move validation and detects checkmate.

## 🚀 Features
- Play chess in the terminal
- Supports UCI move format (e.g., `e2e4`)
- Detects checkmate and game over conditions
- Simple and lightweight

## 🛠 Installation 
1. Clone the repository:
   ```bash  
   git clone https://github.com/yourusername/terminal-chess.git
   cd terminal-chess
   ```
2. Install dependencies:
   ```bash
   pip install chess 
   ``` 

## 🎮 How to Play
1. Run the script:
   ```bash
   python terminal_chess.py
   ```
2. Enter moves in **UCI format** (e.g., `e2e4`).
3. Play until checkmate or type `exit` to quit.

## 📌 Example Gameplay
```
  a b c d e f g h
8 r n b q k b n r 8
7 p p p p p p p p 7
6 . . . . . . . . 6
5 . . . . . . . . 5
4 . . . . . . . . 4
3 . . . . . . . . 3
2 P P P P P P P P 2
1 R N B Q K B N R 1
  a b c d e f g h

Enter your move (in UCI format, e.g., e2e4):
```

## 📜 Future Improvements
- Add AI opponent using **Stockfish**
- Implement a graphical interface
- Save and load games

## 📄 License
This project is licensed under the MIT License.

