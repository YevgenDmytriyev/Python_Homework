secret = input("*Secret:* ")
love_name = input("*name:* ")
birth_year = input("*year:* ")
if len(secret) < 8:
    print("The secret must be at least 8 characters.")
else:
    cipher = secret + love_name
    reversed_cipher = cipher[::-1]
    final_cipher = reversed_cipher + birth_year
    print("Ciphered Secret:", final_cipher)