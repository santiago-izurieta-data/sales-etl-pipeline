# Sales ETL Pipeline

![Python](https://img.shields.io/badge/python-v3.9+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## 📋 Descripción

Pipeline ETL automatizado que procesa datos de ventas desde archivos CSV, realiza transformaciones y validaciones, y carga los resultados en una base de datos PostgreSQL para análisis posterior.

## 🎯 Objetivos

- Extraer datos de múltiples fuentes (CSV, APIs)
- Limpiar y transformar datos inconsistentes
- Validar calidad de datos
- Cargar datos en base de datos relacional
- Generar reportes automáticos

## 🛠️ Stack Tecnológico

- **Python 3.9+**
- **Pandas** - Manipulación de datos
- **SQLAlchemy** - ORM para base de datos
- **PostgreSQL** - Base de datos
- **pytest** - Testing
- **logging** - Monitoreo

## 📁 Estructura del Proyecto

sales-etl-pipeline/ ├── data/ # Datos raw y procesados ├── src/ # Código fuente ├── notebooks/ # Análisis exploratorio ├── tests/ # Tests unitarios └── config/ # Archivos de configuración

## 🚀 Instalación

### Prerrequisitos
- Python 3.9 o superior
- PostgreSQL instalado
- pip o conda

### Pasos

1. Clonar el repositorio:
```bash
git clone https://github.com/tu-usuario/sales-etl-pipeline.git
cd sales-etl-pipeline
```
2.	Crear entorno virtual:
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```
3.	Instalar dependencias:
```bash
pip install -r requirements.txt
```
4.	Configurar variables de entorno:
cp .env.example .env
# Editar .env con tus credenciales
## 💻 Uso
### Ejecutar pipeline completo:
python src/pipeline.py

### Ejecutar etapas individuales:
python src/extract.py
python src/transform.py
python src/load.py
## 🧪 Testing
pytest tests/
## 📊 Resultados
•	Procesamiento de +10,000 registros/minuto
•	Reducción de 30% en datos duplicados
•	Automatización completa del proceso diario
## 🔄 Pipeline Flow
CSV Files → Extract → Validate → Transform → Load → PostgreSQL
                                                   ↓
                                              Data Quality
                                                 Report
## 📈 Próximas Mejoras
•	[ ] Integración con Airflow para scheduling
•	[ ] Dockerización del proyecto
•	[ ] Dashboard de monitoreo
•	[ ] Integración con AWS S3

## 📝 Licencia
Este proyecto está bajo la Licencia MIT - ver LICENSE para detalles.

## 👤 Autor

Santiago Izurieta

LinkedIn: https://ec.linkedin.com/in/santiago-izurieta-844324125

Portfolio: https://my-data-engineer-folio.lovable.app/

## 🙏 Agradecimientos

- Comunidad de Python y Polars
- Documentación de Kaggle y Seaborn
- Google Colab para ejecución reproducible
