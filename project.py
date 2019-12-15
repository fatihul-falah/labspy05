daftar = {}
while True:
    print("")
    c = input("A)dd, E)dit, D)elete, S)earch, L)ist, Q)uit: ")
    if c.lower() == 'a':
        print("Add Data Nilai Siswa")
        nama = input("Nama: ")
        nim = input("NIM: ")
        tugas = float(input("Tugas: "))
        uts = float(input("Uts: "))
        uas = float(input("Uas: "))
        nilai = float(tugas)*30/100 + (uts)*35/100 + (uas)*35/100
        daftar[nim] = nama, tugas, uts, uas, nilai
    elif c.lower() == 'e':
        print("Edit Data Siswa")
        nim = input("NIM: ")
        if nim in daftar.keys():
            nama = input("Nama Baru: ")
            tugas = float(input("Tugas baru: "))
            uts = float(input("Uts baru: "))
            uas = float(input("Uas: "))
            nilai = float(tugas) *30/100 + (uts)*35/100 + (uas)*35/100
            daftar[nim] = nama, tugas, uts, uas, nilai
        else:
            print("nim {0} tidak ada".format(nim))
    elif c.lower() == 'd':
        print("Delete Data Siswa")
        nim = input("NIM: ")
        if nim in daftar.keys():
            del daftar[nim]
        else:
            print("Siswa Dengan NIM {0} tidak ada".format(nim))
    elif c.lower() == 's':
        print("Search Siswa")
        nim = input("NIM: ")
        if nim in daftar.keys():
            print("|Nim         | Nama          | Nilai Tugas | Nilai Uts | Nilai Uas | Nilai Akhir |")
            print("| {0:10s} | {1:13s} | {2:11.2f} | {3:9.2f} | {4:9.2f} | {5:11.2f} |"\
                    .format(nim, nama, tugas, uts, uas, nilai))
        else:
            print("Siswa Dengan NIM : {0} tidak ada".format(nim))
    elif c.lower() == 'l':
        print("Daftar Data Nilai Siswa")
        print("|Nim         | Nama          | Nilai Tugas | Nilai Uts | Nilai Uas | Nilai Akhir |")
        print("==================================================================================")
        i = 0
        for x in daftar.items():
            i +=1
            print("| {0:10s} | {1:13s} | {2:11.2f} | {3:9.2f} | {4:9.2f} | {5:11.2f} |"
                      .format(x[0][:13], x[1][0], x[1][1], x[1][2], x[1][3], x[1][4], no=i))
            print("==============================================================================")
    elif c.lower() == 'q':
        break
    else:
        print("Pilih menu yang tersedia")

print("=============================")
print("       SAMPAIJUMPA      ")
print("=============================")
