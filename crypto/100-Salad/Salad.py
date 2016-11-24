import string

alphabet =  string.ascii_lowercase + string.digits 

ctext = "7sj-ighm-742q3w4t"

def shift(n):
    message = ""
    for index, char in enumerate(ctext):
        if char == "-":
            message += char
        else:
            message += alphabet[(alphabet.index(ctext[index])+n)%len(alphabet)]
    return message.upper()
    
for i in range(len(alphabet)):
    message = shift(i)
    if "RC3" in message:
        print(message)
