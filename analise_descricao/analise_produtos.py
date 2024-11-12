import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk
from nltk.corpus import stopwords
import os
import sys

# Configurar o caminho do nltk_data dentro do projeto
# Ajuste para o caminho relativo onde a pasta nltk_data foi incluída
project_path = os.path.dirname(__file__)
print(os.path.dirname(__file__))
nltk_data_path = os.path.join(project_path, 'nltk_data')
print(nltk_data_path)
os.environ['NLTK_DATA'] = nltk_data_path



# Função principal para análise de descrição
def analise_descricao(caminho, precisao):
    # Carregar a lista de stopwords em português sem realizar download
    portuguese_stopwords = stopwords.words('portuguese')

    # Passo 1: Ler os dados do Excel
    df = pd.read_excel(caminho)  # Substitua com o caminho do seu arquivo

    # Passo 2: Processar as descrições (usando stopwords em português)
    vectorizer = TfidfVectorizer(stop_words=portuguese_stopwords)
    tfidf_matrix = vectorizer.fit_transform(df['DESCRICAO'])  # Substitua 'descricao' pela coluna relevante

    # Passo 3: Calcular a similaridade de cosseno entre as descrições
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

    # Passo 4: Identificar descrições parecidas e incluir as descrições no relatório
    sim_threshold = precisao  # Defina um limiar de similaridade
    similar_items = []

    for i in range(len(cosine_sim)):
        for j in range(i + 1, len(cosine_sim)):
            if cosine_sim[i][j] > sim_threshold:
                similar_items.append({
                    'Produto_ID_1': df.iloc[i]['CODIGO'],
                    'Descricao_1': df.iloc[i]['DESCRICAO'],  # Inclua a descrição do primeiro produto
                    'Produto_ID_2': df.iloc[j]['CODIGO'],
                    'Descricao_2': df.iloc[j]['DESCRICAO']   # Inclua a descrição do segundo produto
                })  # Substitua 'id_produto' e 'descricao' pelas colunas de identificação e descrição

    # Criar DataFrame com os resultados
    results_df = pd.DataFrame(similar_items)

    print(1)
    # Passo 5: Salvar os resultados em um arquivo Excel
    folder_path = os.path.dirname(caminho)
    print(folder_path)
    results_df.to_excel(os.path.join(folder_path, 'analise_similares.xlsx'), index=False)

