with open('./Input/Letters/starting_letter.docx') as file:
    email = file.readlines()

with open('./Input/Names/invited_names.txt') as file:
    names = file.readlines()

old_name = '[name]'
for name in names:
    name = name.strip()
    email[0] = email[0].replace(f'{old_name}', name)
    with open(f'./Output/ReadyToSend/letter_for_{name}.docx', mode='w') as file:
        file.writelines(email)
    old_name = name
