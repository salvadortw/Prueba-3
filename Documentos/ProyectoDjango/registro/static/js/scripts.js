document.addEventListener('DOMContentLoaded', function() {
    // Función para manejar mensajes de éxito y error
    const messages = document.getElementById('messages');
    if (messages) {
        setTimeout(() => {
            messages.style.display = 'none';
        }, 5000);
    }
});
