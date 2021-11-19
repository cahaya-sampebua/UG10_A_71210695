# SOAL 1
n = float(input("Masukkan nilai rata-rata UG anda: "))
n_1 = float(input("Masukkan nilai TTS anda: "))
n_2 = float(input("Masukkan nilai Tas anda:"))
print ("========================")

n_a = ((n*0.7)+(n_1*0.15)+(n_2*0.15))
print ("nilai anda: ",n_a)

if(n_a>=85):
    print("Nilai huruf anda: A")
elif(n_a>=80):
    print("Nilai huruf anda: A-")
elif(n_a>=75):
    print("Nilai huruf anda: B+")
elif(n_a>=70):
    print("Nilai huruf anda: B")
elif(n_a>=65):
    print("Nilai huruf anda: B-")
elif(n_a>=60):
    print("Nilai huruf anda: C+")
elif(n_a>=55):
    print("Nilai huruf anda: C")
elif(n_a>=45):
    print("Nilai huruf anda: D")
elif(n_a>=0):
    print("Nilai huruf anda: E")
