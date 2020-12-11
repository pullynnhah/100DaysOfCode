## Higher Lower Game

# Instructions

Use your skills to create a higher lower game.
The first step is to divide your project into smaller tasks.

# Decomposition of the problem

1. Import the necessary methods:
- `os` to clear the screen after each round.
- `random` to randomly select the users to compare. 
- `game_art` for the ASCII art of the program.
- `game_data` for the data to get the users and know their info for the game.

2. Create a method to clean the screen for the next output.

3. Create a function that receives an element from `game_data.data` and prints a string for the user to see returning the number of followers from that user.

4. Create a variable to keep the indexes for the `game_data.data` elements. This variable will be used to randomly select a person only if she wasn't previously selected or if all the other persons have been selected before.  
    1. Create a function to set this variable so if its length goes to zero if recreates itself, making sure to not add the element already set to A.

5. Create a function that randomly select an element from `game_data.data`.

6. Create a function to compare two people follower count.
   
7. Create a game function that simulates the playing of the game.
