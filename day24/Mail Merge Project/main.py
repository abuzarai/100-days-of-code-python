#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open(r'Mail Merge Project\Input\Names\invited_names.txt') as invited_list:
    invited_people = invited_list.readlines()

with open(r'Mail Merge Project\Input\Letters\starting_letter.txt') as letter_file:
    letter_content = letter_file.read()
    for name in invited_people:
        stripped_name = name.strip()
        new_letter = letter_content.replace("[name]", stripped_name)
        print(new_letter)
        with open(f"Mail Merge Project\Output\ReadyToSend\letter_for_{stripped_name}.txt", mode='w') as final_letter:
            final_letter.write(new_letter)