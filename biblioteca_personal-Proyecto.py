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
    def __init__(self, Libro):
        self.dato = Libro
        self.siguiente = None
        self.anterior = None


class BibliotecaPersonal:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.cantidad = 0

    def esta_vacia(self):
        """ Regresa un valor que puede ser True o False, dependiendo de si la lista tiene al menos un libro o no."""
        return self.cabeza is None

    def cantidad_libros(self):
        if self.esta_vacia():
            return "No hay libros en está lista."
        return f"Número de libros registrados: {self.cantidad}"

    def insertar_libro_al_inicio(self, dato):
        """ Está función se encarga de insertar un libro al inicio de la lista, lo que convierte a este
        libro en la nueva cabeza de la lista. """
        nuevo_libro = NodoLibro(dato)

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

    def insertar_libro_al_final(self, dato):
        """ Está función realiza un proceso similar a la función de insertar al inicio, pero está vez es para insertar al final
        de nuestra lista, ahora el proceso nos identifica que el libro que está antes del que vamos a ingresar
        sea self.cola, después el programa hace que self.cola apunte a nuestro nuevo libro, y posteriormente
        nuestro libro se convierta en el último libro de la lista. """
        nuevo_libro = NodoLibro(dato)

        if self.cabeza is None:
            self.cabeza = self.cola = nuevo_libro
        else:
            nuevo_libro.anterior = self.cola
            self.cola.siguiente = nuevo_libro
            self.cola = nuevo_libro
        self.cantidad += 1

    def insertar_ordenado(self, dato):
        """ Está función a diferencia de las 2 anteriores, hace un proceso un poco diferente, puesto que utiliza el atributo titulo para identificar si el nuevo libro que vamos a ingresar,
        tiene un titulo con una letra inicial menor al titulo que se encuentra en la cabeza, o de lo contrario si el titulo del nuevo libro es mayor a la cabeza, el programa se asegura de que
        nuestro libro se ubique en un lugar donde su letra inicial sea mayor al titulo anterior, pero inferior al titulo que le sigue."""
        nuevo_libro = NodoLibro(dato)

        if self.esta_vacia():
            """ Si la lista está vacia, simplemente se insertara nuestro libro como la nueva cabeza de la lista."""
            self.cabeza = self.cola = nuevo_libro
            self.cantidad += 1
            return

        libro_actual = self.cabeza

        if dato.titulo.lower() < libro_actual.dato.titulo.lower():
            """ De otra forma, si la lista tiene uno o más titulos, el programa comenzara a comparar cada titulo, empezando por el titulo que se encuentra en la cabeza. """
            nuevo_libro.siguiente = self.cabeza
            self.cabeza.anterior = nuevo_libro
            self.cabeza = nuevo_libro
            """ Aquí nuestro libro que vamos a ingresar; le indicamos que debe apuntar a la cabeza, después la cabeza identifica que el nuevo libro este justo detras de ella.
            y finalmente se le asigna el nuevo libro a la cabeza.
            Por supuesto, este proceso también incrementa el número de libros de nuestra lista, por lo que tenemos un atributo contador que nos estará apoyando con eso."""
            self.cantidad += 1
            return

        while (libro_actual.siguiente and libro_actual.siguiente.dato.titulo.lower() < dato.titulo.lower()):
            """ En caso de que nuestro libro tenga una letra inicial mayor a la del libro de la cabeza, comenzara el siguiente proceso: en este while
            el programa identifica que mientras nuestro titulo del nuevo libro sea mayor al que se encuentra adelante de el, el ciclo continuará
            repitiendose, hasta que la condición se cumpla. """
            libro_actual = libro_actual.siguiente

        nuevo_libro.siguiente = libro_actual.siguiente
        nuevo_libro.anterior = libro_actual
        """ Este es uno de los procesos, que suceden para acomodar nuestro libro dentro de la lista, como se puede ver, nuestro libro apunta al libro que sigue del de adelante
        y después nuestro libro confirma que el libro anterior a el, sea el libro que se encuentra en la varianle libro_actual."""

        if libro_actual.siguiente:
            """ Este proceso se hace para evitar, que nos salgamos de la lista, como se puede ver libro_actual.siguiente, ya se encuentra en la cola, pero nuestro libro no debe estar
            especificamente en ella, sino antes de la cola, por lo que aquí es donde se realiza un ligero cambio de posiciones, para hacer que nuestro libro, quede antes de la cola."""
            libro_actual.siguiente.anterior = nuevo_libro
        else:
            """ De otra forma, si nuestro libro justamente es el que cuenta con la letra más adelantada del abecedario, entonces el programa le asignara la posición de la cola."""
            self.cola = nuevo_libro

        libro_actual.siguiente = nuevo_libro
        """ Este mini proceso, nos permite repetir el ciclo, al irse recorriendo libro por libro hasta llegar a el lugar indicado para posicionar nuestro libro."""
        self.cantidad += 1

    def buscar_por_isbn(self, isbn):
        """ Como su nombre lo dice, está función toma el rol de buscador, y revisa a lo largo de la lista, para ver que número de isbn coincide con la clave ingresada."""
        libro_actual = self.cabeza

        while libro_actual:
            if libro_actual.dato.isbn == isbn:
                """ Una vez que el programa identifica la igualdad, simplemente nos regresa todo el contenido del libro encontrado."""
                return libro_actual.dato

            libro_actual = libro_actual.siguiente
            """ De otra forma, simplemente nos dira que no se pudo encontrar un libro que comparta similitud con la clave que ingresamos."""
        return None

    def buscar_por_autor(self, autor):
        """ Está función realiza el mismo proceso que la anterior, pero una diferencia importante es que pueden existir varios libros que comparten el mismo autor
        por lo que, este método utiliza un arreglo para almacenar temporalmente los libros encontrados que comparten el mismo autor, con el autor que nosotros ingresamos."""
        libro_actual = self.cabeza
        encontrados = []

        while libro_actual:
            if libro_actual.dato.autor == autor:
                encontrados.append(libro_actual.dato)
            libro_actual = libro_actual.siguiente

        """ Y finalmente le pedimos al programa, que nos regrese los datos almacenados del arreglo, si es que tiene datos almacenados, de lo contrario simplemente te dira que no
        se encontraron libros que tengan a ese autor."""
        return encontrados if encontrados else None

    def buscar_por_categoria(self, categoria):
        """ Está función realiza el mismo procedimiento que el del autor, pero ahora es con las categorias."""
        libro_actual = self.cabeza
        encontrados = []

        while libro_actual:
            if libro_actual.dato.categoria == categoria:
                encontrados.append(libro_actual.dato)
            libro_actual = libro_actual.siguiente

        return encontrados if encontrados else None

    def actualizar_libro(self, isbn, nuevo_titulo, nuevo_autor, nuevo_anio, nueva_categoria):
        """ Está función se encarga de actualizar, los datos de un libro ya existente, para lograrlo debe recibir una clave isbn, para poder ubicar al libro que se desea actualizar."""
        libro_actual = self.cabeza
        while libro_actual:
            if libro_actual.dato.isbn == isbn:
                """ Una vez que el buscador encuentra el libro, accede a una función especial proporcionada por la clase Libro, dicha función nos permitirá actualizar los datos del libro
                encontrado. Por supuesto, los datos como el titulo, autor, año y categoria deben ser proporcionados por el usuario, además del isbn para que el proceso pueda funcionar."""
                libro_actual.dato.actualizar(
                    nuevo_titulo, nuevo_autor, nuevo_anio, nueva_categoria)
                return f"El libro {libro_actual.dato.isbn} a sido actualizado exitosamente"
            libro_actual = libro_actual.siguiente

        """ En caso de que el isbn, sea incorrecto o no se encuentre, el programa te lo hara saber con un pequeño mensaje."""
        return "No se encontró el libro que se desea actualizar."

    def eliminar_por_isbn(self, isbn):
        """ Está función se encarga de borrar libros de nuestrá lista, para lograrlo debe recibir una clave isbn, para poder buscar y encontrar el libro que deseamos quitar el listado."""
        if self.esta_vacia():
            """ Si la lista está vacia, utilizamos esté if, para avisarnos."""
            return "No se pudo eliminar el libro"

        libro_actual = self.cabeza

        while libro_actual:
            if libro_actual.dato.isbn == isbn:
                """ Aquí se realizan 3 casos posibles, el primero es cuando nuestro libro buscado se encuentra en la cabeza de la lista."""
                if libro_actual == self.cabeza:
                    self.cabeza = libro_actual.siguiente
                    if self.cabeza:
                        self.cabeza.anterior = None
                    else:
                        self.cola = None
                    """ Lo que procede a hacer el programa es identificar a la cabeza, como el libro que sigue del nuestro, ahora que estámos en la cabeza debemos identificar si el libro anterior al nuestro, ya es un None.
                    para confirmar que el libro que estaba originalmente en la cabeza, fue eliminado exitosamente."""

                    """ De otra forma, si solo contamos con un libro en la lista, entonces le indicamos a la cola que ahora su valor será None, es decir que ya no habra libros en la lista."""

                elif libro_actual == self.cola:
                    """ El siguiente caso ocurre, si nuestro libro encontrado es la cola, si es así se le indica a la cola que su nuevo libro será el que se encuentra antes de ella.
                    Y ahora el que se encuentra después de la cola, pasara a hacer un None. Indicandonos que la cola original fue eliminada exitosamente."""
                    self.cola = libro_actual.anterior
                    self.cola.siguiente = None

                else:
                    """ El último caso posible, es cuando nos encontramos en medio de dos libros."""
                    libro_actual.anterior.siguiente = libro_actual.siguiente
                    libro_actual.siguiente.anterior = libro_actual.anterior
                    """ Aquí, la lista puede decidir si retroceder o adelantarse, dependiendo de que libro queramos quitar."""

                self.cantidad -= 1
                return f"Eliminación completada del libro {libro_actual.dato.titulo}"

            libro_actual = libro_actual.siguiente
        return "No se pudo eliminar el libro"

    def mostrar_todos(self):
        """ Estpa función, nos permite ver cuantos libros hay almacenados en nuestra lista doblemenete enlazada."""
        if self.esta_vacia():
            return "La lista de libros está vacia"

        libro_actual = self.cabeza
        libros = ""

        """ Si nuestra lista, cuenta con libros dentro de ella, utilizamos una variable llamada libros para crear una cadena de texto con cada uno de los libros almacenados."""
        while libro_actual:
            libros += str(libro_actual.dato) + "\n\n"
            libro_actual = libro_actual.siguiente

        """ Y finalmente dicha cadena, será lo que recibiremos cuando imprimamos la función."""
        return libros

    def mostrar_todos_inverso(self):
        """ Está función realiza el mismo proceso que la función anterior, pero lo que cambia es que ahora en lugar se moverse hacia adelante, empezando desde la cabeza.
        Ahora comenzara desde la cola, y comenzará a moverse hacia atras. """
        if self.esta_vacia():
            return "La lista de libros está vacia"

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

