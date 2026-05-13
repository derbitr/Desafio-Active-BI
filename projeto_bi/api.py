from openai import OpenAI
import extracao_pdf,prompt_IA, os, dotenv,logging

#Criação da API para extração do texto extraído do arquivo PDF e sistema de pergunta e resposta
def analisar_bot(texto_pdf:str,pergunta_usuario):
    try:
        cliente = OpenAI(
            api_key=os.environ.get("OPENAI_API_KEY")
        )
        lista_mensagem = []
        lista_mensagem.append({
            "role": "system",
            "content": prompt_IA.prompt_string
        })
        lista_mensagem.append({
            "role":"user", "content": f"Documento PDF:\n{texto_pdf}\nPergunta do Analista:\n{pergunta_usuario}"
        })
        resposta_bot = cliente.chat.completions.create(model="gpt-4o-mini",
                                                           messages=lista_mensagem,
                                                           max_completion_tokens=1000,
                                                           temperature=0.1
                                                           response_format={"type":"json_object"})
        tokens = resposta_bot.usage.total_tokens
        maximo_token = (tokens/1000)*0.00015 #Custo total
        logging.info(f"Custo total: {maximo_token:.6f}")
        return resposta_bot.choices[0].message.content
    except Exception:
        return "{}"
    