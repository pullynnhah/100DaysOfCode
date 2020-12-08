import os
import auction_art


def clear_screen():
    os.system("cls" if os.name == 'nt' else 'clear')

bid_dict = {}
another = 'yes'
while another == 'yes':
    print(auction_art.logo)
    name = input('What is your name? ')
    bid = float(input('What is your bid? $'))
    print("Are there any other bidders? Type 'yes' or 'no'.")
    another = input()
    bid_dict[name] = bid
    clear_screen()

reverse_bid_dict = {}
for name in bid_dict:
    bid = bid_dict[name]
    reverse_bid_dict[bid] = name

highest_bid = max(reverse_bid_dict)
print(f'The highest bid is ${highest_bid:.2f} and it was made by {reverse_bid_dict[highest_bid]}')
