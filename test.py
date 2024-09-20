#in ra va fix
import time
#1
def tong(n):
    s = 0
    tong = 0
    while n != 0:
        du = n % 10
        tong = tong + du
        n = n // 10
    print(tong)
#tong(1234)
#2
def LT(a,n):
    p = 1
    for i in range(n):
        p = p * a
    print(p)
#LT(2,8)
#3
def dao_so(n):
    kq = 0
    while n != 0:
        so_du = n % 10
        kq = kq * 10 + so_du 
        n = n // 10
    print(kq)
#dao_so(987)
#4
import math 
def sohoanhao(n):
    sum = 1
    if n < 6:
        return False
    for i in range(2,(n)+1):
        if n % i == 0:
            sum = sum + i 
            if i != n // i:
                sum = sum + n//i
    print(sum == n) 
#sohoanhao(12)
#5
def sobb(a,b):
    soa = 0
    sob = 0
    for i in range(2, a//2+1):
        if a%i == 0: 
            soa += i 
    for i in range(2, b//2+1):
        if b % i == 0:
            sob += i    
    if a == sob or b == soa:
        print('a va b la 2 so ban be')
    else:
        return False  
#sobb(12,15)
#6
def thuasonguyento(n):
    i = 2
    while n != 1:
        while n % i == 0:
            print(i, end=',')
            n = n/i 
        i+=1
#thuasonguyento(20)
#kiểm tra số nguyên tố
def snt(n):
    if n<2:
        return False 
    for i in range(2, int(math.sqrt(n))):
        if n % i == 0:
            return False
    return True
#n = int(input('nhap n'))
#for i in range(1,n):
    if snt(i) == True:
        print(i, end='')
#thuật toán sàng số nguyên tố
#import math đã làm trước đó
global m
m = 100000001
global prim
prim = [1]*m 
def snt1():
    n = int(input('nhap n:'))
    prim[0] = 0
    prim[1] = 0
    for i in range(2, int(math.sqrt(m))):
        if prim[i] == 1:
            for j in range(i*i, m, i):
                prim[j] = 0
    for z in range(1,n):
        if prim[z] == 1:
            print(z, end='')
#snt1()
#sàng số nguyên tố trên đoạn L,R:
#import math
def snt_L_R(L,R):
    for i in range(2, int(math.sqrt(R))):
        for j in range (max(i*i, (L+i-1)//i*i), R+1, i):
            print(j-L) == 0
def ctc():
    L = 10
    R = 50
    prim = 1*(R-L+1)
    snt_L_R(L,R)
    print(prim)
    for i in range(max(L,2), R+1):
        if prim(i-L) != 1:
            print(i, end ='')
#ctc()
#Tìm số nguyên tố nhỏ nhất của các số trong dãy số nguyên
#import math
def uocnguyentonhonhat(n):
    global j
    prim = [0] * 10000
    for i in range(1, n+1):
        prim[i] = i
    for i in range(1,int(math.sqrt(n+1))):
        if prim[i]==i:
            for j in range(i*i, n+1, i):
                if prim[j] == j:
                    prim[j] = i
def chuongtrinhchinh():
    n = 20
    uocnguyentonhonhat(n)
    print(prim)
    for i in range (1,n+1):
        print(i, ':', prim[j])
#chuongtrinhchinh()
#Tìm số nguyên tố n gần nhất
def prim(n):
    if n <= 1:
        return False
    for i in range (2, (int(n**0.5)+1)):
        if n % i == 0:
            return False
    return True
def find_closest_prim(n):
    if prim(n):
        return n
    closest_prim = n - 1
    while True:
        if prim(closest_prim):
            return closest_prim
        closest_prim -= 1
def chuong_trinh_chinh_cua_prim_n():
    n = int(input('Nhap n'))
    print(find_closest_prim(n))
#chuong_trinh_chinh_cua_prim_n()
def read_files_example():
    f = open('doc.inp', 'r')
    o = open('doc.out', 'w')
    a,b = map(int, f.readline().split())
    print(a+b, f=o)
    f.close
    o.close
#sàng số nguyên tố n<=10**6
#thuật toán sàng số nguyên tố
#import math
fi = open('timso.inp', 'r')
fo = open('timso.out', 'w')
m = 10**6
b=[]
#sàng số nguyên tố
prim=[1]*(m+1)
prim[0] = prim[1] = 0
for i in range(2, int(math.sqrt(m))+1):
    if prim[i] == 1:
       for j in range(i*i, m, i):
            prim[j]=0
#đưa các số đã sàng qua danh sách b
def mo_file():
    for i in range(m):
        if prim[i] == 1:
                b.append(i)
    for x in fi:
        print(b[int(x)-1], file=fo)
    fi.close()
    fo.close()
def uoc_chung_lon_nhat(a,b):
    while b!= 0:
        r = a%b
        a = b
        b = r
    return a
def BCNN(a,b):
    ket_qua = uoc_chung_lon_nhat(a,b)
    return a*b//ket_qua
def input_cho_BCNN_va_UCLN():
    a = int(input('Nhập a'))
    b = int(input('Nhập b'))
    print(uoc_chung_lon_nhat(a,b))
    print(BCNN(a,b))
#input_cho_BCNN_va_UCLN()
#Mảng
#2
def bt2():
    chan = 0
    le = 0
    fi = open('timso.inp', 'r')
    a = fi.readline
    for i in range(len(a)):
        if len(a) % 2 == 0:
            if a[i] % 2 == 0:
                chan = chan + 1
        else: 
            if a[i] % 2 !=0:
                le = le + 1
    if chan>le and len(a)%2 == 0 or le>chan and len(a)%2 != 0:
        print('Dãy a là dãy ưu thế')
    else:
        print('Dãy a không phải là dãy ưu thế')
#bt2()
#bt3
def bt3():
    file_input = open('input_camera.inp', 'r')
    file_output = open('output_camera.out', 'w')
    a = [2,2,2,2,3,4,5,5,5,5,8,8,8,8]
    a.sort()
    t = 0
    for i in range(len(a)):
        if a[i] != a[i-1]: #chạy từ đầu lên, nên để i-1 để tránh số trước giống số đang chạy
            t = t + 1
    print('số loại xe khác nhau là', t)
#bt3()
def bt4():
    fi = open('timso.inp', 'r') 
    file_output = open('timso.out', 'w')
    w = int(fi.readline())
    i = 0
    s = 0
    a = list(map(int, fi.readline().split()))
    a.sort()
    for i in range(len(a)):
        i = i + a[i]
        s = s + 1
        if i>w:
            break
    print(s, file = file_output)
#bt4()
#bt5
#def bt5():
    file_input = open('noiday.inp', 'r')
    file_output = open('noiday.out', 'w')
    so = (file_input.readline())
    a = list(map(int, file_input.read().split()))
    a.sort()
    summ = 0
    sum2 = 0
    i = 1
    while i in range(len(a)):
        i = i + a[i]  
        sum2 = i+sum2  
        i = i + 1  
    print(sum2, file=file_output)
#bt5()
#bt6
#def bt6():
    fi = open('MILK.inp', 'r')
    fo = open('MILK.out', 'w')
  
    so_lit_moi_con = list(map(int, fi.read().split()))
    so_lit_moi_con.sort(reverse=True) 
    for i in range(len(so_lit_moi_con)):
        print( file=fo)
#bt6()
def bt10():
    fi = open('CHIADAY.inp', 'r')
    fo = open('CHIADAY.out', 'w')
    n=int(fi.readline())
    a = list(map(int, fi.readline().split()))
    a.sort(reverse=True)
    B = []
    for i in range(n//2+1):
        B = B + [a[i]]
        del(a[i])
    s = sum(B)
    a = sum(a)
    print(s-a, file=fo)
#bt10()    
def bt_them():
    fi = open('input.inp', 'r')
    fo = open('output.out', 'w')
    n = int(fi.readline())
    s = list(map(int, fi.readline().split()))
    k = int(fi.readline())
    s.sort()
    abc=[]
    xyz= []
    for i in range(len(s)):
        abc = abc+[s[i]]
        xyz = sum(abc)
        if xyz == k:
            break
    print(abc, file=fo)
    fi.close()
    fo.close()
#bt_them()
#bthem fix o nha

    
    
        
        

    
        

