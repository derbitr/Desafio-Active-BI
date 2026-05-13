AI - Analisador de Documentos PDF

Esse projeto utiliza conceitos de arquitetura limpa e modularização para testes singulares nos arquivos, separação entre bibliotecas e orquestração de registros, utilizando bibliotecas como pdfplumber para extração de texto em arquivos PDF, a biblioteca logging para informações de registros e o uso da API da openai para criar um prompt json utilizando lógica da programação para perguntas e respostas.

**Justificativa**
Utilizei o modelo *gpt-4o-mini* pelo seu baixo custo de tokens e por ter uma alta perfomance em processo de extração de dados

*Como instalar*

*Clone ou baixe o repositório*
```bash
git clone "url-do-repositório"
cd Desafio-Active-BI

**Configurar o ambiente bash**

criar o ambiente = python -m venv venv

ativar no windows = venv/scripts/activate

ativar no linux/mac = source venv/bin/activate

*Dependências necessárias!*
bash
pip install -r requirements.txt

**Variáveis do ambiente(.env)**
OPENAI_API_KEY = sua_chave

**Executar**
python projeto_bi/main.py

