HEAD
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

The game is a number guessing game where the user tries to guess a secret number, with hints telling them whether their guess is too high or too low. The game runs on Streamlit, and the user has a limited number of attempts to guess correctly.


When I first ran the game, I encountered the following bugs:
The secret number kept changing every time I clicked "Submit". This issue was related to how Streamlit handles state. Without storing the secret number in session state, it got reset every time the app reran.
The game would tell me to "Go HIGHER" when my guess was too high, and "Go LOWER" when it was too low. This was a logic error that needed to be corrected in the game’s flow.
I used Streamlit's session state to store the secret number. This way, the number doesn’t reset every time the user clicks "Submit". I also used session state for other variables like the score and the number of attempts.
I fixed the conditional statements for providing hints so that the game would tell the player to go "Higher" or "Lower" correctly. This involved ensuring that the game checked whether the guess was greater or less than the secret number before giving a hint.
I moved the logic into a separate file, logic_utils.py, to keep the code organized and easier to maintain. I also added some tests using pytest to check if the key functions were working as expected. These tests ensured that the guess checking and score updating logic were correct.



## 📸 Demo

I added the screenshot to the github. It's name Game.png. I am not able to add screenshot directly into my ReadMe file. You can see in the screenshot it says I won the game
=======
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
- [ ] Detail which bugs you found.
- [ ] Explain what fixes you applied.

## 📸 Demo

- [ ] [Insert a screenshot of your fixed, winning game here]

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
>>>>>>> ba0d1ecd2a3358c4a2f9c1299fe8e8fd59097f02
