document.addEventListener("DOMContentLoaded", function () {
    setTimeout(() => appendBotMessage("👋 ¡Hola! Soy el Chatbot USC. Antes de comenzar, ¿cómo te llamas?"), 500);
});

function sendMessage() {
    let inputField = document.getElementById("user-input");
    let userMessage = inputField.value.trim();
    if (userMessage === "") return;

    appendUserMessage(userMessage);
    inputField.value = "";

    // Agregar "Escribiendo..." antes de responder
    let typingIndicator = document.createElement("div");
    typingIndicator.classList.add("bot-message");
    typingIndicator.textContent = "Escribiendo...";
    let chatBox = document.getElementById("chat-box");
    chatBox.appendChild(typingIndicator);
    chatBox.scrollTop = chatBox.scrollHeight;

    // Simular retraso antes de la respuesta del chatbot
    setTimeout(() => {
        chatBox.removeChild(typingIndicator); // Eliminar "Escribiendo..."

        fetch("/chat", {
            method: "POST",
            body: JSON.stringify({ message: userMessage, user_id: "default_user" }),
            headers: { "Content-Type": "application/json" }
        })
        .then(response => response.json())
        .then(data => appendBotMessage(formatLinks(data.response))) // Formatear los enlaces
        .catch(error => console.error("Error:", error));

    }, 1500); // Delay de 1.5 segundos antes de responder
}

function appendUserMessage(message) {
    let chatBox = document.getElementById("chat-box");
    let div = document.createElement("div");
    div.classList.add("user-message");
    div.textContent = message;
    chatBox.appendChild(div);
    chatBox.scrollTop = chatBox.scrollHeight;
}

function appendBotMessage(message) {
    let chatBox = document.getElementById("chat-box");
    let div = document.createElement("div");
    div.classList.add("bot-message");
    div.innerHTML = message.replace(/\n/g, "<br>"); // Agregar saltos de línea en respuestas
    chatBox.appendChild(div);
    chatBox.scrollTop = chatBox.scrollHeight;
}

// Detectar la tecla Enter para enviar mensajes
document.getElementById("user-input").addEventListener("keypress", function (event) {
    if (event.key === "Enter") {
        event.preventDefault(); // Evita saltos de línea en el input
        sendMessage();
    }
});

// Función para convertir enlaces en clickeables
function formatLinks(text) {
    let urlPattern = /(https?:\/\/[^\s]+)/g; // Detecta enlaces en el texto
    return text.replace(urlPattern, '<a href="$1" target="_blank">$1</a>'); // Hace los enlaces clickeables
}
