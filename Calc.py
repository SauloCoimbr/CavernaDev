y =int(input('Digite um valor: '))
x =int(input('Digite outro valor: '))
oper1=str(input('Digite um operador [+ - x % :] '))
if oper1 == '+':
    soma = y + x
    print (f'{y} + {x} = {soma}')
elif oper1 == '%':  
    div = x / y
    print(f'{y} % {x} = {div:.2f}')
elif oper1 == 'x':
    mult = x * y
    print(f'{y} X {x} = {mult}')
else:
  menos = x - y
  print(f'{x} - {y} = {menos}')

