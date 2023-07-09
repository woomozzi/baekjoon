TC = int(input())
OX_list = []
for i in range(TC) :
    OX = input()
    OX_list = list(OX)
    OX_total = 0
    OX_sum = 0 
    for j in OX_list :
        if j == "O" :
            OX_total += 1
            OX_sum += OX_total
        else :
            OX_total = 0
    print(OX_sum)