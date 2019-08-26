# Landmarks Recognition

# Organização geral

Essa pasta contem os arquivos usados para a realização do projeto. Basicamente podemos organizar tudo em duas seções, uma relacionada à construção dos datasets e a outra relacionada aos Notebooks de experimentações.

## Construção dos datasets

O arquivo `train.csv` é o arquivo com dados de todas as 4M de imagens e suas landmarks. Ele foi usado para criação de dois datasets, um com 100 classes e outro com 20 classes.

O arquivo `analise.py` foi usado para construir a pasta `data`. Ele basicamente carrega o `train.csv`, agrupa as fotos por landmark_id, ordena e seleciona as classes de 50 à 149. Com essa sub lista, separamos os datasets de treino e teste e criamos um subconjunto de 20 classes com seus respectivos conjunto de treino e teste.

O arquivo `download_files.sh` foi o arquivo fornecido pelo Rafael, com uma pequena modificação que deletava os arquivos `.tar.gz` após a descompactação.

Por fim, usamos os arquivos `find_files.py` e `find_files_subset.py` para criar uma pasta para cada categoria e depois copiar as imagens para suas respectivas pastas a partir da estrutura de pastas e imagens criadas originalmente pela descompactação dos arquivos `.tar.gz` baixados pelo `download_files.sh`.

## Notebooks de experimentações

Foram gerados diferentes notebooks para os diferentes experimentos realizados. Os nomes dos notebooks indicam sua utilidade.