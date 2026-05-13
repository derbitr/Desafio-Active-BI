import extracao_pdf, prompt_IA, api
import os, dotenv,logging,json

dotenv.load_dotenv()

#Função para iniciar o sistema de logs do código
def config():
    logging.basicConfig(level=logging.INFO,format="%(levelname)s:%(message)s")
    return "Sistema de registro iniciado"

#Função principal para ligar todos os arquivos
def iniciar():
    try:
        caminho = input("Digite o caminho do PDF: ")
        pergunta = input("Qual sua pergunta sobre o documento? ")
        if not caminho or not pergunta:
            logging.warning("Caminho do arquivo ou pergunta vazio")
            return None
        if pergunta:
            texto_extraido = extracao_pdf.processar_pdf(caminho)
            if not texto_extraido:
                logging.warning("Não foi possível ler o texto")
                return
            string = api.analisar_bot(texto_extraido,pergunta_usuario=pergunta)
        try:
            dicionario_string = json.loads(string)
            if dicionario_string:
                print(f"Documento analisado: {dicionario_string.get('source')}")
                print(f"\nAnálise:\n{dicionario_string.get('text')}")
                print("Perguntas sugeridas")
                for pergunta in dicionario_string.get('suggestions'):
                    print(pergunta)
        except Exception as h:
            logging.error(f"Erro ao buscar json: {h}")
            return None
    except Exception as j:
        logging.error(f"Erro ao iniciar procedimento: {j}")
        return None
if __name__ == "__main__":
    config()
    iniciar()

