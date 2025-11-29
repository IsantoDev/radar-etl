# 📡 AI-Radar ETL

> Pipeline automatizado de Engenharia de Dados para monitoramento de tendências tech.

## 🎯 Objetivo
Projeto desenvolvido para automatizar a coleta, análise e distribuição de inteligência sobre o mercado de tecnologia. O sistema atua como um analista pessoal que trabalha 24/7, buscando notícias na web, resumindo com Inteligência Artificial (Gemini) e enviando relatórios executivos por e-mail automaticamente.

## 🛠️ Stack Tecnológico
* **Linguagem:** Python 3.12+
* **Extração (Extract):** `duckduckgo-search` (Web Scraping/API)
* **Transformação (Transform):** `google-generativeai` (Gemini 2.0 Flash)
* **Carregamento (Load):** `smtplib` (Envio via SMTP Gmail)
* **Automação:** `schedule` (Agendamento de tarefas e Loop Infinito)

## 🚀 Como Rodar

1. Clone o repositório:
   git clone https://github.com/IgorBiodev/radar-etl.git
   cd radar-etl

2. Crie e ative o ambiente virtual (Recomendado):
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # Linux/Mac
   python3 -m venv venv
   source venv/bin/activate

3. Instale as dependências:
   pip install -r requirements.txt

4. Configure as chaves de acesso:
   Crie um arquivo chamado .env na raiz do projeto e adicione suas credenciais (sem aspas):
   
   GEMINI_API_KEY=sua_chave_do_aistudio_google
   EMAIL_REMETENTE=seu_email@gmail.com
   EMAIL_SENHA=sua_senha_de_app_do_google

5. Execute o pipeline:
   python app.py

## 👨‍💻 Autor
Desenvolvido por Igor Santos.