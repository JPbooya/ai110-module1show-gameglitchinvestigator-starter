# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- While playing the game I notice some of my guesses did not match the hints and also the new game did not properly reset the game. 

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input |             Expected Behavior |           Actual Behavior |                                Console Output / Error |
|-------|            -------------------|           -----------------|------------------------|
Guessed 60,      "Go higer" Hint 60 was to low      messaged showed but arrow showed wrong direction.     none
output was 80.

Clicked new game      Game resets fully             won/lost screen presisted, game was unplayable.       none
after winning a round

guessed a number        score goes down.            score results went up instead of down.                           none  

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
I used Claude Ai
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
One issue that me and the Ai worked on was when the Ai spotted a conversion bug on even attempts. The way I verified this was when playing the game on even attempts. The Ai suggested to remove the entire if/else block and replacing it with just a secret variable. The secret number was being converted into string which caused a int to string comparison to fail.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
Essenitally the Ai mislead to move the functions to logic_utils.py but the game was still showing wrong hints. I eventually found out that the old broken functions were still defined in app.py and overriding imports.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
After fixing the hint bugs, I ran the game and checked that guessing a number lower than the secret showed "GO HIGHER" and vice versa...
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  What I did was I ran the game after each fix to verify the behavior, I also ran pytests using command line ytest tests/test_game_logic.py -v and got the 5 tests passing
- Did AI help you design or understand any tests? How?
  Yes! The Ai suggested the structure of the tests and helped me understand that check_guess returns a tuple so you needed to unpack it with outcome, message =...
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
So essentially reruns is what makes the whole app run. It runs python scripts from top too bottom again and again. st.session_state are essenitally where you store things that you always want to remeber and stay what it does. Other than that everything resets.
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
adding fix comments and adding them every pytest that I run. Also commiting after every fix.
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
Veryifying more thorughly the Ai's work and suggestions.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
What I learned from the way how Ai's code work is, its a must to always double check its work. Bcause it makes mistakes and I think verifying its code manually is also a big help. We want too engineer the Ai and not us.
