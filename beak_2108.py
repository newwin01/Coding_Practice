import sys
from collections import Counter

number_count=int(sys.stdin.readline())
number_arr=[];
for i in range (number_count):
    number_arr.append(int(sys.stdin.readline()))


number_arr.sort()
frequent_letter = Counter(number_arr).most_common()
    
print(round(sum(number_arr)/number_count))    
print(number_arr[number_count//2])
if(len(frequent_letter)>1):
    if frequent_letter[0][1] == frequent_letter[1][1]:
        print(frequent_letter[1][0])
    else:
        print(frequent_letter[0][0])
else:
    print(frequent_letter[0][0])
    
    
print(max(number_arr)-min(number_arr))