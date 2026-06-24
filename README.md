# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose.
A number guessing game where the player tries to guess a secret number within a limited number of attempts. The player receives hints after each guess and a score that updates based on performance.

- [ ] Detail which bugs you found.
Found 6 bugs including backwards hints, string conversion on even attempts, New Game not resetting status/history, hardcoded difficulty range, score increasing on wrong guesses, and attempts starting at 1 instead of 0.

- [ ] Explain what fixes you applied.
Fixed hint messages in check_guess, removed string conversion bug, fixed New Game to reset status/history and use correct difficulty range, fixed score to always decrease on wrong guesses, and fixed attempts to start at 0.



## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. User selects "Normal" difficulty (range 1-100, 8 attempts)
2. User enters a guess of 40 → Game returns "Go HIGHER" (secret is higher)
3. User enters a guess of 70 → Game returns "Go LOWER" (secret is lower)
4. Score decreases by 5 after each wrong guess
5. User enters a guess of 55 → "🎉 Correct!" Game ends with final score displayed
6. User clicks "New Game" → Game fully resets with new secret number

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

pytest tests/test_game_logic.py -v
======================= test session starts =======================
platform darwin -- Python 3.12.0, pytest-9.1.1, pluggy-1.6.0 -- /Library/Frameworks/Python.framework/Versions/3.12/bin/python3.12
cachedir: .pytest_cache
rootdir: /Users/johncarloperez/Desktop/game-glitch-investigate
plugins: anyio-4.13.0
collected 5 items                                                 

tests/test_game_logic.py::test_winning_guess PASSED         [ 20%]
tests/test_game_logic.py::test_guess_too_high PASSED        [ 40%]
tests/test_game_logic.py::test_guess_too_low PASSED         [ 60%]
tests/test_game_logic.py::test_update_score_wrong_guess PASSED [ 80%]
tests/test_game_logic.py::test_parse_guess_invalid PASSED   [100%]

======================== 5 passed in 0.02s ========================

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
