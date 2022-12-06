import getpass
user = input("Username: ")


sandi = getpass.getpass()

if sandi == '123' and user == 'abc':
    print("Anda Telah Login")

else:
    print("Username atau Password Anda Salah")
