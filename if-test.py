money = False
if money:
    print('택시를 타고 가라')
else:
    print('걸어 가라')

if 1 in [1,2,3]:
    print('yes')
else:
    print('no')


pocket=['paper','cellphone','money']
if 'money' in pocket:
    print("택시")
else:
    print("걷기")

pocket=['paper','cellphone','money']
if 'money' in pocket:
    pass
else:
    print("걷기")
card=True
if 'money' in pocket:
    print("택시")
elif card:
    print("택시")
else:
    print("걷기")

#score = int(input('점수를 입력하세요\n'))
#message='success' if score>=60 else 'failure'
#print(message)

#number = input("주민번호를 넣어 주세요\n :")

#if number[7]=='1' or number[7]=='3':
#   message = "Man"
#    print(message)
#elif number[7]=='2' or number[7]=='4':
#    print("woman")
#    message = "Woman"
