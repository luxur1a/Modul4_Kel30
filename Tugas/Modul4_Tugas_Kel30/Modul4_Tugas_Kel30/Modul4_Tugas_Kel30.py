import metod
print("Buat passsword User 1")
pw1 = input()
print("Buat password User 2")
pw2 = input()
print("Login")
print("User1(1)")
print("User2(2)")
print("Input 1 atau 2")
user = int(input())
if user == 1:
    print("Masukkan password User1")
    pw = input()
    while pw != pw1:
            print("Password salah")
            print("Masukkan password")
            pw = input()
            print("Login berhasil")
    
else:
    print("Masukkan password User2")
    pw = input()
    while pw != pw2:
            print("Password salah")
            print("Masukkan password")
            pw = input()
            print("Login berhasil")

