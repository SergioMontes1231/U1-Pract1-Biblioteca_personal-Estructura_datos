#Crear un sistema para insertar: al inicio, al final, o en orden alfabético por título.
#Consultar: recorrido normal e inverso, búsquedas específicas
#Actualizar: modificar datos de un libro existente.
#Eliminar: remover un libro y mantener los enlaces correctos.
# Nota: Debo manejar casos especiales (lista vacia, un solo elemento, eliminación de cabeza/cola)
""" Primer intento: prototipo de las funciones. """

class BibliotecaPersonal:
  def __init__(self):
    self.cabeza = None
    self.cola = None
    self.cantidad = 0

  def esta_vacia(self):
    """ Regresa un valor que puede ser True o False, dependiendo de si la lista tiene al menos un libro o no."""
     return self.cabeza is None

  def cantidad_libros(self):
    return self.cantidad
    
  def __str__(self): #Solo puede existir uno por clase
     if self.esta_vacia():
       return "Lista vacía"
      return f"Cantidad de libros: {self.cantidad}"
    
  def insertar_libro_al_inicio(self, libro):
    """ Está función se encarga de como su nombre lo indica, insertar un libro al inicio de la lista, lo que convierte a este
    libro en la nueva cabeza de la lista. """
    nuevo_libro = NodoLibro(libro)

    if self.cabeza is None:
      """ Aquí el programa verifica si la cabeza está vacia, en caso de que así sea se iguala con la cola
      y a ambos se les asigna el mismo libro."""
      self.cabeza = self.cola = nuevo_libro
    else:
      """ De lo contrario, si la lista ya cuenta con un libro en la cabeza, entonces lo que procede es
      que el programa identifique dicho libro y haga que nuestro libro que queremos ingresar, apunte al libro que está
      en la cabeza, y por último convertir nuestro libro en la nueva cabeza, recorriendo al otro libro, a la cola de
      nuestra lista. """
      nuevo_libro.siguiente = self.cabeza
      self.cabeza.anterior = nuevo_libro
      self.cabeza = nuevo_libro
    self.cantidad += 1
    
  def insertar_libro_al_final(self, libro):
    """ Está función realiza un proceso similar a la función de insertar al inicio, pero está vez es para insertar al final
    de nuestra lista, ahora el proceso nos identifica que el libro que está antes del que vamos a ingresar
    sea self.cola, después el programa hace que self.cola apunte a nuestro nuevo libro, y posteriormente
    nuestro libro se convierta en el último libro de la lista. """
    nuevo_libro = NodoLibro(libro)

    if self.cabeza is None:
      self.cabeza = self.cola = nuevo_objeto
    else:
      nuevo_objeto.anterior = self.cola
      self.cola.siguiente = nuevo_objeto
      self.cola = nuevo_objeto
    self.cantidad += 1
# Hasta aquí me quede :)
    
