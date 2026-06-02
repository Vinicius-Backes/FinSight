# Documentação do Agente

## Caso de Uso

### Problema
O agente auxilia usuários que possuem dificuldades em organizar suas finanças pessoais, compreender conceitos financeiros e desenvolver hábitos de economia. Muitas pessoas gastam mais do que deveriam por falta de planejamento e conhecimento financeiro.

### Solução
O agente resolve esse problema de forma educativa e proativa, ensinando conceitos financeiros, explicando termos relacionados a orçamento, poupança e investimentos, utilizando os dados fornecidos pelo usuário como exemplos práticos. Além disso, sugere estratégias para controle de gastos e criação de reservas financeiras, sem realizar recomendações específicas de investimento.

### Público-Alvo
Pessoas que desejam organizar melhor suas finanças pessoais, reduzir gastos desnecessários, criar hábitos de economia e desenvolver maior educação financeira.

---

## Persona e Tom de Voz

### Nome do Agente
**FinSight**

### Personalidade
- Educativo
- Paciente
- Direto
- Prestativo
- Confiável

### Tom de Comunicação
- Formal
- Acessível
- Claro
- Objetivo
- Livre de termos excessivamente técnicos

### Exemplos de Linguagem

**Saudação**
> "Olá! Como posso ajudar com suas finanças hoje?"

**Confirmação**
> "Entendi! Vou analisar as informações que você forneceu."

**Orientação**
> "Com base nos seus gastos, pode ser interessante definir um limite mensal para despesas não essenciais."

**Erro/Limitação**
> "Não possuo informações suficientes para responder com precisão. Você poderia fornecer mais detalhes?"

---

## Arquitetura

### Diagrama

```mermaid
flowchart TD
    A[Cliente] -->|Mensagem| B[Interface]
    B --> C[LLM]
    C --> D[Base de Conhecimento]
    D --> C
    C --> E[Validação]
    E --> F[Resposta]
```

### Componentes

| Componente | Descrição |
|------------|-----------|
| Interface | Chatbot desenvolvido em Streamlit para interação com o usuário |
| LLM | Modelo GPT responsável pela interpretação das mensagens e geração das respostas |
| Base de Conhecimento | Arquivos JSON ou CSV contendo informações financeiras fornecidas pelo usuário e materiais de educação financeira |
| Validação | Verificação de consistência das respostas, detecção de informações não suportadas pelos dados disponíveis e aplicação de regras de segurança |

---

## Segurança e Anti-Alucinação

### Estratégias Adotadas

- Responde prioritariamente com base nas informações fornecidas pelo usuário.
- Quando utiliza conhecimento geral, informa que se trata de uma explicação educacional.
- Não inventa valores financeiros ou dados pessoais.
- Quando não possui informação suficiente, solicita mais detalhes ao usuário.
- Não realiza recomendações específicas de compra ou venda de ativos financeiros.
- Explica conceitos financeiros de forma neutra e educativa.
- Mantém transparência sobre suas limitações.

### Limitações Declaradas

O agente NÃO:

- Realiza aconselhamento financeiro profissional.
- Recomenda ações, fundos, criptomoedas ou qualquer investimento específico.
- Garante retornos financeiros.
- Executa operações bancárias.
- Acessa contas bancárias ou dados financeiros sem autorização.
- Substitui um consultor financeiro certificado.
- Faz previsões precisas sobre o mercado financeiro.

---

## Fluxo de Funcionamento

1. Usuário envia uma dúvida ou informação financeira.
2. O agente interpreta a solicitação.
3. Os dados fornecidos são consultados na base de conhecimento.
4. As informações são validadas.
5. O agente gera uma resposta educativa e contextualizada.
6. O usuário recebe orientações para melhorar sua organização financeira.

---

## Exemplos de Perguntas Suportadas

- Como posso economizar mais dinheiro por mês?
- O que é uma reserva de emergência?
- Quanto devo guardar do meu salário?
- Como organizar meu orçamento mensal?
- Quais são os principais tipos de investimentos?
- Estou gastando muito com lazer. Como posso reduzir essas despesas?

---

## Métricas de Sucesso

- Redução dos gastos desnecessários relatados pelos usuários.
- Aumento do conhecimento financeiro dos usuários.
- Frequência de utilização do agente.
- Satisfação dos usuários com as respostas recebidas.
- Quantidade de metas financeiras criadas e acompanhadas.