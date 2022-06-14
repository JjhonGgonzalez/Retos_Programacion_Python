def cliente (informacion:dict)-> dict:
    edad=informacion["edad"]
    pir= informacion["primer_ingreso"]
    
    if edad > 18:
        atraccion = 'X-Treme'
        apto = True
        if pir == True:
            total_boleta =20000-(20000*0.05)
        else: total_boleta = 20000
    elif edad >= 15 and edad<=18:
        atraccion ='Carros chocones'
        apto = True
        if pir == True:
            total_boleta = 5000-(5000*0.07)
        else: total_boleta = 5000
    elif edad >= 7 and edad < 15:
        atraccion = 'Sillas voladoras'
        apto = True
        if pir == True:
            total_boleta = 10000 - (10000*0.05)
        else: total_boleta = 10000
    else:
        atraccion="N/A"
        apto = False
        total_boleta = "N/A"         
    diccionario_salida={'nombre':informacion['nombre'],'edad':edad,'atraccion': atraccion,'apto': apto,'primer_ingreso': pir,'total_boleta': total_boleta}
       
    return diccionario_salida 
        
e={'nombre': 'Gloria Suarez', 'edad': 3, 'atraccion': 'N/A', 'apto':
False,'primer_ingreso': True}

print(cliente(e))
