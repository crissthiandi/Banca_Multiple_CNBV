CNBV descarga de Banca Múltiple
================

## Propósito

Desarrollar una técnica que permita obtener los archivos .xls y .xlsx
del almacén publico de la Comisión Nacional Bancaria y de Valores [Banca
múltiple](http://portafolioinfo.cnbv.gob.mx/PUBLICACIONES/IO/Paginas/bm.aspx).

## Métodologia

A través de 3 tecnologías trataremos de obtener los archivos entre los
años 2011 y 2021. Las publicaciones son mensuales y se alternan entre
archivos .xls y archivos .xlsx de forma desconocida, por lo que para
nuestros fines decimos, aleatoria.

Las 3 tecnologías a usar son,

1.  R Software ![imagen](img/testR.png)
2.  Python ![imagen](img/test1200px-Python.png)
3.  Js usando motor V8
    ![imagen](img/test1024px-V8_JavaScript_engine_logo_2.png)

## Resultados

Mientras el código en R funciona sin ningún problema usando el método
“wininet” cada archivo se descarga dañado. Al intentar abrirlos Excel
usa una rutina de recuperación que termina por corromper los archivos.
El resultado es un fracaso.

Se opta por usar un método diferente a “wininet”, pero cada uno muestra
el mismo resultado. Sin embargo en ningún momento parece haber algún
problema con las descargas continuas ya que R descarga archivos en un
modelo similar a una cola (es decir de uno a uno).

Como parte de la solución del problema se usa python a través de
selenium. Aunque en principio no parece haber algún problema con esta
solución. Se descarta dejarla como única solución por motivos de gustos.

Por último se usa Js a través de la consola de Chrome (motor V8)
pudiendo hacer uso del objeto document se crea una función de descarga y
se realizan las peticiones a tiempos de 10 segundos para evitar saturar
las solicitudes y entrar en paro de descarga.

## Conclusión

Las soluciones dados por python y Js parchan el problema que se tiene al
usar R en windows. Aunque no se probo que el método “curl” en R (debido
a que “curl” esta disponible nativamente en linux) pueda funcionar y
solucionar los problemas. Se cree que es una solución valida al
problema.

Aunque la solución en python es más rápido que la de Js, Js demostró ser
una solución más artesanal y de mayor gusto para mí.

## Resultado final

El resultado final de este repositorio estará publico en
[crissthiandi/Banca-Multiple](https://rpubs.com/Crissthiandi/estadistica-conceptos-basicos)
y actualizado en cada request de este repositorio.
