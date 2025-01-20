# Chatbot-USC

Repositorio oficial para el desarrollo del Chatbot Académico de la Universidad USC. Este chatbot está diseñado para asistir a los estudiantes en la gestión de trámites académicos y administrativos, ofreciendo orientación paso a paso de manera interactiva.

## **Descripción del Proyecto**
El chatbot guía a los estudiantes a través de diversas opciones, tales como:

1. Inscripción o modificación de materias.
2. Solicitud de certificados.
3. Realización de pagos online.
4. Consulta del historial académico.
5. Ayuda con otras consultas generales.

El sistema está desarrollado en **Python** utilizando el framework **Flask** y permite interactuar con los usuarios mediante mensajes iterativos basados en un menú.

## **Características**
- Interfaz de conversación simple y efectiva.
- Respuestas dinámicas basadas en las selecciones del usuario.
- Submenús para volver al menú principal o finalizar la conversación.
- Potencial para integraciones futuras con bases de datos y otros servicios avanzados.

## **Requisitos Previos**
Antes de ejecutar este proyecto, asegúrate de tener instalado:

- Python 3.8 o superior
- pip (el gestor de paquetes de Python)

## **Instalación y Configuración**
Sigue estos pasos para ejecutar el proyecto localmente:

1. **Crear un entorno virtual:**
   ```bash
   python -m venv venv
   ```

2. **Activar el entorno virtual:**
   - En Windows:
     ```bash
     venv\Scripts\activate
     ```
   - En macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

3. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Ejecutar la aplicación:**
   ```bash
   python app.py
   ```

5. **Probar el chatbot:**
   - Accede al chatbot en tu navegador: `http://127.0.0.1:5000`
   - Usa Postman o una herramienta similar para simular las interacciones.

## **Estructura del Proyecto**
```plaintext
Chatbot-USC/
├── app.py                # Código principal del chatbot
├── requirements.txt      # Dependencias necesarias para el proyecto
├── README.md             # Documentación del repositorio
└── venv/                 # Entorno virtual (no incluido en el repositorio)
```

## **Uso del Chatbot**
1. El chatbot se inicia con un saludo e identifica al usuario si se proporciona un nombre.
2. Presenta un menú con opciones numeradas:
   - 1. Como inscribir o modificar materias
   - 2. Como solicitar certificados
   - 3. Como realizar pagos online
   - 4. Como consultar de historial académico
   - 5. Ayuda con otras consultas
3. El usuario responde con el número correspondiente para recibir las instrucciones detalladas.
4. Al finalizar cada interacción, el chatbot ofrece las opciones de volver al menú principal o finalizar la conversación.
