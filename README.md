# Visualizando os Notebooks
https://app.reviewnb.com/tiagodeliberali/mdc-tcc


# Datas importantes
Apresentação Parcial **(10/08/2019): 20% da nota**.
 - A Apresentação Parcial será feita de forma oral (4 a 5 minutos), com auxílio de slides (entre 5 e 10).
 - A Apresentação Parcial será avaliada pelo professor e pelos monitores.
 - O coordenador de cada grupo deverá submeter no Moodle um arquivo PDF com a apresentação
parcial, até dia 09/08/2019.

Apresentação Final **(24/08/2019): 80% da nota**.
 - A Apresentação Final será feita por vídeos de 4 a 5 minutos, preparados por cada grupo, que serão
exibidos para a turma no dia 24/08/2019.
 - A nota da Apresentação Final será dada pela média simples de duas notas: a média das notas da
Banca de Avaliação (composta pelo professor e pelos monitores) e a média das notas dos alunos.
 - Para cada projeto haverá notas bônus para as apresentações e para as avaliações realizadas pelos
alunos.
 - As apresentações serão publicadas no canal YouTube do curso (http://bit.ly/youtube-mdc).
 - O coordenador de cada grupo deverá submeter no Moodle um arquivo compactado (zip) contendo
um relatório (máximo de 10 páginas em formato PDF) e todos os arquivos fontes usados na realização
do projeto, devidamente documentados, até dia 23/08/2019.

# Fruits-360

## Descrição do projeto
Esse conjunto de dados é composto de imagens de diversas frutas para classificação.

### Objetivo Principal
Classificar corretamente as frutas contidas nas imagens.

### Técnicas Envolvidas
 - Classificação multi-classe.
 -  Técnicas para análise de imagem.

### Desafios
Para esse projeto, alguns desafios são:
 -  Classificação de 64 tipos de frutas no total.
 -  Montar uma rede capaz de identificar características nas imagens para identificar frutas de diferentes tipos.


### Conjunto de Dados
 -  http://bit.ly/mdc-fruits360
 -  https://www.kaggle.com/moltean/fruits


## Extra Info
The following fruits are included: Apples (different varieties: Crimson Snow, Golden, Golden-Red, Granny Smith, Pink Lady, Red, Red Delicious), Apricot, Avocado, Avocado ripe, Banana (Yellow, Red, Lady Finger), Cactus fruit, Cantaloupe (2 varieties), Carambula, Cherry (different varieties, Rainier), Cherry Wax (Yellow, Red, Black), Chestnut, Clementine, Cocos, Dates, Granadilla, Grape (Blue, Pink, White (different varieties)), Grapefruit (Pink, White), Guava, Hazelnut, Huckleberry, Kiwi, Kaki, Kohlrabi, Kumsquats, Lemon (normal, Meyer), Lime, Lychee, Mandarine, Mango, Mangostan, Maracuja, Melon Piel de Sapo, Mulberry, Nectarine, Orange, Papaya, Passion fruit, Peach (different varieties), Pepino, Pear (different varieties, Abate, Kaiser, Monster, Red, Williams), Pepper (Red, Green, Yellow), Physalis (normal, with Husk), Pineapple (normal, Mini), Pitahaya Red, Plum (different varieties), Pomegranate, Pomelo Sweetie, Quince, Rambutan, Raspberry, Redcurrant, Salak, Strawberry (normal, Wedge), Tamarillo, Tangelo, Tomato (different varieties, Maroon, Cherry Red, Yellow), Walnut.

### Dataset properties

Total number of images: 71125.

Training set size: 53177 images (one fruit per image).

Test set size: 17845 images (one fruit per image).

Multi-fruits set size: 103 images (more than one fruit (or fruit class) per image)

Number of classes: 103 (fruits).

Image size: 100x100 pixels.

Filename format: image_index_100.jpg (e.g. 32_100.jpg) or r_image_index_100.jpg (e.g. r_32_100.jpg) or r2_image_index_100.jpg or r3_image_index_100.jpg. "r" stands for rotated fruit. "r2" means that the fruit was rotated around the 3rd axis. "100" comes from image size (100x100 pixels).

Different varieties of the same fruit (apple for instance) are stored as belonging to different classes.

## Download dataset
`kaggle datasets download -d moltean/fruits`

http://bit.ly/mdc-fruits360

https://www.kaggle.com/moltean/fruits


# Landmark Recognition

## Descrição do projeto
Esse conjunto de dados é composto de imagens de pontos de referência (landmarks) naturais ou feitos pelo homem
espalhados pelo mundo.

### Objetivo Principal
Identificar corretamente o landmark retratado na imagem.

### Técnicas Envolvidas
 - Classificação multi-classe.
 - Clusterização.
 - Técnicas para análise de imagem.

### Desafios
Para esse projeto, alguns desafios são:
 - Lidar com a grande quantidade de imagens capturadas em diferentes condições (iluminação, ruído, ângulos).
 - Classificar a imagem entre 100 possíveis categorias.
 - Agrupar landmarks visualmente semelhantes.
 
### Conjunto de Dados
 - https://github.com/cvdfoundation/google-landmark
 - http://bit.ly/mdc-landmark
 - https://www.kaggle.com/c/landmark-recognition-2019

 
## Dados processados
./azcopy copy "https://landmarkdata.blob.core.windows.net/landmarks/?sv=2018-03-28&ss=bfqt&srt=sco&sp=rwdlacup&st=2018-08-04T00%3A00%3A00Z&se=2025-08-05T00%3A00%3A00Z&sig=5OGK9y1MLco0gmF30J2IxerMBzWOZfDME31inzAQDYU%3D" "/media/slow/data" --recursive=true
 
## Extra info
(Marcio)
Eu conversei um pouco com o Rafael sobre o projeto avançado. Segue resumo do que foi conversado.

1. temos 500 arquivos tar com imagens para treino. cada arquivo tar tem 1GB totalizando 500GB de imagens para treino. total de imagens para treino 4.132.914
2. cada arquivo .tar traz uma série de diretórios.
3. cada diretório tem mais de uma classe de imagens.
4. O arquivo train.csv tem a lista de todas as imagens e suas respectivas classes.
5. as classes são números e não textos.
6. importei o arquivo train.csv para um pandas dataframe. analisando o arquivo train.csv, identifiquei 203.094 classes distintas "len(df.landmark_id.unique())"
7. entre estas 203.094 classes, fica a nosso critério selecionar a quantidade de classes (recomendado 150 classes) bem como a quantidade de imagens por classe. priorizar as classes que tem mais imagens.
8. temos que segregar as imagens selecionadas entre treino, validação
9. temos 20 arquivos tar com imagens para teste. cada arquivo tar tem 500MB totalizando 10GB de imagens para teste. total de imagens para teste 117.577
10. temos que montar um diretório para cada classe selecionada. as imagens ficarão agrupadas nesses diretórios.
11. treinar um modelo que seja capaz de classificar a imagem corretamente. podemos fazer também clusterização.

O site abaixo detalha bem o dataset deste projeto.
https://github.com/cvdfoundation/google-landmark


Tem um outro conjunto de dados mais enxuto 52GB que podemos utilizar para estrutura a solução...mas este conjunto não pode ser utilizado no trabalho final. ele serve apenas para entendermos os dados.
https://www.kaggle.com/c/landmark-recognition-2019/discussion/91770#latest-537550

O link para fazer o donwload do arquivo tar de 52GB é esse.
https://drive.google.com/uc?id=10yVowvmFjMkY21-DGF2pej_Lbecfqou7
