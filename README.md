# 📡 AI-Radar ETL

> **Seu Agente de Inteligência de Mercado.** Um pipeline ETL autônomo que monitora, filtra e resume as novidades tech diariamente.

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white)
![AI](https://img.shields.io/badge/AI-Google%20Gemini-orange?logo=google&logoColor=white)
![Automation](https://img.shields.io/badge/Automation-Daemon-green)

---

## 💡 O Problema
O volume de notícias sobre IA é avassalador. Acompanhar lançamentos, novas ferramentas e tendências manualmente consome horas preciosas e gera "FOMO" (Fear Of Missing Out).

## 🛠️ A Solução
O **AI-Radar** é um Agente Autônomo que roda em segundo plano (Daemon). Ele atua como um Analista de Inteligência pessoal.
1.  **Extração (Extract):** O sistema varre a web em busca de notícias recentes usando a API do **DuckDuckGo**.
2.  **Transformação (Transform):** Utiliza o **Google Gemini 1.5** para ler as manchetes, filtrar o ruído (clickbait) e gerar um resumo executivo técnico.
3.  **Carga (Load):** Entrega o relatório formatado diretamente na caixa de entrada (E-mail) do usuário via SMTP.

---

## 🏗️ Stack Tecnológico

O projeto aplica conceitos de **Engenharia de Dados** e **Automação Inteligente**.

* **Linguagem:** Python 3.12
* **IA Core:** `Google Generative AI` (Gemini API)
* **Web Scraping:** `duckduckgo-search` (Busca sem API Key)
* **Orquestração:** `schedule` (Agendamento de Tarefas) & `smtplib` (Protocolo de E-mail)
* **Resiliência:** Implementação de `Polite Polling` e tratamento de erros de conexão (`try/except` com backoff).

---

## 🚀 Como rodar localmente

Se você quiser testar este agente na sua máquina:

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/IsantoDev/radar-etl.git](https://github.com/IsantoDev/radar-etl.git)
    cd radar-etl
    ```

2.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configure as Chaves:**
    * Crie um arquivo `.env` na raiz.
    * Adicione suas credenciais:
      ```env
      GEMINI_API_KEY="sua_chave_aqui"
      EMAIL_ADDRESS="seu_email@gmail.com"
      EMAIL_PASSWORD="senha_de_app_do_google"
      ```

4.  **Execute o Agente:**
    ```bash
    python app.py
    ```
    *(O robô ficará rodando em loop, aguardando o horário agendado).*

---

## 🧠 Estrutura do Código

* **`app.py`**: O Orquestrador. Gerencia o loop de vida do agente e conecta os módulos.
* **Módulo Buscador**: Classe responsável pela conexão com a web e extração de dados brutos.
* **Módulo Resumidor**: Classe que encapsula a inteligência da LLM para processar o texto.
* **Módulo Notificador**: Classe responsável pela entrega (Delivery) da informação.

---

### 👨‍💻 Autor

Desenvolvido por **[Igor Santos](https://www.linkedin.com/in/isantosdev/)**
