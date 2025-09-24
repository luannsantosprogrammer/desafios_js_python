

# Jogo da Velha - HTML, CSS e JavaScript

Este é um **Jogo da Velha** desenvolvido com **HTML**, **CSS** e **JavaScript puro**. O objetivo desse projeto é praticar e aprimorar os meus conhecimentos em **JavaScript**.


![Jogo da Velha](/img-jogodavelha.jpg)



## Descrição do Código

### 1. Definição das Variáveis

Iniciamos criando as variáveis que serão utilizadas em todo o código. Elas referenciam as tags HTML necessárias para o funcionamento do jogo:

```javascript
const jogo = document.querySelector('#quadrados');
var quadrados = jogo.querySelectorAll(".padrao");
var jogador1 = document.querySelector(".jogador1");
var jogador2 = document.querySelector(".jogador2");
var win = document.querySelector(".win");
var vencedor = win.querySelector("h2");
var titulo = document.querySelector(".titulo");
```

### 2. Definição do Primeiro Jogador

A variável global `vez` foi utilizada para determinar que o jogador com o símbolo **"X"** será sempre o primeiro a jogar:

```javascript
var vez = "x";
```

### 3. Validação do Vencedor

Esta função verifica os elementos que possuem os símbolos "chis" (X) ou "bola" (O) dentro de um conjunto de divs, representando os quadrados do jogo. No final, ela chama a função `efeitoVencedor` para mostrar a mensagem do vencedor.

```javascript
function validacaoGanhador(quadrado1, quadrado2, quadrado3) {
    var valor1 = quadrados[quadrado1].children;
    var valor2 = quadrados[quadrado2].children;
    var valor3 = quadrados[quadrado3].children;

    if (valor1[0].className == "chis1" && valor2[0].className == "chis1" && valor3[0].className == "chis1") {
        efeitoVencedor("O vencedor foi X");
    } else if (valor1[0].className == "bola" && valor2[0].className == "bola" && valor3[0].className == "bola") {
        efeitoVencedor("O vencedor foi Bola");
    }
}
```

### 4. Alternando Entre os Jogadores

A função `vezDoJogador` altera a vez entre o jogador "X" e o jogador "O", além de mudar a cor de fundo dos jogadores para indicar quem está jogando:

```javascript
function vezDoJogador(guardar) {
    if (vez == "x") {
        tipoX(guardar);
        jogador1.style.backgroundColor = "white";
        jogador2.style.backgroundColor = "#FF5733";
        vez = "bola";
    } else {
        tipoBola(guardar);
        jogador1.style.backgroundColor = "#FF5733";
        jogador2.style.backgroundColor = "white";
        vez = "x";
    }
}
```

### 5. Eventos de Clique nos Quadrados

Por fim, são atribuídos eventos de clique para cada quadrado do tabuleiro, acionando a função `vezDoJogador` quando um quadrado é clicado:

```javascript
quadrados[0].addEventListener("click", () => vezDoJogador(quadrados[0]));
quadrados[1].addEventListener("click", () => vezDoJogador(quadrados[1]));
quadrados[2].addEventListener("click", () => vezDoJogador(quadrados[2]));
quadrados[3].addEventListener("click", () => vezDoJogador(quadrados[3]));
quadrados[4].addEventListener("click", () => vezDoJogador(quadrados[4]));
quadrados[5].addEventListener("click", () => vezDoJogador(quadrados[5]));
quadrados[6].addEventListener("click", () => vezDoJogador(quadrados[6]));
quadrados[7].addEventListener("click", () => vezDoJogador(quadrados[7]));
quadrados[8].addEventListener("click", () => vezDoJogador(quadrados[8]));
```

## Tecnologias Utilizadas

- **HTML5**
- **CSS3**
- **JavaScript**

---

Feito com 😎 por [Luann Rodrigo de Souza Santos]
