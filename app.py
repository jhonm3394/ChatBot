from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Diccionario para almacenar datos del usuario
user_data = {}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "").strip().lower()
    user_id = data.get("user_id", "default_user")

    # Si el usuario no tiene datos almacenados, se le pide el nombre
    if user_id not in user_data:
        user_data[user_id] = {}

    if "name" not in user_data[user_id]:
        user_data[user_id]["name"] = user_message.capitalize()
        return jsonify({"response": f"**Bienvenido, {user_data[user_id]['name']}** 👋\n\n"
                                    "Para continuar, elige una opción del menú escribiendo el número correspondiente.\n\n"
                                    f"{get_main_menu()}"})

    response = handle_user_message(user_message, user_id)
    return jsonify({"response": response})

def get_main_menu():
    """ Devuelve el menú principal con instrucciones claras """
    return (
        "**📌 Menú Principal:**\n\n"
        "Escribe el número de la opción que deseas seleccionar.\n\n"
        "1️⃣ Inscribir o Modificar Materias\n"
        "2️⃣ Solicitar Certificados\n"
        "3️⃣ Realizar Pagos Online\n"
        "4️⃣ Consultar Historial Académico\n"
        "5️⃣ Actualización de Datos Personales\n"
        "6️⃣ Consulta de Documentos\n"
        "7️⃣ Resumen del Semestre\n"
        "8️⃣ Solicitud de Grado\n"
        "9️⃣ Evaluación a Docentes\n"
        "🔟 Contacto\n\n"
        "🔹 98. Volver al menú\n"
        "🔹 99. Finalizar Chat"
    )

def handle_user_message(user_message, user_id):
    """ Procesa la entrada del usuario y devuelve la respuesta del chatbot """
    if user_message == "99":
        user_data.pop(user_id, None)  # Elimina los datos del usuario
        return "✅ **Chat finalizado. Recarga la página si deseas empezar de nuevo.**"

    responses = {
        "1": "📌 **Inscribir o Modificar Materias**\n\n"
             "- Ingresar al [Sistema Académico USC] https://sinu.usc.edu.co:8443/\n"
             "- Iniciar sesión con tu número de identificación y contraseña.\n"
             "- Acceder a 'Proceso de Matrícula Académica'.\n"
             "- Seleccionar el semestre y las materias.\n"
             "- Confirmar y guardar el comprobante.",
        "2": "📌 **Solicitar Certificados**\n\n"
             "- Acceder a [Sistema Académico USC] https://sinu.usc.edu.co:8443/\n"
             "- Ir a la sección 'Procesos de Certificados'.\n"
             "- Seleccionar el tipo de certificado.\n"
             "- Completar datos, enviar solicitud y realizar pago si aplica.",
        "3": "📌 **Realizar Pagos Online**\n\n"
             "- Ingresar a [Plataforma de Pagos] https://apps.usc.edu.co\n"
             "- Consultar recibos pendientes.\n"
             "- Descargar recibo o pagar en línea.\n"
             "- Guardar el comprobante como respaldo.",
        "4": "📌 **Consultar Historial Académico**\n\n"
             "- Ingresar al [Sistema Académico] https://sinu.usc.edu.co:8443/\n"
             "- Acceder a 'Proceso de Matrícula Académica'.\n"
             "- Hacer clic en 'Histórico de Notas'.\n"
             "- Ver las materias cursadas, calificaciones y créditos acumulados.",
        "5": "📌 **Actualización de Datos Personales**\n\n"
             "- Ingresar al [Sistema Académico USC] https://sinu.usc.edu.co:8443/\n"
             "- Iniciar sesión con tu número de identificación y contraseña.\n"
             "- Dirigirse a 'Actualización de Datos Personales'.\n"
             "- Modificar correo, dirección, teléfono, etc.\n"
             "- Aceptar la autorización de datos y guardar los cambios.",
        "6": "📌 **Consulta de Documentos**\n\n"
             "- Ingresar al [Sistema Académico] https://sinu.usc.edu.co:8443/\n"
             "- Acceder con tu usuario y contraseña.\n"
             "- Seleccionar la opción 'Consulta de Documentos'.\n"
             "- Elegir el programa académico y visualizar la información en pantalla.",
        "7": "📌 **Resumen del Semestre**\n\n"
             "- Acceder al [Sistema Académico] https://sinu.usc.edu.co:8443/\n"
             "- Iniciar sesión con tu número de identificación y contraseña.\n"
             "- Ir a la opción 'Resumen de Periodo'.\n"
             "- Elegir el programa académico y visualizar la información en pantalla.",
        "8": "📌 **Solicitud de Grado**\n\n"
             "- Verificar que cumplas con todos los requisitos académicos.\n"
             "- Ingresar a la [Plataforma de Grados] https://www.usc.edu.co/grados \n"
             "- Descargar y completar el formulario de solicitud.\n"
             "- Realizar el pago correspondiente.\n"
             "- Enviar el formulario y documentos requeridos al correo de la Secretaría Académica.\n"
             "- Esperar confirmación de la fecha de la ceremonia de grado.",
        "9": "📌 **Evaluación a Docentes**\n\n"
             "- Acceder al [Sistema Académico] https://sinu.usc.edu.co:8443/\n"
             "- Iniciar sesión con tus credenciales.\n"
             "- Seleccionar la opción 'Encuesta de Evaluación Docente'.\n"
             "- Responder todas las preguntas con base en tu experiencia.\n"
             "- Enviar la evaluación y verificar que haya quedado registrada correctamente.",
        "10": "📌 **Contacto**\n\n"
             "Si necesitas más información sobre las carreras de pregrado, visita el siguiente enlace:\n\n"
             "🔗 [Página Oficial de Pregrados] https://www.usc.edu.co/pregrados\n\n"
             "En la página encontrarás información sobre:\n"
             "- Facultad a la que pertenece.\n"
             "- Identificación del programa.\n"
             "- Total de créditos.\n"
             "- Título otorgado.\n"
             "- Metodología y duración.\n"
             "- Plan de estudios.\n"
             "- Datos de contacto: correo, teléfono y oficina.",
        "98": get_main_menu()
    }
    
    return responses.get(user_message, "❌ Opción no válida. Escribe el número de la opción que deseas seleccionar.")

if __name__ == "__main__":
    app.run(debug=True)
