test=int(input());
for i in range(test):
    number,string = input().split();
    number = int(number);
    for i in range(len(string)):
        print(string[i]*number,end='');
    print();