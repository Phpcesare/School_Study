// Seleciona o elemento das opções de acessibilidade
const ace = document.querySelector(".opcoes-acessibilidade");

// Função para alternar a exibição das opções de acessibilidade
function acessibilidade() {
  if (ace.style.display === "none" || ace.style.display === "") {
	ace.style.display = "block";
  } else {
	ace.style.display = "none";
  }
}

// Função para aumentar o tamanho da fonte
function aumentarFonte() {
  const body = document.body;
  const currentSize = parseFloat(window.getComputedStyle(body).fontSize);
  body.style.fontSize = (currentSize + 2) + "px"; // Usar px para consistência
}

// Função para diminuir o tamanho da fonte
function diminuirFonte() {
  const body = document.body;
  const currentSize = parseFloat(window.getComputedStyle(body).fontSize);
  body.style.fontSize = (currentSize - 2) + "px"; // Usar px para consistência
}