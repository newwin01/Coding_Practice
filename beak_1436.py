n = int(input())
count = 0
the_number = 666

while True:
    if '666' in str(the_number):
        count+=1
    if count == n:
        print(the_number)
        break
    the_number+=1