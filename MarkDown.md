# Tutorial basico de MarkDown
Este tutorial esta orientado a personas que quieren aprender lenguaje Markdown para redaccion de un documento
## Contenido
- [Encabezado](#Encabezado)
- [Citas](#Citas)
- [Listas](#Listas)
  - [Listas desordenadas ](#Listas-desordenadas )
  - [Listas ordenadas](#Listas-ordenadas)
- [Linea Horizontal](#Linea-Horizontal)
- [Intesertar codigo](#Intesertar-codigo)
  - [Agregar varias lineas de codigo](#Agregar-varias-lineas-de-codigo)
  - [Agregar una linea de codigo](Agregar-una-linea-de-codigo)
- [Enfasis en palabras](#Enfasis-en-palabras)
  - [Cursiva](#Cursiva)
  - [Negritas](#Negritas)
- [Enlaces](#Enlaces)
- [Imagenes](#Imagenes)
- [Tablas](#Tablas)
---
## Encabezado
para colocar encabezados utiliza el simbolo "#" 

(para dar un salto de linea o cambio de parrafo debe ser doble entender)

Ejemplo:

# Encabezado 1 
"# Encabezado 1"
## Encabezado 2 
"## Encabezado 2"
### Encabezado 3 
"### Encabezado 3"
###### Encabezado 6 
"###### Encabezado 6"

# Citas
Para insertar una cita utiliza el caracter " > "(mayor que), seguido del texto

Ejemplo:

> Yo solo se que no se nada. - Socrates

## Listas
### Listas desordenadas 
Para realizar listas con viñetas, utiliza el simbolo " * "(asterisco), " - " (menos) o " + " (mas)

Ejemplo:

- Elemento 1
- Elemento 2
- Elemento 3
- Elemento 4
    - Elemento interno
        - Elemento interno interno

### Listas ordenadas 
Para las listas ordenadas, utiliza la numeraion arabiga en cada elemento de la lista

1. Elemento 
2. Elemento 
3. Elemento
  - Elemento sin orden 1
  - Elemento sin orden 2

## Linea Horizontal
Para insertar una linea horizontal utiliza tres veces un simpolo de estos " - "(guiones), " * "(asteriscos) o " _ "(guiones bajo)

Ejemplo:
---
***
___

## Intesertar codigo
### Agregar varias lineas de codigo
Para insertar una seccion de codigo utiliza el simbolo " ~ " tres veces al inicio y al final de la ccion de codigo (este para varias lineas de codigo)

Ejemplo:

~~~
x = True
if x:
  print("Hola")
else:
  print("No hola")
~~~

### Agregar una linea de codigo
Si se quiere insertar una sola linea de codigo, se puede utilizar el simbolo "``" (comilla invertida, no se como se llama) al inicio y al final de lo que sea el codigo
`print("hola juan")`

Nota: otra forma de añadir codigo es dando 4 espacios de separacion al inicio (suele ser un Tab, pero puede variar con la configuracion del equipo asi que es mas seguro dar 4 espacios)

Ejemplo:

    print("codigo CON TAB")

## Enfasis en palabras
### Cursiva
Para colocar formato de cursiva utiliza un " * "(asterisco) o " _ "(guion bajo) al inicio y final del texto que quieras darle el formato

Ejemplo:

*Texto en cursiva asterisco*
_Texto en cursiva guion bajo_

### Negritas
Para colocar formato de negritas utiliza dos " * "(asterisco) o " _ "(guion bajo) al inicio y final del texto que quieras darle el formato

Ejemplo:

**Texto en negritas asterisco**
__Texto en negritas guion bajo__

Nota: Si agregas 3 guiones bajos o 3 asteriscos al inicio y al final, se convierte a formato negrita y en cursiva

Ejemplo:

___Cursiva negrita___

***Cursiva negrita***

## Enlaces 
Para insertar el enlace a una pagina web, un archivo o algun titulo/seccion del mismo documento, se sigue la sintaxis
"[Texto que se muestra](ruta)"

Ejemplo:

[Link de prueba a google](https://www.google.com)

Nota: Si tienes conocimiento en web, funciona similar al <a link =""></a>

## Imagenes
Insertar una imagen se realiza de una manera practicamente identica a insertar links, habiendo dos metodos

Ejemplo:

![Esta es una imagen](https://static.boredpanda.com/blog/wp-content/uploads/2025/03/469620128_886371973687130_3171849922604040918_n-67c6b7076482f__700.jpg "texto si referencia")


<img src=https://static.boredpanda.com/blog/wp-content/uploads/2025/03/funny-random-rare-pictures-99-67c6fb86ab401__700.jpg width = 150>

## Tablas
Para especificar los elementos de la cabecera de cada columna debera encerarlo entre barras

Ejemplo:

| Primer columna | Segunda columna | Tercera columna |
|----------------|-----------------|-----------------|
|opcion 1        |opcion 2         |opcion 3         |
|opcion 1        |opcion 2         |opcion 3         |
