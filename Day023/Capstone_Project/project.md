# Turtle Crossing Game

## Instructions

###Difficulty Normal:
Use all Steps to complete the project.

###Difficulty Hard:
Use only Steps 1 and 2 to complete the project.

###Difficulty Expert:
Only use Step 1 to complete the project.

### Step 1 
A turtle moves forwards when you press the "Up" key. It can only move forwards, not back, left or right.

## Step 2
Cars are randomly generated along the y-axis and will move from the right edge of the screen to the left edge.

### Step 3
When the turtle hits the top edge of the screen, it moves back to the original position, and the player levels up. On the next level, the car speed increases.

### Step 4
When the turtle collides with a car, it's game over and everything stops. 

### Step 5
Create a turtle player that starts at the bottom of the screen and listen for the "Up" keypress to move the turtle north. If you get stuck, check the video walkthrough in Step 3.

### Step 6
Create cars that are 20px high by 40px wide that are randomly generated along the y-axis and move to the left edge of the screen. No cars should be generated in the top and bottom 50px of the screen (think of it as a safe zone for our little turtle). Hint: generate a new car only every 6th time the game loop runs. If you get stuck, check the video walkthrough in Step 4.

## Step 7 
Detect when the turtle player collides with a car and stop the game if this happens. If you get stuck, check the video walkthrough in Step 5.

## Step 8
Detect when the turtle player has reached the top edge of the screen (i.e., reached the FINISH_LINE_Y). When this happens, return the turtle to the starting position and increase the speed of the cars. Hint: think about creating an attribute and using the MOVE_INCREMENT to increase the car speed. If you get stuck, check the video walkthrough in Step 6.

## Step 9
Create a scoreboard that keeps track of which level the user is on. Every time the turtle player does a successful crossing, the level should increase. When the turtle hits a car, GAME OVER should be displayed in the centre. If you get stuck, check the video walkthrough in Step 7.
