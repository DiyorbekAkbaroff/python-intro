name = input("Ismingizni kiriting: ")
last_name = input("Familyangizni kiriting: ")

username1 = name + last_name
username2 = last_name + name
username3 = name.lower() + last_name.lower()
username4 = last_name.lower() + name.lower()

print(username1)
print(username2)
print(username3)
print(username4)