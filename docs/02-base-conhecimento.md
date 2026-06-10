# Base de Conhecimento

## Dados Utilizados

| Arquivo | Formato | Utilização no Agente |
|---------|---------|---------------------|
| `historico_atendimento.csv` | CSV | Contextualizar interações anteriores do usuário |
| `perfil_usuario.json` | JSON | Armazenar objetivos financeiros, renda e preferências |
| `conteudo_educacao_financeira.json` | JSON | Fornecer conceitos e explicações sobre finanças pessoais |
| `transacoes.csv` | CSV | Analisar padrões de gastos e hábitos financeiros do usuário |

---

## Estratégia de Integração

### Como os dados são carregados?

Os arquivos JSON e CSV são carregados no início da sessão por meio da aplicação Streamlit. Os dados são processados e transformados em informações estruturadas para facilitar sua utilização pelo modelo de linguagem.

Os arquivos são mantidos em memória durante a sessão e atualizados sempre que o usuário fornecer novos dados financeiros.

### Como os dados são usados no prompt?

Os dados relevantes são inseridos dinamicamente no contexto enviado ao modelo.

O System Prompt define o comportamento do agente, suas limitações e objetivos. Já as informações do usuário são adicionadas ao contexto da conversa conforme necessário.

Dessa forma, o agente consegue personalizar suas respostas sem alterar suas regras de funcionamento.

Exemplo:

- System Prompt: Define que o FinSight é um assistente educacional de finanças pessoais.
- Contexto Dinâmico: Dados financeiros, perfil do usuário e histórico de interações.
- Pergunta do Usuário: Solicitação atual feita durante a conversa.

---

## Exemplo de Contexto Montado

> Exemplo de informações enviadas ao modelo durante uma consulta.

```text
Você é o FinSight, um assistente de educação financeira.

Dados do Usuário:
- Nome: João Silva
- Idade: 28 anos
- Renda Mensal: R$ 4.500
- Objetivo Financeiro: Criar reserva de emergência
- Perfil: Conservador

Resumo Financeiro:
- Gastos fixos: R$ 2.300
- Gastos variáveis: R$ 1.100
- Economia mensal média: R$ 600

Últimas Transações:
- 01/11: Supermercado - R$ 450
- 03/11: Streaming - R$ 55
- 05/11: Restaurante - R$ 120
- 07/11: Transporte - R$ 180

Histórico de Atendimento:
- Usuário demonstrou interesse em aprender sobre orçamento mensal.
- Usuário possui dificuldade em controlar gastos com lazer.

Pergunta:
"Como posso aumentar minha economia mensal?"