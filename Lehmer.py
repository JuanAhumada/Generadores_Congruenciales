def Save(glc:list):
    archive = input("Escribe el nombre del archivo: ")+".txt"
    m = open(archive, "w")
    for i in range(len(glc)):
        if i != 0:
            string = f"    {i}    |    {glc[i][0]}    |    {glc[i][1]}    |    {glc[i][2]}    |    {glc[i][3]}    \n"
        else:
            string = f"    N    |    {glc[i][0]}    |    {glc[i][1]}    |    {glc[i][2]}    |    {glc[i][3]}    \n" 
        m.write(string)    
def GLC(Xo:int, a:list, c:list, m:int, gl:bool):
    choice_a = int(input(f"{a}:\nDe todos estos numeros elige uno: "))
    while choice_a not in a:
        choice_a = int(input(f"Vuelve a intentar:\n{a}:\nDe estos numeros elige uno: "))
    if gl == 0:
        choice_c = int(input(f"{c}:\nDe todos estos numeros elige uno: "))
        while choice_c not in c:
            choice_c = int(input(f"Vuelve a intentar:\n{c}:\nDe estos numeros elige uno: "))
    else:
        choice_c = 0
    x = 1
    results = [["Xn",f"Xn+1 = {choice_a}Xn+ {choice_c} mod {m}", "Xn+1", "Numero Uniforme"]]
    while True:
        Xn = Xo*choice_a+choice_c
        i = 0
        while Xn >= m:
            Xn -= m
            i +=1
        line = [Xo, f"{i} + {Xn}/{m}", Xn, f"{Xn}/{m}"]
        if line in results:
            break
        results.append(line)
        Xo = Xn
        x +=1
    return results

def GCD(n1, n2):
    while n1:
        n2, n1 = n1, n2 % n1
    return n2

def LCM(n1, n2):
    return n1 * n2 // GCD(n1, n2)

def Prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def Multiplier(m):
    Num = Prime_factors(m)
    if m%4==0:
        Num.append(4)
    result = Num[0]
    for num in Num[1:]:
        result = LCM(result, num)
    a = []
    t = 0
    while True:
        if 1 + result*t >= m:
            return a
        a.append(1 + result*t)
        t+=1

def Root(x, e):
    a = []
    if x == 2:
        if e == 1:
            for t in range(15):
                a.append(1+2*t)
        elif e == 2:
            for t in range(15):
                a.append(3+4*t)
        elif e == 3:
            for t in range(15):
                a.append(7+8*t)
        else:
            for t in range(15):
                a.append(5+8*t)
    else:
        print("Seleccione la p:\n[3,11,13,19,21,27,29,37,53,59,61,67,69,77,83,91]")
        p = int(input("Entre estos numeros escoge 1: "))
        for t in range(15):
            a.append(200*t + p)
    return a

def Increase(m):
    c = []
    for i in range(1, m):
        if GCD(i,m) == 1:
            c.append(i)
    return c
    

def main():
    gl = int(input("Haras Mixto(0) o Multiplicativo?(1): ").strip())
    if gl == 0:
        m = int(input("Digita el modulo del generador: "))
        a = Multiplier(m)
        c = Increase(m)
        print(f"El modulo es {m}:\ntiene {len(a)} multiplicadores pueden ser {a}.\ntiene {len(c)} constantes , las que son {c}")
        Xo = int(input("Selecciona un numero inicial, no puede ser mayor ni igual al modulo: "))
        while Xo >= m:
            Xo = int(input("Vuelve a intentar, selecciona un numero inicial, no puede ser mayor ni igual al modulo: "))
        Save(GLC(Xo, a, c, m, gl))
    elif gl == 1:
        m = int(input("Digita el modulo del generador: "))
        base = Prime_factors(m)
        if base.count(2) == len(base):
            xn = Increase(m)
            xo = int(input(f"Las semillas iniciales optimas pueden ser:\n{xn}\nEscoge 1:"))
            while not xo in xn:
                xo = int(input("Elige uno que este: "))
            a = Root(2, len(base))
            Save(GLC(xo,a, [], m, gl))
        elif len(base)%2==0 and base.count(2)==(len(base)/2) and base.count(5)==(len(base)/2):
            xn = Increase(m)
            xo = int(input(f"Las semillas iniciales optimas pueden ser:\n{xn}\nEscoge 1:"))
            while not xo in xn:
                xo = int(input("Elige uno que este: "))
            a = Root(10, 1)
            Save(GLC(xo,a, [], m, gl))
        else:
            print("El modulo tiene que ser base 2 o base 10")
        
main()