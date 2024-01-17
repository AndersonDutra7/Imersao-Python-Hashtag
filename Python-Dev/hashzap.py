# Instalar framework flet
# Entrar na venv e pip install flet

# Titulo Hashzap
# Botão Iniciar o chat
    # Popup
        # Bem vindo ao Hashzap
        # Escreva seu nome
        # Entrar no chat
# Chat
    # Anderson entrou no chat
    # Mensagens do usuário
# Campo para enviar msg
# Botão de enviar

# Passo 01 - Importar a Biblioteca flet
import flet as ft

# Passo 02 - Criar função para chamar a Biblioteca flet
def main(pagina):
    # Passo 01 - Titulo Hashzap
    titulo = ft.Text("Hashzap")
    pagina.add(titulo)

    # criar chat
    chat = ft.Column()

    # Para poder trocar msg entre usuário, faz-se necessário criar um tunel para transporte dessas msgs
    def enviar_msg_tunel(informacoes):
        # adicionar a msg ao chat
        chat.controls.append(ft.Text(informacoes))
        pagina.update()

    pagina.pubsub.subscribe(enviar_msg_tunel)

    # criar Usuário
    nome_usuario = ft.TextField(label="Escreva seu nome")

    # criar o campo de enviar msg
    # campo_msg = ft.TextField(label="Escreva sua mensagem")

    # criar o botao de enviar msg
    def enviar_msg(evento):
        # criar a msg
        texto_campo_msg = f"{nome_usuario.value}\n {campo_msg.value}"
        
        # adicionar a msg ao chat
        pagina.pubsub.send_all(texto_campo_msg)

        #limpar o campo da msg
        campo_msg.value = ""

        pagina.update()

    campo_msg = ft.TextField(label="Escreva sua mensagem", on_submit=enviar_msg)
    botao_enviar = ft.ElevatedButton("Enviar mensagem", on_click=enviar_msg)

    # Popup
    def entrar_chat(evento):
        # feche o popup
        popup.open = False

        # excluir o botão iniciar chat
        pagina.remove(botao_iniciar)

        # adicionar o nosso chat
        pagina.add(chat)

        # alinhar input + button na mesma linha
        linha_msg = ft.Row(
            [campo_msg, botao_enviar]
        )
        pagina.add(linha_msg)

        texto = f"{nome_usuario.value} entrou no chat"
        pagina.pubsub.send_all(texto)
        pagina.update()

    popup = ft.AlertDialog(
        open = False, 
        modal = True, 
        title = ft.Text("Bem vindo ao Hashzap"),
        content = nome_usuario,
        actions = [ft.ElevatedButton("Entrar", on_click=entrar_chat)]
        )

    # Passo 02 - Botão Iniciar o chat
    def iniciar_chat(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()
        
    botao_iniciar = ft.ElevatedButton("Iniciar chat", on_click=iniciar_chat)
    pagina.add(botao_iniciar)

# Passo 03 - Iniciar o aplicativo
# ft.app(main)
ft.app(main, view=ft.WEB_BROWSER)
