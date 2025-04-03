# Chatbot-USC

Repositorio oficial para el desarrollo del Chatbot Académico de la Universidad USC. Este chatbot está diseñado para asistir a los estudiantes en la gestión de trámites académicos y administrativos, ofreciendo orientación paso a paso de manera interactiva.

## **Descripción del Proyecto**
El chatbot ayuda a los estudiantes con diversas gestiones, como:

✅ Inscripción o modificación de materias.
✅ Solicitud de certificados.
✅ Realización de pagos online.
✅ Consulta del historial académico.
✅ Asistencia en otras consultas generales.

El sistema está desarrollado en Python utilizando el framework Flask y cuenta con una interfaz moderna inspirada en WhatsApp, lo que permite una interacción fluida y natural.

## **Características Principales**
🔹 Interfaz de conversación tipo chat con burbujas de mensajes.
🔹 Mensajes dinámicos, con animación de "escribiendo..." antes de cada respuesta.
🔹 Enlaces clickeables a plataformas académicas y de pagos.
🔹 Fondo de pantalla personalizable (incluyendo soporte para video).
🔹 Diseño responsivo y accesible.
🔹 Submenús para volver al menú principal o finalizar la conversación.

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
├── templates/
│   ├── index.html        # Página principal con la interfaz del chat
├── static/
│   ├── styles.css        # Estilos personalizados
│   ├── script.js         # Lógica del frontend
│   ├── chatbot-icon.png  # Icono del chatbot en el encabezado
│   ├── chat-background.mp4 # Video de fondo (opcional)
├── requirements.txt      # Dependencias necesarias para el proyecto
├── README.md             # Documentación del repositorio
└── venv/                 # Entorno virtual (no incluido en el repositorio)

```
## **Personalizacion**
🔹 Cambiar el fondo:
Si deseas un video de fondo, reemplaza el archivo en:
📁 static/chat-background.mp4

Si prefieres una imagen de fondo, edita el archivo styles.css y ajusta:
.chat-box {
    background-image: url('static/chat-background.jpg');
    background-size: cover;
}

🔹 Modificar los colores y estilos:
Edita los estilos en 📁 static/styles.css

🔹 Actualizar el icono del chatbot:
Reemplaza 📁 static/chatbot-icon.png

## **Enlaces Importantes**
🔹 sistema academico: https://sinu.usc.edu.co:8443/
🔹 plataforma de pagos: https://apps.usc.edu.co/
🔹 plataforma de grados: https://www.usc.edu.co/grados/
🔹 pagina de pregrados: https://www.usc.edu.co/pregrados/

## **Uso del Chatbot**
1️⃣ Inicio de la Conversación
El chatbot inicia con un mensaje de bienvenida y solicita el nombre del usuario para personalizar la interacción.

2️⃣ Selección de Opciones
Luego de identificarse, el usuario accede al menú principal, donde puede elegir entre las siguientes opciones:

1️⃣ Cómo inscribir o modificar materias
2️⃣ Cómo solicitar certificados
3️⃣ Cómo realizar pagos online
4️⃣ Cómo consultar el historial académico
5️⃣ Ayuda con otras consultas
6️⃣ Cómo recuperar contraseña del sistema académico
7️⃣ Información sobre grados y proceso de grado
8️⃣ Cómo descargar recibos de pago
9️⃣ Fechas importantes del calendario académico
🔟 Cómo contactar con soporte o atención al estudiante

3️⃣ Interacción con el Usuario
El usuario selecciona una opción respondiendo con el número correspondiente.
Dependiendo de la opción elegida, el chatbot proporciona una guía paso a paso con información detallada y enlaces directos a las plataformas oficiales cuando sea necesario.

4️⃣ Cierre de la Conversación

Al finalizar cada interacción, el chatbot permite al usuario elegir entre dos opciones:
🔄 Volver al menú principal → Escribiendo "98", el usuario regresa al menú principal para seleccionar otra opción.
❌ Finalizar la conversación → Escribiendo "99", el usuario cierra el chat si ya no necesita más ayuda.

5️⃣ Fluidez en la Conversación
Se ha implementado un indicador de "escribiendo..." antes de cada respuesta para simular una conversación más natural.
Los enlaces proporcionados en las respuestas son clicleables para facilitar el acceso a las plataformas correspondientes.

