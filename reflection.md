# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

Hints were inconsistent – When guessing too high, the game sometimes said “Go HIGHER!” instead of “Go LOWER!” because the secret number is converted to a string every other attempt, which breaks comparisons.
Score behaves unpredictably – Points sometimes increased or decreased in unexpected ways, even going negative, due to the logic in update_score that depends on even/odd attempts.
Game doesn’t always end – Reaching the maximum attempts didn’t always stop the game, again caused by the secret number sometimes being a string and confusing the check_guess function.


## 2. How did you use AI as a teammate?

Correct suggestion: Copilot suggested moving all core game logic into logic_util.py. This made the code cleaner and easier to test.
Incorrect/misleading suggestion: Copilot initially suggested hints logic that sometimes reversed messages. I corrected them manually to match game behavior.

---

## 3. Debugging and testing your fixes

I first identified glitches in hints, scoring, and game-ending logic. I refactored the core game functions into logic_util.py and updated the hint and score logic. I wrote automated tests and confirmed the fixes worked. I also manually played the game to ensure the hints, scores, and attempt limits behaved correctly.

---

## 4. What did you learn about Streamlit and state?

I learned that Streamlit keeps track of variables across reruns. This allows the game to remember the secret number, score, attempts, and history even when the page refreshes. Managing state carefully is crucial because improper updates can cause bugs, like hints or scores showing incorrectly.

---

## 5. Looking ahead: your developer habits

I realized the importance of separating logic from UI. Moving game logic to a separate file made it easier to test and debug. I also learned to rely on tests and careful observation before accepting AI suggestions. Documenting every change helps keep track of reasoning and makes collaboration with AI more effective.


## 6. The hint i would give to students

Always test your game with multiple inputs and difficulty levels before assuming it works. Pay attention to how state changes across attempts. Separating logic from interface and writing simple tests saves a lot of debugging time.