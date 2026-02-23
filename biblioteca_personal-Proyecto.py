# =================================================
# MODELOS
# =================================================

class Libro:
  pass

# =================================================
# ESTRUCTURA
# =================================================

class NodoLibro:
  pass

class BibliotecaPersonal:
  pass
  
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

  
# =================================================
# INTERFAZ (ESTA AL FINAL)
# =================================================
