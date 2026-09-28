## Decisiones de Diseño:
**Diccionarios anidados para los datos:** Se optó por centralizar los datos en el diccionario COLUMNAS y las configuraciones en ROLES. Esto evita el uso de listas paralelas (ej. nombres = [...], tipos = [...]), que son propensas a errores de desincronización si se elimina o agrega un elemento.
**Retornos tempranos (Early Returns):** En la función informar_columnas(), se utilizaron sentencias return luego de manejar el caso por defecto (rol is None) y los errores de validación. Esto evita anidar todo el código principal dentro de un gran bloque else, mejorando la legibilidad.
**Integración de map() y filter():** Para cumplir con los requerimientos técnicos, se implementó filter() evaluando directamente el diccionario, y map() para combinar los datos con el texto de salida.

## Errores encontrados y soluciones:
**Error de KeyError en roles sin completitud:** Al intentar filtrar por completitud mínima en el rol "docente", el programa fallaba porque esa clave no existía en su diccionario. Como solucion se agregó una validación previa usando el operador in (if "completitud_minima" in config:), aplicando el filtro filter() únicamente si el rol exige ese parámetro.
**Error de KeyError cuando se ingresa un rol no existente**: Al intentar informar un rol no existente, el programa fallaba debido a que esa clave no existía en su diccionario. Para solucionar esto, se agrego una verificacion: if rol not in ROLES:, lo que hace que si se ingresa un rol no existente, la funcion pueda retornar alli y devolver un print con un mensaje de que ese rol es incorrecto e informandote de los que si lo son.


## Respuestas a las Preguntas Orientadoras:
**¿Qué ventajas tienen las estructuras elegidas para almacenar los datos de las columnas y roles con respecto a otras de las vistas en la teoría?**
El uso de diccionarios permite acceder a los elementos mediante una clave (el nombre de la columna o el nombre del rol) con mucha mas facilidad. A diferencia de las listas, donde habría que iterar secuencialmente para encontrar a qué índice corresponde "ESTADO", el diccionario encapsula todos los atributos ("tipo", "completitud") en una única entidad directamente accesible.

**¿Qué valores elegiste para los roles y los porcentajes de completitud y por qué? ¿Cómo garantizaste que el programa pueda ser validado con diferentes roles, criterios de ordenamiento y umbrales?**
Se eligieron porcentajes variados (desde 68% hasta 100%) para probar casos límite en los filtros. Los roles se diseñaron representando necesidades reales: el analista requiere todos los datos casi perfectos (90%), el investigador acepta un margen de error (70%) para variables clave (ingresos), y el docente no filtra por completitud. Para asegurarme de que funcione con cualquier rol, armé la función informar_columnas sin valores fijos. Simplemente se adapta leyendo sobre la marcha las reglas de orden y el umbral mínimo directamente del diccionario que recibe.

**¿Por qué conviene separar la configuración de los roles (ROLES) de la lógica que genera el informe?**
Conviene separar por si el día de mañana se deben agregar 10 roles nuevos, modificar los existentes, o cambiar los umbrales, solo se edita la estructura de datos ROLES. El motor de la función informar_columnas() permanece intacto, evitando introducir bugs accidentales en la lógica de filtrado o impresión.

**¿Qué parámetros se pueden definir con valores por defecto?**
El parámetro rol en la función principal se definió con un valor por defecto: def informar_columnas(rol=None). Esto permite que la función asuma un comportamiento estándar (mostrar el reporte completo) si el usuario la invoca sin enviar ningún argumento.

**Si agregás una nueva columna al dataset, ¿en qué partes del código impacta? ¿Y si solo se quiere que un rol existente incluya esa nueva columna?**
Agregar una nueva columna impacta únicamente en el diccionario COLUMNAS. Si se quiere que un rol específico la incluya, solo impactará agregando el nombre de esa columna en la lista "columnas" dentro del diccionario del rol correspondiente en ROLES. La función principal no sufre ninguna modificación.

**¿Qué pasaría si un rol tuviera un criterio de orden distinto a los especificados "nombre" o "completitud" (por ejemplo, "promedio")? ¿Cómo lo detectarías y qué harías para que el programa no falle?**
Actualmente, el código asume que si no es "nombre", ordena por "completitud" (en el else). Si ingresara "promedio", el programa intentaría buscar COLUMNAS[c]["completitud"] igual, pero si intentáramos buscar la clave "promedio", arrojaría un Error. Para evitarlo, implementaría una validación temprana justo después de leer el rol: if config["orden_por"] not in ["nombre", "completitud"]: print("Criterio inválido") return`.

**¿Qué cambiarías si por defecto se pide que el informe debiera salir según uno de los roles?**
Cambiaría el valor por defecto de la función para que apunte a ese rol específico. Por ejemplo: def informar_columnas(rol="docente"):. Luego, eliminaría el bloque condicional que maneja el caso if rol is None:, ya que la función siempre ingresaría con un rol válido, procesándolo directamente bajo la lógica general.

**1) Agregá a la estructura manualmente un rol auditor que vea todas las columnas ordenadas por nombre descendente**: Lo único que tenemos que hacer es agregar al diccionario roles un nuevo rol con nombre auditor, el cual puede ver todas las columnas del informe ordenadas por nombre y de manera descendente (B).

**2) Agregá a la estructura manualmente una columna NIVEL_ED (int) con 88 % de completitud sin tocar los roles existentes que ya tenés en tu código. ¿En qué informes aparece NIVEL_ED y en cuáles no? ¿A qué se debe esa diferencia?**: En los únicos informes en los que aparece NIVEL_ED sería en el informe del auditor y en el informe general, es decir, cuando no se especifica un rol. En el resto no aparecería, ya que tanto el docente como el investigador tienen columnas específicas de interés, mientras que el analista tiene un filtro del 90% o más, haciendo que también quede afuera de este informe.

**3) Uso de   filter() o map(): si lo usaste explicá qué ventajas tiene en lugar de un for. Si no lo utilizaste reemplazá al menos un bucle por algunas de estas funcionalidades y explicá la mejora**: Al utilizarlo, se elimina el código repetitivo. Al no tener que inicializar variables temporales ni llamar a métodos como .append(), se reduce la cantidad de líneas y el riesgo de cometer errores de indentación o de sobrescribir variables por accidente.