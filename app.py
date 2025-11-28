import os
from dotenv import load_dotenv
import google.generativeai as genai
from ddgs import DDGS


load_dotenv()

class Buscador:
    def __init__(self):
        pass

    def procurar(self, termo):
        with DDGS() as dk:
            texto = dk.text(termo, max_results=30)
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
        pass

    def enviar(self,resumo):
 
        pass


if __name__ == "__main__":
    print("Sistema iniciado.")
    
    scout = Buscador() 
    analista = Resumidor()
    dados = scout.procurar("Novas noticias Engenharia de IA")

    relatorio_final = analista.resumir(dados)

    print(relatorio_final)


    
    
    
   