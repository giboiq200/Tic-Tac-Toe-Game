# Tic-Tac-Toe-Game
A simple tic tac toe game made with python
# Tic Tac Toe — Tkinter Version

This project is a simple **Tic Tac Toe (X/O)** game built using **Python** and the **Tkinter** GUI library.
It allows two players to play against each other on the same computer, with automatic turn switching, win detection, and a restart option.

---

## 🎮 Features

* **Interactive 3×3 game board** using Tkinter buttons
* **Randomly selected starting player** (X or O)
* **Turn indicator** displayed at the top of the window
* **Win detection** for:

  * All rows
  * All columns
  * Both diagonals
* **Automatic disabling of buttons** after a win
* **Reset button** to restart the game at any time
* Clean and simple graphical interface

---

## 📦 Requirements

To run this game, you need:

* **Python**
* **Tkinter** (included with most Python installations)

No external libraries are required.

---

## ▶️ How to Run

1. Make sure you have Python installed.
2. Save the provided code to a file, for example:

   ```
   tic_tac_toe.py
   ```
3. Run the file:

   ```bash
   python tic_tac_toe.py
   ```

The Tic Tac Toe window will open immediately.

---

## 🧠 How It Works

### **1. Turn System**

A random number (1 or 2) is generated to decide whether **X** or **O** starts.
The label at the top updates dynamically after each move.

### **2. Button Grid**

A 3×3 matrix of Tkinter buttons is created.
Each button calls:

```python
klik(row, column)
```

This function:

* Places **X** or **O** depending on the current turn
* Switches turn
* Checks for a winner
* Disables the board if someone wins

### **3. Winner Detection**

`proveri_pobednika()` checks:

* All rows
* All columns
* Both diagonals

If three matching (non-empty) symbols are found, it returns the winner.

### **4. Reset**

The **Reset** button calls:

```python
restartGame()
```

which clears and re-enables the board.

---

## 📁 File Structure

Everything is contained in one Python file:

```
tic_tac_toe.py
```
---

## 🛠️ Customization Ideas

* Add score tracking
* Add AI opponent (minimax algorithm)
* Add animations or sound effects
* Improve styling and layout
* Add draw detection

---

## 📜 License

This project is free to use, modify, and distribute.

---
