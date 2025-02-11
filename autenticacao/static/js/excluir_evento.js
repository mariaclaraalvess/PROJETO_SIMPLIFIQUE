document.addEventListener("DOMContentLoaded", function() {
    const buttons = document.querySelectorAll('.btn-excluir');
    
    buttons.forEach(button => {
        button.addEventListener('click', function(event) {
            event.preventDefault(); // Impede o link de navegar imediatamente
            const eventoId = button.getAttribute('data-id'); // ID do evento
            
            // Exibe a caixa de confirmação
            if (confirm("Tem certeza que deseja excluir este evento?")) {
                // Envia a requisição POST para excluir o evento
                fetch(`/excluir_evento/${eventoId}/`, {
                    method: 'POST',
                    headers: {
                        'X-CSRFToken': getCookie('csrftoken'),  // Incluindo o CSRF Token
                    }
                })
                .then(response => {
                    if (response.ok) {
                        // Remove o evento da lista
                        document.querySelector(`#evento-${eventoId}`).remove();
                    } else {
                        alert("Erro ao excluir evento.");
                    }
                })
                .catch(error => {
                    console.error('Erro:', error);
                    alert('Erro ao excluir evento.');
                });
            }
        });
    });

    // Função para obter o CSRF Token
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});
