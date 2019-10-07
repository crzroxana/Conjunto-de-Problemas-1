dia= float(input("Día de nacimiento:"))
mes= float(input("Mes de nacimiento:"))


fecha_valida = True

if mes in [1,3,5,7,8,10,12]:
    if dia > 31:
        print("Dia invalido")
        fecha_valida = False
elif mes == 2:
    if dia > 29:
        print("Dia invalido")
        fecha_valida = False
elif mes in [2,4,6,9,11]:
    if dia > 30:
        print("Dia invalido")
        fecha_valida = False
else:
    print("Mes invalido")
    fecha_valida = False

if fecha_valida:
   if (mes == 1 and dia >= 21) or (mes == 2 and dia <= 18):
    print("Es Acuario")
   if (mes == 2 and dia >= 19) or (mes == 3 and dia <= 20):
    print("Es Piscis")
   if (mes == 3 and dia >= 21) or (mes == 4 and dia <=20 ):
    print("Es Aries")
   if (mes == 4 and dia >= 21) or (mes == 5 and dia <= 20):
    print("Es Tauro")
   if (mes == 5 and dia >= 21) or (mes == 6 and dia <= 20):
    print("Es Geminis")
   if (mes == 6 and dia >= 21) or (mes == 7 and dia <= 22):
    print("Es Cancer")
   if (mes == 7 and dia >= 23) or (mes == 8 and dia <= 23):
    print("Es Leo")
   if (mes == 8 and dia >= 24) or (mes == 9 and dia <= 23):
    print("Es Virgo")
   if (mes == 9 and dia >= 24) or (mes == 10 and dia <= 22):
    print("Es Libra")
   if (mes == 10 and dia >= 23) or (mes == 11 and dia <= 21):
    print("Es Escorpio")
   if (mes == 11 and dia >= 22) or (mes == 12 and dia <= 21):
    print("Es Sagitario")
   if (mes == 12 and dia >= 22) or (mes == 1 and dia <= 20):
    print("Es Capricornio")
