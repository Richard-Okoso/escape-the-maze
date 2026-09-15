#   check positions
#   check if element at position is not a wall
#   movement (w,a,s,d)
#   check if player escaped
#   update movements
#   an 8 x 8 grid maze
#   ask if user still wants to play

maze:list = [
    ["#", "#", "#", "#", "#", "#", "#"],
    ["#", "S", " ", " ", "#", " ", "#"],
    ["#", "#", "#", " ", "#", " ", "#"],
    ["#", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", "#", "E", "#"],
    ["#", "#", "#", "#", "#", "#", "#"]
]   #   our maze to be displayed





def game():

    player_row: int = 1
    player_column: int = 1
    trial: int = 0  # checking the number of trials an individual made

    print("""
    \n Use:
     W for up
     A for left
     S for down
     D for right
    """)
    while True:  # looping through until escaped

        for brick in maze:
            print(" ".join(brick))  # printing our maze


        choice: str = input("\nYour choice> ").lower()  # getting our movement option
        new_row: int = player_row
        new_column: int = player_column

        """ checking our options """
        if choice == 'w':  # making our up movement
            new_row -= 1
        elif choice == 'a':  # making our left movement
            new_column -= 1
        elif choice == 's':  # making our down movement
            new_row += 1
        elif choice == 'd':  # making our right movement
            new_column += 1
        else:
            print('Unknown option')

        trial += 1

        """ checking if position is a wall"""
        if maze[new_row][new_column] == '#':
            print('You hit a wall\n')
            continue

        """ checking if player escaped successfully """
        if maze[new_row][new_column] == 'E':
            print('You escaped successfully\n')
            break

        """ updating our movements """
        player_row = new_row
        player_column = new_column

    print(f'Your won and you did that in {trial} moves ')


def main():
        """ calling the game function """
        game()


        while True: # if user still chooses to play

            x :str = input('Do you wish to play again (Y/N)> ').lower()  # user interest

            """ checking user interest """
            if x == 'y':
                game()
            elif x == 'n':
                print('Thank you for playing')
                break
            else:
                print('Unknown option')


if __name__ == "__main__":
    main()