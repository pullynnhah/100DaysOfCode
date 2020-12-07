import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

possibilities = [rock, paper, scissors]

your_idx = int(input('What do you choose? 0-rock, 1-paper, 2-scissors: '))
pc_idx = random.randint(0, len(possibilities) - 1)

print('You chose:')
print(possibilities[your_idx])
print('Computer chose:')
print(possibilities[pc_idx])

if your_idx == pc_idx:
    print("It's a draw!")
elif your_idx == 0:
    if pc_idx == 1:
        print('You lose!')
    else:
        print('You win!')
elif your_idx == 1:
    if pc_idx == 0:
        print('You win!')
    else:
        print('You lose!')
else:
    if pc_idx == 0:
        print('You lose!')
    else:
        print('You win!')


