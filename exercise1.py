import random 
suits = ["Spades","Hearts","Clubs","Diamonds"]
faces = ["Jack","Queen","King","Ace"]
numbers = [2,3,4,56,7,8,9,10]
def draw_card():
    suit = random.choice(suits)
    card = random.choice(faces+numbers)
    return card, "of", suit
for i in range(8):
    print(draw_card())