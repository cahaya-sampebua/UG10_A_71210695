print("###########################")
print("Kalkulator Advance Sederhana")
print("############################")
print("1. Menghitung sisa hasil bagi")
print("2. Membulatkan ke bawah hasil pembagian")
print("3. Mencari akar kubik sebuah bilangan")

operation = int(input("Masukkan menu yang anda pilih: "))

if operation ==1:
    num1 = float(input ("Masukkan bilangan yang ingin anda bagi "))
    num2 = float(input ("Masukkan bilangan pembagian "))
    hasil = num1 % num2
    print("Sisa hasil bagi",num1,"dibagi dengan",num2,"adalah",hasil)
elif operation ==2:
    num1 = float (input ("Masukkan bilangan yang ingin dibagi: "))
    num2 = float(input ("Masukkan bilangan pembagi: "))
    hasil = num1 // num2
    print("Hasil pembagi",num1,"dibulatkan kebawah",num2,"adalah",hasil)
elif operation ==3:
    num1 = float(input ("Masukkan bilangan yang ingin dicari akar kubiknya: "))
    hasil = round(num1**(1/3))
    print("Akar kubik dari ",num1,"adalah ",hasil)
else:
    print("Menu yang anda pilih tidak tersedia")
