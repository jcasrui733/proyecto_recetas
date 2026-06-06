# Aplicación web de recetas con Django

Proyecto realizado por **Juan Antonio Castro Ruiz**.

## Descripción

Este proyecto consiste en el desarrollo de una aplicación web utilizando Django. La finalidad de la aplicación es permitir la gestión de recetas de cocina, mostrando un listado de recetas, su detalle, la creación de nuevas recetas y la participación de usuarios poniendo comentarios.

La idea del proyecto ha sido desarrollar una aplicación sencilla pero útil, en la que se pudieran aplicar varios de los conocimientos trabajados durante el curso. A lo largo de su desarrollo se han puesto en práctica conceptos como modelos, vistas, formularios, rutas, plantillas HTML, base de datos y autenticación de usuarios.

## Repositorio

Enlace al repositorio:  
[https://github.com/jcasrui733/proyecto_recetas](https://github.com/jcasrui733/proyecto_recetas)

## Instalación y ejecución

Para ejecutar el proyecto en local, lo primero que hay que hacer es crear un entorno virtual. Esto se realiza con el siguiente comando:

```bash
python -m venv venv
```

Después, para activarlo en PowerShell, se utiliza:

```bash
venv\Scripts\activate
```

Una vez activado el entorno virtual, el siguiente paso es instalar Django, ya que es el framework que se ha utilizado para desarrollar la aplicación. Para ello se usa el siguiente comando:

```bash
pip install django
```

Después de tener Django instalado, se deben realizar las migraciones para que la base de datos se cree correctamente a partir de los modelos del proyecto. Los comandos necesarios son los siguientes:

```bash
python manage.py makemigrations
python manage.py migrate
```

El comando `makemigrations` genera los archivos necesarios a partir de los cambios hechos en los modelos, y `migrate` aplica esos cambios a la base de datos para crear o actualizar sus tablas.

Para arrancar el servidor de desarrollo y ejecutar el proyecto en local, se utiliza este comando:

```bash
python manage.py runserver
```

Después de hacer esto, la aplicación se puede abrir en el navegador entrando en la dirección:

```bash
http://127.0.0.1:8000/
```

Si se quiere acceder al panel de administración de Django, se puede entrar en:
```
http://127.0.0.1:8000/admin/
```

En ese caso, también sería necesario crear previamente un superusuario con este comando:
```
python manage.py createsuperuser
```

La base de datos que se ha utilizado en este proyecto es SQLite, ya que es la que viene configurada por defecto en Django y es suficiente para una aplicación de este tipo en entorno local.

## Tecnologías utilizadas

Para el desarrollo del proyecto se ha utilizado Python como lenguaje principal y Django como framework web. Django ha sido la base del proyecto porque permite crear aplicaciones web de una forma bastante organizada, trabajando con modelos, vistas, plantillas, formularios y autenticación.

También se ha utilizado HTML para las plantillas. Como base de datos se ha utilizado SQLite, que es la base de datos que Django incorpora por defecto.

Además, se han utilizado herramientas propias del framework, como los modelos para definir la estructura de los datos, `ModelForm` para la creación de formularios, vistas genéricas basadas en clases, sistema de rutas con `urls.py` y autenticación de usuarios.

## Funcionalidades implementadas

Entre las funcionalidades implementadas, una de las principales es el listado de recetas, donde se muestran las recetas disponibles dentro de la aplicación. Desde este listado se puede acceder a la vista de detalle para consultar mejor la información de cada receta.

También se ha implementado la creación de nuevas recetas mediante formulario. Esta funcionalidad permite que los usuarios autenticados puedan añadir contenido a la aplicación.

Además, se han añadido opciones para editar y eliminar recetas, restringiendo estas acciones para que solo pueda hacerlas el autor de cada receta. Esto permite que exista un control básico sobre el contenido publicado.

Otra de las funcionalidades que se han incorporado es la posibilidad de añadir comentarios dentro de cada receta. De esta manera, los usuarios pueden participar e interactuar con el contenido publicado.

También se ha trabajado en la búsqueda y filtrado de recetas, permitiendo buscar por texto y por autor, y preparando también la relación con categorías para organizar mejor el contenido.

## Estructura del proyecto

La aplicación está organizada siguiendo la estructura típica de Django, basada en el patrón MVT, es decir, Modelo, Vista y Template. Esta organización permite separar la lógica del proyecto y facilita que cada archivo tenga una función concreta dentro de la aplicación.

En `models.py` se han definido los modelos principales del proyecto, que son categoría, receta y comentario.

En `forms.py` se han creado formularios basados en modelos para trabajar con las recetas y los comentarios.

En `views.py` se han utilizado vistas genéricas basadas en clases, como `ListView`, `DetailView`, `CreateView`, `UpdateView` y `DeleteView`, además de alguna vista basada en función para acciones concretas.

Las rutas se han configurado a través de `urls.py`, donde cada URL se asocia a una vista concreta.

En cuanto a la parte visual, se han utilizado varias plantillas HTML, entre ellas una plantilla base común y otras más concretas como la de listado de recetas, la de detalle y la de creación o edición.

## Uso de IA generativa

En este proyecto también se ha hecho uso de herramientas de IA generativa como apoyo durante el desarrollo. Se han utilizado principalmente para resolver dudas, entender errores concretos, revisar fragmentos de código.

Algunos ejemplos de prompts utilizados han sido los siguientes:

- “Explícame cómo se relacionan los modelos Categoria, Receta y Comentario en Django”.
- “Corrígeme este filtro en Django y dime por qué da error”.

## Mejoras futuras

Si se dispusiera de más tiempo, una de las principales mejoras sería trabajar más la parte visual de la aplicación, ya que el objetivo principal hasta ahora ha sido centrarse en que la funcionalidad estuviera bien implementada. También se podrían añadir imágenes para las recetas, un sistema de valoración, favoritos, paginación y filtros más avanzados.
