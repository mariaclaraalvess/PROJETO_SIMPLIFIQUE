import { Calendar } from '@fullcalendar/core';
import dayGridPlugin from '@fullcalendar/daygrid';

const eventList = [];

// Função para renderizar os eventos na página
function renderEvents() {
    const eventListElement = document.getElementById('events');
    eventListElement.innerHTML = '';

    eventList.forEach((event, index) => {
        const eventItem = document.createElement('li');
        eventItem.innerHTML = `
            <span><strong>${event.title}</strong> - ${event.date}</span>
            <div class="event-actions">
                <button class="btn-view" onclick="viewEvent(${index})">Ver</button>
                <button class="btn-edit" onclick="editEvent(${index})">Editar</button>
                <button class="btn-delete" onclick="deleteEvent(${index})">Excluir</button>
            </div>
        `;
        eventListElement.appendChild(eventItem);
    });
}

// Função para adicionar evento
document.getElementById('event-form').addEventListener('submit', function(event) {
    event.preventDefault();

    const title = document.getElementById('event-title').value;
    const description = document.getElementById('event-description').value;
    const dateTime = document.getElementById('event-date-time').value;
    const location = document.getElementById('event-location').value;
    const eventType = document.getElementById('event-type').value;

    const newEvent = {
        title,
        description,
        date: new Date(dateTime).toLocaleString(),
        location,
        type: eventType,
    };

    eventList.push(newEvent);
    renderEvents();

    // Limpar o formulário após o envio
    document.getElementById('event-form').reset();
});

// Função para visualizar detalhes do evento
function viewEvent(index) {
    const event = eventList[index];
    alert(`
        Título: ${event.title}
        Descrição: ${event.description}
        Data e Hora: ${event.date}
        Local: ${event.location}
        Tipo de Evento: ${event.type}
    `);
}

// Função para editar evento
function editEvent(index) {
    const event = eventList[index];
    const title = prompt("Editar título:", event.title);
    const description = prompt("Editar descrição:", event.description);
    const dateTime = prompt("Editar data e hora:", event.date);
    const location = prompt("Editar local:", event.location);
    const eventType = prompt("Editar tipo de evento:", event.type);

    if (title) event.title = title;
    if (description) event.description = description;
    if (dateTime) event.date = new Date(dateTime).toLocaleString();
    if (location) event.location = location;
    if (eventType) event.type = eventType;

    renderEvents();
}

// Função para excluir evento
function deleteEvent(index) {
    if (confirm("Tem certeza que deseja excluir este evento?")) {
        eventList.splice(index, 1);
        renderEvents();
    }
}

// Inicializar a página
renderEvents();

//TENTANDO

document.addEventListener('DOMContentLoaded', function() {
    var calendarEl = document.getElementById('calendar');
  
    var calendar = new FullCalendar.Calendar(calendarEl, {
      locale: 'pt-br',  // Definindo o idioma para português
      headerToolbar: {
        left: 'prev,next today',  // Navegação de meses
        center: 'title',          // Título do calendário
        right: 'dayGridMonth,dayGridWeek,dayGridDay', // Visualização por mês, semana e dia
      },
      events: '/calendar/events/',  // URL onde os eventos são carregados (ajuste conforme necessário)
      editable: true,
      droppable: true,  // Permite arrastar e soltar eventos
      eventClick: function(info) {
        alert('Evento: ' + info.event.title);
      },
    });
  
    calendar.render();
  });
  