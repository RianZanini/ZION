# GPT Chatbot

Chatbot simples em Python que conversa com a API da OpenAI pelo terminal.

O programa usa a variavel de ambiente `OPENAI_API_KEY` para autenticacao e mantem o contexto da conversa usando o `previous_response_id` retornado pela API.

## Requisitos

- Python 3 instalado
- Conta na OpenAI com creditos ou billing ativo
- Chave de API da OpenAI
- Pacote `requests`

Instale a dependencia:

```powershell
python -m pip install requests
```

## Configurando a chave da API

No PowerShell, configure a chave para a sessao atual:

```powershell
$env:OPENAI_API_KEY="sua_chave_aqui"
```

Para verificar se funcionou:

```powershell
python -c "import os; print('OK' if os.getenv('OPENAI_API_KEY') else 'FALHOU')"
```

Se aparecer `OK`, a variavel esta configurada nesse terminal.

Para salvar a variavel de forma permanente no Windows:

```powershell
[Environment]::SetEnvironmentVariable("OPENAI_API_KEY", "sua_chave_aqui", "User")
```

Depois disso, feche e abra novamente o terminal ou o VS Code.

## Executando

Rode o chatbot com:

```powershell
python .\chatbot.py
```

Digite sua pergunta no terminal. Para finalizar:

```text
encerrar
```

## Alterando o modelo

O modelo padrao fica definido no arquivo `chatbot.py`:

```python
MODELO = os.getenv("OPENAI_MODEL", "gpt-5.5")
```

Voce tambem pode alterar o modelo pelo PowerShell sem mexer no codigo:

```powershell
$env:OPENAI_MODEL="nome_do_modelo"
python .\chatbot.py
```

## Erros comuns

### `OPENAI_API_KEY` nao configurada

Esse erro aparece quando a variavel de ambiente nao foi definida no mesmo terminal em que o programa esta rodando.

Configure novamente:

```powershell
$env:OPENAI_API_KEY="sua_chave_aqui"
```

### `insufficient_quota`

Esse erro significa que a conta ou o projeto da OpenAI esta sem creditos, sem billing ativo ou atingiu o limite mensal.

Verifique:

- Uso: https://platform.openai.com/usage
- Billing: https://platform.openai.com/settings/organization/billing

### Chave exposta

Se uma chave de API foi colada no codigo, no terminal, em prints ou em repositorios, revogue essa chave no painel da OpenAI e gere outra.

## Estrutura

```text
.
|-- chatbot.py
`-- README.md
```

## Observacoes

Este projeto e um exemplo educacional. Evite colocar chaves de API diretamente no codigo e prefira sempre variaveis de ambiente.
