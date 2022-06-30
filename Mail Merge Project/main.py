PLACEHOLDER = "[name]"
with open("./Mail Merge Project/Input/Names/invited_names.txt")as file:
    names = file.readlines()

with open("./Mail Merge Project/Input/Letters/starting_letter.txt") as file:
    letter_content = file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter_content = letter_content.replace(PLACEHOLDER, stripped_name)
        with open(f"./Mail Merge Project/Output/ReadyToSend/letter_for_{stripped_name}.txt", mode='w') as file:
            file.write(new_letter_content)
