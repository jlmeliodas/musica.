musica = [
    ("musica 1", "rock"),
    ("musica 2", "pop"),
    ("musica 3", "jazz"),
    ("musica 4", "rock"),
    ("musica 5", "pop"),
]

# historico de musica ouvidas pelo usuario
historico_usuario = ["rock", "jazz", "pop", "jazz", "pop"]


# função para recomendar musicas
def recomendar_musica(historico):
    # contar a frequencia de cada genero no historico
    frequencia = {}
    for genero in historico:
        if genero in frequencia:
            frequencia[genero] += 1
        else:
            frequencia[genero] = 1 

    # encontrar o genero mais frequente
    genero_mais_frequente = max(frequencia, key=frequencia.get)

    # recomendar musica desse genero
    recomendacoes = []
    for titulo, genero_ in musica:
        if genero == genero_mais_frequente:
            recomendacoes.append(titulo)
    return recomendacoes


# obter recomendacoes para o usuario 
recomendacoes_usuario = recomendar_musica(historico_usuario)
print("Música recomendadas:", recomendacoes_usuario)
