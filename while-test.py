#1.커피메뉴등록
#2.커피가격
#3.종료

#enter menu >>
coffee={'아메리카노':2500,'카페라떼':3000,'카푸치노':3500}
Menu = True

while Menu == True:
    prompt = """

    1. coffee Menu add
    2. coffee price
    3. end
    enter menu >>>>>:"""
    print(prompt)
    number = input("Enter Menu >>")
    if number == "1":
        A = input("추가메뉴 :")
        B = input("가격 :")
        coffee[A] = B
        print("메뉴 {} 가격 {}원을 등록 합니다.".format(A,B))
        print(coffee)
    elif number == "2":
        print(coffee)
        for c in coffee.keys():
            print(c,end=' ')
        print()
        menu = input("선택:")
        for k,v in coffee.items():
            if k==menu:
                print(v,"원",k, '메롱')
    elif number == "3":
        print("종료합니다.")
        Menu = False
        print(Menu)
        #break