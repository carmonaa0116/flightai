# FlightAI ✈️

**FlightAI** es un chatbot de ejemplo que demuestra cómo integrar llamadas a funciones (function calling) con el SDK de Gemini (Google Generative AI). El bot responde preguntas sobre precios de billetes a distintas ciudades usando una función interna `get_ticket_price`.

---

## ✅ Qué contiene este repositorio

- Código del chatbot: `main.py` (loop interactivo con Gemini)
- Lógica de llamadas a herramientas: `tool_schema.py` y `handler.py`
- Datos de ejemplo de precios: `tools.py`
- Tests simples por módulo: `test_*.py`
- Archivo de dependencias: `requirements.txt`
- `.gitignore` ya incluido (configurado para Python/VSCode/venv)

---

## 🔧 Requisitos

- Python 3.10+ recomendado
- Acceso a la API de Gemini (clave en `GEMINI_API_KEY`)
- Dependencias del proyecto:

```bash
pip install -r requirements.txt
```

---

## 🛠️ Instalación y configuración rápida

1. Clona el repositorio:

```bash
git clone https://github.com/tuusuario/flightai.git
cd flightai
```

2. Crea y activa un entorno virtual:

Windows (PowerShell):
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Linux / macOS:
```bash
python -m venv .venv
source .venv/bin/activate
```

3. Instala dependencias:

```bash
pip install -r requirements.txt
```

4. Crea un archivo `.env` en la raíz con tu API key (no subirlo a GitHub):

```
GEMINI_API_KEY=tu_api_key_aqui
```

> ⚠️ Nunca subas tu `.env` o claves a GitHub. `.gitignore` ya excluye `.env`.

---

## ▶️ Uso

Ejecuta el chatbot interactivo:

```bash
python main.py
```

- Escribe preguntas en español (por ejemplo: "¿Cuánto cuesta un vuelo a París?")
- Escribe `salir` para terminar la sesión

El flujo es:
- El prompt del sistema guía a Gemini (ver `SYSTEM_PROMPT` en `main.py`)
- Gemini puede decidir llamar a la función `get_ticket_price`
- `handler.py` ejecuta la función (usa `tools.get_ticket_price`) y devuelve el resultado

---

## 🧪 Cómo ejecutar los tests

Los tests están diseñados como scripts ejecutables. Puedes ejecutarlos individualmente:

```bash
python test_tool_schema.py
python test_tools.py
python test_handler.py
python test_main.py
```

Si prefieres usar pytest, instala `pytest` y ejecuta:

```bash
pip install pytest
pytest
```

> Nota: Los tests son simples y comprueban importaciones, estructura del schema y comportamiento básico de `get_ticket_price`.

---

## 💡 Desarrollo y contribuciones

- Añade nuevas ciudades o mejora la base de datos de precios en `tools.py`.
- Extiende `tool_schema.py` si quieres exponer más funciones a Gemini.
- Agrega tests para nuevos comportamientos.

Si quieres contribuir:
- Haz fork, crea una rama (`feature/mi-cambio`), añade tests y abre un pull request.

---

## 🔐 Consideraciones de seguridad

- Mantén la clave de Gemini en variables de entorno (`.env`) y **no** la subas al repo.
- Revisa límites y facturación de la API de Gemini antes de usarla en producción.

---

## 📄 Licencia

Este repositorio no incluye un archivo `LICENSE`. Añade una licencia (por ejemplo MIT) si quieres permitir contribuciones externas y uso libre.

---

Si quieres, puedo además:
- Añadir un archivo `LICENSE` (MIT)
- Configurar un `Makefile` o `tasks.json` para comandos comunes
- Añadir un ejemplo de `workflow` de GitHub Actions para ejecutar tests

¿Qué prefieres que agregue ahora? 🚀
