import os
import datetime
import pandas as pd

FILE_ADMIN = 'data_admin.csv'
FILE_USER = 'data_user.csv'
folder_toko = 'data_toko'
folder_pembeli = 'data_pembeli'

#UNTUK PROGRAM UTAMA
def cek_data():
    if not os.path.exists(FILE_USER):  
        user = pd.DataFrame(columns=['username', 'password', 'email', 'role']) 
        user.to_csv(FILE_USER, index=False) 
    if not os.path.exists(FILE_ADMIN):  
        user = pd.DataFrame(columns=['username', 'password']) 
        user.to_csv(FILE_ADMIN, index=False) 
    if not os.path.exists(folder_toko):
        os.makedirs(folder_toko)
    if not os.path.exists(folder_pembeli):
        os.makedirs(folder_pembeli)

#UNTUK REGISTRASI
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

#MENU AWAL
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
        
        print('╔' + '═'*48 + '╗')
        print('║' + 'Registrasi Akun'.center(48) + '║')
        print('║' + 'Penjual'.center(48) + '║')
        print('╚' + '═'*48 + '╝')
        print()
        
        username = input('Masukkan username : ')
        
        while kondisi:
            password = input('Masukkan password : ')
            
            if len(password) < 8:
                print('Password harus berisi minimal 8 karakter!')
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
        
        print(f'\nRegistrasi {username} sebagai penjual telah berhasil') 
        
        i = input('\nKetik apa saja untuk kembali')
        
    elif pilihan == '2':
        os.system('cls')
        
        buyer = pd.read_csv(FILE_USER)
        
        kondisi = True
        kondisi2 = True
        
        print('╔' + '═'*48 + '╗')
        print('║' + 'Registrasi Akun'.center(48) + '║')
        print('║' + 'Pembeli'.center(48) + '║')
        print('╚' + '═'*48 + '╝')
        print()
        
        username = input('Masukkan username : ')
        
        while kondisi:
            password = input('Masukkan password : ')
            
            if len(password) < 8:
                print('Password harus berisi minimal 8 karakter!')
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

#MENU SETELAH LOGIN
def menu_admin(user):
    kondisi = True
    
    while kondisi:
        os.system('cls')
        
        print('╔' + '═'*48 + '╗')
        print('║' + 'Menu Admin'.center(48) + '║')
        print('╠' + '═'*48 + '╣')
        print('║' + user.center(48) + '║')
        print('╚' + '═'*48 + '╝')
        
        print('\n1. Edit akun penjual\n2. Edit akun pembeli\n3. Total Penjualan\n4. Keluar akun')
        
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
    print(f'{'Index':<7} | {'Username':<15} | {'Email':<25} | {'Password':<15} | {'ID':<10}')
    print('═'*82)
    
    idx = 1
    
    for index, row in seller.iterrows():
        print(f'{idx:<7} | {row['username']:<15} | {row['email']:<25} | {row['password']:<15} | {row['id']:<10}')
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
    print(f'{'Index':<7} | {'Username':<15} | {'Email':<25} | {'Password':<15} | {'ID':<10}')
    print('═'*82)
    
    idx = 1
    
    for index, row in seller.iterrows():
        print(f'{idx:<7} | {row['username']:<15} | {row['email']:<25} | {row['password']:<15} | {row['id']:<10}')
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
    print(f'{'Index':<7} | {'Username':<15} | {'Email':<25} | {'Password':<15} | {'ID':<10}')
    print('═'*82)
    
    idx = 1
    
    for index, row in seller.iterrows():
        print(f'{idx:<7} | {row['username']:<15} | {row['email']:<25} | {row['password']:<15} | {row['id']:<10}')
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
        print('║' + 'Menu Edit Akun Buyer'.center(48) + '║')
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
    print(f'{'Index':<7} | {'Username':<15} | {'Email':<25} | {'Password':<15} | {'ID':<10}')
    print('═'*82)
    
    idx = 1
    
    for index, row in buyer.iterrows():
        print(f'{idx:<7} | {row['username']:<15} | {row['email']:<25} | {row['password']:<15} | {row['id']:<10}')
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
    print('║' + 'Penjual'.center(48) + '║')
    print('╚' + '═'*48 + '╝')
    print()
    
    if buyer.empty:
        print('Tidak ada akun pembeli yang terdaftar')
        
        i = input('\nTekan enter untuk kembali')
        return
    
    print('═'*82)
    print(f'{'Index':<7} | {'Username':<15} | {'Email':<25} | {'Password':<15} | {'ID':<10}')
    print('═'*82)
    
    idx = 1
    
    for index, row in buyer.iterrows():
        print(f'{idx:<7} | {row['username']:<15} | {row['email']:<25} | {row['password']:<15} | {row['id']:<10}')
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
    print(f'{'Index':<7} | {'Username':<15} | {'Email':<25} | {'Password':<15} | {'ID':<10}')
    print('═'*82)
    
    idx = 1
    
    for index, row in buyer.iterrows():
        print(f'{idx:<7} | {row['username']:<15} | {row['email']:<25} | {row['password']:<15} | {row['id']:<10}')
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
        
        print('\n1. Profil akun\n2. Edit barang\n3. Riwayat Penjualan\n4. Total Penjualan\n5. Keluar akun')
        
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
                    tampilkan_histori(user)
                    kondisi2 = False
                elif pilihan == '4':
                    kondisi2 = False
                elif pilihan == '5':
                    kondisi2 = False
                    kondisi = False
                else:
                    print('\nMasukkan input yang benar!')
    
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
        
        kondisi2 = True
            
        while kondisi2:
                pilihan = input('\nGunakan menu nomor : ')
                
                if pilihan == '1':
                    profil(index)
                    kondisi2 = False
                elif pilihan == '2':
                    menu_belibarang()
                elif pilihan == '3':
                    tampilkan_riwayat_belanja()
                    kondisi2 = False
                elif pilihan == '4':
                    kondisi2 = False
                    kondisi = False
                else:
                    print('Masukkan input yang benar!')

def menu_belibarang():
    pilih = True

    while pilih:
        os.system('cls')
        print('╔' + '═'*48 + '╗')
        print('║' + 'Menu Beli Barang'.center(48) + '║')
        print('╚' + '═'*48 + '╝')
        
        print('\n1. Daftar Toko\n2. Keranjang Belanja\n3. Kembali')
        
        pilihan = input('\nGunakan menu nomor : ')
        
        if pilihan == '1':    
            daftar_toko()
            pilih = False
        elif pilihan == '2':
            tampilkan_keranjang()
            pilih = False
        elif pilihan == '3':
            pilih = False
        else:
            print('Masukkan input yang benar!')
            
#FITUR PROFIL        
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

#FITUR PENJUAL
def edit_barang_penjual(user):    
    sub_folder = os.path.join(folder_toko, f'toko_{user}')
    
    if not os.path.exists(sub_folder):
        os.makedirs(sub_folder)
    
    barang = os.path.join(sub_folder, f'toko_{user}.csv')
    histori = os.path.join(sub_folder, f'histori_{user}.csv')
    
    if not os.path.exists(barang):  
        user_df = pd.DataFrame(columns=['barang', 'harga', 'stok']) 
        user_df.to_csv(barang, index=False)
    if not os.path.exists(histori):  
        user_df = pd.DataFrame(columns=['barang', 'terjual']) 
        user_df.to_csv(histori, index=False) 
        
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

#FITUR EDIT BARANG
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
        
        try:
            hapus_item = int(input('Hapus item nomor : '))
            
            if 1 <= hapus_item <= len(baca):
                kondisi = False
            else:
                print('Masukkan nomor barang yang sudah ada di atas!')
        except:
            print('Masukkan input yang benar!')
    
    baca.drop(baca.index[hapus_item - 1], inplace=True)
    baca.to_csv(file_barang, index=False)
    
    print(f'\nBarang urutan {hapus_item} telah dihapus')

    i = input('\nTekan enter untuk kembali')
    
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
        try:
            index_ubah = int(input('Ubah item nomor : '))
            
            if 1 <= index_ubah <= len(baca):
                kondisi = False
            else:
                print('Masukkan nomor barang yang sudah ada di atas!')
        except:
            print('Masukkan input yang benar!')
    
    barang_dipilih = baca.iloc[index_ubah-1]
    print(f'\nBarang yang dipilih: {barang_dipilih['barang']} | harga saat ini = {barang_dipilih['harga']}\n')
    
    kondisi2 = True
    
    while kondisi2:
        try:
            harga_baru = int(input('Masukkan harga baru : '))
            
            kondisi2 = False
        except:
            print('Masukkan input berupa angka!')
            
    baca.at[index_ubah-1, 'harga'] = harga_baru
    baca.to_csv(file_barang, index=False)
    
    print(f'\nHarga barang {barang_dipilih['barang']} berhasil diubah menjadi {harga_baru}.')
    
    i = input('\nTekan enter untuk kembali')
    
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
        try:
            index_ubah = int(input('Ubah item nomor : '))
            
            if 1 <= index_ubah <= len(baca):

                kondisi = False
            else:
                print('Masukkan nomor barang yang sudah ada di atas!')
        except:
            print('Masukkan input yang benar!')
    
    barang_dipilih = baca.iloc[index_ubah-1]
    print(f'\nBarang yang dipilih: {barang_dipilih['barang']} | stok saat ini = {barang_dipilih['stok']}\n')
    
    kondisi2 = True
    
    while kondisi2:
        try:
            stok_baru = int(input('Masukkan stok baru : '))
            
            kondisi2 = False
        except:
            print('Masukkan input berupa angka!')
            
    baca.at[index_ubah-1, 'stok'] = stok_baru
    baca.to_csv(file_barang, index=False)
    
    print(f'\nStok barang {barang_dipilih['barang']} berhasil diubah menjadi {stok_baru}.')
    
    i = input('\nTekan enter untuk kembali')

def tampilkan_histori(user):
    sub_folder = os.path.join('data_toko', f'toko_{user}')
    histori_file = os.path.join(sub_folder, f'histori_{user}.csv')

    # Pastikan file histori ada
    if not os.path.exists(histori_file):
        print("File histori belum dibuat.")
        return

    # Baca file histori
    histori_df = pd.read_csv(histori_file)

    print('╔' + '═' * 50 + '╗')
    print('║' + 'Histori Penjualan'.center(50) + '║')
    print('╚' + '═' * 50 + '╝')

    if histori_df.empty:
        print("Tidak ada histori penjualan.")
        return

    # Tampilkan histori
    for index, row in histori_df.iterrows():
        print(f"{index + 1}. Barang: {row['barang']}, Terjual: {row['terjual']}")
    print()

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<BAGIAN PEMBELI>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
keranjang = []
riwayat_belanja = []

# Fungsi untuk menampilkan daftar toko
def daftar_toko():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('╔' + '═' * 48 + '╗')
    print('║' + 'Daftar Toko'.center(48) + '║')
    print('╚' + '═' * 48 + '╝')
    print()
    
    # Mendapatkan daftar toko dari folder
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

# Fungsi untuk menampilkan daftar barang dari toko yang dipilih
def daftar_barang(nama_toko):
    os.system('cls' if os.name == 'nt' else 'clear')
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
    
    # Membaca file CSV
    try:
        baca = pd.read_csv(file_barang)
        if baca.empty:
            print('Tidak ada barang dalam toko ini!')
            i = input('\nTekan enter untuk kembali')
            return
    except Exception as e:
        i = input('\nTekan enter untuk kembali')
        return
    
    # Menampilkan list barang
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
                    # Kurangi stok barang di CSV
                    baca.loc[baca.index == barang_dipilih.name, 'stok'] -= jumlah
                    baca.to_csv(file_barang, index=False)
                    
                    # Tambahkan ke keranjang
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
            return

def tampilkan_keranjang():
    os.system('cls' if os.name == 'nt' else 'clear')
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
        pilihan = input('\nApakah Anda ingin checkout? (y/n): ')
        if pilihan.lower() == 'y':
            checkout(total_harga)
            keadaan = False
        elif pilihan.lower() == 'n':
            hapus_keranjang_belanja()
            ubah_jumlah_barang()
            keadaan = False
        else:
            input('\nTekan enter untuk kembali')
            

# Fungsi untuk checkout barang dan cetak nota
def checkout(total_harga):
    os.system('cls' if os.name == 'nt' else 'clear')
    print('╔' + '═' * 48 + '╗')
    print('║' + 'Nota Belanja'.center(48) + '║')
    print('╚' + '═' * 48 + '╝')
    print()
    
    print(f'{"Barang":<20} {"Nama Toko":<15} {"Jumlah":<8} {"Harga Satuan":<12} {"Subtotal":<12}')
    print('-' * 78)

    # Validasi dan tampilkan barang di keranjang
    transaksi = []  # Menyimpan transaksi saat ini
    for item in keranjang:
        if not all(key in item for key in ['barang', 'harga', 'jumlah', 'toko']):
            continue

        subtotal = item['jumlah'] * item['harga']
        print(f'{item["barang"]:<20} {item["toko"]:<15} {item["jumlah"]:<8} Rp{item["harga"]:<12,} Rp{subtotal:<12}')
        
        # Tambahkan item ke transaksi saat ini
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

    # Simpan transaksi ke riwayat belanja
    riwayat_belanja.append({
        'total': total_harga,
        'item': transaksi
    })

    # Kosongkan keranjang
    keranjang.clear()
    input('\nTekan enter untuk kembali ke menu utama')

def tampilkan_riwayat_belanja():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('╔' + '═' * 48 + '╗')
    print('║' + 'Riwayat Belanja'.center(48) + '║')
    print('╚' + '═' * 48 + '╝')
    print()

    if not riwayat_belanja:
        print('Belum ada riwayat belanja.')
    else:
        for i, transaksi in enumerate(riwayat_belanja, start=1):
            print(f'Transaksi #{i}')
            print(f'{"Barang":<20} {"Nama Toko":<15} {"Jumlah":<8} {"Harga Satuan":<12} {"Subtotal":<12}')
            print('-' * 78)
            for item in transaksi['item']:
                print(f'{item["barang"]:<20} {item["toko"]:<15} {item["jumlah"]:<8} Rp{item["harga"]:<12,} Rp{item["subtotal"]:<12}')
            print('-' * 78)
            print(f'Total Belanja: Rp{transaksi["total"]:,}')
            print()

    input('\nTekan enter untuk kembali ke menu utama')

def hapus_keranjang_belanja():
    os.system('cls' if os.name == 'nt' else 'clear')
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
        pilihan = int(input('\nMasukkan nomor barang yang ingin dihapus (tekan enter untuk melanjutkan): '))
        if 1 <= pilihan <= len(keranjang):
            item_hapus = keranjang.pop(pilihan - 1)
            print(f'{item_hapus["barang"]} dari {item_hapus["toko"]} telah dihapus dari keranjang.')
        else:
            print('Pilihan tidak valid!')
    except ValueError:
        print('Apakah anda ingin mengubah jumlah barang?')

def ubah_jumlah_barang():    
    try:
        pilihan = int(input("\nMasukkan nomor barang yang ingin diubah (enter untuk kembali): "))
        if 1 <= pilihan <= len(keranjang):
            item = keranjang[pilihan - 1]
            file_barang = os.path.join(folder_toko, item['toko'], f'{item["toko"]}.csv')

            # Ambil stok maksimum dari file toko
            baca = pd.read_csv(file_barang)
            stok_tersedia = baca.loc[baca['barang'] == item['barang'], 'stok'].values[0] + item['jumlah']  # Tambahkan kembali stok lama
            
            print(f"Stok tersedia untuk {item['barang']}: {stok_tersedia}")
            jumlah_baru = int(input(f"Masukkan jumlah baru untuk {item['barang']}: "))
            if 0 < jumlah_baru <= stok_tersedia:
                # Update stok di file toko
                baca.loc[baca['barang'] == item['barang'], 'stok'] = stok_tersedia - jumlah_baru
                baca.to_csv(file_barang, index=False)
                # Update keranjang
                item['jumlah'] = jumlah_baru
                print(f"Jumlah {item['barang']} dari {item["toko"]} telah diperbarui menjadi {jumlah_baru}.")
            else:
                print("Jumlah yang dimasukkan tidak valid.")
        else:
            print("Pilihan tidak valid!")
    except ValueError:
        print("Masukkan nomor yang valid!")
    
    input('\nTekan enter untuk checkout')
    tampilkan_keranjang()
      
#PROGRAM UTAMA
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
    
main()
