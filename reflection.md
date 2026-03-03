# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- It looked fine when we started, the only way to input numbers is only by using the button, entering didn't work. The show hint toggle doesn't turn back on after turning it off.

- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

---
 - when the correct number was 61, I started guessing 100->50->25->12->6->3->1 and the hint always states go lower eventhough the number was 61.
 - The game won't restart at all when I tap the new game button; it stays in the current state if I finish all 7 attempts, and it is game over. The same happens if you guess the right number and you win.


## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Claude AI
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.


## 6. The hint i would give to students

Start by playing the game before reading any code, try guessing and document any issues you notice, whether minor or major. Also think about different cases like giving invalid input or entering input in different ways (keyboard, mouse).

Once you spot something wrong, open app.py and find the function responsible, then use AI to explore and confirm the bug.

When prompting AI, ask "What could cause X behavior in this function?" rather than just "Fix this" and you'll get much more useful insights, and you'll actually understand the bug yourself before moving to Phase 2.