# Web Scraping Project

Este proyecto realiza web scraping de frases de la página https://quotes.toscrape.com/ y almacena la información en una base de datos MySQL. Incluye funcionalidades para la extracción de datos, almacenamiento en base de datos y actualización automática.

## Características

- Extrae frases, autores, tags y la información "about" de los autores.
- Almacena los datos en una base de datos MySQL.
- Utiliza pandas para el manejo eficiente de los datos.
- Proporciona funcionalidades para consultar la base de datos.
- Incluye un script para actualización automática de la base de datos.

## Instalación

1. Clonar el repositorio:

2. Crear un entorno virtual (opcional pero recomendado): python -m venv venv
source venv/bin/activate  # En Windows usa venv\Scripts\activate

3. Instalar las dependencias: pip install -r requirements.txt

4. Configurar la base de datos MySQL:
- Crear una base de datos llamada `quotes_db`
- Actualizar las credenciales de la base de datos en `src/database.py`

## Uso

Para ejecutar el script principal de scraping: python src/main.py
Para iniciar la actualización automática: python src/auto_update.py

## Estructura del Proyecto

web-scraping-project/
│
├── src/
│   ├── scraper.py
│   ├── database.py
│   ├── main.py
│   └── auto_update.py
│
├── tests/
│   └── test_scraper.py
│
├── logs/
│   ├── scraper.log
│   └── auto_update.log
│
├── requirements.txt
├── Dockerfile
├── .gitignore
└── README.md

## Tecnologías Utilizadas

- Python
- BeautifulSoup
- Requests
- pandas
- MySQL
- SQLAlchemy
- schedule (para actualizaciones automáticas)

## Funcionalidades de la Base de Datos

La clase `Database` en `database.py` proporciona las siguientes funcionalidades:

- Inserción de citas con su texto, autor, información "about" y tags.
- Recuperación de todas las citas.
- Búsqueda de citas por ID.
- Búsqueda de citas por autor.
- Búsqueda de citas por tag.

## Actualización Automática

El proyecto incluye un script (`src/auto_update.py`) para actualizar automáticamente la base de datos con nuevos datos a intervalos regulares.

Para ejecutar la actualización automática: python src/auto_update.py
Por defecto, este script actualizará la base de datos cada 24 horas. Puedes modificar el intervalo en el archivo `src/auto_update.py`.

## Tests

Para ejecutar los tests unitarios: pytest

## Docker

El proyecto incluye un Dockerfile para containerizar la aplicación. Para construir y ejecutar el contenedor:
docker build -t web-scraping-project .
docker run web-scraping-project

## Notas

- Asegúrate de tener un servidor MySQL en ejecución y actualiza las credenciales en `src/database.py` antes de ejecutar el script.
- El proceso de scraping puede llevar algún tiempo debido a que se obtiene información adicional de la página "about" de cada autor.
- Para la actualización automática, asegúrate de que tu servidor y conexión a internet sean estables si planeas ejecutar este script por largos períodos de tiempo.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue para discutir los cambios propuestos antes de realizar un pull request.

## Licencia

[MIT](https://choosealicense.com/licenses/mit/)

## Contacto

[Freddy] - [jmc.fredd1y@gmail.com]

Enlace del proyecto: [https://github.com/AI-School-F5-P3/WebScraping_freddy](https://github.com/AI-School-F5-P3/WebScraping_freddy)