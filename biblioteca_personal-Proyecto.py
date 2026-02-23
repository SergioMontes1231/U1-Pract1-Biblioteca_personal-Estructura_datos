# =================================================
# MODELOS
# =================================================

class Libro:
  """
    Representa un libro dentro de un sistema de gestión.

    Attributes:
        titulo (str): Título del libro.
        autor (str): Nombre del autor.
        anio (int): Año de publicación.
        isbn (str): Código ISBN del libro.
        categoria (str): Categoría o género del libro.
  """
  def __init__(self, titulo, autor, anio, isbn, categoria):
    """
      Inicializa una instancia de Libro con sus datos principales.

      Args:
        titulo (str): Título del libro.
        autor (str): Nombre del autor.
        anio (int): Año de publicación.
        isbn (str): Código ISBN.
        categoria (str): Categoría del libro.
    """
    self.titulo = titulo
    self.autor = autor
    self.anio = anio
    self.isbn = isbn
    self.categoria = categoria

  def __str__(self):
    """
      Devuelve una representación en texto del libro.
        
      Returns:
        str: Información formateada del libro.
    """
    return (
        f"Titulo: {self.titulo}\n"
        f"Autor: {self.autor}\n"
        f"Anio: {self.anio}\n"
        f"ISBN: {self.isbn}\n" 
        f"Categoria: {self.categoria}"
        )

  def actualizar(self, titulo, autor, anio, categoria):
    """
      Actualiza la información editable del libro.

      Args:
        titulo (str): Nuevo título.
        autor (str): Nuevo autor.
        anio (int): Nuevo año de publicación.
        categoria (str): Nueva categoría.
    """
    self.titulo = titulo
    self.autor = autor
    self.anio = anio
    self.categoria = categoria

# =================================================
# ESTRUCTURA
# =================================================

class NodoLibro:
  pass

#comentario prueba de un commit

class BibliotecaPersonal:
  pass

# =================================================
# Logica
# =================================================

# =========================
# LOGICA
# =========================
class SistemaGestion:
    def __init__(self):
        self.biblioteca = BibliotecaPersonal()

    def agregar_libro(self, titulo, autor, anio, isbn, categoria):
        # Agrega un libro al sistema
        libro = Libro(titulo, autor, anio, isbn, categoria)
        self.biblioteca.insertar_libro_al_final(libro)
        return "Libro agregado correctamente"

    def buscar_libro(self, isbn):
        return self.biblioteca.buscar_por_isbn(isbn)

    def buscar_por_autor(self, autor):
        return self.biblioteca.buscar_por_autor(autor)

    def eliminar_libro(self, isbn):
        if self.biblioteca.eliminar_por_isbn(isbn):
            return "Libro eliminado correctamente"
        return "Libro no encontrado"

    def mostrar_todos(self):
        if self.biblioteca.cantidad == 0:
            return "No hay libros en la biblioteca"

        resultado = f"Total: {self.biblioteca.cantidad} libros\n"
        resultado += "==========================\n"
        
        actual = self.biblioteca.cabeza
        while actual:
            resultado += str(actual.libro) + "\n"
            actual = actual.siguiente

        return resultado