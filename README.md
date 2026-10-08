# Red Social

Proyecto final de Python que implementa una pequeña red social inspirada en Twitter/X.

El proyecto está desarrollado utilizando programación orientada a objetos, clases, herencia, clases abstractas, propiedades, métodos mágicos, lectura de archivos JSON y tests automatizados con `pytest`.

## Funcionalidades

El proyecto permite:

- Crear y registrar usuarios.
- Seguir a otros usuarios y comprobar los seguimientos.
- Crear tweets, respuestas y retweets.
- Dar "Me gusta" a las publicaciones.
- Extraer hashtags de las publicaciones.
- Mostrar el timeline de un usuario:
  - Solo incluye publicaciones de los usuarios a los que sigue.
  - Las publicaciones aparecen de más reciente a más antigua.
- Calcular las tendencias de hashtags.
- Cargar usuarios y seguimientos desde un archivo JSON.
- Utilizar métodos mágicos para trabajar con la red social:
  - `len(red)`
  - `for usuario in red`
  - `alias in red`
  - `red[alias]`

## Estructura del proyecto

```text
red_social/
├── pyproject.toml
├── main.py
├── datos/
│   └── usuarios.json
├── red_social/
│   ├── usuario.py
│   ├── publicacion.py
│   └── red.py
└── tests/
    ├── conftest.py
    ├── test_usuario.py
    ├── test_publicacion.py
    └── test_red.py
```

## Clases principales

### `Usuario`

Representa a un usuario de la red social.

Sus principales funcionalidades son:

- Nombre y alias.
- Seguimiento de otros usuarios.
- Comprobación de seguimientos.
- Número de usuarios seguidos.
- Conversión a diccionario.
- Creación de usuarios desde un diccionario.
- Comparación de usuarios mediante su alias.

### `Publicacion`

Es la clase base abstracta para las publicaciones.

Se encarga de:

- Validar el texto de la publicación.
- Limitar el contenido a 280 caracteres.
- Gestionar los "Me gusta".
- Extraer hashtags.

De esta clase heredan:

- `Tweet`
- `Respuesta`
- `Retweet`

### `RedSocial`

Gestiona los usuarios y las publicaciones de la red.

Permite:

- Añadir usuarios.
- Registrar nuevos usuarios.
- Publicar contenido.
- Consultar timelines.
- Obtener tendencias.
- Cargar una red social desde JSON.
- Recorrer los usuarios ordenados por alias.

## Datos iniciales

Los usuarios y sus seguimientos se cargan desde:

```text
datos/usuarios.json
```

El programa utiliza este archivo para construir la red social inicial.

## Tests

El proyecto utiliza `pytest` para comprobar el funcionamiento de las diferentes clases y métodos.

Para ejecutar todos los tests:

```bash
uv run pytest -v
```

Los tests cubren:

- `Usuario`
- `Publicacion`
- `Tweet`
- `Respuesta`
- `Retweet`
- `RedSocial`
- Seguimientos
- Timelines
- Tendencias
- Métodos mágicos
- Carga desde JSON

## Comprobación del código

Para comprobar el estilo y detectar errores con Ruff:

```bash
uv run ruff check .
```

Para ejecutar el programa:

```bash
uv run python main.py
```

## Ejemplo de funcionamiento

Al ejecutar el programa se muestra información sobre los usuarios, publicaciones, hashtags, timeline y tendencias.

```text
Usuarios registrados: 3
  Ana (@ana) sigue a 0
  Luis (@luis) sigue a 1
  Marta (@marta) sigue a 2

Nuevo usuario: Pablo (@pablo)
¿Está @pablo en la red? True
¿Sigue @pablo a @ana? True
¿Sigue @ana a @pablo? False

Publicaciones:
  @ana: Hola a todos #python #pytest  ♥ 2
  @luis ↩ @ana: ¡Bienvenida! #Python  ♥ 0
  @marta 🔁 @ana: Hola a todos #python #pytest  ♥ 0
  @pablo: Mi primer tweet #hola  ♥ 0

Hashtags del tweet de Ana (@ana): ['#python', '#pytest']

Timeline de Marta (@marta):
  @luis ↩ @ana: ¡Bienvenida! #Python  ♥ 0
  @ana: Hola a todos #python #pytest  ♥ 2

Tendencias:
  #python (3)
  #pytest (2)
```

## Tecnologías utilizadas

- Python
- `pytest`
- `pytest-mock`
- `ruff`
- `uv`
- JSON
- Programación orientada a objetos

## Objetivo del proyecto

El objetivo del proyecto es aplicar los conceptos aprendidos de Python mediante la creación de una pequeña aplicación estructurada en diferentes clases y módulos, acompañada de tests automatizados.