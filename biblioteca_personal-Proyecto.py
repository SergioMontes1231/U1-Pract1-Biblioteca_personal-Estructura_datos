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
        """
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        self.categoria = categoria


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
    """
    Coordina las operaciones entre la interfaz y la estructura de datos.
    Actua como puente entre la lista doblemente enlazada y la interfaz de usuario.
    
    Atributos:
        biblioteca (BibliotecaPersonal): Instancia de la biblioteca que maneja la lista de libros.
    """
    
    def __init__(self):
        """
        Inicializa el sistema de gestion con una biblioteca vacia.
        """
        self.biblioteca = BibliotecaPersonal()

    def agregar_libro(self, titulo, autor, anio, isbn, categoria):
        """
        Agrega un nuevo libro a la biblioteca.
        
        Args:
            titulo (str): Título del libro.
            autor (str): Autor del libro.
            anio (int): Año de publicacion.
            isbn (str): ISBN unico del libro.
            categoria (str): Categoria del libro.
            
        Returns:
            str: Mensaje de confirmacion.
        """
        # Verificar si ya existe un libro con el mismo ISBN
        if self.biblioteca.buscar_por_isbn(isbn):
            return f"Ya existe un libro con el ISBN {isbn}"
        
        libro = Libro(titulo, autor, anio, isbn, categoria)
        self.biblioteca.insertar_ordenado(libro)
        return f"Libro '{titulo}' agregado correctamente"

    def buscar_por_isbn(self, isbn):
        """
        Busca un libro por su ISBN.
        
        Args:
            isbn (str): ISBN del libro a buscar.
            
        Returns:
            str: Información del libro o mensaje de no encontrado.
        """
        libro = self.biblioteca.buscar_por_isbn(isbn)
        if libro:
            return str(libro)
        return f"No se encontro ningun libro con ISBN {isbn}"

    def buscar_por_autor(self, autor):
        """
        Busca libros por autor.
        
        Args:
            autor (str): Nombre del autor.
            
        Returns:
            str: Lista de libros del autor o mensaje de no encontrados.
        """
        libros = self.biblioteca.buscar_por_autor(autor)
        if libros:
            resultado = f"Libros de {autor}:\n"
            resultado += "==========================\n"
            for libro in libros:
                resultado += str(libro) + "\n" + "-" * 20 + "\n"
            return resultado
        return f"No se encontraron libros del autor {autor}"

    def buscar_por_categoria(self, categoria):
        """
        Busca libros por categoria.
        
        Args:
            categoria (str): Categoria a buscar.
            
        Returns:
            str: Lista de libros de la categoria o mensaje de no encontrados.
        """
        libros = self.biblioteca.buscar_por_categoria(categoria)
        if libros:
            resultado = f"Libros en categoria '{categoria}':\n"
            resultado += "==========================\n"
            for libro in libros:
                resultado += str(libro) + "\n" + "-" * 20 + "\n"
            return resultado
        return f"No se encontraron libros en la categoria {categoria}"

    def actualizar_libro(self, isbn, titulo, autor, anio, categoria):
        """
        Actualiza la informacion de un libro existente.
        
        Args:
            isbn (str): ISBN del libro a actualizar.
            titulo (str): Nuevo título.
            autor (str): Nuevo autor.
            anio (int): Nuevo año.
            categoria (str): Nueva categoría.
            
        Returns:
            str: Mensaje de confirmacion o error.
        """
        resultado = self.biblioteca.actualizar_libro(isbn, titulo, autor, anio, categoria)
        return resultado

    def eliminar_libro(self, isbn):
        """
        Elimina un libro por su ISBN.
        
        Args:
            isbn (str): ISBN del libro a eliminar.
            
        Returns:
            str: Mensaje de confirmación o error.
        """
        return self.biblioteca.eliminar_por_isbn(isbn)

    def mostrar_todos(self):
        """
        Muestra todos los libros en orden alfabético.
        
        Returns:
            str: Lista completa de libros o mensaje de biblioteca vacía.
        """
        if self.biblioteca.esta_vacia():
            return "La biblioteca esta vacia"
        
        resultado = f"=== BIBLIOTECA PERSONAL ===\n"
        resultado += f"Total de libros: {self.biblioteca.cantidad}\n"
        rresultado += "==========================\n"
        resultado += self.biblioteca.mostrar_todos()
        return resultado

    def mostrar_inverso(self):
        """
        Muestra todos los libros en orden inverso.
        
        Returns:
            str: Lista completa de libros en orden inverso.
        """
        if self.biblioteca.esta_vacia():
            return "La biblioteca esta vacia"
        
        resultado = f"=== BIBLIOTECA PERSONAL (ORDEN INVERSO) ===\n"
        resultado += f"Total de libros: {self.biblioteca.cantidad}\n"
        resultado += "==========================\n\n"
        resultado += self.biblioteca.mostrar_todos_inverso()
        return resultado

    def obtener_estadisticas(self):
        """
        Obtiene estadísticas de la biblioteca.
        
        Returns:
            str: Estadisticas de la biblioteca.
        """
        if self.biblioteca.esta_vacia():
            return "La biblioteca está vacia"
        
        # Contar categorias unicas
        categorias = set()
        actual = self.biblioteca.cabeza
        while actual:
            categorias.add(actual.dato.categoria)
            actual = actual.siguiente
        
        stats = f"=== ESTADISTICAS ===\n"
        stats += f"Total de libros: {self.biblioteca.cantidad}\n"
        stats += f"Categorias: {len(categorias)}\n"
        stats += f"Categorias: {', '.join(categorias)}"
        return stats

# =================================================
# INTERFAZ (ESTA AL FINAL)
# =================================================

