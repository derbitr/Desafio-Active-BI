import logging
import pdfplumber


#Lógica de extração de texto em arquivo PDF
def processar_pdf(caminho_pdf :str) -> str:
    try:
        if not caminho_pdf.endswith(".pdf"):
            logging.warning("Não é um arquivo PDF")
            return ""
        with pdfplumber.open(caminho_pdf) as pdf:
            if pdf is None:
                logging.warning("Arquivo vazio")
                return ""
            texto = ""
            for numero, pagina in enumerate(pdf.pages): #Loop para buscar em cada arquivo (numero) os textos internos (pagina)
                texto_extraido = pagina.extract_text()
                if texto_extraido is not None: 
                    logging.info(f"Pagina {numero} processada ")
                    texto += texto_extraido + "\n"
            return texto
    except FileNotFoundError as e:
        logging.error(f"Arquivo não encontrado: {e}")
        return ""