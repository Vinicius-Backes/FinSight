from agente import FinSightAgent

agent = FinSightAgent()
agent.carregar_base_conhecimento()

resposta = agent.responder(
    "Como posso economizar mais dinheiro?"
)

print(resposta)