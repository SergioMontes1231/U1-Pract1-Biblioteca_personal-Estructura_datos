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

  def insertar_libro_al_inicio(self, libro):
    nuevo_libro = NodoLibro(libro)

    if self.cabeza is None:
      self.cabeza = self.cola = nuevo_objeto
    else:
     nuevo_libro.siguiente = self.cabeza
      self.cabeza.anterior = nuevo_libro
      self.cabeza = nuevo_libro

  def insertar_libro_al_final(self, libro):
    nuevo_libro = NodoLibro(libro)

    if self.cabeza is None:
      self.cabeza = self.cola = nuevo_objeto
    else:
      nuevo_objeto.anterior = self.cola
      self.cola.siguiente = nuevo_objeto
      self.cola = nuevo_objeto
