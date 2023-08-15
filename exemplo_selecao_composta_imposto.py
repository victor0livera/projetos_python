def inicio():
    salatual = float(input('Digite seu salário atual: '))
    irrf1 = 7.5
    irrf2 = 15 
    irrf3 = 22.5
    irrf4 = 27.5
    deduz1 = 158.40
    deduz2 = 370.40
    deduz3 = 651.73
    deduz4 = 884.96

    if (salatual >= 2112.01 and salatual <=2826.65):
        desconto = (salatual*irrf1)/100 - deduz1
    else:
        if (salatual >= 2826.66 and salatual <=3751.05):
            desconto = (salatual*irrf2)/100 - deduz2
        else:
            if (salatual >= 3751.06 and salatual <= 4664.68):
                desconto=(salatual*irrf3)/100 - deduz3
            else:
                desconto=(salatual*irrf4)/100 - deduz4    

    arredonda = round(desconto, 2)
    salliq = round((salatual-desconto), 2)

    print(f'Valor do desconto irrf: {arredonda}')
    print(f'Salário líquido: {salliq}')

inicio()