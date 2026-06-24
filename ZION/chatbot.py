import os
import sys

import requests


API_URL = "https://api.openai.com/v1/responses"
MODELO = os.getenv("OPENAI_MODEL", "gpt-5.5")


def obter_chave_api():
    chave_api = os.getenv("OPENAI_API_KEY")
    if not chave_api:
        print(
            "Erro: defina a variavel de ambiente OPENAI_API_KEY antes de executar.",
            file=sys.stderr,
        )
        sys.exit(1)
    return chave_api


def extrair_texto(resposta_json):
    if resposta_json.get("output_text"):
        return resposta_json["output_text"]

    textos = []
    for item in resposta_json.get("output", []):
        if item.get("type") != "message":
            continue

        for conteudo in item.get("content", []):
            if conteudo.get("type") in {"output_text", "text"}:
                textos.append(conteudo.get("text", ""))

    return "\n".join(textos).strip()


def enviar_mensagem(mensagem, chave_api, resposta_anterior_id=None):
    dados = {
        "model": MODELO,
        "input": mensagem,
    }

    if resposta_anterior_id:
        dados["previous_response_id"] = resposta_anterior_id

    resposta = requests.post(
        API_URL,
        headers={
            "Authorization": f"Bearer {chave_api}",
            "Content-Type": "application/json",
        },
        json=dados,
        timeout=60,
    )

    if not resposta.ok:
        print(f"Erro da API ({resposta.status_code}): {resposta.text}", file=sys.stderr)
        sys.exit(1)

    resposta_json = resposta.json()
    texto = extrair_texto(resposta_json)

    if not texto:
        print("Erro: a resposta da API veio sem texto.", file=sys.stderr)
        sys.exit(1)

    return texto, resposta_json.get("id")


def main():
    chave_api = None
    resposta_anterior_id = None

    while True:
        texto = input(
            "ZION:\nFaca sua pergunta ou digite 'encerrar' para encerrar a conversa: "
        ).strip()

        if texto.lower() == "encerrar":
            print("ZION:\nObrigado por conversar comigo! Ate a proxima.")
            break

        if chave_api is None:
            chave_api = obter_chave_api()

        resposta, resposta_anterior_id = enviar_mensagem(
            texto, chave_api, resposta_anterior_id
        )
        print("ZION:\n" + resposta)


if __name__ == "__main__":
    main()
