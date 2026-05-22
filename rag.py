from pypdf import PdfReader
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import os
from llm import gerar_resposta

def ler_pdf(caminho_pdf):

    texto = ""

    leitor = PdfReader(caminho_pdf)

    for pagina in leitor.pages:

        conteudo = pagina.extract_text()

        if conteudo:

            conteudo = conteudo.replace("\n", " ")

            # remove espaços duplicados
            conteudo = " ".join(conteudo.split())

            texto += conteudo + " "

    return texto

def dividir_chunks(texto, tamanho=800, overlap=150):
    chunks = []

    inicio = 0

    while inicio < len(texto):
        fim = inicio + tamanho

        chunk = texto[inicio:fim]

        chunks.append(chunk)

        inicio += tamanho - overlap

    return chunks

modelo = SentenceTransformer("all-MiniLM-L6-v2")


def gerar_embeddings(chunks):
    textos = [item["chunk"] for item in chunks]

    embeddings = modelo.encode(textos)

    return embeddings

def criar_indice(embeddings):
    dimensao = embeddings.shape[1]

    indice = faiss.IndexFlatL2(dimensao)

    embeddings = np.array(embeddings).astype("float32")

    indice.add(embeddings)

    return indice

def buscar_chunks(pergunta, modelo, indice, chunks, top_k=3):

    pergunta_lower = pergunta.lower()

    chunks_filtrados = []

    for item in chunks:
        nome_arquivo = item["arquivo"].lower()

        nome_limpo = (
            nome_arquivo
            .replace(".pdf", "")
            .replace("_", " ")
        )
        nome_base = nome_limpo.split("-")[0]

        if nome_base in pergunta_lower:
            chunks_filtrados.append(item)

    if chunks_filtrados:

        resultados = []

        vistos = set()

        for item in chunks_filtrados:

            if item["chunk"] not in vistos:

                resultados.append(item)

                vistos.add(item["chunk"])

        return resultados[:top_k]


    embedding_pergunta = modelo.encode(
        [pergunta]
    )

    embedding_pergunta = np.array(
        embedding_pergunta
    ).astype("float32")

    distancias, indices = indice.search(
        embedding_pergunta,
        top_k
    )

    resultados = []

    vistos = set()

    for i in indices[0]:

        item = chunks[i]

        if len(item["chunk"]) < 50:
            continue

        if item["chunk"] not in vistos:

            resultados.append(item)

            vistos.add(item["chunk"])

    print("\nCHUNKS RECUPERADOS:\n")

    for r in resultados:
        print("=" * 50)
        print(r["arquivo"])
        print(r["chunk"][:300])

    
    if not resultados:
        return []

    return resultados

def montar_contexto(chunks_encontrados):
    contexto = ""

    for item in chunks_encontrados:

        contexto += (
            f"[FONTE: {item['arquivo']}]\n"
            f"{item['chunk']}\n\n"
        )

    contexto = contexto[:4000]
    return contexto

def carregar_documentos(pasta="data"):
    documentos = []

    for arquivo in os.listdir(pasta):
        if arquivo.endswith(".pdf"):
            caminho = os.path.join(pasta, arquivo)

            texto = ler_pdf(caminho)

            documentos.append({
                "arquivo": arquivo,
                "texto": texto
            })

    return documentos

def criar_chunks_documentos(documentos):

    todos_chunks = []

    for documento in documentos:

        chunks = dividir_chunks(documento["texto"])

        for chunk in chunks:

            # ignora chunks pequenos
            if len(chunk.strip()) < 100:
                continue

            texto_lower = chunk.lower()

            if "downloaded from ieee" in texto_lower:
                continue

            if "restrictions apply" in texto_lower:
                continue

            if "universidade federal de mato grosso do sul" in texto_lower:
                continue

            todos_chunks.append({
                "arquivo": documento["arquivo"],
                "chunk": chunk
            })

    return todos_chunks

def responder_pergunta(
    pergunta,
    modelo,
    indice,
    chunks
):
    resultados = buscar_chunks(
        pergunta,
        modelo,
        indice,
        chunks
    )

    contexto = montar_contexto(resultados)

    resposta = gerar_resposta(
        pergunta,
        contexto
    )

    return resposta

def recuperar_contexto(
    pergunta,
    modelo,
    indice,
    chunks
):

    resultados = buscar_chunks(
        pergunta,
        modelo,
        indice,
        chunks
    )

    if not resultados:
        return ""

    contexto = montar_contexto(resultados)

    return contexto