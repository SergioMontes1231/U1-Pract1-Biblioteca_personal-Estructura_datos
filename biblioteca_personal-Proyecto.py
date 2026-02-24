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
    def __init__(self, libro):
        self.dato = libro
        self.siguiente = None
        self.anterior = None


class BibliotecaPersonal:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.cantidad = 0

    def esta_vacia(self):
        """Indica si la lista está vacía."""
        return self.cabeza is None

    def cantidad_libros(self):
        if self.esta_vacia():
            return "No hay libros en esta lista."
        return f"Número de libros registrados: {self.cantidad}"

    def insertar_libro_al_inicio(self, dato):
        """Inserta un libro al inicio de la lista."""
        nuevo_libro = NodoLibro(dato)

        if self.cabeza is None:
            # Si la lista está vacía, cabeza y cola apuntan al nuevo libro.
            self.cabeza = self.cola = nuevo_libro
        else:
            # El nuevo libro apunta a la cabeza actual.
            nuevo_libro.siguiente = self.cabeza
            self.cabeza.anterior = nuevo_libro
            self.cabeza = nuevo_libro

        self.cantidad += 1

    def insertar_libro_al_final(self, dato):
        """Inserta un libro al final de la lista."""
        nuevo_libro = NodoLibro(dato)

        if self.cabeza is None:
            # Si la lista está vacía, cabeza y cola apuntan al nuevo libro.
            self.cabeza = self.cola = nuevo_libro
        else:
            # Se enlaza el nuevo libro después de la cola.
            nuevo_libro.anterior = self.cola
            self.cola.siguiente = nuevo_libro
            self.cola = nuevo_libro

        self.cantidad += 1

    def insertar_ordenado(self, dato):
        """Inserta un libro manteniendo el orden alfabético por título."""
        nuevo_libro = NodoLibro(dato)

        if self.esta_vacia():
            # Si la lista está vacía, se inserta como único elemento.
            self.cabeza = self.cola = nuevo_libro
            self.cantidad += 1
            return

        libro_actual = self.cabeza

        if dato.titulo.lower() < libro_actual.dato.titulo.lower():
            # Si el nuevo título es menor que el de la cabeza, se inserta al inicio.
            nuevo_libro.siguiente = self.cabeza
            self.cabeza.anterior = nuevo_libro
            self.cabeza = nuevo_libro
            self.cantidad += 1
            return

        # Se avanza mientras el siguiente título sea menor al nuevo.
        while (
            libro_actual.siguiente
            and libro_actual.siguiente.dato.titulo.lower()
            < dato.titulo.lower()
        ):
            libro_actual = libro_actual.siguiente

        # Se ajustan los enlaces para insertar en medio o al final.
        nuevo_libro.siguiente = libro_actual.siguiente
        nuevo_libro.anterior = libro_actual

        if libro_actual.siguiente:
            libro_actual.siguiente.anterior = nuevo_libro
        else:
            # Si no hay siguiente, el nuevo libro pasa a ser la cola.
            self.cola = nuevo_libro

        libro_actual.siguiente = nuevo_libro
        self.cantidad += 1

    def buscar_por_isbn(self, isbn):
        """Busca un libro por su ISBN."""
        libro_actual = self.cabeza

        while libro_actual:
            if libro_actual.dato.isbn == isbn:
                return libro_actual.dato
            libro_actual = libro_actual.siguiente

        return None

    def buscar_por_autor(self, autor):
        """Busca todos los libros de un autor."""
        libro_actual = self.cabeza
        encontrados = []

        while libro_actual:
            if libro_actual.dato.autor == autor:
                encontrados.append(libro_actual.dato)
            libro_actual = libro_actual.siguiente

        return encontrados if encontrados else None

    def buscar_por_categoria(self, categoria):
        """Busca todos los libros de una categoría."""
        libro_actual = self.cabeza
        encontrados = []

        while libro_actual:
            if libro_actual.dato.categoria == categoria:
                encontrados.append(libro_actual.dato)
            libro_actual = libro_actual.siguiente

        return encontrados if encontrados else None

    def actualizar_libro(self, isbn, nuevo_titulo, nuevo_autor, nuevo_anio, nueva_categoria):
        """Actualiza los datos de un libro existente mediante su ISBN."""
        libro_actual = self.cabeza

        while libro_actual:
            if libro_actual.dato.isbn == isbn:
                libro_actual.dato.actualizar(
                    nuevo_titulo, nuevo_autor, nuevo_anio, nueva_categoria
                )
                return f"El libro {isbn} ha sido actualizado exitosamente"

            libro_actual = libro_actual.siguiente

        return "No se encontró el libro que se desea actualizar."

    def eliminar_por_isbn(self, isbn):
        """Elimina un libro de la lista mediante su ISBN."""
        if self.esta_vacia():
            return "No se pudo eliminar el libro"

        libro_actual = self.cabeza

        while libro_actual:
            if libro_actual.dato.isbn == isbn:

                if libro_actual == self.cabeza:
                    # Caso: el libro está en la cabeza.
                    self.cabeza = libro_actual.siguiente
                    if self.cabeza:
                        self.cabeza.anterior = None
                    else:
                        self.cola = None

                elif libro_actual == self.cola:
                    # Caso: el libro está en la cola.
                    self.cola = libro_actual.anterior
                    self.cola.siguiente = None

                else:
                    # Caso: el libro está en medio de la lista.
                    libro_actual.anterior.siguiente = libro_actual.siguiente
                    libro_actual.siguiente.anterior = libro_actual.anterior

                self.cantidad -= 1
                return f"Eliminación completada del libro {libro_actual.dato.titulo}"

            libro_actual = libro_actual.siguiente

        return "No se pudo eliminar el libro"

    def mostrar_todos(self):
        """Muestra todos los libros desde la cabeza hacia adelante."""
        if self.esta_vacia():
            return "La lista de libros está vacía"

        libro_actual = self.cabeza
        libros = ""

        while libro_actual:
            libros += str(libro_actual.dato) + "\n\n"
            libro_actual = libro_actual.siguiente

        return libros

    def mostrar_todos_inverso(self):
        """Muestra todos los libros desde la cola hacia atrás."""
        if self.esta_vacia():
            return "La lista de libros está vacía"

        libro_actual = self.cola
        libros = ""

        while libro_actual:
            libros += str(libro_actual.dato) + "\n\n"
            libro_actual = libro_actual.anterior

        return libros

# =================================================
# Logica
# =================================================

class SistemaGestion:
  pass

# =================================================
# INTERFAZ (ESTA AL FINAL)
# =================================================

