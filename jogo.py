from random import randint
n=int(randint(1,20)) #número randomico
p=0 #palpite
t=0 #tentativas
while p!=n:
    p=int(input("seu palpite: "))
    t+=1
    if p==n:
        print("vc acertou! placar %i" % t)
    elif p<n:
        print("chute um valor maior")
    else:
        print("chute um valor menor")
print("fim de jogo")
