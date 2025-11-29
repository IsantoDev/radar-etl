import os
from dotenv import load_dotenv
import google.generativeai as genai
from ddgs import DDGS
import smtplib
from email.message import EmailMessage
import schedule
import time


load_dotenv()

class Buscador:
    def __init__(self):
        pass

    def procurar(self, termo):
        with DDGS() as dk:
            texto = dk.text(termo, max_results=17)
            return texto


class Resumidor:
    def __init__(self):
        print('Iniciando Agente...')

        chave = os.getenv('GEMINI_TOKEN')
        genai.configure(api_key=chave)
        self.model = genai.GenerativeModel('gemini-2.0-flash')
    

    def resumir(self, texto):
        text_ia = f'Aqui estão os dados brutos: {texto}'

        prompt = F'''Você é um Engenheiro de IA Sênior. Analise as seguintes notícias coletadas da web:
        {text_ia}

        Sua missão:
        1 - Filtre o que é inrrelevante ou incosistente
        2 - Analise o que é viavel e benefico entre: Noticias,Vagas,Ensinamentos,Tedencias,Educativo
        3 - Crie um resumo executivo em português (pt-BR)
        4 - Use topicos (bullet points) e dinamismo para facilitar leitura e absorção do conteudo
        5 - Priorize novas noticias diarias'''

        print('Agente está pensando...')

        resposta = self.model.generate_content(prompt)
        return resposta.text
        



class Notificador:
    def __init__(self):
        
        self.email_origem = os.getenv("EMAIL_REMETENTE")
        self.senha_app = os.getenv("EMAIL_SENHA")

    def enviar(self, relatorio_final, destinatario):
        
        msg = EmailMessage()
        msg.set_content(relatorio_final) 
        msg['Subject'] = "Relatório Diário: Inteligência Artificial"
        msg['From'] = self.email_origem
        msg['To'] = destinatario

        print(f"Disparando e-mail para {destinatario}...")

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
      
            smtp.login(user=self.email_origem, password=self.senha_app)
            
            smtp.send_message(msg)
            print("✅ Missão cumprida. E-mail enviado.")


def tardefa_diaria():
    print('Hora de trabalhar! Iniciando pipeline...')

    scout = Buscador() 
    analista = Resumidor()
    dados = scout.procurar("Novas noticias Engenharia de IA")

    relatorio_final = analista.resumir(dados)

    print('Relatorio gerado, enviando email...')

    carteiro = Notificador()
    carteiro.enviar(relatorio_final, 'igorcodd@gmail.com')


if __name__ == "__main__":
    print("Sistema iniciado.")

    schedule.every().day.at('07:52').do(tardefa_diaria)

    print('Aguardando horario agendado...')

    while True:
        schedule.run_pending()
        time.sleep(1)
    
   



    
    
    
   