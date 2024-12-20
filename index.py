import os
import datetime
import pandas as pd

FILE_ADMIN = 'data_admin.csv'
FILE_USER = 'data_user.csv'
folder_admin = 'data_admin'
folder_toko = 'data_toko'
folder_pembeli = 'data_pembeli'

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<UNTUK PROGRAM UTAMA>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def cek_data():
    if not os.path.exists(FILE_USER):  
        user = pd.DataFrame(columns=['username', 'password', 'email', 'role', 'id']) 
        user.to_csv(FILE_USER, index=False) 
    if not os.path.exists(FILE_ADMIN):  
        user = pd.DataFrame(columns=['username', 'password']) 
        user.to_csv(FILE_ADMIN, index=False) 
    if not os.path.exists(folder_admin):
        os.makedirs(folder_admin)
    if not os.path.exists(folder_toko):
        os.makedirs(folder_toko)
    if not os.path.exists(folder_pembeli):
        os.makedirs(folder_pembeli)

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<UNTUK REGISTRASI>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def cek_email(email):
    if '@' not in email or '.' not in email:
        return False

    local, _, domain = email.partition('@')

    if not local or not domain:
        return False

    if '.' not in domain or domain.startswith('.') or domain.endswith('.'):
        return False

    char_email = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_'
    for char in email:
        if char not in char_email and char != '@':
            return False

    return True

def bikin_id(username):
    baca = pd.read_csv(FILE_USER)
    
    huruf_pertama = ord(username[0].upper())
    kondisi = True

    while kondisi:
            sekarang = datetime.datetime.now()
            hari = sekarang.day
            jam = sekarang.hour
            menit = sekarang.minute

            id_mentah = (hari * jam * menit) / huruf_pertama
            
            id_jadi = int(id_mentah * 1000000) % 1000000
                
            if id_jadi in baca['id'].values:
                pass
            else:
                kondisi = False
    
    return f'{str(id_jadi)}'

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<MENU AWAL>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def register():
    os.system('cls')
    print('╔' + '═'*48 + '╗')
    print('║' + 'Registrasi Akun'.center(48) + '║')
    print('╚' + '═'*48 + '╝')
        
    print('\n1. Penjual\n2. Pembeli\n3. Kembali\n')
    pilihan = input('Registrasi sebagai : ')
     
    if pilihan == '1':
        os.system('cls')
        
        seller = pd.read_csv(FILE_USER)
        
        kondisi = True
        kondisi2 = True
        kondisi3 = True
        
        print('╔' + '═'*48 + '╗')
        print('║' + 'Registrasi Akun'.center(48) + '║')
        print('║' + 'Penjual'.center(48) + '║')
        print('╚' + '═'*48 + '╝')
        print()
        
        while kondisi:
            username = input('Masukkan username : ')
            if len(username) < 3:
                print('Username harus berisi minimal 3 karakter!')
            else:
                kondisi = False
        
        while kondisi2:
            password = input('Masukkan password : ')
            
            if len(password) < 8:
                print('Password harus berisi minimal 8 karakter!')
            else:
                kondisi2 = False
        
        while kondisi3:
            email = input('Masukkan email : ')
        
            if email in seller['email'].values:
                print('Email sudah digunakan, silahkan gunakan email lain.')
            if cek_email(email):
                kondisi3 = False
            else:
                print('Masukkan email yang valid!')
                
        data_baru = {'username': username, 'password': password, 'email': email, 'role': 'seller', 'id': bikin_id(username)}
        data_baru_df = pd.DataFrame([data_baru])
        seller = pd.concat([seller, data_baru_df], ignore_index=True)
        seller.to_csv(FILE_USER, index=False)     
        
        print(f'\nRegistrasi {username} sebagai penjual telah berhasil') 
        
        i = input('\nKetik apa saja untuk kembali')
        
    elif pilihan == '2':
        os.system('cls')
        
        buyer = pd.read_csv(FILE_USER)
        
        kondisi = True
        kondisi2 = True
        kondisi3 = True
        
        print('╔' + '═'*48 + '╗')
        print('║' + 'Registrasi Akun'.center(48) + '║')
        print('║' + 'Pembeli'.center(48) + '║')
        print('╚' + '═'*48 + '╝')
        print()
        
        while kondisi:
            username = input('Masukkan username : ')
            if len(username) < 3:
                print('Username harus berisi minimal 3 karakter!')
            else:
                kondisi = False
        
        while kondisi2:
            password = input('Masukkan password : ')
            
            if len(password) < 8:
                print('Password harus berisi minimal 8 karakter!')
            else:
                kondisi2 = False
        
        while kondisi3:
            email = input('Masukkan email : ')
        
            if email in buyer['email'].values:
                print('Email sudah digunakan, silahkan gunakan email lain.')
            if cek_email(email):
                kondisi3 = False
            else:
                print('Masukkan email yang valid!')
        
        data_baru = {'username': username, 'password': password, 'email': email, 'role': 'buyer', 'id': bikin_id(username)}
        data_baru_df = pd.DataFrame([data_baru])
        seller = pd.concat([buyer, data_baru_df], ignore_index=True)
        seller.to_csv(FILE_USER, index=False)    
        
        print(f'\nRegistrasi {username} sebagai penjual telah berhasil') 
        
        i = input('\nKetik apa saja untuk kembali')
        
    elif pilihan == '3':
        pass
    else:
        print('Masukan anda salah, anda akan dikembalikan ke menu awal')
        

def login():
    os.system('cls')
        
    print('╔' + '═'*48 + '╗')
    print('║' + 'Login Akun'.center(48) + '║')
    print('╚' + '═'*48 + '╝')
        
    print('\n1. Admin\n2. Penjual\n3. Pembeli\n4. Kembali\n')
    pilihan = input('Login sebagai : ')
    
    if pilihan == '1':
        os.system('cls')
        
        admin = pd.read_csv(FILE_ADMIN)
        
        i = 0
        
        print('╔' + '═'*48 + '╗')
        print('║' + 'Login Akun'.center(48) + '║')
        print('║' + 'Admin'.center(48) + '║')
        print('╚' + '═'*48 + '╝')
        
        while i < 3:
            admin['username'] = admin['username'].astype(str)
            admin['password'] = admin['password'].astype(str)

            username = input('\nMasukkan username : ')
            password = input('Masukkan password : ')

            user = admin[(admin['username'] == username) & (admin['password'] == password)]
            if not user.empty:
                menu_admin(username)
                i+=3
            else:
                print('\nLogin gagal! Username atau password salah.')
                i+=1
    
    elif pilihan == '2':
        os.system('cls')
        
        seller = pd.read_csv(FILE_USER)
        
        i = 0
        
        print('╔' + '═'*48 + '╗')
        print('║' + 'Login Akun'.center(48) + '║')
        print('║' + 'Penjual'.center(48) + '║')
        print('╚' + '═'*48 + '╝')
        
        while i < 3:
            seller['email'] = seller['email'].astype(str)
            seller['password'] = seller['password'].astype(str)

            email = input('\nMasukkan email : ')
            password = input('Masukkan password : ')

            user = seller[(seller['email'] == email) & (seller['password'] == password) & (seller['role'] == 'seller')]
            if not user.empty:
                menu_penjual(email)
                i+=3
            else:
                print('\nLogin gagal! email atau password salah.')
                i+=1
    
    elif pilihan == '3':
        os.system('cls')
        
        buyer = pd.read_csv(FILE_USER)
        
        i = 0
        
        print('╔' + '═'*48 + '╗')
        print('║' + 'Login Akun'.center(48) + '║')
        print('║' + 'Pembeli'.center(48) + '║')
        print('╚' + '═'*48 + '╝')
        
        while i < 3:
            buyer['email'] = buyer['email'].astype(str)
            buyer['password'] = buyer['password'].astype(str)
            
            email = input('\nMasukkan email : ')
            password = input('Masukkan password : ')

            user = buyer[(buyer['email'] == email) & (buyer['password'] == password) & (buyer['role'] == 'buyer')]
            if not user.empty:
                menu_pembeli(email)
                i+=3
            else:
                print('\nLogin gagal! Username atau password salah.')
                i+=1
                
    elif pilihan == '4':
        pass
    else:
        print('Masukan anda salah, anda akan dikembalikan ke menu awal')

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<MENU ADMIN>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def menu_admin(user):
    kondisi = True
    
    while kondisi:
        os.system('cls')
        
        print('╔' + '═'*48 + '╗')
        print('║' + 'Menu Admin'.center(48) + '║')
        print('╠' + '═'*48 + '╣')
        print('║' + user.center(48) + '║')
        print('╚' + '═'*48 + '╝')
        
        print('\n1. Edit akun penjual\n2. Edit akun pembeli\n3. Pendapatan Biaya Admin\n4. Keluar akun')
        
        kondisi2 = True
        
        while kondisi2:
            pilihan = input('\nGunakan menu nomor : ')
            
            if pilihan == '1':
                edit_akun_seller()
                kondisi2 = False
            elif pilihan == '2':
                edit_akun_buyer()
                kondisi2 = False
            elif pilihan == '3':
                pilih_pembeli_dan_hitung()
                kondisi2 = False
            elif pilihan == '4':
                kondisi2 = False
                kondisi = False
            else:
                print('Masukkan input yang benar!')

# FITUR EDIT AKUN SELLER
def edit_akun_seller():
    pilih = True

    while pilih:
        os.system('cls')
        
        print('╔' + '═'*48 + '╗')
        print('║' + 'Menu Edit Akun'.center(48) + '║')
        print('║' + 'Penjual'.center(48) + '║')
        print('╚' + '═'*48 + '╝')
        
        print('\n1. Lihat akun penjual\n2. Tambah akun penjual\n3. Ubah akun penjual\n4. Hapus akun penjual\n5. Kembali')
        
        pilih2 = True
        
        while pilih2:
            pilihan = input('\nGunakan menu nomor : ')
            
            if pilihan == '1':
                lihat_akun_seller()
                pilih2 = False
            elif pilihan == '2':
                tambah_akun_seller()
                pilih2 = False
            elif pilihan == '3':
                ubah_akun_seller()
                pilih2 = False
            elif pilihan == '4':
                hapus_akun_seller()
                pilih2 = False
            elif pilihan == '5':
                pilih2 = False
                pilih = False
            else:
                print('Masukkan input yang benar!')
# 
# FITUR LEBIH LENGKAP
def tambah_akun_seller():
    os.system('cls')
        
    seller = pd.read_csv(FILE_USER)
    
    kondisi = True
    kondisi2 = True
    
    print('╔' + '═'*48 + '╗')
    print('║' + 'Tambah Akun'.center(48) + '║')
    print('║' + 'Penjual'.center(48) + '║')
    print('╚' + '═'*48 + '╝')
    print()
    
    username = input('Masukkan username : ')
    
    while kondisi:
        password = input('Masukkan password : ')
        
        if len(password) < 1:
            print('Password harus berisi minimal 1 karakter!')
        else:
            kondisi = False
    
    while kondisi2:
        email = input('Masukkan email : ')
    
        if email in seller['email'].values:
            print('Email sudah digunakan, silahkan gunakan email lain.')
        if cek_email(email):
            kondisi2 = False
        else:
            print('Masukkan email yang valid!')
            
    data_baru = {'username': username, 'password': password, 'email': email, 'role': 'seller', 'id': bikin_id(username)}
    data_baru_df = pd.DataFrame([data_baru])
    seller = pd.concat([seller, data_baru_df], ignore_index=True)
    seller.to_csv(FILE_USER, index=False)     
    
    print(f'\nTelah menambah {username} sebagai penjual')
    
    i = input('\nKetik enter untuk kembali')

def ubah_akun_seller():
    baca = pd.read_csv(FILE_USER)
    seller = baca[baca['role'] == 'seller']
    
    os.system('cls')
    
    print('╔' + '═'*48 + '╗')
    print('║' + 'Edit Akun'.center(48) + '║')
    print('║' + 'Penjual'.center(48) + '║')
    print('╚' + '═'*48 + '╝')
    print()
    
    if seller.empty:
        print('Tidak ada akun penjual yang terdaftar')
        
        i = input('\nTekan enter untuk kembali')
        return
    
    print('═'*82)
    print(f"{'Index':<7} | {'Username':<15} | {'Email':<25} | {'Password':<15} | {'ID':<10}")
    print('═'*82)
    
    idx = 1
    
    for index, row in seller.iterrows():
        print(f"{idx:<7} | {row['username']:<15} | {row['email']:<25} | {row['password']:<15} | {row['id']:<10}")
        idx += 1
    
    print('═'*82)
    print()
    
    kondisi = True
    kembali = 0
    kondisi2 = True
    kondisi3 = True
        
    while kondisi:
        try:
            id_tanya = int(input('Ubah user ID : '))
            
            if id_tanya not in seller['id'].values:
                if kembali == 2:
                    i = input('\nTekan enter untuk kembali')
                    return
                kembali +=1
                print('Masukkan ID penjual yang valid!')
            else:
                kondisi = False
        except:
            if kembali == 2:
                i = input('\nTekan enter untuk kembali')
                return
            kembali +=1
            print('Masukkan ID penjual yang valid!')
        
    username = input('\nMasukkan username baru : ')
    
    while kondisi2:
        password = input('Masukkan password baru : ')
        
        if len(password) < 1:
            print('Password harus berisi minimal 1 karakter!')
        else:
            kondisi2 = False
    
    while kondisi3:
        email = input('Masukkan email baru : ')
    
        if email in seller['email'].values:
            print('Email sudah digunakan, silahkan gunakan email lain.')
        if cek_email(email):
            kondisi3 = False
        else:
            print('Masukkan email yang valid!')
            
    baca['password'] = baca['password'].astype(str)        
    baca.loc[baca['id'] == id_tanya, 'username'] = username
    baca.loc[baca['id'] == id_tanya, 'password'] = str(password)
    baca.loc[baca['id'] == id_tanya, 'email'] = email
    
    baca.to_csv(FILE_USER, index=False)
    
    print(f'\nTelah mengubah profil pengguna #{id_tanya}')
    
    i = input('\nKetik enter untuk kembali')
    
def lihat_akun_seller():
    baca = pd.read_csv(FILE_USER)
    seller = baca[baca['role'] == 'seller']
    
    os.system('cls')
    
    print('╔' + '═'*48 + '╗')
    print('║' + 'List Akun'.center(48) + '║')
    print('║' + 'Penjual'.center(48) + '║')
    print('╚' + '═'*48 + '╝')
    print()
    
    if seller.empty:
        print('Tidak ada akun penjual yang terdaftar')
        
        i = input('\nTekan enter untuk kembali')
        return
    
    print('═'*82)
    print(f"{'Index':<7} | {'Username':<15} | {'Email':<25} | {'Password':<15} | {'ID':<10}")
    print('═'*82)
    
    idx = 1
    
    for index, row in seller.iterrows():
        print(f"{idx:<7} | {row['username']:<15} | {row['email']:<25} | {row['password']:<15} | {row['id']:<10}")
        idx += 1
        
    print('═'*82)
        
    i = input('\nKetik enter untuk kembali')

def hapus_akun_seller():
    baca = pd.read_csv(FILE_USER)
    seller = baca[baca['role'] == 'seller']
    
    os.system('cls')
    
    print('╔' + '═'*48 + '╗')
    print('║' + 'Hapus Akun'.center(48) + '║')
    print('║' + 'Penjual'.center(48) + '║')
    print('╚' + '═'*48 + '╝')
    print()
    
    if seller.empty:
        print('Tidak ada akun penjual yang terdaftar')
        
        i = input('\nTekan enter untuk kembali')
        return
    
    print('═'*82)
    print(f"{'Index':<7} | {'Username':<15} | {'Email':<25} | {'Password':<15} | {'ID':<10}")
    print('═'*82)
    
    idx = 1
    
    for index, row in seller.iterrows():
        print(f"{idx:<7} | {row['username']:<15} | {row['email']:<25} | {row['password']:<15} | {row['id']:<10}")
        idx += 1
        
    print('═'*82)
    print()
    
    kondisi = True
    kembali = 0
    
    while kondisi:
        try:
            id_tanya = int(input('Hapus user ID : '))
            
            if id_tanya not in seller['id'].values:
                if kembali == 2:
                    i = input('\nTekan enter untuk kembali')
                    return
                kembali +=1
                print('Masukkan ID penjual yang valid!')
            else:
                kondisi = False
        except:
            if kembali == 2:
                i = input('\nTekan enter untuk kembali')
                return
            kembali +=1
            print('Masukkan ID penjual yang valid!')
            
    tanya = input('\nApakah anda yakin untuk menghapus akun ini (y) : ').lower()
    
    if tanya == 'y':
        pass
    else:
        i = input('\nTekan enter untuk kembali')
        return

    index_hapus = baca[baca['id'] == id_tanya].index 
    baca.drop(index=index_hapus, inplace=True)
    
    baca.to_csv(FILE_USER, index=False)
    
    print(f'\nTelah menghapus profil pengguna #{id_tanya}')
    
    i = input('\nKetik enter untuk kembali')
    
# FITUR EDIT AKUN BUYER 
def edit_akun_buyer():
    pilih = True

    while pilih:
        os.system('cls')
        
        print('╔' + '═'*48 + '╗')
        print('║' + 'Menu Edit Akun'.center(48) + '║')
        print('║' + 'Pembeli'.center(48) + '║')
        print('╚' + '═'*48 + '╝')
        
        print('\n1. Lihat akun pembeli\n2. Tambah akun pembeli\n3. Ubah akun pembeli\n4. Hapus akun pembeli\n5. Kembali')
        
        pilih2 = True
        
        while pilih2:
            pilihan = input('\nGunakan menu nomor : ')
            
            if pilihan == '1':
                lihat_akun_buyer()
                pilih2 = False
            elif pilihan == '2':
                tambah_akun_buyer()
                pilih2 = False
            elif pilihan == '3':
                ubah_akun_buyer()
                pilih2 = False
            elif pilihan == '4':
                hapus_akun_buyer()
                pilih2 = False
            elif pilihan == '5':
                pilih2 = False
                pilih = False
            else:
                print('Masukkan input yang benar!')

# FITUR LEBIH LENGKAP
def tambah_akun_buyer():
    os.system('cls')
        
    buyer = pd.read_csv(FILE_USER)
    
    kondisi = True
    kondisi2 = True
    
    print('╔' + '═'*48 + '╗')
    print('║' + 'Tambah Akun'.center(48) + '║')
    print('║' + 'Pembeli'.center(48) + '║')
    print('╚' + '═'*48 + '╝')
    print()
    
    username = input('Masukkan username : ')
    
    while kondisi:
        password = input('Masukkan password : ')
        
        if len(password) < 1:
            print('Password harus berisi minimal 1 karakter!')
        else:
            kondisi = False
    
    while kondisi2:
        email = input('Masukkan email : ')
    
        if email in buyer['email'].values:
            print('Email sudah digunakan, silahkan gunakan email lain.')
        if cek_email(email):
            kondisi2 = False
        else:
            print('Masukkan email yang valid!')
            
    data_baru = {'username': username, 'password': password, 'email': email, 'role': 'buyer', 'id': bikin_id(username)}
    data_baru_df = pd.DataFrame([data_baru])
    buyer = pd.concat([buyer, data_baru_df], ignore_index=True)
    buyer.to_csv(FILE_USER, index=False)     
    
    print(f'\nTelah menambah {username} sebagai pembeli')
    
    i = input('\nKetik enter untuk kembali')

def ubah_akun_buyer():
    baca = pd.read_csv(FILE_USER)
    buyer = baca[baca['role'] == 'buyer']
    
    os.system('cls')
    
    print('╔' + '═'*48 + '╗')
    print('║' + 'Edit Akun'.center(48) + '║')
    print('║' + 'Pembeli'.center(48) + '║')
    print('╚' + '═'*48 + '╝')
    print()
    
    if buyer.empty:
        print('Tidak ada akun pembeli yang terdaftar')
        
        i = input('\nTekan enter untuk kembali')
        return
    
    print('═'*82)
    print(f"{'Index':<7} | {'Username':<15} | {'Email':<25} | {'Password':<15} | {'ID':<10}")
    print('═'*82)
    
    idx = 1
    
    for index, row in buyer.iterrows():
        print(f"{idx:<7} | {row['username']:<15} | {row['email']:<25} | {row['password']:<15} | {row['id']:<10}")
        idx += 1
    
    print('═'*82)
    print()
    
    kondisi = True
    kembali = 0
    kondisi2 = True
    kondisi3 = True
        
    while kondisi:
        try:
            id_tanya = int(input('Ubah user ID : '))
            
            if id_tanya not in buyer['id'].values:
                if kembali == 2:
                    i = input('\nTekan enter untuk kembali')
                    return
                kembali +=1
                print('Masukkan ID pembeli yang valid!')
            else:
                kondisi = False
        except:
            if kembali == 2:
                i = input('\nTekan enter untuk kembali')
                return
            kembali +=1
            print('Masukkan ID pembeli yang valid!')
        
    username = input('\nMasukkan nama baru : ')
    
    while kondisi2:
        password = input('Masukkan password baru : ')
        
        if len(password) < 1:
            print('Password harus berisi minimal 1 karakter!')
        else:
            kondisi2 = False
    
    while kondisi3:
        email = input('Masukkan email baru : ')
    
        if email in buyer['email'].values:
            print('Email sudah digunakan, silahkan gunakan email lain.')
        if cek_email(email):
            kondisi3 = False
        else:
            print('Masukkan email yang valid!')
            
    baca['password'] = baca['password'].astype(str)        
    baca.loc[baca['id'] == id_tanya, 'username'] = username
    baca.loc[baca['id'] == id_tanya, 'password'] = str(password)
    baca.loc[baca['id'] == id_tanya, 'email'] = email
    
    baca.to_csv(FILE_USER, index=False)
    
    print(f'\nTelah mengubah profil pengguna #{id_tanya}')
    
    i = input('\nKetik enter untuk kembali')

def lihat_akun_buyer():
    baca = pd.read_csv(FILE_USER)
    buyer = baca[baca['role'] == 'buyer']
    
    os.system('cls')
    
    print('╔' + '═'*48 + '╗')
    print('║' + 'List Akun'.center(48) + '║')
    print('║' + 'Pembeli'.center(48) + '║')
    print('╚' + '═'*48 + '╝')
    print()
    
    if buyer.empty:
        print('Tidak ada akun pembeli yang terdaftar')
        
        i = input('\nTekan enter untuk kembali')
        return
    
    print('═'*82)
    print(f"{'Index':<7} | {'Username':<15} | {'Email':<25} | {'Password':<15} | {'ID':<10}")
    print('═'*82)
    
    idx = 1
    
    for index, row in buyer.iterrows():
        print(f"{idx:<7} | {row['username']:<15} | {row['email']:<25} | {row['password']:<15} | {row['id']:<10}")
        idx += 1
        
    print('═'*82)
        
    i = input('\nKetik enter untuk kembali')

def hapus_akun_buyer():
    baca = pd.read_csv(FILE_USER)
    buyer = baca[baca['role'] == 'buyer']
    
    os.system('cls')
    
    print('╔' + '═'*48 + '╗')
    print('║' + 'Hapus Akun'.center(48) + '║')
    print('║' + 'Pembeli'.center(48) + '║')
    print('╚' + '═'*48 + '╝')
    print()
    
    if buyer.empty:
        print('Tidak ada akun pembeli yang terdaftar')
        
        i = input('\nTekan enter untuk kembali')
        return
    
    print('═'*82)
    print(f"{'Index':<7} | {'Username':<15} | {'Email':<25} | {'Password':<15} | {'ID':<10}")
    print('═'*82)
    
    idx = 1
    
    for index, row in buyer.iterrows():
        print(f"{idx:<7} | {row['username']:<15} | {row['email']:<25} | {row['password']:<15} | {row['id']:<10}")
        idx += 1
        
    print('═'*82)
    print()
    
    kondisi = True
    kembali = 0
    
    while kondisi:
        try:
            id_tanya = int(input('Hapus user ID : '))
            
            if id_tanya not in buyer['id'].values:
                if kembali == 2:
                    i = input('\nTekan enter untuk kembali')
                    return
                kembali +=1
                print('Masukkan ID pembeli yang valid!')
            else:
                kondisi = False
        except:
            if kembali == 2:
                i = input('\nTekan enter untuk kembali')
                return
            kembali +=1
            print('Masukkan ID pembeli yang valid!')
            
    tanya = input('\nApakah anda yakin untuk menghapus akun ini (y) : ').lower()
    
    if tanya == 'y':
        pass
    else:
        i = input('\nTekan enter untuk kembali')
        return

    index_hapus = baca[baca['id'] == id_tanya].index 
    baca.drop(index=index_hapus, inplace=True)
    
    baca.to_csv(FILE_USER, index=False)
    
    print(f'\nTelah menghapus profil pengguna #{id_tanya}')
    
    i = input('\nKetik enter untuk kembali')

def get_user_by_role(role):
    file_user = 'data_user.csv'
    
    if not os.path.exists(file_user):
        print(f"File {file_user} tidak ditemukan.")
        return None
    
    try:
        df_user = pd.read_csv(file_user)
    except Exception as e:
        print(f"Error membaca file data_user.csv: {e}")
        return None
    
    if 'username' not in df_user.columns or 'role' not in df_user.columns:
        print("File data_user.csv tidak memiliki kolom yang diperlukan: 'username' dan 'role'.")
        return None
    
    buyer_users = df_user[df_user['role'] == role]['username'].tolist()
    
    if not buyer_users:
        print(f"Tidak ada pengguna dengan role {role}.")
        return None
    
    return buyer_users
    
def biaya_admin(folder_pembeli, buyer_users):
    sub_folder = os.path.join(folder_pembeli, f'{buyer_users}')
    histori_file = os.path.join(sub_folder, f'histori_{buyer_users}.csv')

    os.system('cls')
    if not os.path.exists(histori_file):
        print(f"Tidak ada data pembelian untuk {buyer_users}.")
        i = input('\nTekan enter untuk kembali...')
        return
    
    try:
        df = pd.read_csv(histori_file)
    except Exception as e:
        print(f"Error membaca file CSV: {e}")
        return

    required_columns = {'barang', 'harga', 'jumlah'}
    if not required_columns.issubset(df.columns):
        print(f"File CSV tidak memiliki kolom yang diperlukan: {required_columns}")
        return

    df['total_harga'] = df['harga'] * df['jumlah']

    try:
        print("\nTabel Data Belanja:")
        print("-" * 60)
        print(f"{'Barang':<20} {'Jumlah':<10} {'Harga':<10} {'Total Harga':<10}")
        print("-" * 60)
        
        for _, row in df.iterrows():
            print(f"{row['barang']:<20} {row['jumlah']:<10} {row['harga']:<10} {row['total_harga']:<10}")
        
        total_belanja = df['total_harga'].sum()
        biaya_admin_total = total_belanja * 0.08

        print("-" * 60)
        print(f"\nTotal Belanja: {total_belanja}")
        print(f"Total Biaya Admin (8%): {biaya_admin_total}")
    except ValueError:
        print("Masukkan nomor yang valid!")
    
    input('\nTekan enter untuk kembali...')
    pilih_pembeli_dan_hitung()
    
    result_df = pd.DataFrame({
        'Total Belanja': [total_belanja],
        'Total Biaya Admin': [biaya_admin_total]
    })

    sub_folder = os.path.join(folder_admin,f'{buyer_users}')
    if not os.path.exists(sub_folder):
        os.makedirs(sub_folder)
    
    total_terbeli_file = os.path.join(sub_folder, f'total_terbeli_{buyer_users}.csv')
    if not os.path.exists(total_terbeli_file):  
        user_df = pd.DataFrame(columns=['Total Belanja', 'Total Biaya Admin']) 
        user_df.to_csv(total_terbeli_file, index=False)

    try:
        result_df = pd.DataFrame({'Total Belanja': [total_belanja], 'Total Biaya Admin': [biaya_admin_total]})
        result_df.to_csv(total_terbeli_file, index=False)
    except Exception as e:
        print(f"Error menyimpan file CSV: {e}")
        return

def pilih_pembeli_dan_hitung():
    buyer_users = get_user_by_role('buyer')
    if buyer_users:
        while True:
            os.system('cls')
            print("\nDaftar pembeli yang tersedia:")
            for idx, user in enumerate(buyer_users, 1):
                print(f"{idx}. {user}")
            print(f"{len(buyer_users) + 1}. Kembali ke menu sebelumnya") 

            try:
                pilihan_user = int(input("\nPilih pembeli (nomor): ")) - 1
                if 0 <= pilihan_user < len(buyer_users):
                    user = buyer_users[pilihan_user] 
                    folder_pembeli = 'data_pembeli'  
                    biaya_admin(folder_pembeli, user)
                    break
                elif pilihan_user == len(buyer_users):
                    print("Kembali ke menu sebelumnya")
                    break
                else:
                    print("Pilihan tidak valid.")
                    input("\nTekan Enter untuk kembali ke pilihan...")
            except ValueError:
                print("Inputan tidak valid. Masukkan nomor yang sesuai.")
                input("\nTekan Enter untuk kembali ke pilihan...")
    else:
        print("Tidak ada pembeli terdaftar.")
    
    
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<FITUR PROFIL>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def profil(index):
    os.system('cls')
    
    baca = pd.read_csv(FILE_USER)
    
    user = baca.at[index, 'username']
    email = baca.at[index, 'email']
    role = baca.at[index, 'role']
    
    print('╔' + '═'*48 + '╗')
    print('║' + 'Profil Akun'.center(48) + '║')
    print('╚' + '═'*48 + '╝')
    
    print(f'\nUsername : {user}\nEmail : {email}\nPeran : {role}')
    
    i = input('\nKetik apa saja untuk kembali')

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<MENU PENJUAL>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def menu_penjual(email):
    baca = pd.read_csv(FILE_USER)
    
    kondisi = True
    
    index = baca[baca['email'] == email].index[0]
    user = baca.at[index, 'username']
    
    while kondisi:
        os.system('cls')
        
        print('╔' + '═'*48 + '╗')
        print('║' + 'Menu Penjual'.center(48) + '║')
        print('╠' + '═'*48 + '╣')
        print('║' + user.center(48) + '║')
        print('╚' + '═'*48 + '╝')
        
        print('\n1. Profil akun\n2. Edit barang\n3. Riwayat Penjualan\n4. Keluar akun')
        
        kondisi2 = True
        
        while kondisi2:
                pilihan = input('\nGunakan menu nomor : ')
                
                if pilihan == '1':
                    profil(index)
                    kondisi2 = False
                elif pilihan == '2':
                    edit_barang_penjual(user)
                    kondisi2 = False
                elif pilihan == '3':
                    tampilkan_histori_penjualan(user)
                    kondisi2 = False
                elif pilihan == '4':
                    kondisi2 = False
                    kondisi = False
                else:
                    print('\nMasukkan input yang benar!')

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<FITUR ISI DARI MENU EDIT BARANG PENJUAL>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def edit_barang_penjual(user):    
    sub_folder = os.path.join(folder_toko, f'toko_{user}')
    
    if not os.path.exists(sub_folder):
        os.makedirs(sub_folder)
    
    barang = os.path.join(sub_folder, f'toko_{user}.csv')
    
    if not os.path.exists(barang):  
        user_df = pd.DataFrame(columns=['barang', 'harga', 'stok']) 
        user_df.to_csv(barang, index=False)
        
    kondisi = True

    while kondisi:
        os.system('cls')
        
        print('╔' + '═'*48 + '╗')
        print('║' + 'Edit Barang'.center(48) + '║')
        print('╚' + '═'*48 + '╝')
        
        print('\n1. List barang\n2. Tambah jenis barang\n3. Hapus jenis barang\n4. Edit harga\n5. Edit stok barang\n6. Kembali')
        
        kondisi2 = True
            
        while kondisi2:
                pilihan = input('\nGunakan menu nomor : ')
                
                if pilihan == '1':
                    list_barang(user)
                    kondisi2 = False
                elif pilihan == '2':
                    tambah_barang(user)
                    kondisi2 = False
                elif pilihan == '3':
                    hapus_barang(user)
                    kondisi2 = False
                elif pilihan == '4':
                    edit_harga(user)
                    kondisi2 = False
                elif pilihan == '5':
                    edit_stok(user)
                    kondisi2 = False
                elif pilihan == '6':
                    kondisi2 = False
                    kondisi = False
                else:
                    print('Masukkan input yang benar!')

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<FITUR EDIT BARANG>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#FITUR LIHAT LIST BARANG
def list_barang(user):
    sub_folder = os.path.join(folder_toko, f'toko_{user}')
    file_barang = os.path.join(sub_folder, f'toko_{user}.csv')
    
    baca = pd.read_csv(file_barang)
    os.system('cls')

    print('╔' + '═'*48 + '╗')
    print('║' + 'List Barang'.center(48) + '║')
    print('╚' + '═'*48 + '╝')
    print()
    
    if baca.empty:
        print('Tidak ada barang dalam toko ini!')
        i = input('\nTekan enter untuk kembali')
        return
    
    print('List barang:')
    print(f"{'No':<5}{'Nama Barang':<20}{'Harga':<10}{'Stok':<10}")
    print('-' * 45)
    for index, row in baca.iterrows():
        no = index + 1
        barang = row['barang']
        harga = row['harga']
        stok = row['stok']
        print(f"{no:<5}{barang:<20}{harga:<10}{stok:<10}")
    print('-' * 45)
    
    i = input('\nTekan enter untuk kembali')

#FITUR TAMBAH BARANG
def tambah_barang (user):
    sub_folder = os.path.join(folder_toko, f'toko_{user}')
    file_barang = os.path.join(sub_folder, f'toko_{user}.csv')
    baca = pd.read_csv(file_barang)

    os.system('cls')
    print('╔' + '═'*48 + '╗')
    print('║' + 'Tambah Jenis Barang'.center(48) + '║')
    print('╚' + '═'*48 + '╝')
    print()
    
    kondisi2 = True
    while kondisi2:
        barang = input('Masukkan nama barang : ')
        
        if not barang:  # Jika input kosong, kembali ke menu
            print("\nKembali ke menu sebelumnya.")
            input("Tekan enter untuk kembali.")
            return
        
        if barang in baca['barang'].values:
            print('Barang sudah ada dalam data!')
        else:
            kondisi2 = False
    
    kondisi3 = True
    while kondisi3:
        try:
            harga = int(input('Masukkan harga barang : '))
            
            kondisi3 = False
        except:
            print('Masukkan input berupa angka!')
            
    kondisi4 = True
    while kondisi4:
        try:
            stok = int(input('Masukkan stok barang : '))
            
            kondisi4 = False
        except:
            print('Masukkan input berupa angka!')
            
    data_baru = {'barang': barang, 'harga': harga, 'stok': stok}
    df_barang = pd.concat([baca, pd.DataFrame([data_baru])], ignore_index=True)
    df_barang.to_csv(file_barang, index=False)
    
    print(f'\n{barang} telah ditambahkan dengan harga : {harga} dan stok : {stok}')
    i = input('\nTekan enter untuk kembali')

#FITUR HAPUS BARANG    
def hapus_barang(user):
    sub_folder = os.path.join(folder_toko, f'toko_{user}')
    file_barang = os.path.join(sub_folder, f'toko_{user}.csv')
    baca = pd.read_csv(file_barang)
    
    os.system('cls')
    print('╔' + '═'*48 + '╗')
    print('║' + 'Hapus Barang'.center(48) + '║')
    print('╚' + '═'*48 + '╝')
    print()
    
    if baca.empty:
        print('Tidak ada barang dalam toko ini!')
        i = input('\nTekan enter untuk kembali')
        return
    
    print('List barang:')
    for index, row in baca.iterrows():
        barang = row['barang']
        harga = row['harga']
        stok = row['stok']
        print(f'{index + 1}. {barang} | harga = {harga} | stok = {stok}')
        
    kondisi = True
    print()
    
    while kondisi:
        hapus_item = input('Hapus item nomor (kosong untuk kembali): ')

        if hapus_item.strip() == '':
            print('\nTidak ada barang yang dihapus. Kembali ke menu.')
            input('\nTekan enter untuk kembali')
            return
        
        if hapus_item.isdigit():
            hapus_item = int(hapus_item)
            if 1 <= hapus_item <= len(baca):
                kondisi = False
            else:
                print('Masukkan nomor barang yang sudah ada di atas!')
        else:
            print('Masukkan input yang benar!')
    
    baca.drop(baca.index[hapus_item - 1], inplace=True)
    baca.to_csv(file_barang, index=False)
    
    print(f'\nBarang urutan {hapus_item} telah dihapus')

    i = input('\nTekan enter untuk kembali')
    
#FITUR EDIT HARGA BARANG
def edit_harga(user):
    sub_folder = os.path.join(folder_toko, f'toko_{user}')
    file_barang = os.path.join(sub_folder, f'toko_{user}.csv')
    baca = pd.read_csv(file_barang)
    
    os.system('cls')
    print('╔' + '═'*48 + '╗')
    print('║' + 'Edit Harga'.center(48) + '║')
    print('╚' + '═'*48 + '╝')
    print()
    
    if baca.empty:
        print('Tidak ada barang dalam toko ini!')
        i = input('\nTekan enter untuk kembali')
        return
    
    print('List barang:')
    for index, row in baca.iterrows():
        barang = row['barang']
        harga = row['harga']
        stok = row['stok']
        print(f'{index + 1}. {barang} | harga = {harga} | stok = {stok}')
        
    kondisi = True
    print()
    
    while kondisi:
        index_ubah = input('Ubah item nomor : ')
        
        if index_ubah == '':  # Jika input kosong, kembali ke menu
            print("\nKembali ke menu sebelumnya.")
            input("\nTekan enter untuk kembali.")
            return

        if index_ubah.isdigit():  # Validasi input angka
            index_ubah = int(index_ubah)
            if 1 <= index_ubah <= len(baca):
                kondisi = False
            else:
                print("Masukkan nomor barang yang sesuai daftar!")
        else:
            print("Masukkan nomor berupa angka!")

    barang_dipilih = baca.iloc[index_ubah-1]
    print(f'\nBarang yang dipilih: {barang_dipilih['barang']} | harga saat ini = {barang_dipilih['harga']}\n')
    
    kondisi2 = True
    
    while kondisi2:
        harga_baru = input('Masukkan harga baru : ')
        
        if harga_baru == '':  # Jika input kosong, kembali ke menu
            print("\nTidak ada perubahan harga. Kembali ke menu.")
            input("\nTekan enter untuk kembali.")
            return

        if harga_baru.isdigit():
            harga_baru = int(harga_baru)
            kondisi2 = False
        else:
            print("Masukkan input berupa angka!")
            
    baca.at[index_ubah-1, 'harga'] = harga_baru
    baca.to_csv(file_barang, index=False)
    
    print(f'\nHarga barang {barang_dipilih['barang']} berhasil diubah menjadi {harga_baru}.')
    i = input('\nTekan enter untuk kembali')
    
#FITUR EDIT STOK BARANG
def edit_stok(user):
    sub_folder = os.path.join(folder_toko, f'toko_{user}')
    file_barang = os.path.join(sub_folder, f'toko_{user}.csv')
    baca = pd.read_csv(file_barang)
    
    os.system('cls')
    print('╔' + '═'*48 + '╗')
    print('║' + 'Edit Stok'.center(48) + '║')
    print('╚' + '═'*48 + '╝')
    print()
    
    if baca.empty:
        print('Tidak ada barang dalam toko ini!')
        i = input('\nTekan enter untuk kembali')
        return
    
    print('List barang:')
    for index, row in baca.iterrows():
        barang = row['barang']
        harga = row['harga']
        stok = row['stok']
        print(f'{index + 1}. {barang} | harga = {harga} | stok = {stok}')
        
    kondisi = True

    print()
    
    while kondisi:
        index_ubah = input('Ubah item nomor : ')
        
        if index_ubah == '':  # Jika input kosong, kembali ke menu
            print("\nKembali ke menu sebelumnya.")
            input("\nTekan enter untuk kembali.")
            return
        
        if index_ubah.isdigit():  # Validasi input angka
            index_ubah = int(index_ubah)
            if 1 <= index_ubah <= len(baca):
                kondisi = False
            else:
                print("Masukkan nomor barang yang sesuai daftar!")
        else:
            print("Masukkan nomor berupa angka!")
    
    barang_dipilih = baca.iloc[index_ubah-1]
    print(f'\nBarang yang dipilih: {barang_dipilih['barang']} | stok saat ini = {barang_dipilih['stok']}\n')
    
    kondisi2 = True
    
    while kondisi2:
        stok_baru = input('Masukkan stok baru : ')
        
        if stok_baru == '': 
            print("\nTidak ada perubahan harga. Kembali ke menu.")
            input("\nTekan enter untuk kembali.")
            return

        if stok_baru.isdigit():
            stok_baru = int(stok_baru)
            kondisi2 = False
        else:
            print("Masukkan input berupa angka!")
            
    baca.at[index_ubah-1, 'stok'] = stok_baru
    baca.to_csv(file_barang, index=False)
    
    print(f'\nStok barang {barang_dipilih['barang']} berhasil diubah menjadi {stok_baru}.')
    
    i = input('\nTekan enter untuk kembali')

def tampilkan_histori_penjualan(user):
    folder_toko = 'data_toko'
    sub_folder = os.path.join(folder_toko, f'toko_{user}')
    file_histori = os.path.join(sub_folder, f'histori_toko_{user}.csv')
    os.system('cls')
    print('╔' + '═' * 50 + '╗')
    print('║' + 'Histori Penjualan'.center(50) + '║')
    print('╚' + '═' * 50 + '╝')

    if not os.path.exists(file_histori):
        print(f"Belum ada histori penjualan untuk toko {user}.")
        input("\nTekan enter untuk kembali.")
        return

    try:
        histori_df = pd.read_csv(file_histori)
    except Exception as e:
        print(f"Terjadi kesalahan saat membaca file histori: {e}")
        input("\nTekan enter untuk kembali.")
        return

    if histori_df.empty:
        print("File histori penjualan kosong.")
        input("\nTekan enter untuk kembali.")
        return

    if 'harga' not in histori_df.columns or 'terjual' not in histori_df.columns:
        print("File CSV tidak memiliki kolom 'harga' atau 'terjual'.")
        print("Kolom yang ditemukan:", histori_df.columns)
        input("\nTekan enter untuk kembali.")
        return

    print(f"\nHistori penjualan untuk toko {user}:")
    print(f"{'No':<5} {'Barang':<30} {'Terjual':<10} {'Harga':<10} {'Total Harga':<15}")
    print('-' * 70)

    total_penjualan = 0
    for index, row in histori_df.iterrows():
        total_harga = row['terjual'] * row['harga']
        total_penjualan += total_harga
        print(f"{index + 1:<5} {row['barang']:<30} {row['terjual']:<10} {row['harga']:<10} {total_harga:<15}")

    print('-' * 70)
    print(f"{'Total Penjualan:':<55} {total_penjualan:<15}")

    input("\nTekan enter untuk kembali.")


def perbarui_histori_penjualan(riwayat_belanja):
    for transaksi in riwayat_belanja:
        for item in transaksi['item']:
            toko = item['toko']
            nama_barang = item['barang']
            jumlah_terjual = item['jumlah']
            harga_terjual = item['harga']

            sub_folder = os.path.join('data_toko', f'{toko}')
            
            if not os.path.exists(sub_folder):
                os.makedirs(sub_folder)
            
            file_histori = os.path.join(sub_folder, f'histori_{toko}.csv')

            if not os.path.exists(file_histori):
                histori_df = pd.DataFrame(columns=['barang', 'terjual', 'harga', 'total_harga', 'total_penjualan'])
                histori_df.to_csv(file_histori, index=False)
            else:
                histori_df = pd.read_csv(file_histori)

            if nama_barang in histori_df['barang'].values:
                histori_df.loc[histori_df['barang'] == nama_barang, 'terjual'] += jumlah_terjual
                histori_df.loc[histori_df['barang'] == nama_barang, 'total_harga'] = \
                    histori_df.loc[histori_df['barang'] == nama_barang, 'terjual'] * harga_terjual
            else:
                total_harga = jumlah_terjual * harga_terjual
                new_row = {'barang': nama_barang, 'terjual': jumlah_terjual, 'harga': harga_terjual, 
                           'total_harga': total_harga, 'total_penjualan': 0}  
                histori_df = pd.concat([histori_df, pd.DataFrame([new_row])], ignore_index=True)

            total_penjualan = histori_df['total_harga'].sum()
            histori_df['total_penjualan'] = total_penjualan

            histori_df.to_csv(file_histori, index=False)


#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<MENU PEMBELI>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def menu_pembeli(email):
    baca = pd.read_csv(FILE_USER)
    
    kondisi = True
    
    index = baca[baca['email'] == email].index[0]
    user = baca.at[index, 'username']
    
    while kondisi:
        os.system('cls')
        
        print('╔' + '═'*48 + '╗')
        print('║' + 'Menu Pembeli'.center(48) + '║')
        print('╠' + '═'*48 + '╣')
        print('║' + user.center(48) + '║')
        print('╚' + '═'*48 + '╝')
        
        print('\n1. Profil akun\n2. Beli barang\n3. Histori pembelian\n4. Keluar akun')
        
        pilihan = input('\nGunakan menu nomor : ')
        
        if not pilihan: 
            print("Kembali ke menu sebelumnya...")
            i = input('\nTekan enter untuk kembali')
            break
        
        if pilihan == '1':
            profil(index)
        elif pilihan == '2':
            menu_belibarang(user)
        elif pilihan == '3':
            tampilkan_riwayat_belanja(user)
        elif pilihan == '4':
            kondisi = False
        else:
            print('Masukkan input yang benar!')
            i = input('\nTekan enter untuk kembali')

#FITUR ISI DARI MENU BELI BARANG
def menu_belibarang(user):
    while True:
        os.system('cls')
        print('╔' + '═'*48 + '╗')
        print('║' + 'Menu Beli Barang'.center(48) + '║')
        print('╚' + '═'*48 + '╝')
        
        print('\n1. Daftar Toko\n2. Keranjang Belanja\n3. Kembali')
        
        pilihan = input('\nGunakan menu nomor : ')
        
        if not pilihan: 
            print("Kembali ke menu sebelumnya...")
            break
        
        if pilihan == '1':    
            daftar_toko()
        elif pilihan == '2':
            tampilkan_keranjang(user)
        elif pilihan == '3':
            break  
        else:
            print('Masukkan input yang benar!')
            i = input('\nTekan enter untuk kembali')

keranjang = []
riwayat_belanja = []

# FITUR DAFTAR TOKO
def daftar_toko():
    os.system('cls')
    print('╔' + '═' * 48 + '╗')
    print('║' + 'Daftar Toko'.center(48) + '║')
    print('╚' + '═' * 48 + '╝')
    print()
    
    list_toko = os.listdir(folder_toko)
    
    if not list_toko:
        print('Tidak ada toko yang terdaftar.')
        i = input('\nTekan enter untuk kembali')
        return
    
    for idx, toko in enumerate(list_toko, start=1):
        print(f'{idx}. {toko}')
    
    print()
    try:
        pilihan_toko = int(input('Pilih toko (nomor): '))
        if 1 <= pilihan_toko <= len(list_toko):
            nama_toko = list_toko[pilihan_toko - 1]
            daftar_barang(nama_toko)
        else:
            print('Pilihan tidak valid!')
    except ValueError:
        print('Masukkan nomor yang valid!')
        i = input('\nTekan enter untuk kembali')

# FITUR DAFTAR BARANG (setelah daftar toko)
def daftar_barang(nama_toko):
    os.system('cls')
    print('╔' + '═' * 48 + '╗')
    print('║' + 'Daftar Barang'.center(48) + '║')
    print('║' + nama_toko.center(48) + '║')
    print('╚' + '═' * 48 + '╝')
    print()
    
    file_barang = os.path.join(folder_toko, nama_toko, f'{nama_toko}.csv')
    
    if not os.path.exists(file_barang):
        print(f'Error: File {file_barang} tidak ditemukan!')
        i = input('\nTekan enter untuk kembali')
        return
    
    try:
        baca = pd.read_csv(file_barang)
        if baca.empty:
            print('Tidak ada barang dalam toko ini!')
            i = input('\nTekan enter untuk kembali')
            return
    except Exception as e:
        i = input('\nTekan enter untuk kembali')
        return
    
    print('List barang:')
    for index, row in baca.iterrows():
        barang = row['barang']
        harga = row['harga']
        stok = row['stok']
        print(f'{index + 1}. {barang} | harga = Rp{harga:,} | stok = {stok}')
    
    print()
    pilihan_barang = input('Masukkan nomor barang untuk ditambahkan ke keranjang: ')
    
    if pilihan_barang:
        try:
            pilihan = int(pilihan_barang)
            if 1 <= pilihan <= len(baca):
                barang_dipilih = baca.iloc[int(pilihan_barang) - 1]
                jumlah = int(input('Masukkan jumlah yang ingin dibeli: '))
                if 0 < jumlah <= barang_dipilih["stok"]:
                    baca.loc[baca.index == barang_dipilih.name, 'stok'] -= jumlah
                    baca.to_csv(file_barang, index=False)
                    
                    keranjang.append({
                        "barang": barang_dipilih["barang"],
                        "harga": barang_dipilih["harga"],
                        "jumlah": jumlah,
                        "toko": nama_toko
                    })
                    print(f'{barang_dipilih["barang"]} sebanyak {jumlah} telah ditambahkan ke keranjang.')
                else:
                    print('Jumlah melebihi stok yang tersedia atau tidak valid.')
                    jumlah = int(input('Masukkan jumlah yang ingin dibeli sesuai stok: '))
            else:
                print('Pilihan tidak valid!')
                jumlah = int(input('Masukkan jumlah yang ingin dibeli: '))
        except ValueError:
            print('Masukkan angka yang valid!')
            i = input('\nTekan enter untuk kembali')
        
    daftar_toko()

#FITUR KERANJANG BELANJA
def tampilkan_keranjang(user):
    os.system('cls')
    print('╔' + '═' * 48 + '╗')
    print('║' + 'Keranjang Belanja'.center(48) + '║')
    print('╚' + '═' * 48 + '╝')
    print()

    if not keranjang:
        print('Keranjang kosong!')
        input('\nTekan enter untuk kembali')
        return
    
    total_harga = 0
    print(f'{"No":<3} {"Barang":<20} {"Nama Toko":<15} {"Jumlah":<8} {"Harga Satuan":<12} {"Subtotal":<12}')
    print('-' * 78)
    for idx, item in enumerate(keranjang, start=1):
        subtotal = item['jumlah'] * item['harga']
        total_harga += subtotal
        print(f'{idx:<3} {item["barang"]:<20} {item["toko"]:<15} {item["jumlah"]:<8} Rp{item["harga"]:<12,} Rp{subtotal:<12}')
        if not all(key in item for key in ['barang', 'harga', 'jumlah', 'toko']):
            continue

    print('-' * 78)
    print(f'Total Belanja: Rp{total_harga:,}')

    keadaan = True
    while keadaan:
        print("\nApakah anda yakin ingin checkout?\n1. Checkout\n2. Hapus Keranjang Belanja\n3. Ubah Keranjang Belanja\n4. kembali")
        pilihan = input('\nSilahkan Pilih: ')
        if pilihan.lower() == '1':
            checkout(total_harga)
            simpan_riwayat_belanja(user, riwayat_belanja)
            keadaan = False
        elif pilihan.lower() == '2':
            hapus_keranjang_belanja(user)
            keadaan = False
        elif pilihan.lower() == '3':
            ubah_jumlah_barang(user)
            keadaan = False
        elif pilihan.lower() == '4':
            keadaan = False
        else:
            input('\nTekan enter untuk kembali')

# FITUR CHECKOUT DAN NOTA
def checkout(total_harga):
    os.system('cls')
    print('╔' + '═' * 48 + '╗')
    print('║' + 'Nota Belanja'.center(48) + '║')
    print('╚' + '═' * 48 + '╝')
    print()
    
    print(f'{"Barang":<20} {"Nama Toko":<15} {"Jumlah":<8} {"Harga Satuan":<12} {"Subtotal":<12}')
    print('-' * 78)

    transaksi = []  
    for item in keranjang:
        if not all(key in item for key in ['barang', 'harga', 'jumlah', 'toko']):
            continue

        subtotal = item['jumlah'] * item['harga']
        print(f'{item["barang"]:<20} {item["toko"]:<15} {item["jumlah"]:<8} Rp{item["harga"]:<12,} Rp{subtotal:<12}')
        
        transaksi.append({
            'barang': item['barang'],
            'toko': item['toko'],
            'jumlah': item['jumlah'],
            'harga': item['harga'],
            'subtotal': subtotal
        })

    print('-' * 78)
    print(f'Total Belanja: Rp{total_harga:,}')
    print('\nTerima kasih telah berbelanja!')

    riwayat_belanja.append({
        'total': total_harga,
        'item': transaksi
    })

    keranjang.clear()
    input('\nTekan enter untuk kembali ke menu utama')
    perbarui_histori_penjualan(riwayat_belanja)

#FITUR TIDAK JADI CHECKOUT
def hapus_keranjang_belanja(user):
    os.system('cls')
    print('╔' + '═' * 48 + '╗')
    print('║' + 'Hapus Barang dari Keranjang'.center(48) + '║')
    print('╚' + '═' * 48 + '╝')
    print()
    
    if not keranjang:
        print('Keranjang Anda kosong.')
        input('\nTekan enter untuk kembali ke menu utama.')
        return

    try:
        total_harga = 0
        print(f'{"No":<3} {"Barang":<20} {"Nama Toko":<15} {"Jumlah":<8} {"Harga Satuan":<12} {"Subtotal":<12}')
        print('-' * 78)
        for idx, item in enumerate(keranjang, start=1):
            subtotal = item['jumlah'] * item['harga']
            total_harga += subtotal
            print(f'{idx:<3} {item["barang"]:<20} {item["toko"]:<15} {item["jumlah"]:<8} Rp{item["harga"]:<12,} Rp{subtotal:<12}')
            if not all(key in item for key in ['barang', 'harga', 'jumlah', 'toko']):
                continue

        print('-' * 78)
        print(f'Total Belanja: Rp{total_harga:,}')
        pilihan = int(input('\nMasukkan nomor barang yang ingin dihapus: '))
        if 1 <= pilihan <= len(keranjang):
            item_hapus = keranjang.pop(pilihan - 1)
            file_barang = os.path.join(folder_toko, item_hapus['toko'], f'{item_hapus["toko"]}.csv')
            if os.path.exists(file_barang):
                baca = pd.read_csv(file_barang)
                baca.loc[baca['barang'] == item_hapus['barang'], 'stok'] += item_hapus['jumlah']
                baca.to_csv(file_barang, index=False)
                print(f'{item_hapus["barang"]} dari {item_hapus["toko"]} telah dihapus dari keranjang.')
        else:
            print('Pilihan tidak valid!')
    except ValueError:
        print("Masukkan nomor yang valid!")
    
    input('\nTekan enter untuk checkout')
    tampilkan_keranjang(user)

#FITUR TIDAK JADI CHECKOUT
def ubah_jumlah_barang(user):   
    os.system('cls')
    print('╔' + '═' * 48 + '╗')
    print('║' + 'Ubah Jumlah Barang dari Keranjang'.center(48) + '║')
    print('╚' + '═' * 48 + '╝')
    print()
    
    if not keranjang:
        print('Keranjang Anda kosong.')
        input('\nTekan enter untuk kembali ke menu utama.')
        return

    try:
        total_harga = 0
        print(f'{"No":<3} {"Barang":<20} {"Nama Toko":<15} {"Jumlah":<8} {"Harga Satuan":<12} {"Subtotal":<12}')
        print('-' * 78)
        for idx, item in enumerate(keranjang, start=1):
            subtotal = item['jumlah'] * item['harga']
            total_harga += subtotal
            print(f'{idx:<3} {item["barang"]:<20} {item["toko"]:<15} {item["jumlah"]:<8} Rp{item["harga"]:<12,} Rp{subtotal:<12}')
            if not all(key in item for key in ['barang', 'harga', 'jumlah', 'toko']):
                continue

        print('-' * 78)
        print(f'Total Belanja: Rp{total_harga:,}') 
        pilihan = int(input("\nMasukkan nomor barang yang ingin diubah (enter untuk kembali): "))
        if 1 <= pilihan <= len(keranjang):
            item = keranjang[pilihan - 1]
            file_barang = os.path.join(folder_toko, item['toko'], f'{item['toko']}.csv')

            baca = pd.read_csv(file_barang)
            stok_tersedia = baca.loc[baca['barang'] == item['barang'], 'stok'].values[0] + item['jumlah']  # Tambahkan kembali stok lama
            
            print(f"Stok tersedia untuk {item['barang']}: {stok_tersedia}")
            jumlah_baru = int(input(f"Masukkan jumlah baru untuk {item['barang']}: "))
            if 0 < jumlah_baru <= stok_tersedia:
                baca.loc[baca['barang'] == item['barang'], 'stok'] = stok_tersedia - jumlah_baru
                baca.to_csv(file_barang, index=False)
                item['jumlah'] = jumlah_baru
                print(f"Jumlah {item['barang']} dari {item['toko']} telah diperbarui menjadi {jumlah_baru}.")
            else:
                print("Jumlah yang dimasukkan tidak valid.")
        else:
            print("Pilihan tidak valid!")
    except ValueError:
        print("Masukkan nomor yang valid!")
    
    input('\nTekan enter untuk checkout')
    tampilkan_keranjang(user)

def simpan_riwayat_belanja(user, riwayat_belanja):
    folder_pembeli = 'data_pembeli'
    sub_folder = os.path.join(folder_pembeli, f'{user}')

    if not os.path.exists(folder_pembeli):
        os.makedirs(folder_pembeli)
    if not os.path.exists(sub_folder):
        os.makedirs(sub_folder)

    histori = os.path.join(sub_folder, f'histori_{user}.csv')

    data = []
    for transaksi in riwayat_belanja:
        tanggal_transaksi = transaksi.get('tanggal', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        for item in transaksi['item']:
            data.append({
                'tanggal': tanggal_transaksi,
                'barang': item['barang'],
                'toko': item['toko'],
                'jumlah': item['jumlah'],
                'harga': item['harga'],
                'subtotal': item['subtotal'],
                'total': transaksi['total']
            })

    try:
        if os.path.exists(histori):
            df_lama = pd.read_csv(histori)
            df_baru = pd.DataFrame(data)
            df_tergabung = pd.concat([df_lama, df_baru], ignore_index=True)
        else:
            df_tergabung = pd.DataFrame(data)
        
        df_tergabung.to_csv(histori, index=False)
        print(f"Riwayat belanja telah berhasil disimpan untuk user {user}.")
    except Exception as e:
        print(f"Error menyimpan file riwayat: {e}")

def tampilkan_riwayat_belanja(user):
    sub_folder = os.path.join(folder_pembeli, f'{user}')
    histori_file = os.path.join(sub_folder, f'histori_{user}.csv')
    os.system('cls')
    print('╔' + '═' * 48 + '╗')
    print('║' + 'Riwayat Belanja'.center(48) + '║')
    print('╠' + '═' * 48 + '╣')
    print('║' + 'Pembeli: {}'.format(user).center(48) + '║')
    print('╚' + '═' * 48 + '╝')
    print()

    if not os.path.exists(histori_file):
        print('Belum ada riwayat belanja.')
        input('\nTekan enter untuk kembali ke menu utama')
        return

    try:
        histori_df = pd.read_csv(histori_file)
    except Exception as e:
        print(f"Terjadi kesalahan saat membaca file riwayat: {e}")
        input('\nTekan enter untuk kembali ke menu utama')
        return

    if histori_df.empty:
        print('Belum ada riwayat belanja.')
    else:
        grouped = histori_df.groupby('tanggal')
        for tanggal, transaksi in grouped:
            print(f'Transaksi Tanggal: {tanggal}')
            print(f'{"Barang":<20} {"Nama Toko":<15} {"Jumlah":<8} {"Harga Satuan":<12} {"Subtotal":<12}')
            print('-' * 78)
            for _, row in transaksi.iterrows():
                print(
                    f'{row["barang"]:<20} {row["toko"]:<15} {row["jumlah"]:<8} '
                    f'Rp{row["harga"]:<12,} Rp{row["subtotal"]:<12,}'
                )
            total = transaksi['total'].iloc[0] 
            print('-' * 78)
            print(f'Total Belanja: Rp{total:,}')
            print()

    input('\nTekan enter untuk kembali ke menu utama')

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<PROGRAM UTAMA>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def main():
    os.system('cls')

    cek_data()
    
    kondisi = True
    
    while kondisi:
        print('╔' + '═'*48 + '╗')
        print('║' + 'NANDOER'.center(48) + '║')
        print('╠' + '═'*48 + '╣')
        print('║' + 'Pilihan Terpercaya Petani Indonesia'.center(48) + '║')
        print('╚' + '═'*48 + '╝') 
        print('\n1. Registrasi\n2. Login\n3. Keluar\n')
        
        kondisi2 = True
        
        while kondisi2:
            pilihan = input('Masukkan pilihan (1/2/3): ')
            
            if pilihan == '1':
                register()
                kondisi2 = False
                os.system('cls')
                '''pilihan2 = input('\n(Y) untuk kembali | (enter) untuk keluar : ').lower()
                if pilihan2 == 'y':
                    os.system('cls')
                else:
                    kondisi = False'''
            elif pilihan == '2':
                login()
                kondisi2 = False
                os.system('cls')
                '''pilihan2 = input('\n(Y) untuk kembali | (enter) untuk keluar : ').lower()
                if pilihan2 == 'y':
                    os.system('cls')
                else:
                    kondisi = False'''
            elif pilihan == '3':
                kondisi = False
                kondisi2 = False
            else:
                os.system('cls')
                print('╔' + '═'*48 + '╗')
                print('║' + 'NANDOER'.center(48) + '║')
                print('╠' + '═'*48 + '╣')
                print('║' + 'Pilihan Terpercaya Petani Indonesia'.center(48) + '║')
                print('╚' + '═'*48 + '╝') 
                print('\n1. Registrasi\n2. Login\n3. Keluar\n')
                print('Input anda tidak sesuai pilihan!')
    
    print('\nTerima kasih telah menggunakan program ini :)')
    
main()v
