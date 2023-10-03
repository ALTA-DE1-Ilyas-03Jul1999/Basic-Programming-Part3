# input
nama_siswa = input('Nama: ')

nilai_str = input('Nilai: ')
nilai_int = int(nilai_str)
# Process: Your Solution Code Here
if 80 < nilai_int < 100:
    print("Selamat",nama_siswa,",kamu dapat A!")

elif 65 < nilai_int < 79:
    print('Selamat',nama_siswa,',kamu dapat B+!')

elif 50 < nilai_int < 64:
    print('Selamat',nama_siswa,',kamu dapat B!')

elif 35 < nilai_int < 49:
    print('Selamat',nama_siswa,', kamu dapat nilai C!')

elif 0 < nilai_int < 34:
    print('Selamat',nama_siswa,',kamu dapat D!')
else:
    print('Masukan nilai dengan benar')

# Output "Nilai A"