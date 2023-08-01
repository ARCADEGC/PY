from os import system as sys
sys("cls")

from colorama import Fore, Back

hand = list(input(f"{Fore.RED}Hand: {Fore.RESET}"))

cards = []
for card in range(0, 2):
    match hand[card]:
        case "A": cards.append(10)
        case "K": cards.append(8)
        case "Q": cards.append(7)
        case "J": cards.append(6)
        case "T": cards.append(5)
        case _: cards.append(int(hand[card]) / 2)

if len(hand) == 2:
    hand.append("")
    cards.append("")

passer = 0
if cards[0] == cards[1]:
    high = cards[0] * 2
    print(f"\n\t{Fore.YELLOW}|  Hand Value: {high}  |{Fore.RESET}\t  \n")
    passer = 1

if passer == 0:
    high = max(cards[0], cards[1])

    if hand[2] == "s":
        high += 2

    deck = []
    for card in range(0, 2):
        match hand[card]:
            case "A": deck.append(14)
            case "K": deck.append(13)
            case "Q": deck.append(12)
            case "J": deck.append(11)
            case "T": deck.append(10)
            case _: deck.append(int(hand[card]))

    gap = max(deck[0], deck[1]) - min(deck[0], deck[1]) - 1
    if gap == 3:
        gap = 4
    elif gap >= 4:
        gap = 5
    high -= gap

    if cards[0] <= 6 and cards[1] <= 6 and (gap == 0 or gap == 1):
        high += 1
    
    high = max(0, round(high))

    print(f"\n\t{Fore.YELLOW}|  Hand Value: {int(high)}  |{Fore.RESET}\t  \n")

if high >= 12:
    print(f"\t{Back.GREEN}| Always raise or reraise |{Back.RESET}\n")
    exit()
elif high >= 10:
    print(f"\t{Back.GREEN}| Consider call or raise |{Back.RESET}\n")
    exit()
elif high <= 6:
    print(f"\t{Back.RED}| Fold |{Back.RESET}\n")
    exit()

position = input(f"{Fore.RED}[Early/Mid/Late] What is your position: {Fore.RESET}").lower()
if position == "e":
    print(f"\n\t{Back.RED}| Fold |{Back.RESET}\n")
elif position == "m":
    if high >= 9:
        print(f"\n\t{Back.CYAN}| Raise |{Back.RESET}\n")
    else:
        print(f"\n\t{Back.RED}| Fold |{Back.RESET}\n")
else: 
    print(f"\n\t{Back.CYAN}| Raise |{Back.RESET}\n")