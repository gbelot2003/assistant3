// Conexión con el servidor WebSocket
var socket = io();

// Al hacer clic en el botón enviar en el chat
document.getElementById('send-btn').addEventListener('click', function() {
    sendMessage();
});

// Enviar mensaje con la tecla Enter en el chat
document.getElementById('message').addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
        sendMessage();
    }
});

// Función para enviar el mensaje en el chat
function sendMessage() {
    let message = document.getElementById('message').value;
    if (message) {
        socket.send(message);  // Enviar el mensaje al servidor
        addMessageToChat(message, 'user');  // Añadir el mensaje del usuario al chat
        document.getElementById('message').value = '';  // Limpiar el campo
    }
}

// Escuchar mensajes desde el servidor en el chat
socket.on('message', function(msg) {
    addMessageToChat(msg, 'other');  // Añadir el mensaje de otros al chat
});

// Función para añadir un mensaje al chat
function addMessageToChat(message, sender) {
    let chatBox = document.getElementById('chat-box');
    let messageElement = document.createElement('div');
    messageElement.classList.add('message', sender);  // Añadir clase 'user' o 'other'
    messageElement.textContent = message;
    chatBox.appendChild(messageElement);
    chatBox.scrollTop = chatBox.scrollHeight;  // Scroll automático
}