import math
nom = input('Bienvenido, ¿Cuál es tu nombre? ')
print('Hola', nom, ', Bienvenido a la Calculadora de Progresiones Geométricas y Aritméticas')
rango = False
while not rango == True:
    pro = int(input('¿Deseas calcular Progresiones Geométricas (1) o Aritméticas (2)? '))
    print('')
    if pro == 1:
        print('Progresiones Geométricas')
        x= int(input('Con el primer término y la razón(1), Con los primeros tres términos(2), Encontrar el número de términos de la Progesión(3) '))
        if x == 1:
            r = int(input('Razón '))
            p = int(input('Primer Término '))
            n = int(input('Posición(n) '))
            un = p*(r**(n-1))
            print('El término en la', n, 'posición es', un)
            print('El proceso es el siguiente')
            print('un = u1*r^n-1 =>', p, '*', r, '^', n, '- 1', '=', un)
        if x == 2:
            pt= int(input('Primer Término '))
            st= int(input('Segundo Término '))
            tt= int(input('Tercer Término '))
            r1 = st/pt
            r2 = tt/st
            if r1 == r2:
                ct = tt*r1
                qt = ct*r1
                sxt = qt*r1
                spt = sxt*r1
                ot = spt*r1
                seq=[pt,st,tt,ct,qt,sxt,spt,ot]
                print(seq)
                print('El proceso es el siguiente')
                print('un = u1*r^n-1 =>', pt, ',', pt, '*', r1, ',', st, '*', r1, ',', tt, '*', r1, ',', ct, '*', r1, ',', qt, '*', r1, ',', sxt, '*', r1, spt, '*', r1, '=', seq)
        if x == 3:
            pt= int(input('Primer Término '))
            st= int(input('Segundo Término '))
            tt= int(input('Tercer Término '))
            nt= int(input('Introducir Último Término '))
            r1 = st/pt
            r2 = tt/st
            if r1 == r2:
                num = math.log(nt/pt)
                dem = math.log(r1)
                n = (num/dem)+1
                print('La progesión tiene',n, 'términos')
    print('')
    if pro == 2:
        print('Progresiones Aritméticas')
        x= int(input('Con el primer término y diferencia(1), Con los primeros tres términos(2), Enoncantrar el número de términos(3) '))
        if x == 1:
            d = int(input('Diferencia '))
            p = int(input('Primer Término '))
            n = int(input('Posición(n) '))
            un = p + (n-1)*(d)
            print('El término en la', n, 'posición es', un)
            print('El proceso es el siguiente')
            print('un = u1+(n-1)*d =>', p, '+', '(', n, '- 1', ')', '*', d,  '=', un)
        if x == 2:
            pt= int(input('Primer Término '))
            st= int(input('Segundo Término '))
            tt= int(input('Tercer Término '))
            d1 = tt-st
            d2 = st-pt
            if d1 == d2:
                ct = tt + d1
                qt = ct + d1
                sxt = qt + d1
                spt = sxt + d1
                ot = spt + d1
                seq=[pt,st,tt,ct,qt,sxt,spt,ot]
                print(seq)
                print('El proceso es el siguiente')
                #print('un = u1*r^n-1 =>', pt, ',', pt, '*', r1, ',', st, '*', r1, ',', tt, '*', r1, ',', ct, '*', r1, ',', qt, '*', r1, ',', sxt, '*', r1, spt, '*', r1, '=', seq)
        if x == 3:
            pt= int(input('Primer Término '))
            st= int(input('Segundo Término '))
            tt= int(input('Tercer Término '))
            nt= int(input('Introducir Último Término '))
            d1 = tt-st
            d2 = st-pt
            if d1 == d2:
                n = (nt-(pt-d1))/d1
                print('La progesión tiene',n, 'términos')
                #print('El proceso es el siguiente')
                #print('un = u1+(n-1)*d =>', pt, '+', '(', n, '- 1', ')', '*', d,  '=', un)
    print('')
