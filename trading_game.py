#
# The Trading Game Project v0.2
#

import os
import time
from random import randint
import thread

# Print title
print ' _______ _            _______            _ _                _____                      '
print '|__   __| |          |__   __|          | (_)              / ____|                     '
print '   | |  | |__   ___     | |_ __ __ _  __| |_ _ __   __ _  | |  __  __ _ _ __ ___   ___ '
print '   | |  | `_ \ / _ \    | | `__/ _` |/ _` | | `_ \ / _` | | | |_ |/ _` | `_ ` _ \ / _ \\'
print '   | |  | | | |  __/    | | | | (_| | (_| | | | | | (_| | | |__| | (_| | | | | | |  __/'
print '   |_|  |_| |_|\___|    |_|_|  \__,_|\__,_|_|_| |_|\__, |  \_____|\__,_|_| |_| |_|\___|'
print '                                                    __/ |                              '
print '                                                   |___/                               v0.2 beta'
print '                          $$$$$             $$$$$             $$$$$      '
print '                          $:::$             $:::$             $:::$      '
print '                      $$$$$:::$$$$$$    $$$$$:::$$$$$$    $$$$$:::$$$$$$ '
print '                    $$::::::::::::::$ $$::::::::::::::$ $$::::::::::::::$'
print '                   $:::::$$$$$$$::::$$:::::$$$$$$$::::$$:::::$$$$$$$::::$'
print '                   $::::$       $$$$$$::::$       $$$$$$::::$       $$$$$'
print '                   $::::$            $::::$            $::::$            '
print '                   $::::$      +-----------------------------+           '
print '                   $:::::$$$$$$|     Press ENTER to Buy      |$$$$$$$$   '
print '                    $$:::::::  |  Press ENTER again to Sell  |    ::::$$ '
print '                      $$$$$$$$$+-----------------------------+$$$$$:::::$'
print '                               $::::$            $::::$            $::::$'
print '                               $::::$            $::::$            $::::$'
print '                   $$$$$       $::::$$$$$$       $::::$$$$$$       $::::$'
print '                   $::::$$$$$$$:::::$$::::$$$$$$$:::::$$::::$$$$$$$:::::$'
print '                   $::::::::::::::$$ $::::::::::::::$$ $::::::::::::::$$ '
print '                    $$$$$$:::$$$$$    $$$$$$:::$$$$$    $$$$$$:::$$$$$   '
print '                         $:::$             $:::$             $:::$       '
print '                         $$$$$             $$$$$             $$$$$       '

# Prompt user to begin
print ''
begin = raw_input('So You Think You Can Trade? (Press ENTER to begin): ')

def game_loop(begin):
    # Game loop
    if begin == "":
        # Initialize game variables
        WIDTH = 40 
        HEIGHT = 20

        # Track the horizontal position on screen
        offset = 0

        # Store prices
        prices = []

        # Execution prices
        buy = None 
        sell = None
        profit = 0

        # Game score
        score = 0
        
        # Start round 1
        round = 1

        # Set game ending condition
        total_rounds = 100

        # Start separate thread to capture user input
        L = []
        thread.daemon = True
        thread.start_new_thread(input_thread, (L,))

        # Game loop
        while round <= total_rounds:
            # If <CR> key is pressed
            if L:
                if not buy:
                    # If not holding any position, buy
                    print 'Bought at ' + str(prices[0])
                    buy = prices[0]
                    profit = 0
                else:
                    # If holding a position, sell
                    sell = prices[0]
                    profit = sell - buy

                    print 'Bought at', str(buy)
                    print 'Sold at', str(sell)
                    print 'Profit:', str(profit)

                    score += profit

                    buy = None

                # Reset event listener thread
                L = []
                thread.daemon = True

                thread.start_new_thread(input_thread, (L,))
                time.sleep(1)

            # Redraw screen
            os.system('cls')

            # Generate random stock price
            prices = [randint(1, 20)] + prices

            print 'Score:', '$' + str(score)

            if not sell:
                print 'HINT: Press ENTER to Buy and Sell'

            # Print chart line by line, moving right to left
            for h in range(HEIGHT, 0, -1):
                line = ''
                for w in range(WIDTH):
                    if w < len(prices) and h <= prices[w]:
                        line = '##' + line
                    else:
                        line = '  ' + line

                # Y axis label
                line += '||' + str(h).rjust(2)

                # Mark buy price
                if buy == h:
                    line += ' BUY'

                # Mark buy/sell and profit indicator
                if profit > 0 and (h >= (sell - profit) and h <= sell):
                    if h == (sell - profit):
                        line += ' BUY'
                    elif h == sell:
                        line += ' SELL'
                    else:
                        line += ' ++'
                elif profit < 0 and (h <= (sell - profit) and h >= sell):
                    if h == (sell - profit):
                        line += ' BUY'
                    elif h == sell:
                        line += ' SELL'
                    else:
                        line += ' --'

                print line

            # Footer
            print '==' * WIDTH
            print 'Round:', str(round), '/', str(total_rounds)
            print ''

            offset += 1

            # Continue scrolling once screen is filled
            if offset > WIDTH:
                del prices[-1]

            # Increment rounds counter
            round += 1

            # Screen redraw delay
            time.sleep(0.05)

        # Loop ends
        os.system('cls')
        print '   _____                         ____                 ' 
        print '  / ____|                       / __ \                '
        print ' | |  __  __ _ _ __ ___   ___  | |  | |_   _____ _ __ '
        print ' | | |_ |/ _` | `_ ` _ \ / _ \ | |  | \ \ / / _ \ `__|'
        print ' | |__| | (_| | | | | | |  __/ | |__| |\ V /  __/ |   '
        print '  \_____|\__,_|_| |_| |_|\___|  \____/  \_/ \___|_|   '
        print ''
        print 'You made', '$' + str(score)
        print ''
        print 'You did NOT beat Steve\'s score'
        print ''
        print 'Press ENTER to continue'

        begin = raw_input('Do you want to play again? (Press ENTER to replay): ')
        game_loop(begin)
    else:
        print 'Too Bad'

def input_thread(L):
    # Thread to listen for user input
    raw_input()
    L.append(None)

# Start game
game_loop(begin)
