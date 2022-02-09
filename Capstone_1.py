# ========== Data Pasien Rumah Sakit ===========

# List Data Pasien
# 5 kolom : No.Pasien, Nama Depan, Nama Belakang, Gender, Tahun Lahir
# No.Pasien diambil dari detail pasien dengan menambahkan nomor urut didepannya
# Contoh : 00 + 1980 + Inisial nama depan + Inisial nama belakang = 011980BS --> Ben Stone 
# Akan banyak menggunakan try, except, else (check suatu blok kode dan mengatasi errornya)


listPasien = [
              ['001980BS','Ben','Stone','Male',1980],
              ['011985JV','Jared','Smith','Male',1985],
              ['021981GK','Grace','Kelly','Female',1981],
              ['032000OG','Olive','Green','Female',2000],
             ] 


# Function cari index dari sublist di dalam list dengan input no. pasien
def findIndex(noPas):
    for i in range(len(listPasien)):
        try:
            j = listPasien[i].index(noPas)
            return i
        except:
            pass    

# Function kembali ke Menu Utama
def back_menu_utama(function):
    back = input('\nKembali ke Menu Utama? [Y/N]: ').upper()

    if back == 'Y':
        menu_utama()
                    
    elif back == 'N':
        function()
            
    else:
        print('\n**Input yang anda masukkan salah!**\n')
        function()

# Function Menu Utama 
def menu_utama():
    
    print(f'''
====== Data Base Pasien Rumah Sakit Purwadhika ======\n
Menu Utama:
1. List Data Pasien
2. Menambahkan Data Pasien
3. Mengubah Data Pasien
4. Menghapus Data Pasien
5. Exit
    ''')

    pilihan_menu = input('Silahkan Pilih Menu [1-5]: ')

    if pilihan_menu == '1':
        read_data()
        
    elif pilihan_menu == '2':
        create_data()
        
    elif pilihan_menu == '3':
        update_data()
        
    elif pilihan_menu == '4':
        delete_data()
        
    elif pilihan_menu == '5':
        yakin = input('Yakin ingin keluar? [Y/N]: ').upper()
        if yakin == 'Y':
            print('\n== Terima Kasih ==\n')
            quit()
        elif yakin == 'N':
            menu_utama()
        else:
            print('\n**Input yang anda masukkan salah!**')
            menu_utama()        
            
    else:
        print('\n**Input yang anda masukkan salah!**\n')
        menu_utama()        



# Function Read Data
def read_data():

    while True:

        # Print list menu read
        print('''
====== List Data Pasien ======\n
1. List Seluruh Data
2. Report Data Tertentu
3. Kembali ke Menu Utama''')

        sub_read_input = input('\nSilahkan Pilih Sub Menu Read Data [1-3]: ')

        # Jika input 1, maka akan print semua data
        if sub_read_input == '1':
            if len(listPasien) == 0:    # Menghitung isi list, jika = 0 maka tidak ada data
                print('\n***** Tidak ada data pasien di database *****\n')
                
            else:     # Jika ada data menmpilkan semua isi list
                print('====== List Seluruh Data Pasien ======\n')
                print('No. Pasien \t| Nama Depan\t| Nama Belakang\t| Gender  \t| Tahun Lahir')

                for i in range(len(listPasien)):
                    print(f'{listPasien[i][0]}\t| {listPasien[i][1]}\t\t| {listPasien[i][2]}\t\t| {listPasien[i][3]}  \t| {listPasien[i][4]}')

        # Jika input 2, maka akan print hanya data yang dipilih saja   
        elif sub_read_input == '2':
            noPasien = input('\nMasukkan No. Pasien: ').upper()
            print(f'\nData Pasien dengan Nomor: {noPasien}\n')

            try:    # mencoba mencari no pasien di dalam list pasien
                x = findIndex(noPasien)   
                print(f'No. Pasien : {listPasien[x][0]} | Nama Depan: {listPasien[x][1]} | Nama Belakang: {listPasien[x][2]} | Gender: {listPasien[x][3]} | Tahun Lahir: {listPasien[x][4]}')

            except:   # kalau tidak ada / error
                print(f'\n==== {noPasien} tidak ada di list Data Pasien ====')

            else:
                read_data()

            finally:
                read_data()

        # Jika input 3, maka akan kembali ke menu utama atau kembali ke menu read
        elif sub_read_input == '3':
            back_menu_utama(read_data)
            pass

        # Jika memasukkan input lain akan kembali ke menu read
        else:
            print('\n**Input yang anda masukkan salah!**\n')
            pass


# Function Create Data
def create_data():

    while True:

        # Print menu create data
        print('''
====== Menambah Data Pasien ======\n
1. Tambah Data Pasien
2. Kembali ke Menu Utama''')

        sub_create_input = input('\nSilahkan Pilih Sub Menu Create Data [1-2]: ')

        # Jika input 1, maka akan mencari dan menambah data
        if sub_create_input == '1':
            noPasien = input('\nMasukkan No. Pasien: ').upper()

            try:    # Ketika ditemukan indexnya akan mengembalikan print
                findIndex(noPasien) >= 0

                print(f'\n *** Pasien dengan nomor {noPasien} sudah ada ***')

            except:   # Ketika tidak ada index, maka akan diberikan input dibawah
                print('\nNomor Pasien Belum Ada, Masukkan Detail Pasien Dibawah:\n')
                nama_depan = input('Masukkan Nama Depan: ').capitalize()
                nama_belakang = input('Masukkan Nama Belakang: ').capitalize()
                gender = input('Masukkan Gender [Male/Female]: ').capitalize()
                tahun_lahir = int(input('Masukkan Tahun Lahir: '))
                noPas = '0' + str(len(listPasien)) + str(tahun_lahir) + nama_depan[0].upper() + nama_belakang[0].upper()

                while True: # Untuk mengkonfirmasi apakah benar data ingin disimpan
                    confirm = input(f'Simpan data? [Y/N]: ').upper()

                    if confirm == 'Y':
                        listPasien.append([noPas,nama_depan,nama_belakang,gender,tahun_lahir])
                        print('\n== Data Telah Tersimpan ==')
                        break
                        
                    elif confirm == 'N':
                        create_data()
                    
                    else:   
                        confirm
                                               
        # Jika input 2, maka akan kembali ke menu utama
        elif sub_create_input == '2':
            back_menu_utama(create_data)
            pass

        # Jika memasukkan input lain akan kembali ke menu read
        else:
            print('\n**Input yang anda masukkan salah!**\n')
            pass


# Function Update Data:
def update_data():
    
    while True:
      
        # Print menu update data
        print('''
====== Mengubah Data Pasien ======\n
1. Ubah Data Pasien
2. Kembali ke Menu Utama''')

        sub_update_input = input('\nSilahkan Pilih Sub Menu Ubah Data [1-2]: ')

        # Jika input 1, maka akan mencari no pasien dan tanya update data
        if sub_update_input == '1':
            noPasien = input('\nMasukkan No. Pasien: ').upper()

            # Function untuk mengubah data dilist dengan input judul kolom
            def ubah(kolom):
                edit = input(f'Masukkan {kolom} baru: ').title()
                list_kolom = ['No. Pasien','Nama Depan','Nama Belakang','Gender','Tahun Lahir']

                # Untuk mengkonfirmasi apakah benar data ingin disimpan
                confirm = input(f'\nUbah data? [Y/N]: ').upper()

                if confirm == 'Y':
                    listPasien[x][list_kolom.index(kolom)] = edit
                    print('\nPerubahan Data Telah Tersimpan\n')
                                            
                elif confirm == 'N':
                    update_data()
                    
                else:
                    print('\n**Input yang anda masukkan salah!**\n')
                    update_data()                


            try:    # Ketika ditemukan indexnya akan mengembalikan tanya update
                x = findIndex(noPasien)
                print(f'No. Pasien : {listPasien[x][0]} | Nama Depan: {listPasien[x][1]} | Nama Belakang: {listPasien[x][2]} | Gender: {listPasien[x][3]} | Tahun Lahir: {listPasien[x][4]}')

                update_input = input('\nLanjut mengubah data? [Y/N]: ').upper()

                if update_input == 'Y':
                    kolom_input = input('Masukkan kolom yang ingin diubah (Kecuali No. Pasien): ').title()
                    ubah(kolom_input) # fungsi ubah
                                        
                elif update_input == 'N':
                    update_data()
                    
                else:
                    print('\n**Input yang anda masukkan salah!**\n')
                    pass                        

            except:   # jika no pasien tidak ditemukan dalam list pasien
                print(f'\n**** {noPasien} tidak ada di list Data Pasien ****')
                update_data()
            
            else:
                update_data()
                
        # Jika input 2, maka akan kembali ke menu utama            
        elif sub_update_input == '2':
            back_menu_utama(update_data)
            pass

        # Jika memasukkan input lain akan kembali ke menu read
        else:
            print('\n**Input yang anda masukkan salah!**\n')
            pass
    
# Function Delete Data:
def delete_data():
    
    while True:
      
        # Print menu delete data
        print('''
====== Menghapus Data Pasien ======\n
1. Hapus Data Pasien
2. Kembali ke Menu Utama''')

        sub_delete_input = input('\nSilahkan Pilih Sub Menu Ubah Data [1-2]: ')

        # Jika 1, maka tanya no pasien yang akan dihapus datanya
        if sub_delete_input == '1':
            noPasien = input('\nMasukkan No. Pasien: ').upper()

            try:    # Ketika ditemukan indexnya akan mengembalikan tanya delete
                x = findIndex(noPasien)
                print(f'No. Pasien : {listPasien[x][0]} | Nama Depan: {listPasien[x][1]} | Nama Belakang: {listPasien[x][2]} | Gender: {listPasien[x][3]} | Tahun Lahir: {listPasien[x][4]}')

                delete_input = input('\nLanjut hapus data? [Y/N]: ').upper()  

                if delete_input == 'Y':
                    del listPasien[x]
                    print('\n** Data berhasil dihapus **')
                    
                elif delete_input == 'N':
                    delete_data()
                    
                else:
                    print('\n**Input yang anda masukkan salah!**\n')
                    pass                        

            except:   # jika no pasien tidak ditemukan dalam list pasien
                print(f'\n**** {noPasien} tidak ada di list Data Pasien ****')
                delete_data()                
        
        # Jika input 2, maka akan kembali ke menu utama            
        elif sub_delete_input == '2':
            back_menu_utama(delete_data)
            pass

        # Jika memasukkan input lain akan kembali ke menu read
        else:
            print('\n**Input yang anda masukkan salah!**\n')
            pass        
    
menu_utama()
