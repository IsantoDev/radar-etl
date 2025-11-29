# 📡 AI-Radar ETL

> Pipeline automatizado de Engenharia de Dados para monitoramento de tendências tech.

## 🎯 Objetivo
Projeto desenvolvido para automatizar a coleta, análise e distribuição de inteligência sobre o mercado tech. O sistema atua como um analista pessoal que trabalha 24/7, buscando notícias, resumindo com GenAI e enviando relatórios por e-mail.

## 🛠️ Stack Tecnológico
* **Linguagem:** Python 3.12+
* **Extração:** `duckduckgo-search` (Web Scraping/API)
* **Transformação:** `google-generativeai` (Gemini 2.0 Flash)
* **Carregamento:** `smtplib` (Envio via SMTP Gmail)
* **Automação:** `schedule` (Agendamento de tarefas)

## 🚀 Como Rodar

1. Clone o repositório:
   ```bash
   git clone [https://github.com/IgorBiodev/radar-etl.git](https://github.com/IgorBiodev/radar-etl.git)

