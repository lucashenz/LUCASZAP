import flet as ft 
import datetime

def main(pagina):
    titulo = ft.Text("LUCASZAP")
    hora = datetime.time 
    titulo_janela = ft.Text("Bem vindo ao LUCASZAP")

    def enviar_mensagem_tunel(mensagem):
        texto_mensagem = ft.Text(mensagem)
        chat.controls.append(texto_mensagem)
        pagina.update()
    
    # websocket
    pagina.pubsub.subscribe(enviar_mensagem_tunel)
    
    def enviar_mensagem(evento):
        mensagem = f"{campo_nome.value}: {campo_mensagem.value} ({hora.value})"
        # enviar mensagem tunel 
        pagina.pubsub.send_all(mensagem)
        campo_mensagem = ""
        pagina.update()
    
    campo_mensagem = ft.TextField(label="Digite a sua mensagem:", on_submit=enviar_mensagem)
    botao_enviar = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)
    
    chat = ft.Column()
    linha_mensagem = ft.Row([campo_mensagem, botao_enviar])
    def entrar_chat(evento):
        pagina.pubsub.send_all(f"{campo_nome.value} entrou no chat ({hora.value})")
        janela.open = False
        pagina.remove(botao_iniciar)
        pagina.remove(titulo)
        
        pagina.add(chat)
        
        pagina.add(linha_mensagem)
        pagina.update()
    
    campo_nome = ft.TextField(label="Digite o seu nome:", on_submit=entrar_chat)
    botao_entrar = ft.ElevatedButton("ENTRAR NO CHAT", on_click=entrar_chat)
    
    janela = ft.AlertDialog(
        title=titulo_janela,
        content=campo_nome,
        actions=[botao_entrar]
    )
    
    def abrir_dialog(evento):
        pagina.dialog = janela
        janela.open = True
        pagina.update()       
    
    botao_iniciar = ft.ElevatedButton("Iniciar chat", on_click=abrir_dialog)
    

# elementos
    pagina.add(titulo)
    pagina.add(botao_iniciar)


ft.app(main)
