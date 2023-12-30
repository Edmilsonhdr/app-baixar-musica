## Descrição do Projeto: Baixar Música MP3 com Pytube e Tkinter

Este projeto consiste em uma aplicação simples desenvolvida em Python utilizando a biblioteca Pytube para baixar músicas no formato MP3 a partir de vídeos do YouTube. A interface gráfica é construída com a biblioteca Tkinter, proporcionando uma experiência amigável ao usuário.

### Funcionalidades:

1. **Inserção da URL do Vídeo:**
   - O usuário insere a URL do vídeo do YouTube desejado na interface.

2. **Seleção do Destino:**
   - Ao clicar no botão "Procurar Destino", o usuário pode escolher o diretório onde deseja salvar o arquivo MP3 resultante.

3. **Download do Áudio:**
   - A aplicação utiliza a biblioteca Pytube para criar um objeto YouTube com base na URL fornecida.
   - Em seguida, é identificado o stream de áudio no formato MP3 associado ao vídeo.
   - O áudio é baixado para o diretório selecionado pelo usuário.

4. **Feedback ao Usuário:**
   - Durante o processo de download, a aplicação fornece feedback ao usuário, informando sobre o progresso ou possíveis erros.

### Como Utilizar:

1. **Insira a URL:**
   - Informe a URL do vídeo do YouTube na caixa de entrada.

2. **Escolha o Destino:**
   - Clique no botão "Procurar Destino" para selecionar o local onde o arquivo MP3 será salvo.

3. **Inicie o Download:**
   - Execute a aplicação para iniciar o processo de download.

4. **Acompanhe o Progresso:**
   - Observe as mensagens na interface para saber se o download foi concluído com sucesso ou se houve algum problema.

### Pré-requisitos:

- Python instalado na máquina.

### Bibliotecas Utilizadas:

- [Pytube](https://github.com/pytube/pytube): Utilizada para interagir com a API do YouTube e realizar o download do vídeo.
- [Tkinter](https://docs.python.org/3/library/tkinter.html): Utilizada para criar a interface gráfica da aplicação.

### Executando o Projeto:

1. Clone o repositório.
2. Execute o script Python.
3. Siga as instruções na interface para baixar a música desejada.

Esperamos que esta aplicação simplifique o processo de obtenção de músicas no formato MP3 a partir do YouTube. Sinta-se à vontade para contribuir, reportar problemas ou fazer sugestões de melhorias.
