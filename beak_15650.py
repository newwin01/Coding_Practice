N,M = map(int,input().split())
Seq = [] 

def Seq_f(start):
    if len(Seq) == M:
        print(' '.join(map(str,Seq)))
        return
    
    for i in range(start,N+1):
        if i not in Seq:
            Seq.append(i)
            Seq_f(i+1)
            Seq.pop()

Seq_f(1)