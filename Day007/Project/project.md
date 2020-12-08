# Hangman
Can also be considered as Challenge 5

# Instructions
Finish the Hangman game started on the Challenges.  
Use the ascii_art, and the list of words from the modules [hangman_art.py](hangman_art.py) and [hangman_words.py](hangman_words.py) respectively.

### TODO-1:
- Update the word list to use the 'word_list' from [hangman_words.py](hangman_words.py)
- Delete this line: `word_list = ["aardvark", "baboon", "camel"]`

### TODO-2:
- Import the stages from [hangman_art.py](hangman_art.py).

### TODO-3: 
- Import the logo from [hangman_art.py](hangman_art.py) and print it at the start of the game.
- Import loser and winner from [hangman_art](hangman_art.py) to display a message at the end of the game.
### TODO-4: 
- If the user has entered a letter they've already guessed, print the letter and let them know.

### TODO-5:
- If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.


# Example Output
```
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    
_ _ _ _ _
Enter a letter:> p
p _ p p _

  +---+
  |   |
      |
      |
      |
      |
=========
Enter a letter:> u
p u p p _

  +---+
  |   |
      |
      |
      |
      |
=========
Enter a letter:> y
p u p p y

  +---+
  |   |
      |
      |
      |
      |
=========

__   __                          _         _ 
\ \ / /  ___   _   _  __      __(_) _ __  | |
 \ V /  / _ \ | | | | \ \ /\ / /| || '_ \ | |
  | |  | (_) || |_| |  \ V  V / | || | | ||_|
  |_|   \___/  \__,_|   \_/\_/  |_||_| |_|(_)

```
```
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    
_ _ _ _ _
Enter a letter:> p
Ops! Letter: 'p' is not in the word.
_ _ _ _ _

  +---+
  |   |
  O   |
      |
      |
      |
=========
Enter a letter:> a
_ _ a _ _

  +---+
  |   |
  O   |
      |
      |
      |
=========
Enter a letter:> u
Ops! Letter: 'u' is not in the word.
_ _ a _ _

  +---+
  |   |
  O   |
  |   |
      |
      |
=========
Enter a letter:> l
Ops! Letter: 'l' is not in the word.
_ _ a _ _

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
Enter a letter:> a
_ _ a _ _

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
Enter a letter:> b
Ops! Letter: 'b' is not in the word.
_ _ a _ _

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
Enter a letter:> u
Ops! Letter: 'u' is not in the word.
_ _ a _ _

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
Enter a letter:> e
Ops! Letter: 'e' is not in the word.
_ _ a _ _

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========

__   __                _                    _ 
\ \ / /  ___   _   _  | |  ___   ___   ___ | |
 \ V /  / _ \ | | | | | | / _ \ / __| / _ \| |
  | |  | (_) || |_| | | || (_) |\__ \|  __/|_|
  |_|   \___/  \__,_| |_| \___/ |___/ \___|(_)

The word was: khaki!
```
OBS.: `>` represents input
