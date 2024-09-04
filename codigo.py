n = int(input('digite um número:'))
c = 0 
while(c<100000):
    n = n**2
    print(n)
    c = c+0.1
    break

#média de um aluno

n1 = float(input("primeira nota do aluno:"))
n2 = float(input('segunda nota do aluno:'))
m  =  (n1+n2)/2
print(f'a média do aluno é {m}')