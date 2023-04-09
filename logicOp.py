# a = 10
# b = 2
# # != sama juga kaya not

# if not a == 10: # False
# 	print("It is True!")
# else:
# 	print("It is False")

username = input("Masukkan username anda: ")
password = input("Masukkan password anda: ")

if username == "Fadzar" or username == "Admin" and password == "fadzarargans":
	print("Logged in!")
else:
	print("Wrong!")
