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
                                                           temperature=0.1,
                                                           response_format={"type":"json_object"})
        #Precisei pesquisar a fundo a documentação de pricing pois fiz o cálculo erroneamente
        
        token_entrada = resposta_bot.usage.prompt_tokens
        token_saida = resposta_bot.usage.completion_tokens
        custo_token_entrada = (token_entrada/1000000)*0.15 #Custo de entrada (enviar)
        custo_token_saida = (token_saida/1000000)*0.60
        custo_total = custo_token_entrada + custo_token_saida
        logging.info(f"Custo total: {custo_total:.6f}")
        return resposta_bot.choices[0].message.content
    except Exception:
        return "{}"
    