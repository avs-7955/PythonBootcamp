PLACEHOLDER = "[name]"
# Opening the file and extracting all the lines and appending it to a list.
with open("./Mail Merge Project/Input/Names/invited_names.txt")as file:
    names = file.readlines()


with open("./Mail Merge Project/Input/Letters/starting_letter.txt") as file:
    # Saving the letter content
    letter_content = file.read()
    for name in names:
        # Stripping the name so that no extra space is available
        stripped_name = name.strip()
        new_letter_content = letter_content.replace(PLACEHOLDER, stripped_name)
        # Using f-string to make the file name for each seperate name
        with open(f"./Mail Merge Project/Output/ReadyToSend/letter_for_{stripped_name}.txt", mode='w') as file:
            file.write(new_letter_content)
