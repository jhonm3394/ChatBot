from flask import Flask, request, jsonify

app = Flask(__name__)

# Variables para almacenar el nombre del usuario y el estado de la conversación
user_name = None
in_conversation = False

# Función para detectar un saludo
def es_saludo(mensaje):
    saludos = ["hola", "buenos días", "buenas tardes", "buenas noches", "hey"]
    return any(saludo in mensaje for saludo in saludos)

@app.route('/chat', methods=['POST'])
def chat():
    global user_name, in_conversation
    user_message = request.json.get('message').lower().strip()

    # Si el usuario saluda, pedir el nombre
    if user_name is None:
        if es_saludo(user_message):
            return jsonify({'response': "Soy el asistente virtual. ¿Cuál es tu nombre?"})
        else:
            user_name = user_message
            in_conversation = True
            return jsonify({
                'response': f"¡Hola, {user_name}! Soy el asistente virtual. ¿Cómo te puedo ayudar hoy?\n"
                            "1. Inscribir o modificar materias\n"
                            "2. Solicitar certificados\n"
                            "3. Realizar pagos online\n"
                            "4. Consultar historial académico\n"
                            "5. Otras consultas\n"
                            "98. Volver al menú principal\n"
                            "99. Finalizar conversación\n"
                            "Escribe el número de la opción que deseas."
            })

    # Si estamos en la conversación, procesar las opciones del menú
    if in_conversation:
        if user_message == '1':
            return jsonify({
                'response': "Para inscribir o modificar materias, sigue estos pasos:\n"
                            "1. Ingresa al sistema académico: [https://sinu.usc.edu.co:8443/].\n"
                            "2. Inicia sesión con tu número de identificación y contraseña.\n"
                            "3. Ve a 'Proceso de Matrícula Académica'.\n"
                            "4. Selecciona tu semestre y materias.\n"
                            "5. Confirma tu matrícula.\n"
                            "98. Volver al menú principal\n"
                            "99. Finalizar conversación"
            })
        elif user_message == '2':
            return jsonify({
                'response': "Para solicitar un certificado:\n"
                            "1. Ingresa al sistema académico: [https://sinu.usc.edu.co:8443/].\n"
                            "2. Ve a 'Procesos de Certificados'.\n"
                            "3. Selecciona el tipo de certificado y llena los datos.\n"
                            "4. Envía la solicitud y realiza el pago.\n"
                            "98. Volver al menú principal\n"
                            "99. Finalizar conversación"
            })
        elif user_message == '3':
            return jsonify({
                'response': "Para realizar pagos online:\n"
                            "1. Ingresa al sistema de pagos: [https://apps.usc.edu.co/].\n"
                            "2. Ingresa tu número de documento y consulta tus recibos.\n"
                            "3. Descarga los recibos o realiza el pago online.\n"
                            "98. Volver al menú principal\n"
                            "99. Finalizar conversación"
            })
        elif user_message == '4':
            return jsonify({
                'response': "Para consultar tu historial académico:\n"
                            "1. Ingresa al sistema académico: [https://sinu.usc.edu.co:8443/].\n"
                            "2. Ve a 'Histórico de Notas'.\n"
                            "3. Verás tus materias cursadas, notas y créditos.\n"
                            "98. Volver al menú principal\n"
                            "99. Finalizar conversación"
            })
        elif user_message == '5':
            return jsonify({
                'response': "Si tienes otra consulta, por favor indícalo.\n"
                            "98. Volver al menú principal\n"
                            "99. Finalizar conversación"
            })
        elif user_message == '98':  # Volver al menú principal
            return jsonify({
                'response': f"De acuerdo, {user_name}. ¿Cómo te puedo ayudar hoy?\n"
                            "1. Inscribir o modificar materias\n"
                            "2. Solicitar certificados\n"
                            "3. Realizar pagos online\n"
                            "4. Consultar historial académico\n"
                            "5. Otras consultas\n"
                            "98. Volver al menú principal\n"
                            "99. Finalizar conversación"
            })
        elif user_message == '99':  # Finalizar conversación
            in_conversation = False
            return jsonify({'response': f"¡Gracias por utilizar el chatbot, {user_name}! ¡Hasta pronto! 😊"})

    # Si la opción no es válida
    return jsonify({
    'response': "Opción no válida. Elige una de las siguientes:\n"
                "1. Inscribir/modificar materias\n"
                "2. Solicitar certificados\n"
                "3. Realizar pagos online\n"
                "4. Consultar historial académico\n"
                "5. Otras consultas\n"
                "98. Volver\n"
                "99. Finalizar"
})

if __name__ == '__main__':
    app.run(debug=True)
