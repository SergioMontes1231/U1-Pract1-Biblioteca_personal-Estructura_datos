# 📚 Biblioteca Personal --- Manual de Trabajo en Equipo

## 🎯 Objetivo

Implementar el sistema descrito en el documento en un solo archivo
`.py`, utilizando clases y respetando la arquitectura definida en el
diagrama UML.

El enfoque del equipo es mantener:

-   Código limpio\
-   Separación clara de responsabilidades\
-   Buen uso de Git\
-   Estilo PEP8\
-   Flujo ordenado de trabajo

------------------------------------------------------------------------

# 🧱 Arquitectura del Archivo

El archivo principal se organiza en bloques fijos.\
**No se deben mover ni mezclar secciones.**

``` python
# =========================
# MODELOS
# =========================

class Libro:
    ...

# =========================
# ESTRUCTURA
# =========================

class NodoLibro:
    ...

class BibliotecaPersonal:
    ...

# =========================
# LOGICA
# =========================

class SistemaGestion:
    ...

# =========================
# INTERFAZ
# =========================
```

------------------------------------------------------------------------

# 🌿 Ramas del Proyecto

## `main`

-   Rama estable.
-   Solo contiene código funcional y revisado.
-   No se programa directamente aquí.

## `feature/modelos`

Responsable de: - Clase `Libro` - Constructor - Método `__str__` -
Método `actualizar`

## `feature/estructura`

Responsable de: - `NodoLibro` - `BibliotecaPersonal` - Lista doblemente
enlazada - Métodos de inserción, búsqueda, actualización y eliminación

⚠ No debe usar `input()` ni `print()`.

## `feature/logica`

Responsable de: - Clase `SistemaGestion` - Uso de métodos de
`BibliotecaPersonal` - Coordinación general del sistema

⚠ No debe implementar lógica interna de la lista.

## `feature/interfaz`

Se desarrolla al final.

Responsable de: - Menú - Interacción con el usuario - `input()` y
`print()`

Solo debe llamar métodos de `SistemaGestion`.

------------------------------------------------------------------------

# 🔄 Flujo de Trabajo

1.  Nunca programar en `main`.
2.  Trabajar únicamente en la rama asignada.
3.  Hacer commits pequeños y frecuentes.
4.  Antes de hacer merge:
    -   Actualizar rama con `main`
    -   Probar que el código funcione
5.  Hacer Pull Request.
6.  Solo mergear cuando esté revisado.

------------------------------------------------------------------------

# ✍ Convención de Commits

Formato:

    tipo: descripcion clara y breve

Tipos permitidos:

-   `feat:` nueva funcionalidad
-   `fix:` corrección de error
-   `refactor:` mejora interna sin cambiar funcionalidad
-   `docs:` documentación
-   `style:` formato o PEP8

### Ejemplos

    feat: agregar clase Libro con constructor
    feat: implementar insercion al final en lista doble
    fix: corregir enlace anterior en eliminacion
    docs: agregar docstrings a BibliotecaPersonal
    style: aplicar formato PEP8

------------------------------------------------------------------------

# 📘 Estándar de Código (PEP8)

## Nombres de clases

PascalCase

    Libro
    NodoLibro
    BibliotecaPersonal
    SistemaGestion

## Métodos y variables

snake_case

    insertar_al_final
    buscar_por_isbn
    cantidad_total

## Indentación

-   4 espacios
-   Línea en blanco entre clases
-   Código claro y legible

------------------------------------------------------------------------

# 🧾 Documentación (Docstrings)

Todas las clases y métodos deben tener docstrings.

### Ejemplo de clase

``` python
class Libro:
    """
    Representa un libro dentro de la biblioteca personal.

    Atributos:
        titulo (str): Titulo del libro.
        autor (str): Autor del libro.
        anio (int): Año de publicacion.
        isbn (str): Identificador unico del libro.
        categoria (str): Categoria del libro.
    """
```

### Ejemplo de método

``` python
def insertar_al_final(self, libro: Libro) -> None:
    """
    Inserta un libro al final de la lista.

    Args:
        libro (Libro): Libro a insertar.

    Returns:
        None
    """
```

------------------------------------------------------------------------

# 🧠 Dependencias del Sistema

Orden lógico del proyecto:

    Libro
       ↓
    NodoLibro
       ↓
    BibliotecaPersonal
       ↓
    SistemaGestion
       ↓
    Interfaz

------------------------------------------------------------------------

# 🚫 Reglas Importantes

-   No borrar comentarios de sección.
-   No mover clases de lugar.
-   No mezclar responsabilidades.
-   No meter lógica de estructura dentro de `SistemaGestion`.
-   No meter interfaz dentro de estructura.

------------------------------------------------------------------------

# 🏁 Resultado Esperado

El proyecto debe:

-   Funcionar correctamente\
-   Estar bien organizado\
-   Cumplir con el diagrama UML\
-   Seguir buenas prácticas de Git\
-   Estar documentado\
-   Ser fácil de explicar
