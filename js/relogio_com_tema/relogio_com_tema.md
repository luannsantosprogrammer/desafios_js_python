⏰ Relógio com Tema Alternável
Este projeto é um relógio digital feito com HTML, CSS e JavaScript puro, com suporte a tema claro/escuro através de um botão animado. Tudo sem framework! Só na raça e na criatividade. 🚀

📁 Estrutura do Projeto
bash
Copiar
Editar
📦 index.html
💡 O que esse projeto faz?
Mostra a hora atual e a data no formato brasileiro.

Atualiza a hora em tempo real (a cada segundo).

Permite alternar entre tema claro e escuro com um clique.

Inclui uma animação suave no botão de tema pra dar aquele charme. 😎

🧱 Tecnologias usadas
HTML5

CSS3 (incluindo @keyframes)

JavaScript (Vanilla JS)

📜 Explicação do Código
🎨 Estilização com CSS
O CSS organiza o layout de forma centralizada e responsiva com flexbox. Destaques:

#relogio é o container principal com sombra e bordas arredondadas.

O botão de tema (input) é circular e tem sombra própria.

Dois temas (claro e escuro) são controlados dinamicamente via JavaScript.

Animações @keyframes:

paraOPreto: move o botão para a direita.

paraOBranco: move o botão para a esquerda.

🧠 Lógica com JavaScript
Funções principais:

js
Copiar
Editar
function dataAtual() {...}
Pega a data atual e insere no DOM no formato dd/mm/aaaa.

js
Copiar
Editar
function horaAtual() {...}
Atualiza o horário a cada segundo, no formato hh:mm:ss.

js
Copiar
Editar
function tema() {...}
Alterna o tema da página entre claro e escuro ao clicar no botão.

Muda a cor de fundo, texto, sombra do relógio e dispara a animação de deslize no botão.

js
Copiar
Editar
function atualizarRelogio() {...}
Inicializa o relógio e mantém o horário atualizando em tempo real com setInterval.

🎯 Resultado final
Ao abrir a página, você verá:

Um título estiloso: Relógio com tema

Um botão redondo que muda a cor do site de branco para preto (e vice-versa)

Um painel com a hora atualizada ao vivo e a data de hoje.
