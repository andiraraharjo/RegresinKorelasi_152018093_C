#Nama : Andira Raharjo (152018093)
import random
def interval(inprobkum):
    top = []
    bottom = []
    bottom.append(0)
    for j in range((len(inprobkum))-1):
        n = inprobkum[j] + 0.001
        bottom.append(n)
    for j in range((len(inprobkum))):
        n = inprobkum[j]
        top.append(n)
    return bottom, top

def probabilitas():
    ftot = 0
    out = []
    for j in range(len(datainput)):
        ftot += datainput[j][1]
    for j in range(len(datainput)):
        n = datainput[j][1] / ftot
        out.append(n)
    return out


def probkumulatif(inprob):
    out = []
    out.append(inprob[0])
    panjang = len(inprob) - 1
    for j in range(panjang):
        n = out[j] + inprob[j+1]
        out.append(round(n,1))
    return out


def predict(banyaknya, bottom, top, harga):
    total1 = 0
    total2 = 0
    data = []
    out = []
    for j in range(banyaknya):
        data.append(random.random())
    for j in range(banyaknya):
        if (data[j] >= bottom[0]) and (data[j] <= top[0]):
            n=0
        elif (data[j] >= bottom[1]) and (data[j] <= top[1]):
            n=1
        elif (data[j] >= bottom[2]) and (data[j] <= top[2]):
            n=2
        elif (data[j] >= bottom[3]) and (data[j] <= top[3]):
            n=3
        elif (data[j] >= bottom[4]) and (data[j] <= top[4]):
            n=4
        elif (data[j] >= bottom[5]) and (data[j] <= top[5]):
            n=5
        elif (data[j] >= bottom[6]) and (data[j] <= top[6]):
            n=6
        elif (data[j] >= bottom[7]) and (data[j] <= top[7]):
            n=7
        out.append(n)
    data = []
    for j in  range(len(out)):
        total1 += out[j]
        n = out[j] * harga
        total2 += n
    print('Prediksi Permintaan = ', total1, 'pcs')
    print('Prediksi Pengeluaran = Rp.',total2)

def inputdata():
    while True:
        ent1 = input('Permintaan = ')
        ent2 = input('minggu : ')
        if (ent1 == '') and (ent2 == ''):
                break
        try:
            datainput.append((int(ent1),int(ent2)))
        except:
            print("Masukkan yang anda input tidak valid")


datainput = []
inputdata()
alpha = probabilitas()
beta = probkumulatif(alpha)
bo, ab = interval(beta)[:2]
npredict = int(input('Masukkan prediksi: '))
price = int(input('Tentukan modal : '))
predict(npredict, bo, ab, price)
