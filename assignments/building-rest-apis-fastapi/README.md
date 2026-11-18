# 📘 Atividade: Building REST APIs com FastAPI

## 🎯 Objetivo

Crie uma API REST de catálogo de livros com FastAPI, praticando rotas HTTP, validação de dados e parâmetros de caminho. A atividade começa com um endpoint simples e evolui para operações de criação, consulta, atualização e remoção de recursos.

## 📝 Tarefas

### 🛠️ Criar o endpoint inicial

#### Descrição
Instale as dependências com `python -m pip install fastapi uvicorn` e execute o código inicial usando `uvicorn main:app --reload`. Implemente uma rota inicial para confirmar que a API está funcionando.

#### Requisitos
O programa concluído deve:

- Responder a uma requisição `GET /` com uma mensagem em JSON indicando que a API de livros está pronta.
- Iniciar sem erros e disponibilizar a documentação interativa do FastAPI em `/docs`.

### 🛠️ Listar e cadastrar livros

#### Descrição
Use os modelos Pydantic e o armazenamento em memória do código inicial para implementar as rotas da coleção de livros.

#### Requisitos
O programa concluído deve:

- Responder a `GET /books` com a lista de livros cadastrados, começando com uma lista vazia.
- Aceitar `POST /books` com um título e um autor, atribuir um ID único e retornar o livro criado.
- Validar o corpo da requisição com um modelo Pydantic.
- Aceitar um corpo como este para cadastrar um livro:

  ```json
  {
    "title": "The Hobbit",
    "author": "J. R. R. Tolkien"
  }
  ```

### 🛠️ Gerenciar um livro pelo ID

#### Descrição
Implemente rotas para consultar, atualizar e remover um livro específico usando seu ID como parâmetro de caminho.

#### Requisitos
O programa concluído deve:

- Responder a `GET /books/{book_id}` com o livro correspondente ao ID informado.
- Aceitar `PUT /books/{book_id}` para atualizar o título e o autor do livro.
- Aceitar `DELETE /books/{book_id}` para remover o livro.
- Retornar o status HTTP `404` quando o ID solicitado não existir.
