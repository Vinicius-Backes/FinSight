# FinSight 💰

FinSight é um agente de Inteligência Artificial voltado para **educação financeira e organização das finanças pessoais**. O sistema utiliza um modelo de linguagem local através do Ollama para analisar dados do usuário e fornecer orientações personalizadas sobre controle de gastos, planejamento financeiro e hábitos financeiros saudáveis.

---

## Objetivo

O FinSight auxilia usuários a:

* Organizar suas finanças pessoais;
* Entender conceitos financeiros;
* Identificar padrões de gastos;
* Desenvolver hábitos de economia;
* Planejar objetivos financeiros;
* Criar maior consciência sobre o uso do dinheiro.

O agente possui caráter exclusivamente educacional e não realiza recomendações específicas de investimentos.

---

## Tecnologias Utilizadas

* Python 3.12+
* Streamlit
* Pandas
* Ollama
* Llama 3

---

## Estrutura do Projeto

```text
agentefinanceiro/
│
├── data/
│   ├── transacoes.csv
│   ├── historico_atendimento.csv
│   ├── perfil_usuario.json
│   └── conteudo_educacao_financeira.json
│
├── src/
│   ├── app.py
│   ├── agente.py
│   ├── config.py
│   └── requirements.txt
│
└── README.md
```

---

## Instalação

### 1. Clonar o projeto

```bash
git clone <url-do-repositorio>
cd agentefinanceiro
```

### 2. Criar ambiente virtual

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

Linux/Mac:

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Instalar dependências

```bash
pip install -r src/requirements.txt
```

Exemplo de `requirements.txt`:

```txt
streamlit
pandas
ollama
```

---

## Instalação do Ollama

### Windows

Baixe e instale:

https://ollama.com/download/windows

Após a instalação, abra um novo terminal e execute:

```bash
ollama --version
```

---

## Download do Modelo

Baixe o modelo que será utilizado pelo FinSight:

```bash
ollama pull llama3
```

ou

```bash
ollama pull gemma3:4b
```

---

## Execução do Projeto

### Iniciar o Ollama

Certifique-se de que o Ollama está executando:

```bash
ollama serve
```

Em algumas instalações ele inicia automaticamente.

---

### Executar o sistema

Entre na pasta `src`:

```bash
cd src
```

Execute:

```bash
streamlit run app.py
```

O sistema ficará disponível em:

```text
http://localhost:8501
```

---

## Arquivos de Dados

### perfil_usuario.json

Armazena informações básicas do usuário.

Exemplo:

```json
{
    "nome": "João Silva",
    "idade": 28,
    "renda_mensal": 4500,
    "objetivo": "Criar reserva de emergência"
}
```

### transacoes.csv

Contém o histórico financeiro do usuário.

Exemplo:

```csv
data,categoria,valor
2025-01-10,Supermercado,250
2025-01-15,Streaming,39.90
2025-01-20,Transporte,120
```

### historico_atendimento.csv

Armazena atendimentos anteriores realizados pelo agente.

### conteudo_educacao_financeira.json

Base de conhecimento com conceitos e materiais educativos.

---

## Funcionalidades

* Análise de gastos;
* Consulta ao histórico financeiro;
* Explicação de conceitos financeiros;
* Sugestões de economia;
* Contextualização utilizando dados do usuário;
* Atendimento conversacional por IA.

---

## Limitações

O FinSight NÃO:

* Faz recomendações de investimentos específicos;
* Executa operações financeiras;
* Acessa contas bancárias;
* Garante retorno financeiro;
* Substitui consultores financeiros profissionais.

---

## Exemplo de Uso

Pergunta:

```text
Estou gastando muito com delivery. O que posso fazer?
```

Resposta:

```text
Uma estratégia interessante é estabelecer um limite mensal para gastos com delivery e planejar refeições antecipadamente. Isso ajuda a reduzir despesas sem comprometer sua rotina.
```

---


Nome do projeto: FinSight
