import clase

x = clase.opciones()
if x ==1:
    objeto = clase.cuadrado()
else:
    objeto = clase.operaciones()

match x:
    case 1:
        objeto.elev()
    case 2:
        objeto.sum()
    case 3:
        objeto.rest()
    case 4:
        objeto.mult()
    case 5:
        objeto.div()

