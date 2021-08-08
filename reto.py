productos = {
    1:["Manzanas", 6000.0, 97],
    2:["Limones", 2600.0, 45],
    3:["Peras", 2700.0, 45],
    4:["Arandanos", 7300.0, 44],
    5:["Tomates", 8100.0, 42],
    6:["Fresas", 9100.0, 99],
    7:["Helado", 4500.0, 41],
    8:["Galletas", 600.0, 18],
    9:["Chocolates", 4500.0, 990],
    10:["Jamon", 18000.0, 55],
}

def AGREGAR(producto):
    id_producto = int(producto[0])
    nombre = producto[1]
    precio = float(producto[2])
    inventario = float(producto[3])
    
    if id_producto not in productos:
        productos[id_producto] = [nombre, precio, inventario]
        return "EXIT"

    return "ERROR"    

def ACTUALIZAR(producto):
    id_producto = int(producto[0])
    nombre = producto[1]
    precio = float(producto[2])
    inventario = float(producto[3])
    if id_producto in productos:
        productos[id_producto] = [nombre, precio, inventario]        
        return "EXIT"
    return "ERROR"
    

def BORRAR(producto):
    id_producto = int(producto[0])
    if id_producto in productos:
        productos.pop(id_producto)
        return "EXIT"
    return "ERROR"

def producto_precio_mayor():
    precio_mayor = 0.0
    producto_return = []
    for producto in productos:
        product_aux =  productos[producto]
        if precio_mayor < product_aux[1]:
            precio_mayor = product_aux[1]
            producto_return = product_aux
    return producto_return


def producto_precio_menor():
    precio_menor = productos[1][1]
    producto_return = []
    for producto in productos:
        product_aux = productos[producto]
        if precio_menor > product_aux[1]:
            precio_menor = product_aux[1]
            producto_return = product_aux
    return producto_return


def precio_promedio():
    precio_promedio = 0
    for producto in productos:
        product_aux = productos[producto]
        precio_promedio += product_aux[1]
    precio_promedio = precio_promedio / len(productos)
    return round(precio_promedio, 1)

def valor_total_inventario():
    valor_inventario = 0
    for producto in productos:
        product_aux = productos[producto]        
        valor_inventario += product_aux[1] * product_aux[2]
    return round(valor_inventario, 1)

if __name__ == "__main__":
    operecion = input()
    producto = input().split()
    result = ''

    if operecion == "ACTUALIZAR":
        result = ACTUALIZAR(producto)
    
    elif operecion == "AGREGAR":
        result = AGREGAR(producto)
    
    elif operecion == "BORRAR":
        result = BORRAR(producto)

    if result != "ERROR":
        print(str(producto_precio_mayor()[0])+ ' '+str(producto_precio_menor()[0])+' '+str(precio_promedio())+' '+str(valor_total_inventario()))
    else:
        print(result)
    
    

