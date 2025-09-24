const jogo = document.querySelector('#quadrados');
var quadrados = jogo.querySelectorAll(".padrao");
var jogador1 = document.querySelector(".jogador1")
var jogador2 = document.querySelector(".jogador2");
var win = document.querySelector(".win");
var vencedor = win.querySelector("h2");
var titulo = document.querySelector(".titulo");


var vez = "x";


vencedor.addEventListener("click", ()=>{
    location.reload();
})
function efeitoVencedor(frase){
    win.style.animationName = "vencedor";
    win.style.display = "flex";
    setTimeout(function(){vencedor.innerText = frase},2000);

}
function validacaoGanhador(quadrado1,quadrado2,quadrado3){
    var valor1 = quadrados[quadrado1].children
    var valor2 = quadrados[quadrado2].children
    var valor3 = quadrados[quadrado3].children
    console.log(valor1[0].className)
    if(valor1[0].className == "chis1" && valor2[0].className == "chis1" && valor3[0].className == "chis1"){
        
        efeitoVencedor("O vencedor foi X")
        
    }else if(valor1[0].className == "bola" && valor2[0].className == "bola" && valor3[0].className == "bola"){
        efeitoVencedor("O vencedor foi Bola")
   

    }
    
}
function tipoBola(qualQuadrado){
    var bolaDentro = document.createElement("div");
    bolaDentro.className = "bola"
    qualQuadrado.appendChild(bolaDentro);
}
function tipoX(qualQuadrado){
    var xDentro1 = document.createElement("div");
    xDentro1.className = "chis1"
    var xDentro2 = document.createElement("div");
    xDentro2.className = "chis2"
    qualQuadrado.appendChild(xDentro1);
    qualQuadrado.appendChild(xDentro2);

}
function vezDoJogador(guardar){

    var chis1 = guardar.querySelector(".chis1")
    var chis2 = guardar.querySelector(".chis2")
    var bola = guardar.querySelector(".bola")
    
    
    if (vez == "x"){
        tipoX(guardar);
        jogador1.style.backgroundColor = "white";
        jogador2.style.backgroundColor = "#FF5733";
        vez = "bola"

       

    }else{
        tipoBola(guardar);
        jogador1.style.backgroundColor = "#FF5733";
        jogador2.style.backgroundColor = "white";
        vez = "x"
    }
    
    setInterval(()=>{validacaoGanhador(0,1,2)},1000);
    setInterval(()=>{validacaoGanhador(3,4,5)},1000);
    setInterval(()=>{validacaoGanhador(6,7,8)},1000);

    setInterval(()=>{validacaoGanhador(0,3,6)},1000);
    setInterval(()=>{validacaoGanhador(1,4,7)},1000);
    setInterval(()=>{validacaoGanhador(2,5,8)},1000);

    setInterval(()=>{validacaoGanhador(0,4,8)},1000);
    setInterval(()=>{validacaoGanhador(2,4,6)},1000);
}

quadrados[0].addEventListener("click",()=>{vezDoJogador(quadrados[0])})
quadrados[1].addEventListener("click",()=>{vezDoJogador(quadrados[1])})
quadrados[2].addEventListener("click",()=>{vezDoJogador(quadrados[2])})
quadrados[3].addEventListener("click",()=>{vezDoJogador(quadrados[3])})
quadrados[4].addEventListener("click",()=>{vezDoJogador(quadrados[4])})
quadrados[5].addEventListener("click",()=>{vezDoJogador(quadrados[5])})
quadrados[6].addEventListener("click",()=>{vezDoJogador(quadrados[6])})
quadrados[7].addEventListener("click",()=>{vezDoJogador(quadrados[7])})
quadrados[8].addEventListener("click",()=>{vezDoJogador(quadrados[8])})


