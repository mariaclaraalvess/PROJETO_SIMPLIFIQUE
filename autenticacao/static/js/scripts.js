document.addEventListener("DOMContentLoaded", function () {
  const mesAnoInput = document.getElementById("mesAno");
  const diasContainer = document.getElementById("dias");

  function criarCalendario(ano, mes) {
      diasContainer.innerHTML = "";

      const primeiroDia = new Date(ano, mes, 1).getDay();
      const ultimoDia = new Date(ano, mes + 1, 0).getDate();
      const diasSemana = ["Dom", "Seg", "Ter", "Qua", "Qui", "Sex", "Sáb"];

      let tabela = "<table><tr>";

      diasSemana.forEach(dia => {
          tabela += `<th>${dia}</th>`;
      });

      tabela += "</tr><tr>";

      for (let i = 0; i < primeiroDia; i++) {
          tabela += "<td></td>";
      }

      for (let dia = 1; dia <= ultimoDia; dia++) {
          tabela += `<td>${dia}</td>`;
          if ((dia + primeiroDia) % 7 === 0) {
              tabela += "</tr><tr>";
          }
      }

      tabela += "</tr></table>";
      diasContainer.innerHTML = tabela;
  }

  mesAnoInput.addEventListener("change", function () {
      const [ano, mes] = this.value.split("-");
      criarCalendario(parseInt(ano), parseInt(mes) - 1);
  });

  const hoje = new Date();
  mesAnoInput.value = `${hoje.getFullYear()}-${String(hoje.getMonth() + 1).padStart(2, "0")}`;
  criarCalendario(hoje.getFullYear(), hoje.getMonth());
});
