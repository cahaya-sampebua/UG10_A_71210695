mendatar= "Mendatar"
menurun= "Menurun"
tanda1 = "#"
tanda2 = "*"
kata = str(input('Mendatar/Menurun?: '))

if  kata =="Mendatar":
    baris = int(input('Masukkan baris: '))
    print (tanda1 * baris )
       
elif kata =="Menurun":
    kolom = int(input('Masukkan kolom: '))
    lst= '\n'.join(tanda2 * kolom)
    print (lst)
        
else:
    print("Pola tidak dikenali")
