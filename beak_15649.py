N,M = map(int,input().split())
Seq = [] 

def Seq_f():
    if len(Seq) == M:
        print(' '.join(map(str,Seq)))
        return
    
    for i in range(1,N+1):
        if i in Seq:
            continue
        Seq.append(i)
        Seq_f()
        Seq.pop()
        
Seq_f() 