# Reconhecimento de Fala e Execução de Comandos
Este script em Python utiliza a biblioteca SpeechRecognition para ouvir a entrada de voz do usuário e executa comandos específicos com base em padrões reconhecidos.

# Como Funciona
O script segue estes passos:

1. Inicializa o microfone do usuário usando a biblioteca SpeechRecognition.
2. Ajusta para o ruído ambiente para melhorar a precisão do reconhecimento de fala.
3. Solicita ao usuário para falar algo.
4. Ouve a entrada do usuário.
5. Usa a API de Reconhecimento de Fala do Google para converter a entrada de áudio em texto.
6. nExecuta comandos específicos com base nos padrões reconhecidos na fala do usuário.

# Uso

1. Certifique-se de ter o Python instalado no seu sistema.
2. Instale as bibliotecas necessárias usando o seguinte comando:
   
pip install SpeechRecognition

3. Execute o script:

python nome_do_seu_script.py

4. Fale algo quando solicitado e observe a resposta do script.

# Comandos Suportados
Se a palavra "navegador" for reconhecida, o script tentará iniciar o navegador Opera.
Se a palavra "jogo" for reconhecida, o script tentará iniciar o Valorant.
Sinta-se à vontade para personalizar o script para adicionar mais comandos ou alterar os existentes de acordo com suas necessidades.

# Requisitos
Python
Biblioteca SpeechRecognition

# Observações
Se o script não entender a entrada de fala, imprimirá "Não entendi".
# Contribuições
Sinta-se à vontade para contribuir para aprimorar a funcionalidade ou corrigir problemas. Envie um pull request com suas alterações.
