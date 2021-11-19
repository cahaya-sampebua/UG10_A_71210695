kalimat = input("Masukkan artikel yang ingin dipindai: ").split()
klub = input ("Masukkan nama klub favorit anda: ")
skor = input ("Masukkan skor yang ingin dicari: ")
list = []
ditemukan = 0
for i in kalimat:
    
    if i in klub:
        list.append(i)
        ditemukan += 1
    elif i in skor:
        list.append(i)
        ditemukan += 1
        print("Hasil pencarian ditemukan")
    else:
        print("Hasil pencarian",klub, "dan", skor,"tidak ditemukan")
        

