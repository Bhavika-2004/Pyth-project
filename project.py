def encrypt(text):
    text_list = text.split(" ")
    encrypted_text = ""
    
    for word in text_list:
        if len(word) > 3:
            if word[-3:] != "erb":
                word_ending = word[1:]
                encrypted_text = encrypted_text + word[1:] + word[0] + "erb "
            else:
                encrypted_text = "Already in Ferb-Latin!"
        else:
            encrypted_text = encrypted_text + word + " "
    
    return encrypted_text
def decrypt(text):
    text_list = text.split(" ")
    decrypted_text = ""

    for word in text_list:
        if len(word) > 3:
            if word[-3:] == "erb":
                word = word[:-3]
                first_letter = word[-1]
                word = word[:-1]
                decrypted_text = decrypted_text + first_letter + word + " "
            else:
                decrypted_text = "Only Use Ferb Latin!"
        
        else:
            decrypted_text = decrypted_text + word + " "
    
    return decrypted_text
print("Welcome to Ferb-Latin\n")

while True:

    n = input("Select the desired option:\n1.Encrypt\n2.Decrypt\n3.Exit\n\n")
    if n == '1':
        a = input("Enter the text to encrypt: ")
        print("\n",encrypt(a))
    elif n == '2':
        a = input("Enter the text to decrypt: ")
        print("\n",decrypt(a))
    elif n == '3':
        break
    else:
        print("Invalid option!!")