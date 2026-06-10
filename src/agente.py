import json
import pandas as pd
import ollama

from config import (
    MODEL_NAME,
    SYSTEM_PROMPT
)


class FinSightAgent:

    def __init__(self):

        self.transacoes = pd.DataFrame()
        self.historico = pd.DataFrame()
        self.perfil = {}
        self.conhecimento = {}

    # ==================================
    # CARREGAMENTO DOS DADOS
    # ==================================

    def carregar_base_conhecimento(self):

        try:
            self.transacoes = pd.read_csv(
                "data/transacoes.csv"
            )
        except:
            self.transacoes = pd.DataFrame()

        try:
            self.historico = pd.read_csv(
                "data/historico_atendimento.csv"
            )
        except:
            self.historico = pd.DataFrame()

        try:
            with open(
                "data/perfil_usuario.json",
                "r",
                encoding="utf-8"
            ) as f:

                self.perfil = json.load(f)

        except:
            self.perfil = {}

        try:
            with open(
                "data/conteudo_educacao_financeira.json",
                "r",
                encoding="utf-8"
            ) as f:

                self.conhecimento = json.load(f)

        except:
            self.conhecimento = {}

    # ==================================
    # CONTEXTO
    # ==================================

    def montar_contexto(self):

        contexto = []

        contexto.append(
            "=== PERFIL DO USUÁRIO ===\n"
        )

        contexto.append(
            json.dumps(
                self.perfil,
                indent=2,
                ensure_ascii=False
            )
        )

        contexto.append(
            "\n=== ÚLTIMAS TRANSAÇÕES ===\n"
        )

        if not self.transacoes.empty:

            contexto.append(
                self.transacoes.tail(20)
                .to_string(index=False)
            )

        contexto.append(
            "\n=== HISTÓRICO DE ATENDIMENTO ===\n"
        )

        if not self.historico.empty:

            contexto.append(
                self.historico.tail(10)
                .to_string(index=False)
            )

        contexto.append(
            "\n=== BASE EDUCACIONAL ===\n"
        )

        contexto.append(
            json.dumps(
                self.conhecimento,
                ensure_ascii=False,
                indent=2
            )
        )

        return "\n".join(contexto)

    # ==================================
    # ANÁLISE DE GASTOS
    # ==================================

    def resumo_financeiro(self):

        if self.transacoes.empty:
            return "Nenhuma transação encontrada."

        try:

            total = self.transacoes["valor"].sum()

            media = self.transacoes["valor"].mean()

            return f"""
Total movimentado: R$ {total:.2f}

Média por transação: R$ {media:.2f}
"""

        except:
            return "Não foi possível gerar resumo financeiro."

    # ==================================
    # CHAT
    # ==================================

    def responder(self, pergunta):

        contexto = self.montar_contexto()

        resposta = ollama.chat(
         model=MODEL_NAME,
         messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "system",
                "content": contexto
            },
            {
                "role": "user",
                "content": pergunta
            }
        ]
    )

        return resposta["message"]["content"]