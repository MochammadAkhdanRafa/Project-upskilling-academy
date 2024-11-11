import csv
import os

nama_file = r'12.data_karyawan.csv'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def init_csv():
    if not os.path.exists(nama_file):
        with open(nama_file, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['ID', 'Nama', 'Jabatan', 'Gaji'])

def tambah_karyawan(id, name, jabatan, gaji):
    with open(nama_file, mode='a', newline='') as file:  
        writer = csv.writer(file)
        writer.writerow([id, name, jabatan, gaji])
    print("Data Berhasil Ditambahkan")

def hapus_karyawan(id):
    rows = []
    with open(nama_file, mode='r', newline='') as file:
        reader = csv.reader(file)
        rows = list(reader)

    found = False
    with open(nama_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(rows[0])
        for row in rows[1:]:
            if row[0] != id:
                writer.writerow(row)
            else:
                found = True

    if found:
        print(f'Data dengan ID {id} Berhasil Dihapus')
    else:
        print(f'Data dengan ID {id} Tidak Ditemukan')

def update(id, nama=None, jabatan=None, gaji=None):
    rows = []
    updated = False
    with open(nama_file, mode='r', newline='') as file:
        reader = csv.reader(file)
        rows = list(reader)

    with open(nama_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(rows[0])
        for row in rows[1:]:
            if row[0] == id:
                if nama is not None:
                    row[1] = nama
                if jabatan is not None:
                    row[2] = jabatan
                if gaji is not None:
                    row[3] = gaji
                updated = True
            writer.writerow(row)

    if updated:
        print(f'Data dengan ID {id} Berhasil Diperbarui')
    else:
        print(f'Data dengan ID {id} Tidak Dapat Diperbarui')

def tampilkan_data():
    with open(nama_file, mode='r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            print(f'ID: {row[0]}, Nama: {row[1]}, Jabatan: {row[2]}, Gaji: {row[3]}')

def tampilkan_data_id(id):
    show_id = False
    with open(nama_file, mode='r', newline='') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            if row[0] == id:
                print(f'ID: {row[0]}, Nama: {row[1]}, Jabatan: {row[2]}, Gaji: {row[3]}')
                found = True
                break
    if not show_id:
        print(f'Tidak Dapat Menemukan Data dengan ID {id}')

def menu():
    while True:
        clear_screen()
        print('\nPilihan')
        print('1. Menambahkan Karyawan')
        print('2. Menghapus Karyawan')
        print('3. Update Karyawan')
        print('4. Tampilkan Karyawan')
        print('5. Tampilkan Karyawan Berdasarkan ID')
        print('6. Keluar')

        input_user = int(input('Masukan Pilihan: '))
        if input_user == 1:
            id = input('Masukan ID: ')
            nama = input('Masukan Nama Karyawan: ')
            jabatan = input('Masukan Jabatan: ')
            gaji = input('Masukan Gaji: ')
            tambah_karyawan(id, nama, jabatan, gaji)
        elif input_user == 2:
            id = input('Masukan ID Karyawan Yang Ingin Dihapus: ')
            hapus_karyawan(id)
        elif input_user == 3:
            id = input('Masukan ID Karyawan Yang Ingin Diperbarui: ')
            nama = input('Masukan Nama Baru (kosongkan jika tidak diubah): ')
            jabatan = input('Masukan Jabatan Baru (kosongkan jika tidak diubah): ')
            gaji = input('Masukan Gaji Baru (kosongkan jika tidak diubah): ')
            update(id, nama if nama else None, jabatan if jabatan else None, gaji if gaji else None)
        elif input_user == 4:
            tampilkan_data()
        elif input_user == 5:
            id = input('Masukan ID Karyawan Yang Ingin Anda Cari: ')
            tampilkan_data_id(id)
        elif input_user == 6:
            print('Keluar dari program.')
            break
        else:
            print('Perintah Tidak Valid')
        input('\nTekan Enter untuk melanjutkan...')

if __name__ == "__main__":
    init_csv()
    while True:
        menu()
        kondisi = input("\nApakah kamu ingin menjalankan program lagi? (y/n): ")
        if kondisi.lower() == 'n':
            break
