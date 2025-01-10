email = input("Emailni kiriting: ")

if '@' in email:
    domen = email.split('@')[1]
    print(domen)
else:
    print("Notogri kiritilgan")