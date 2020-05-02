""" Aqui se escriben las operaciones sobre la base de datos simulada """

""" TODO: Debe devolver todas las categorias de los productos en la 
base de datos sin repeticiones """
def categorias(db):
    return ["categoria1", "categoria2"]
    
""" TODO: Debe devolver todas las marcas de los productos en la 
base de datos sin repeticiones """
def marcas(db):
    return ["marca1", "marca2"]

""" TODO: Debe devolver todas los descuentos de los productos en la 
base de datos sin repeticiones """
def descuentos(db):
    return [20, 10]

""" TODO: Debe listar todos los productos cuya condicion sea igual a la del
parametro """
def filtrar_por_condicion(db, condicion):
    return db['productos']

""" TODO: Debe listar todos los productos cuyo nombre o descripcion 
contengan algunas de las palabras enviadas por parametros """
def buscar_productos(db, palabras):
    return db['productos']

""" TODO: Agregar el resto de las funciones necesarias para que la
aplicacion funcione perfectamente """