# Bloomberg Coding Workshop 2016

## Maze Runner Project
Implement controls to navigate through a maze

### Project Instructions
In this project, we will build user controls to navigate through a pre-defined maze.  The maze will be in a plain text file consisting of the following characters:

    'X': A wall that the user cannot go through
    ' ': A possible route (space)
    'S': The starting spot for the player
    'E': The ending spot for the player

Each maze line will end with a newline escape sequence (`\n`).  Load the maze into a 2-dimensional list, recording the start and end position.  Create a function to print the maze to the screen.  Add player controls to allow the user to move up, down, left or right.  After each move, re-print the maze showing the player's new position.  Make sure that the player cannot go through walls or back out the start position.  The game ends when the player reaches the exit.

### Files

Filename | Description
---|---
maze.py | Maze program
maze1.txt | Easy maze to navigate
maze2.txt | Medium maze to navigate
maze3.txt | Hard maze to navigate

### External Libraries Required
None

### Key Concepts Used
- Variables
- For Loop
- While Loop
- Opening Files
- Escape Sequence (Newline)
- Functions
- If-Then-Else
- List
- 2-Dimensional List
- Operator +=

### Code Walkthrough

#### Function to Print Maze
Create a function that takes the maze object (a 2-D list) and print to screen.  Note: this function must be defined before it is used later on in the program.  Loop through each line and print each character to the screen, with a space in-between.  We use Python's built-in string join() method to create the spaces.  Reference [here](https://docs.python.org/2/library/stdtypes.html#str.join).

``` python
# Define function to print maze to screen
def print_maze(maze):
    """Prints the maze object to the screen

    The maze object is a 2-dimensional list.
    """
    for line in maze:
        print ' '.join(line)
```

#### Setup
Open the maze text file and create a list to hold the layout of the maze.

``` python
# Open maze file
maze_file = open('maze3.txt')

# List to hold the maze
maze = []
```

Create variables to hold the player position and exit position.  Note: the first player position will also be the starting position.

``` python
# Player position (and start position)
pos_x = -1
poxY = -1

# Exit position
exit_x = -1
exit_y = -1
```

#### Parse Maze text file into 2-D List
Loop through the maze file, evaluating one line at a time.  Use a counter, `line_ctr`, to track which line is being evaluated.  Create a list that will hold the characters of each line.  When the next line is being evaluated, the list is reset to empty.

``` python
# Start with the first line
line_ctr = 0

# Loop through each line of file
for line in maze_file:
    # Temporary list to hold each line
    maze_line = []
```

Loop through the line, evaluating each character.  Use a counter, `char_ctr` to track the position of the character being evaluated.  

``` python
    # Start with the first character
    char_ctr = 0

    # Loop through each character in the line
    for character in line:
```

First, check to see if we have reached the end of the line.  Look for the newline escape sequence (`\n`).

``` python
        # Check if we are at the end of the line
        if character != '\n':
```

If not at the end, check if the character is the start position 'S'.  If so, set the player coordinates, `pos_x` and `pos_y` to the line and character indices.  Also replace the 'S' with the current player position indicator 'O'.

``` python
            # Check for map start and end positions
            if character == 'S':
                # Map start position
                pos_x = char_ctr
                pos_y = line_ctr
                # Place the player indicator, 'O', at the start position
                character = 'O'
```

If the character is the end position 'E', then set the exit coordinates.  

``` python
            elif character == 'E':
                # Map end position
                exit_x = char_ctr
                exit_y = line_ctr
```

Append the character to the line list and evaluate the next character.

``` python
            # Add character to the line list
            maze_line.append(character)

        # Evaluate next character
        char_ctr += 1
```

When all characters of the line are evaluated, append the entire line list to the maze list.  And evaluate the next line.

``` python
    # Add finished line to the maze list
    maze.append(maze_line)

    # Evaluate next line
    line_ctr += 1
```

#### Game Loop
At the beginning of the loop, print the maze to the screen using our `print_maze` function.

``` python
# Game loop, runs until break is reached
while True:
    # Print maze to the screen
    print_maze(maze)
```

Check if the player has reached the exit position.  If so, end the game.

``` python
    # If the player position are at the exit coordinates, game ends
    if (pos_y == exit_y and pos_x == exit_x):
        print 'Congratulations, you made it out of the maze!'
        break
```

Prompt the user to make a move.

``` python
    # Prompt user to make a move
    userInput = raw_input('Please enter a move (w/a/s/d): ')
```

We need to make sure the player's move is valid.  If so, then change the player's position accordingly.  Note we also refresh the player's position indicator 'O'.

``` python
    # Erase old player indicator
    maze[pos_y][pos_x] = ' '

    # User tries to go up
    if (userInput == 'w' and pos_y != 0 and maze[pos_y - 1][pos_x] != 'X'):
        pos_y = pos_y - 1

    # User tries to go left
    elif (userInput == 'a' and pos_x != 0 and maze[pos_y][pos_x - 1] != 'X'):
        pos_x = pos_x - 1
        
    # User tries to go down
    elif (userInput == 's' and pos_y != len(maze) - 1 and maze[pos_y + 1][pos_x] != 'X'):
        pos_y = pos_y + 1
        
    # User tries to go right
    elif (userInput == 'd' and pos_x != len(maze[pos_y]) - 1 and maze[pos_y][pos_x + 1] != 'X'):
        pos_x = pos_x + 1
    
    # Invalid input
    else:
        print('Invalid move!')

    # Add new player indicator
    maze[pos_y][pos_x] = 'O'
```

### Extending this Project
- Generate a new maze to play each time the program is run, more mazes can be generated [here](http://www.delorie.com/game-room/mazes/genmaze.cgi)
- Refresh the screen after each move (ie., os.system('cls').  Reference [here](https://docs.python.org/2/library/os.html#os.system)
- Create a scoring system, for example, tracking the number of player moves or turns to reach the end of the maze.
