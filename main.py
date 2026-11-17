# MeowGPT
# DEFINISI DAN SPESIFIKASI TYPE BENTUKAN DATE
type Hari = int[1, 31]
type Bulan = int[1, 12]
type Tahun = int
type Date = tuple[Hari, Bulan, Tahun]


# DEFINISI DAN SPESIFIKASI TYPE BENTUKAN ANTARA
type Chat = str
type Cred = tuple[str, str]
type Paket = tuple[str, float, int[1, 12]]
type Kuota = int
type Kupon = str
type Riwayat = tuple[Date, Chat, Chat, Kuota]

# DEFINISI DAN SPESIFIKASI TYPE BENTUKAN AKUN
type Akun = tuple[Cred, Paket, Kuota, Kupon, Riwayat ]

