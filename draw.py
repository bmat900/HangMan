def draw(num):
    if num == 0:
        print('''
    +---+
    |   |
        |
        |
        |
        |
   =========''')
    if num == 1:
        print('''
    +---+
    |   |
    O   |
        |
        |
        |
   =========''')
    if num ==2:
        print('''
    +---+
    |   |
    O   |
    |   |
        |
        |
   =========''')
    if num == 3:
        print('''
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========''')
    if num == 4:
        print('''
     +---+
     |   |
     O   |
    /|\  |
         |
         |
    =========''')
    if num == 5:
        print('''
     +---+
     |   |
     O   |
    /|\  |
    /    |     
         |
    =========''')