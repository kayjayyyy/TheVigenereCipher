# Templanza, Kristine Joy F.
# BSCPE 1-4
# Assignment No.2 - Problem 3

# Greeting and border line
print("")
print("\033[35m※ \033[0m" * 35)
print("")
print("\033[45m ♥ Welcome to Vigenère Cipher! ♥ \033[0m".center(78, "-"))

# Ask the name of the user
name = input("\n\033[3mGood day! What is your name? \033[0m")
print("\n\033[3;33mI hope you are doing well,", name + "!\033[0m")
print("")

print("\033[36m Let's get started! \033[0m".center(78, "~"))

# Remove space and uppercase only
def upper_and_remove_space(mess):
    if mess.isupper() == False or " " in mess:
        print("\033[31mError: Not capitalize and/or has spaces.\033[0m")
        mess = mess.upper()
        for i in mess:
            if " " in i:
                mess = mess.replace(i, "")
        print("\n\033[33mWe converted it for you:", mess + "\033[0m")
    return mess

# Generate and define the Vigenère Cipher program
def generate_vigenere_cipher(message, key):
    key = list(key)
    if len(message) == len(key):
        return(key)
    else:
        for i in range(len(message) - len(key)):
            key.append(key[i % len(key)])
    return("" . join(key))

def encryption_message(message, key):
    encrypt_message = []
    for i in range(len(message)):
        text = (ord(message[i]) + ord(key[i])) % 26
        text += ord("a")
        encrypt_message.append(chr(text))
    return("" . join(encrypt_message))

# Ask the users input (message and key)
if __name__ == "__main__":
    message = input("\n\033[3;35mPlease input the message you want to encrypt: \033[0m")
    message = upper_and_remove_space(message)
    cipher_key = input("\n\033[3;35mWhat is your key? \033[0m")
    cipher_key = upper_and_remove_space(cipher_key)
    
    cipher_text = generate_vigenere_cipher(message, cipher_key)
    encrypt_message = encryption_message(message, cipher_text)