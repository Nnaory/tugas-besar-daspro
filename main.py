# MeowGPT

# DEFINISI DAN SPESIFIKASI TYPE BENTUKAN DATE

# type Day: integer [1, 31]
# {definisi ini hanyalah untuk menamakan type integer dengan nilai tertentu supaya mewakili Day}
type Day = int[1, 31]

# type Month: integer [1 <...< 12]
# {definisi ini hanyalah untuk menamakan type integer dengan nilai tertentu yang mewakili Month}
type Month = int[1, 12]

# type Year: integer >0
# {definisi ini hanyalah untuk menamakan type integer dengan nilai lebih dari nol yang mewakili Year}
type Year = int

# type Date: <d: Day, m: Month, y: Year > 0
#   { <d, m, y> adalah tanggal, bulan m, dan tahun y}
type Date = tuple[Day, Month, Year]


# DEFINISI DAN SPESIFIKASI TYPE BENTUKAN BANTUAN (UNTUK HISTORY DAN CRED)

# type Chat: <pesan: string>
# {<pesan>  definisi ini hanyalah untuk menamakan type string dengan nilai tertentu yang mewakili chat atau pesan} 
type Chat = str

# type Username: <name_user: string>
#   {<name_user> definisi ini hanyalah untuk menamakan type string dengan nilai tertentu yang mewakili nama pengguna}
type Username = str 

# type Password: <kata_sandi: string>
#   {<kata_sandi> definisi ini hanyalah untuk menamakan type string dengan nilai tertentu yang mewakili password pengguna}
type Password = str


# DEFINISI DAN SPESIFIKASI TYPE BENTUKAN BANTUAN (UNTUK AKUN)
# type Cred: <usn: Username, pw: Password>
#   {<usn, pw>  adalah kredensial akun dengan username usn dan password pw}
type Cred = tuple[Username, Password] 

# type Package: <name: string, price: real, duration: integer [1, 12]> 
#   {<name, price, duration> adalah detail sebuah paket yang berisi nama dengan Name, harga dengan Price, dan durasi paket dengan Duration}
type Package = tuple[str, float, int[1, 12]]

# type Quota : <kuota : integer>
#   {<kuota> adalah batasan chat pengguna dengan nilai integer tertentu yang terdiri dari n karakter}
type Quota = int

# type Coupon : <kupon:integer>
# {<kupon> definisi hanyalah untuk menamakan type integer}
type Coupon = str

# type History: <tgl: Date, in: Chat, out: Chat, kta: Quota
#   {<tgl, in, out, kta adalah catatan atau riwayat penggunaan dengan tanggal tgl, input in, output out, dan kuota kta} 
type History = tuple[Date, Chat, Chat, Quota]

# DEFINISI DAN SPESIFIKASI TYPE BENTUKAN AKUN
# type Account: <Cr: Cred, P: Package, Q: Quota, C:Coupon, H: History>
#   {<Cr, P, Q, C, H> adalah informasi dari sebuah akun yang berisikan identitas dengan Cr, paket yang digunakan dengan P
#   kuota per chat dengan Q, kupon yang digunakan dengan C, dan riwayat chat dengan H}
type Account = tuple[Cred, Package, Quota, Coupon, History]


# DEFINISI DAN SPESIFIKASI SELEKTOR TYPE BENTUKAN DATE
# getDay : Date -> Day
#   {getDay(tgl) memberikan hari d dari tanggal tgl yang terdiri dari <d, m, y>}
def getDay(tgl: Date) -> Day :
    return tgl[0]

# getMonth : integer[1,12] -> string :
# {getMonth(tgl) memberikan bulan m dari tanggal tgl yang terdiri dari < d, m ,y>} 
def getMonth(tgl: Date) -> Month :
    return tgl[1]

# getYear : integer > 0 -> string
# {getYear(tgl) memberikan tahun y dari tanggal tgl yang terdiri dari < d, m ,y>} 
def getYear(tgl: Date) -> Year :
    return tgl[2]

# DEFINISI DAN SPEFISIKASI SELEKTOR TYPE BENTUKAN CRED
# getUsername: Cred -> Username
#   {getUsername(cred) memberikan usn dari kredensial cred yang terdiri dari <usn, pw>}
def getUsername(cred: Cred) -> Username:
    return cred[0]

# getPassword: Cred -> Password
#   {getPassword(cred) memberikan pw dari kredensial cred yang terdiri dari <usn, pw> }
def getPassword(cred:Cred) -> Password:
    return cred[1] 



# DEFINISI DAN SPEFISIKASI SELEKTOR TYPE BENTUKAN PACKAGE
# getNamaPaket: Package -> string
#   {getNamaPaket(pkt) memberikan name dari paket pkt yang terdiri dari <name, price, duration>}
def getNamaPaket(pkt: Package) -> str:
    return pkt[0]

# getHargaPaket: Package -> real
#   {getHargaPaket(pkt) memberikan price dari paket pkt yang terdiri dari <name, price, duration>}
def getHargaPaket(pkt: Package) -> float:
    return pkt[1]

# getDurasiPaket: Package -> real
#   {getDurasiPaket(pkt) memberikan duration dari paket pkt yang terdiri dari <name, price, duration>}
def getDurasiPaket(pkt : Package) -> float:
    return pkt[2]

# getDurasiPaket: Package -> integer

# DEFINISI DAN SPEFISIKASI SELEKTOR TYPE BENTUKAN ACCOUNT
# getAccount : Account -> Cred
# {getAccount(cred) mengambil kredensial dari Account yang terdiri dari <Cred, Package, Quota, Coupon, History,}  
def getAccount(akun: Account) -> Cred:
    return akun[0]
# getAccount : Account -> Cred

# Definisi DAN SPESIFIKASI SELEKTOR 
