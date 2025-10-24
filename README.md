# API REST Test

CRUD básico con FastAPI.

## Requerimientos
- Python 3.7 o superior
- pip (gestor de paquetes de Python)

## Instalación paso a paso

### 1. Crear entorno virtual
```bash
python -m venv venv
```

### 2. Activar entorno virtual

**macOS/Linux:**
```bash
source venv/bin/activate
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

## Ejecutar
```bash
uvicorn main:app --reload
```

## Documentación
Abre tu navegador en: http://localhost:8000/docs

## Endpoints
- GET `/items` - Obtener todos los items
- GET `/items/{id}` - Obtener item por ID
- POST `/items` - Crear item
- PUT `/items/{id}` - Actualizar item
- DELETE `/items/{id}` - Eliminar item

## Tests
```bash
pytest test_main.py
```

## Ejemplo de uso
```json
{
  "id": 1,
  "name": "Laptop",
  "price": 2500.0,
  "available": true
}
```