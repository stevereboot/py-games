import os
import time
from random import randint

import sys  # Debugging

def main():
    # Title

    print '            ______ _______ ______ ______    _______ ______  ______ __  __'
    print '           / __  //__  __// __  // __  /   /__  __// __  / / ____// / / /'
    print '          / / /_/   / /  / /_/ // /_/ /      / /  / /_/ / / /__  / //`/`'
    print '          _\ \     / /  / __  //   __/      / /  /   __/ / __ / /  `/`'
    print '        / /_/ /   / /  / / / // /\ \       / /  / /\ \  / /___ / /\ \\'
    print '       /_____/   /_/  /_/ /_//_/  \_\     /_/  /_/  \_\/_____//_/  \_\\'
    print '               ____        _   _   _           _     _       _ '
    print '              |  _ \      | | | | | |         | |   (_)     | |'
    print '              | |_) | __ _| |_| |_| | ___  ___| |__  _ _ __ | |'
    print '              |  _ < / _` | __| __| |/ _ \/ __| `_ \| | `_ \| |'
    print '              | |_) | (_| | |_| |_| |  __/\__ \ | | | | |_) |_|'
    print '              |____/ \__,_|\__|\__|_|\___||___/_| |_|_| .__/(_)'
    print '                                                      | |      '
    print '                                                      |_|      v0.1 beta'
    print ''
    print '                                _____..---========+*+==========---.._____'
    print '   ______________________ __,-=`=====____  =================== _____=====`='
    print '  (._____________________I__) - _-=_/    `---------=+=--------`'
    print '      /      /__...---====`---+---_`'
    print '     `------`---.___ -  _ =   _.-`'
    print '                    `--------`'
    print '                       +-----------------------------+'
    print '                       |     Game Types:             |'
    print '                       |     1. Single-Player        |'
    print '                       |     2. Two-Player           |'
    print '                       |     3. AI vs AI             |'
    print '                       +-----------------------------+'
    print ''

    # Prompt user to choose game type
    type = raw_input('Choose Game Type (Enter 1, 2 or 3): ')

    # Define game parameters
    BOARD_SIZE = 10
    SHIP_COUNT = 2

    SHIP_LENGTH = 3

    p1_board = []
    p2_board = []

    p1_radar = []
    p2_radar = []

    p1_ships = []
    p2_ships = []

    ship_names = ['USS Adelphi', 'USS Agamemnon', 'USS Ahwahnee', 'USS Ajax', 'USS Akagi', 'USS Al-Batani', 'USS Albert Einstein', 'USS Aleo', 'USS Alka-Selsior', 'USS Antares', 'USS Antares', 'USS Apollo', 'USS Appalachia', 'USS Archer', 'USS Ariel', 'USS Aries', 'USS Armstrong', 'USS Atlantis', 'USS Baton Rouge', 'USS Bellerophon', 'USS Berlin', 'USS Biddeford', 'USS Biko', 'USS Billings', 'USS Bonaventure', 'USS Bonchune', 'USS Bozeman', 'USS Bradbury', 'USS Brattain', 'USS Budapest', 'USS Buran', 'USS Cairo', 'USS Callisto', 'USS Carolina', 'USS Centaur', 'USS Challenger', 'USS Charleston', 'USS Chekov', 'USS Chicago', 'USS Clavyn', 'USS Clayton', 'USS Clement', 'USS Cochrane', 'USS Columbia', 'USS Concord', 'USS Constantinople', 'USS Constellation', 'USS Copernicus', 'USS Cortez', 'USS Crazy Horse', 'USS Crockett', 'USS Curry', 'USS Da-Teplan', 'USS Defiant', 'USS Denver', 'USS Destiny', 'USS D\'hjty', 'USS Discovery', 'USS Donovan', 'USS Drake', 'USS Eagle', 'USS Elkins', 'USS Elmer Fudd', 'USS Emden', 'USS Endeavour', 'USS Entente', 'USS Enterprise', 'USS Equicon', 'USS Equinox', 'USS Essex', 'USS Excalibur', 'USS Excelsior', 'USS Exeter', 'USS Farouk El-Baz', 'USS Farragut', 'USS Fearless', 'USS Firebrand', 'USS Fleming', 'USS Fredrickson', 'USS Galaxy', 'USS Gallico', 'USS Gander', 'USS Gandhi', 'USS Ganges', 'USS Ganymede', 'USS Gettysburg', 'USS G\'Mat', 'USS Goddard', 'USS Gorkon', 'USS Gremlin', 'USS Grissom', 'USS Hathaway', 'USS Havana', 'USS Heart of Gold', 'USS Helin', 'USS Hera', 'USS Hermes', 'USS Hispaniola', 'USS Hokule\'a', 'USS Honshu', 'USS Hood', 'USS Horatio', 'USS Horizon', 'USS Hornet', 'USS Huron', 'USS Intrepid', 'USS James Fennimore Cooper', 'USS Jenolan', 'USS John F. Kennedy', 'USS John Muir', 'USS Kearsarge', 'USS Kelvin', 'USS K\'Marco', 'USS Kongo', 'USS Korolev', 'USS Kyushu', 'USS Lakota', 'USS Lalo', 'USS Lantree', 'USS LaSalle', 'USS Leeds', 'USS Lexington', 'USS Liberator', 'USS Livingston', 'USS Madison', 'USS Malone', 'USS Mare Tranquillitatis',
                  'USS Maryland', 'USS Matte Fringe', 'USS Max Plank', 'USS Mayflower', 'USS Mekong', 'USS Melbourne', 'USS Merrimac', 'USS Minnow', 'USS Min\'ow', 'USS Monitor', 'USS Musashi', 'USS Mustang', 'USS Nash', 'USS Nautilus', 'USS Neil Armstrong', 'USS Newton', 'USS Niels Bohr', 'USS Nightwing', 'USS Nobel', 'USS Noble', 'USS Non Sequitur', 'USS Northridge', 'USS Nova', 'USS Oberth', 'USS Odele', 'USS Odyssey', 'USS Okinawa', 'USS Olympia', 'USS Omaha Nebraska', 'USS Orinoco', 'USS Pasteur', 'USS Pegasus', 'USS Peterson', 'USS Philadelphia', 'USS Phoenix', 'USS Portland', 'USS Potemkin', 'USS Princeton', 'USS Prokofiev', 'USS Prometheus', 'USS Proxima', 'USS Pueblo', 'USS Puget Sound', 'USS Raging Queen', 'USS Raman', 'USS Relativity', 'USS Reliant', 'USS Renegade', 'USS Republic', 'USS Repulse', 'USS Revere', 'USS Rhode Island', 'USS Rio Grande', 'USS Robert Louis Stevenson', 'USS Roosevelt', 'USS Rubicon', 'USS Rutledge', 'USS Sarajevo', 'USS Saratoga', 'USS Sarek', 'USS Scovill', 'USS Seaquest', 'USS Seaview', 'USS Sentinel', 'USS Shenandoah', 'USS Shepard', 'USS Sherlock Holmes', 'USS ShirKahr', 'USS Silversides', 'USS Sitak', 'USS Springfield', 'USS Stargazer', 'USS Strata', 'USS Suleiman', 'USS Sutherland', 'USS Syracuse', 'USS Tecumseh', 'USS Thomas Paine', 'USS Thunderchild', 'USS Tian An Men', 'USS Ticonderoga', 'USS Titan', 'USS T\'Kumbra', 'USS Tolstoy', 'USS Tombaugh', 'USS Tranquillity Base', 'USS Trial', 'USS Trieste', 'USS Tripoli', 'USS Truman', 'USS Tsiolkovsky', 'USS Tycho', 'USS Ulysses', 'USS Umibozu', 'USS Unicorn', 'USS Valdemar', 'USS Valiant', 'USS Valley Forge', 'USS Vengeance', 'USS Venture', 'USS Veracruz', 'USS Vico', 'USS Victory', 'USS Volga', 'USS Voyager', 'USS Wellington', 'USS White Sands', 'USS Whorfin', 'USS Woden', 'USS Wolcott', 'USS Wyoming', 'USS Yamaguchi', 'USS Yamato', 'USS Yangtzee Kiang', 'USS Yeager', 'USS Yellowstone', 'USS Yorkshire', 'USS Yorktown', 'USS Yosemite', 'USS Yukon', 'USS Yuri Gagarin', 'USS Zapata', 'USS Zhukov']

    ai_names = ['Jonathan Archer', 'Ayala', 'Azan', 'Reginald Barclay', 'Bareil Antos', 'Julian Bashir', 'B\'Etor', 'The Borg Queen', 'Phillip Boyce', 'Brunt', 'Joseph Carey', 'Chakotay', 'Chell', 'Christine Chapel', 'Pavel Chekov', 'J. M. Colt', 'Kimara Cretak', 'Beverly Crusher', 'Wesley Crusher', 'Jal Culluh', 'Elizabeth Cutler', 'Leonardo da Vinci', 'Damar', 'Daniels', 'Data', 'Ezri Dax', 'Jadzia Dax', 'Degra', 'The Doctor', 'Dolim', 'Dukat', 'Evek', 'Michael Eddington', 'Female Changeling', 'Vic Fontaine', 'Maxwell Forrest', 'Elim Garak', 'Garrison', 'Sonya Gomez', 'Gowron', 'Amanda Grayson', 'Guinan', 'J. Hayes', 'Erika Hernandez', 'Hogan', 'Mr. Homn', 'Hugh of Borg', 'Icheb', 'Ishka', 'Kathryn Janeway', 'Jannar', 'Michael Jonas', 'K\'Ehleyr', 'Kes', 'Harry Kim', 'Kira Nerys', 'James T. Kirk', 'Kor', 'Kurn', 'Geordi La Forge', 'Leeta', 'Robin Lefler', 'Li Nalas', 'Lore', 'Lursa', 'Maihar\'du', 'Mallora', 'Carol Marcus', 'Martok', 'Travis Mayweather', 'Leonard McCoy', 'Mezoti', 'Mila', 'Mora Pol', 'Morn', 'Mot', 'Neelix', 'Susan Nicoletti', 'Nog', 'Kashimuro Nozawa', 'Number One', 'Keiko O\'Brien', 'Miles O\'Brien', 'Molly O\'Brien', 'Odo', 'Alyssa Ogawa', 'Opaka Sulan', 'Owen Paris', 'Tom Paris', 'Phlox', 'Jean-Luc Picard', 'Christopher Pike', 'Katherine Pulaski', 'Q', 'Quark', 'Janice Rand', 'Rebi', 'Malcolm Reed', 'William Riker', 'Ro Laren', 'Rom', 'William Ross', 'Michael Rostov', 'Alexander Rozhenko', 'Saavik', 'Sarek', 'Hoshi Sato', 'Montgomery Scott', 'Sela', 'Seska', 'Seven of Nine', 'Shakaar Edon', 'Thy\'lek Shran', 'Silik', 'Benjamin Sisko', 'Jake Sisko', 'Jennifer Sisko', 'Joseph Sisko', 'Sarah Sisko', 'Luther Sloan', 'Soval', 'Spock', 'Lon Suder', 'Hikaru Sulu', 'Enabran Tain', 'Tal Celes', 'Tomalak', 'Tora Ziyal', 'B\'Elanna Torres', 'T\'Pol', 'The Traveler', 'Deanna Troi', 'Lwaxana Troi', 'Charles Tucker', 'Tuvok', 'Jose Tyler', 'Nyota Uhura', 'Vash', 'Vorik', 'Weyoun', 'Naomi Wildman', 'Samantha Wildman', 'Winn Adami', 'Worf', 'Tasha Yar', 'Kasidy Yates', 'Zek']

    # Initialize board
    for i in range(BOARD_SIZE):
        row = []
        for j in range(BOARD_SIZE):
            row.append('-')
        p1_board.append(row[:])
        p2_board.append(row[:])
        p1_radar.append(row[:])
        p2_radar.append(row[:])

    header = list(map(chr, range(65, 65 + BOARD_SIZE)))

    # Start game
    os.system('cls')

    if type == '1':
        player_entry(p1_ships, p1_board, header, ship_names, SHIP_COUNT, BOARD_SIZE, SHIP_LENGTH)
        
        print 'Computer placing ships...'
        time.sleep(1)
        ai_entry(p2_ships, p2_board, header, ship_names, ai_names, SHIP_COUNT, BOARD_SIZE, SHIP_LENGTH)

    # Start Game
    print 'Starting game...'
    time.sleep(1)
    # os.system('cls')

    game_on = True
    move_ctr = 0  # Player 1 moves on even, player 2 on odd
    status = ''

    while game_on:
        # Print screen
        display = []
        display.append('Player 1')
        display.append('')
        display.append('   ' + 'Map' + '  ' * BOARD_SIZE + '   ' + 'Radar')
        display.append(
            '   ' + ' '.join([str(x) for x in header]) + 
            ' || ' +
            '   ' + ' '.join([str(x) for x in header])
        )
        for b in range(BOARD_SIZE):
            display.append(
                str(b + 1).rjust(2) + ' ' + ' '.join(p1_board[b]) +
                ' || ' +
                str(b + 1).rjust(2) + ' ' + ' '.join(p1_radar[b])
            )
        
        # Add player scoreboard
        display[2] += ' ' * (len(display[3]) - len(display[2])) + ' ' * 10 + 'Your Ships'
        display[3] += ' ' * 10 + '-' * 20

        for n in range(len(p1_ships)):
            display[n + 4] += (' ' * 10 + str(n + 1) + '. ' + p1_ships[n]['name'] + ' [' + str(len(p1_ships[n]['location'])) + '/' + str(SHIP_LENGTH) + ']')
        
        # Add enemy scoreboard
        display[n + 6] += ' ' * 10 + 'Enemy Ships'
        display[n + 7] += ' ' * 10 + '-' * 20

        for n in range(len(p2_ships)):
            label = ' [' + str(len(p2_ships[n]['location'])) + '/' + str(SHIP_LENGTH) + ']'
            if len(p2_ships[n]['location']) == 0:
                label = ' [SUNK]'

            display[n + 9] += ' ' * 10 + str(n + 1) + '. ' + p2_ships[n]['name'] + label

        # Print display
        for d in display:
            print d

        print status
        status = ''

        if move_ctr % 2 == 0:
            # Player 1 move
            valid = False
            while not valid:
                # Get user input
                coord = raw_input('Enter target coordinates: ')

                # Convert x-axis letter to int and add to location array
                try:
                    coord_x = ord(coord[0].upper()) - 65
                except IndexError:
                    coord_x = -1
                try:
                    coord_y = int(coord[1:]) - 1
                except ValueError:
                    coord_y = -1

                # Check if coordinates are inside board
                if not ((coord_x >= 0 and coord_x < BOARD_SIZE) and (coord_y >= 0 and coord_y < BOARD_SIZE)):
                    print 'Invalid coordinates'
                else:
                    # If spot is free
                    if p1_radar[coord_y][coord_x] != '-':
                        print 'You\'ve already tried there'
                    else:
                        valid = True

            game_on, status = check_move(coord_x, coord_y, p1_radar, p2_ships, p2_board)

        else:
            # Player 2 move
            # Generate random inputs
            valid = False
            while not valid:
                # AI random input
                coord_x = randint(0, BOARD_SIZE)
                coord_y = randint(0, BOARD_SIZE)

                # Check if coordinates are inside board
                if not ((coord_x >= 0 and coord_x < BOARD_SIZE) and (coord_y >= 0 and coord_y < BOARD_SIZE)):
                    print 'Invalid coordinates'
                else:
                    # If spot is free
                    if p2_radar[coord_y][coord_x] != '-':
                        print 'You\'ve already tried there'
                    else:
                        valid = True

            game_on, status = check_move(coord_x, coord_y, p2_radar, p1_ships, p1_board)

        os.system('cls')
        move_ctr += 1


def player_entry(ships, board, header, ship_names, SHIP_COUNT, BOARD_SIZE, SHIP_LENGTH):
    # Player places ships
    for i in range(1, SHIP_COUNT + 1):
        ships.append({})
        ships[-1]['location'] = []
        ships[-1]['name'] = ''
        coord_x = coord_y = None

        error = ''

        for j in range(1, SHIP_LENGTH + 1):
            valid = False

            while not valid:
                display = []
                display.append('_' * 60)
                display.append('Player 1, enter coordinates for your ships')
                display.append('')
                display.append('   ' + ' '.join([str(x) for x in header]))
                for b in range(BOARD_SIZE):
                    display.append(str(b + 1).rjust(2) +
                                   ' ' + ' '.join(board[b]))

                # Add scoreboard
                display[3] += ' ' * 10 + 'Ships Placed'
                display[4] += ' ' * 10 + '-' * 20

                for n in range(len(ships)):
                    display[n + 5] += ' ' * 10 + \
                        str(n + 1) + '. ' + ships[n]['name']

                display.append('_' * 60)

                # Print display
                for d in display:
                    print d

                print error
                error = ''

                # Get user input
                coord = raw_input('Enter coordinates for ship #' + str(i) +
                                  ' (' + str(j) + '/' + str(SHIP_LENGTH) + '): ')

                # Convert x-axis letter to int and add to location array
                try:
                    coord_x = ord(coord[0].upper()) - 65
                except IndexError:
                    coord_x = -1
                try:
                    coord_y = int(coord[1:]) - 1
                except ValueError:
                    coord_y = -1

                valid, error = check_coord(coord_x, coord_y, BOARD_SIZE, SHIP_LENGTH, i, j, board)

                if valid:
                    ships[-1]['location'].append([coord_x, coord_y])
                    board[coord_y][coord_x] = str(i)

                os.system('cls')

        # Ship added
        rand_name = randint(0, len(ship_names))
        ships[-1]['name'] = ship_names[rand_name]
        del ship_names[rand_name]

    # All ships added, print screen
    display = []
    display.append('_' * 60)
    display.append('Player 1')
    display.append('')
    display.append('   ' + ' '.join([str(x) for x in header]))
    for b in range(BOARD_SIZE):
        display.append(str(b + 1).rjust(2) +
                       ' ' + ' '.join(board[b]))

    # Add scoreboard
    display[3] += ' ' * 10 + 'Your Ships'
    display[4] += ' ' * 10 + '-' * 20

    for n in range(len(ships)):
        display[n + 5] += ' ' * 10 + str(n + 1) + '. ' + ships[n]['name']

    display.append('_' * 60)

    # Print display
    for d in display:
        print d

    print 'Ship Entry Finished'
    print ''

def ai_entry(ships, board, header, ship_names, ai_names, SHIP_COUNT, BOARD_SIZE, SHIP_LENGTH):
    for i in range(1, SHIP_COUNT + 1):
        ships.append({})
        ships[-1]['location'] = []
        ships[-1]['name'] = ''
        coord_x = coord_y = None

        error = ''

        for j in range(1, SHIP_LENGTH + 1):
            valid = False

            while not valid:
                # Generate random inputs
                coord_x = randint(0, BOARD_SIZE)
                coord_y = randint(0, BOARD_SIZE)

                valid, error = check_coord(coord_x, coord_y, BOARD_SIZE, SHIP_LENGTH, i, j, board)

                if valid:
                    ships[-1]['location'].append([coord_x, coord_y])
                    board[coord_y][coord_x] = str(i)

        # Ship added
        rand_name = randint(0, len(ship_names))
        ships[-1]['name'] = ship_names[rand_name]
        del ship_names[rand_name]

    os.system('cls')

    # All ships added, print screen
    display = []
    display.append('_' * 60)
    rand = randint(0, len(ai_names))
    
    # TODO(sl): debug this
    print 'DEBUG', rand, len(ai_names)

    display.append('Player 2: ' + ai_names[rand])
    display.append('')
    display.append('   ' + ' '.join([str(x) for x in header]))
    for b in range(BOARD_SIZE):
        display.append(str(b + 1).rjust(2) +
                       ' ' + ' '.join(board[b]))

    # Add scoreboard
    display[3] += ' ' * 10 + 'Your Ships'
    display[4] += ' ' * 10 + '-' * 20

    for n in range(len(ships)):
        display[n + 5] += ' ' * 10 + str(n + 1) + '. ' + ships[n]['name']

    display.append('_' * 60)

    # Print display
    for d in display:
        print d

    print 'Ship Entry Finished'
    print ''


def check_coord(coord_x, coord_y, BOARD_SIZE, SHIP_LENGTH, i, j, board):
    valid = False
    error = ''

    # Check if coordinates are inside board
    if not ((coord_x >= 0 and coord_x < BOARD_SIZE) and (coord_y >= 0 and coord_y < BOARD_SIZE)):
        error = 'Invalid coordinates'
    else:
        # If spot is free
        if board[coord_y][coord_x] != '-':
            error = 'That spot is already taken'
        else:
            # Look ahead for remaining pieces
            rem_pieces = SHIP_LENGTH - j

            clear_y = 0
            adjoin_y = 0

            clear_x = 0
            adjoin_x = 0

            if rem_pieces > 0:
                # Check up/down
                for p in range(1, rem_pieces + 1):
                    # Check if inside board
                    chk = [coord_y - p, coord_y + p]
                    for c in chk:
                        if c >= 0 and c < BOARD_SIZE:
                            if board[c][coord_x] == '-':
                                clear_y += 1
                            elif board[c][coord_x] == str(i):
                                adjoin_y += 1

                    # If enough space
                    if clear_y + adjoin_y >= rem_pieces:
                        if j > 1:
                            # If not first piece, force adjoining
                            if adjoin_y > 0:
                                valid = True
                                break
                        else:
                            valid = True
                            break

                # Check left/right
                for p in range(1, rem_pieces + 1):
                    # Check if inside board
                    chk = [coord_x - p, coord_x + p]
                    for c in chk:
                        if c >= 0 and c < BOARD_SIZE:
                            if board[coord_y][c] == '-':
                                clear_x += 1
                            elif board[coord_y][c] == str(i):
                                adjoin_x += 1

                    # If enough space
                    if clear_x + adjoin_x >= rem_pieces:
                        if j > 1:
                            # If not first piece, force adjoining
                            if adjoin_x > 0:
                                valid = True
                                break
                        else:
                            valid = True
                            break
                if clear_y + clear_x == 0:
                    error = 'There is not enough space to complete to ship'
                elif j > 1 and adjoin_y + adjoin_x == 0:
                    error = 'Pieces must be placed next to each other'

            else:
                # Last piece
                for p in range(1, SHIP_LENGTH):
                    # Check if inside board
                    chk = [coord_y - p, coord_y + p]
                    for c in chk:
                        if c >= 0 and c < BOARD_SIZE:
                            if board[c][coord_x] == str(i):
                                adjoin_y += 1

                    # If enough space
                    if adjoin_y >= j - 1:
                        valid = True
                        break

                for p in range(1, SHIP_LENGTH):
                    # Check if inside board
                    chk = [coord_x - p, coord_x + p]
                    for c in chk:
                        if c >= 0 and c < BOARD_SIZE:
                            if board[coord_y][c] == str(i):
                                adjoin_x += 1

                    # If enough space
                    if adjoin_x >= j - 1:
                        valid = True
                        break

                if j > 1 and adjoin_y + adjoin_x < 2:
                    error = 'Pieces must be placed next to each other'

    return valid, error

def check_move(coord_x, coord_y, radar, enemy_ships, enemy_board):
    game_on = True
    status = ''

    # Check target
    hit = False
    for i in enemy_ships:
        if [coord_x, coord_y] in i['location']:
            hit = True
            status = 'Hit'                    
            i['location'].remove([coord_x, coord_y])
            radar[coord_y][coord_x] = 'x'
            enemy_board[coord_y][coord_x] = 'x'

            if not i['location']:
                status = 'You have sunk the ' + i['name'] + '!'
            break

    if not hit:
        status = 'Miss'
        radar[coord_y][coord_x] = 'o'
        enemy_board[coord_y][coord_x] = 'o'

    # Check score
    rem_hits = 0
    for i in enemy_ships:
        rem_hits += len(i['location'])
    
    if rem_hits == 0:
        game_on = False

    return game_on, status

if __name__ == '__main__':
    main()