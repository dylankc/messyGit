
# I would rather use def/func to streamline this but since its timed I wanted to hurry
deckamt = 0
lstone = ['hearts', 'spades', 'diamonds', 'clubs']
lstHearts = []
lstSpades = []
lstDiamonds = []
lstClubs = []

#initial full deck
while deckamt < 53:
    #14 cards per suite
    if deckamt < 14:
        lstHearts.append(deckamt)
        lstSpades.append(deckamt)
        lstDiamonds.append(deckamt)
        lstClubs.append(deckamt)
        deckamt += 1
        #dict for face cards
        dictNan = {'jack':11, 'queen':12, 'king':13, 'ace':14}




