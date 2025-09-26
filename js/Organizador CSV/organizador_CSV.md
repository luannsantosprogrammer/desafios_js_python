# 📂 Organizador CSV

Este projeto é uma pequena aplicação web feita em **HTML, CSS e JavaScript** que permite:

- Fazer upload de **múltiplos arquivos CSV**.
- Unificar os conteúdos em um **único arquivo**.
- Baixar o resultado já consolidado com o **nome escolhido pelo usuário**.

---

## 🚀 Como funciona

1. **Interface de Upload**  
   - A interface traz um **botão estilizado** (ícone de pasta animada) para selecionar os arquivos `.csv`.
   - É possível escolher **vários arquivos ao mesmo tempo**.

2. **Nome do Arquivo Final**  
   - Um campo de texto (`input`) permite digitar o **nome do arquivo unificado** que será baixado.

3. **Botão "Verificar"**  
   - Ao clicar, o código:
     - Lê todos os arquivos CSV selecionados.
     - Junta os dados mantendo a **primeira linha (cabeçalho)** apenas uma vez.
     - Concatena todas as linhas subsequentes de cada arquivo.

4. **Download Automático**  
   - Gera dinamicamente um arquivo `.csv` no navegador.
   - O download começa automaticamente com o nome definido pelo usuário.

---

## 🧑‍💻 Estrutura do Código

### HTML
- Define a interface:
  - Título (`<h1>`).
  - Botão de upload estilizado.
  - Campo de texto para o nome do arquivo.
  - Botão para processar os CSVs.

### CSS
- Dá o estilo moderno:
  - Pasta animada no upload.
  - Inputs estilizados com animação de rótulo ("NOME-DO-ARQUIVO").
  - Botões com sombra e efeito de clique.

### JavaScript
- Principais funções:
  - `lendoArquivos()`:  
    Lê os arquivos CSV usando `FileReader`, transforma em listas e guarda na variável `lista`.
  - **Processamento no botão**:  
    - Mantém o cabeçalho do primeiro arquivo.
    - Junta todas as linhas dos arquivos seguintes.
    - Cria um **Blob** com o CSV final.
    - Simula o clique em um `<a>` invisível para baixar o arquivo.

---

## 📋 Exemplo de Uso

1. Clique em **Subir arquivos** e selecione múltiplos CSVs.
2. Digite no campo de texto o **nome desejado** para o arquivo final (ex: `dados_unificados`).
3. Clique em **Verificar**.
4. O navegador irá baixar automaticamente o arquivo `dados_unificados.csv` contendo todos os dados unidos.

---

## ⚡ Tecnologias Utilizadas
- **HTML5** para a estrutura.
- **CSS3** com animações para estilo e experiência do usuário.
- **JavaScript** puro para manipulação dos arquivos e download.

---

## 📸 Preview

> Adicione aqui um gif ou imagem mostrando o funcionamento se quiser deixar seu README mais atrativo.
