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
bt4()