$(document).ready(function() {
    $('#calendar').fullCalendar({
      locale: 'pt-br',  // Define o idioma para português brasileiro
      events: '/calendar/events/',
      editable: true,
      droppable: true,
      dayClick: function(date, jsEvent, view) {
        alert('Você clicou no dia: ' + date.format());
      }
    });
  });
  