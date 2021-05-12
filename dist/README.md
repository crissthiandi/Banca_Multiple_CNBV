CNBV descarga de Banca Múltiple
================

## Detalles

La banca múltiple de la CNBV puede ser consultada vía navegador y su
información puede ser descargada una a una. La banca no prohíbe un
número de descargas máximo sin embargo al intentar solicitar múltiples
descargas en simultaneo, al menos en mi caso, suele haber una parada del
proceso.

Esto es especialmente problemático ya que aunque aveces se detiene con
los elementos de interés descargados en orden, otras veces se descargan
aleatoriamente algunos y otros no, haciendo complicada la tarea de
descarga los faltantes.

En este trabajo se buscan los datos de la banca múltiple entre los años
2011-2021 sin embargo el mismo código puede ser adaptado para cualquier
intervalo.

En el caso particular de Js este tiene que ser seriado, es decir, con
intervalos de 1 en 1. Mientras que en R o Python no hay esta limitación.
Aunque normalmente se tiene interés en una serie completa sin rupturas,
por lo que lo comentado anteriormente sobre Js podría no ser una
desventaja.

Un vistazo de la pagina en el momento de este trabajo es la siguiente,

![Not-Found-Gif-:c](../img/clips/output_reduce.gif)

Como podemos ver la pagina tiene por lista los elementos a descargar en
grupos inicialmente de 25. Este valor es modificable. La tabla esta
ordenada por fecha y año, por lo que navegando entre cada grupo podemos
tener rápido acceso al año 2011 o de interés.

Sin embargo esto no es relevante para el método de descarga ya que cada
archivo tiene un link estático de descarga. La estructura de este link
es la siguiente:

``` r
"https://portafolioinfo.cnbv.gob.mx/PortafolioInformacion/BM_Operativa_%s.xls" %>% sprintf(fecha_tag) 
```

En un formato menos programable

> “<https://portafolioinfo.cnbv.gob.mx/PortafolioInformacion/BM_Operativa_>”
> *+* Fecha\_en\_formato\_año\_mes *+* .xls/.xlsx

Como podemos ver hay dos posibles archivos, los de extensión .xls y los
de .xlsx, se distribuyen de forma algo aleatoria sobre los años por lo
que hay que considerar que para cada archivo existe solo un link de
descarga funcional de un total de dos posibles links.

**Teniendo todo esto en consideración se realizan las descargas usando
R, Python y Js.**

## Resultado final

El resultado final de este repositorio estará publico en
[crissthiandi/Banca-Multiple](https://rpubs.com/Crissthiandi/estadistica-conceptos-basicos)
y actualizado en cada request de este repositorio.
