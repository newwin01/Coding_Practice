count=int(input())
word_arr=[]
for i in range(count):
    word_arr.append(input())
word_arr=set(word_arr)
word_arr=list(word_arr)
word_arr.sort()
word_arr.sort(key=len)

for i in word_arr:
    print(i)