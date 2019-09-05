test_list = ['one', 'two', 'three'] 
print("List를 for문으로 출력")
for i in test_list: 
    print(i)

print("List안에 tuple 형태도 for문으로 출력")
a = [(1,2), (3,4), (5,6)]
for (first, last) in a:
    print(first + last)

coffee={'아메리카노':2500,'카페라떼':3000,'카푸치노':3500}
print(coffee)
coffee.keys()
for i in coffee.items():
    print(i)

add=0
for i in range(1,11):
    add=add+i
print("1부터 10까지 합 =",add)

evennumbersum=0
for i in range(1,101):
    if i%2 == 0:
        evennumbersum=evennumbersum+i
print("1부터 100까지 짝수의 합 {}".format(evennumbersum))

for i in range(2,10):
    print("="*3,i,"단","="*3)
    for j in range(1, 10):
        print(i*j, end=" ") 
    print('')

for i in range(2,10):
    print("="*3,i,"단","="*3)
    for j in range(1, 10):
        #print(i*j, end=" ")
        print("{} X {}= {}".format(i,j,i*j))
    print('')

for j in range(1,10):
    for i in range(2, 10):

        print("{} X {}= {:2}".format(i,j,i*j),end='  ')
    print('')

print()
a=[1,2,3,4]
result=[num*3 for num in a]
print(result)

a=[1,2,3,4]
result=[num*3 for num in a if num%2==0]
print(result)