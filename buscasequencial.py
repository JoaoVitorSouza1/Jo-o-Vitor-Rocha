def buscaSeq(x, proc):
    

    for i in range(0,len(x)):
        if x[i] == proc:
        
            return i
    return -1

x = [2, 1, 4, 5, 7, 9, 10, 8, 3]
i = 10
k = buscaSeq(x, i)
if k >= 0:
    print(i, 'Esta na posição',k,'do vetor')
else:
    print(i,'não se encontra no vetor')