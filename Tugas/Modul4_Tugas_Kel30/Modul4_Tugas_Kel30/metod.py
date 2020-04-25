class huhaha:
    cpin1=0
    cpin2=0
    cuser=0
    def __init__(self, user, pin1, pin2):
        self.cuser = user
        self.cpin1 = pin1
        self.cpin2 = pin2
    def mulai(self):
        print(f"Selamat Datang User {self. cuser}")
    def selesai(self, waktu):
        print("Loading")
        while waktu > 0:
                print(waktu)
                waktu -= 1
    def ulang1 (self):
        vpin=self.cpin1 + "1"
        knt=0
        while vpin != self.cpin1:
            if knt > 0:
               print("Password salah")
            knt=1
            print("Masukkan password")
            vpin = input()
        print("Login berhasil")
    def ulang2 (self):
        vpin=self.cpin1 + "1"
        knt=0
        while vpin != self.cpin2:
            if knt > 0:
               print("Password salah")
            knt=1
            print("Masukkan password")
            vpin = input()
        print("Login berhasil")
        
        

