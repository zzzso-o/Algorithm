N = int(input())
cards = [_ for _ in range(1, N+1)]


while True:
    if len(cards) == 1:
        print(cards[0])
        break
    else:
        cards.pop(cards[0])
        cards.append(cards.pop(cards[1]))

