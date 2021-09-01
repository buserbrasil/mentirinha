# Mentirinha - porque a mentira tem URL curta

**Mentirinha** é um encurtador de URL ultra-minimalista feito em Django. Tudo que ele expõe é um Django Admin na url 
`/admin/`, com uma única classe customizada, a `ShortenedUrl`, que guarda um `shortcode` e a URL original a ser
redirecionada. Após salvar um objeto novo, basta acessar `seu-dominio-curti.nho/shortcode` e será redirecionado.

## O que o Mentirinha faz?

- encurta URLs dentro do seu domínio;
- redireciona quem acessa `seu-dominio/shortcode` com HTTP 301;
- guarda o número de vezes que aquela URL encurtada foi acessada.

## O que o Mentirinha (ainda) NÃO faz?

- não expõe nenhuma API;
- não faz nada inteligente com o número de acessos;
- não possui nenhum tipo de gerenciamento além de um CRUD básico;
- não possui nenhuma tela além do próprio Django Admin;
- não é instalável como um pacote à parte pelo pip.

## Tá bem, mas como eu faço pra usar?

### Docker em produção

A maneira mais simples é usando o `docker`. Suponha que você tem uma máquina EC2 Linux na AWS, com o domínio já 
devidamente configurado, você precisaria de apenas três coisas:
- Um banco de dados Postgres (um RDS na AWS, por exemplo). Recomendo a versão 12;
- Um arquivo `mentirinha.env`, definindo no mínimo as mesmas variáveis de ambiente que o arquivo de exemplo contido
neste repositório;
- O pacote `docker` e `docker-compose` devidamente instalado e funcionando.

Tendo isso, basta apenas executar o comando `docker-compose up -d`.

#### Louco, mas como faço algo com ele se tudo que ele expõe é um Django Admin?

Nesse caso, você pode rodar `docker exec -it mentirinha bash` e ir diretamente para dentro do container rodando o Django.
De lá, você pode executar todos os comandos do `manage.py`, como `./manage.py createsuperuser` para criar seu primeiro
usuário, e `./manage.py migrate` para fazer as migrações iniciais, por exemplo.

Eu falei que ele era ultra-minimalista, não falei?

### Docker local

Esse é fácil. Se você tem o `docker` instalado e configurado na sua máquina, basta clonar este repositório e, de dentro
da pasta `docker`, executar no terminal o comando `docker-compose up`. Ele vai criar e subir um container de `postgres` 12
na porta 5432 com o usuário *mentira* e senha *mentira*, salvando todos os dados em um volume persistente na pasta `dkdata`,
e um outro container que constrói a imagem do Mentirinha em si a partir da Dockerfile do repositório e o sobe na porta 8000.

### Local com Python

Este método é o indicado caso você queira desenvolver o Mentirinha em si (você quer mesmo? Eba!). Primeiro, clone este
repositório para a sua máquina. Depois, certifique-se de ter o python 3.8.3 instalado na sua máquina. Recomendo **fortemente** 
que você use um gerenciador de versões e um de ambientes virtuais, como o setup fantástico que o Henrique descreve aqui 
no seu blog https://henriquebastos.net/guia-para-organizar-meu-ambiente-python/. Enfim, após ter criado um ambiente 
virtual para o mentirinha com python 3.8.3 (ou não, sua escolha), basta navegar até a pasta do projeto e executar 
`pip install -r requirements.txt`.

O próximo passo é configurar um banco Postgres local (recomendo a versão 12, mas fica a seu critério). Você pode se virar
para instalar e configurar na unha, baixando o pacote e tudo o mais, ou pode de novo apelar para o docker. Neste caso,
basta executar o arquivo `dev.sh` do repositório e depois chamar a função `dkdb`, que vai subir um banquinho na porta 
5432 com o usuário `mentira` e senha `mentira`.

Pronto, você tem tudo o que precisa. Com o banco rodando, basta, dentro da pasta do projeto, executar `./manage.py migrate`
para criar as tabelas no banco e depois `./manage.py runserver` para subir o mentirinha. Acesse em `localhost:8000/admin/`
e *have fun!*

## Roadmap

// todo