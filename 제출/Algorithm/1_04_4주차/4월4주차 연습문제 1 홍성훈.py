
n = 1 #Count 변수
sum = 0 #합계 변수
#n1 = 472 #첫번째 자연수
#n2 = 385 #두번째 자연수
while True:
    try :
        n1 = int(input("첫번째 3자리 숫자를 입력하세요 : ")) #첫번째 자연수
        break
    except :
        print("숫자만 입력하세요")
        
while True:
    try :
        n2 = int(input("두번쨰 3자리 숫자를 입력하세요 : ")) #두번째 자연수
        break
    except :
        print("숫자만 입력하세요")
    
while n <= len(str(n2)):# 두번째 자연수의 자리수 만큼 반복
    #첫번째 자연수 * 각 자리수
    #10의 n제곱으로 각 자리의 숫자를 계산하여 첫번째 자연수에 곱함
    tmp = int(n1*(n2%10**n - n2%10**(n-1))/10**(n-1)) #임시 변수
    #중간 계산된 숫자 출력
    print(tmp) 
    #자리수 위치 맞게 10의 n제곱을 곱하여 합산
    sum += tmp * 10**(n-1)
    n+=1

#최종 합산 숫자 출력
print(sum)
