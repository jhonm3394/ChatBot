from flask import Flask, request, jsonify

app = Flask(__name__)

# Variables para almacenar el nombre del usuario y el estado de la conversación
user_name = None
in_conversation = False

# Función para validar opciones numéricas
def validar_opcion(opcion):
    opciones_validas = ['1', '2', '3', '4', '5', 'volver', 'finalizar']
    return opcion in opciones_validas

@app.route('/chat', methods=['POST'])
def chat():
    global user_name, in_conversation
    user_message = request.json.get('message').lower().strip()

    # Si el nombre del usuario no está definido, pedirlo
    if user_name is None:
        user_name = user_message
        in_conversation = True
        return jsonify({
            'response': f"¡Hola, {user_name}! Soy el asistente virtual. ¿Cómo te puedo ayudar hoy? Aquí están tus opciones:\n"
                        "1. Como inscribir o modificar materias\n"
                        "2. Como solicitar certificados\n"
                        "3. Como realizar pagos online\n"
                        "4. Como consultar historial académico\n"
                        "5. Ayuda con otras consultas"
        })

    # Si estamos en la conversación, procesar las opciones del menú
    if in_conversation:
        # Opción seleccionada por el usuario
        if user_message == '1':
            return jsonify({
                'response': "Perfecto, te guiaré en el proceso para inscribir o modificar materias. Aquí están los pasos:\n"
                            "1. Ingresa al sistema académico de la universidad en este enlace: [https://sinu.usc.edu.co:8443/].\n"
                            "2. Inicia sesión con tu número de identificación y contraseña.\n"
                            "3. Ve a la sección 'Proceso de Matrícula Académica'.\n"
                            "4. Selecciona tu 'Semestre' y las materias que deseas agregar o modificar.\n"
                            "5. Confirma tu matrícula.\n"
                            "¿Te gustaría hacer algo más? Escribe: 1 para volver al menú o 2 para finalizar."
            })
        elif user_message == '2':
            return jsonify({
                'response': "Para solicitar un certificado, sigue estos pasos:\n"
                            "1. Ingresa al Sistema de Información Académico: [https://sinu.usc.edu.co:8443/].\n"
                            "2. Dirígete a la sección 'Procesos de Certificados'.\n"
                            "3. Selecciona el tipo de certificado y llena los datos.\n"
                            "4. Envía la solicitud y paga el valor del certificado.\n"
                            "¿Te gustaría hacer algo más? Escribe: 1 para volver al menú o 2 para finalizar."
            })
        elif user_message == '3':
            return jsonify({
                'response': "Sigue estos pasos para realizar pagos online:\n"
                            "1. Ingresa al sistema de pagos de la universidad: [https://apps.usc.edu.co/].\n"
                            "2. Ingresa tu número de documento y consulta tus recibos pendientes.\n"
                            "3. Descarga los recibos o realiza el pago online.\n"
                            "4. Guarda el comprobante de pago.\n"
                            "¿Te gustaría hacer algo más? Escribe: 1 para volver al menú o 2 para finalizar."
            })
        elif user_message == '4':
            return jsonify({
                'response': "Para consultar tu historial académico, sigue estos pasos:\n"
                            "1. Ingresa al Sistema de Información Académico: [https://sinu.usc.edu.co:8443/].\n"
                            "2. Ve a la sección 'Proceso de Matrícula Académica' y selecciona 'Histórico de Notas'.\n"
                            "3. Verás tus materias cursadas, notas y créditos.\n"
                            "¿Te gustaría hacer algo más? Escribe: 1 para volver al menú o 2 para finalizar."
            })
        elif user_message == '5':
            return jsonify({
                'response': "Si tienes alguna otra consulta, por favor indícalo y estaré encantado de ayudarte. ¿Te gustaría hacer algo más? Escribe: 1 para volver al menú o 2 para finalizar."
            })

        # Opciones de volver al menú o finalizar la conversación
        elif user_message == 'volver':
            return jsonify({
                'response': "Aquí están tus opciones:\n"
                            "1. Como inscribir o modificar materias\n"
                            "2. Como solicitar certificados\n"
                            "3. Como realizar pagos online\n"
                            "4. Como consultar historial académico\n"
                            "5. Ayuda con otras consultas"
            })
        
        elif user_message == 'finalizar':
            in_conversation = False
            return jsonify({
                'response': f"¡Gracias por utilizar el chatbot, {user_name}! ¡Hasta pronto! 😊"
            })

    # Respuesta predeterminada si la opción no es válida
    return jsonify({'response': "Lo siento, no entendí eso. Por favor, selecciona una opción válida o escribe 'volver' para regresar al menú."})

if __name__ == '__main__':
    app.run(debug=True)