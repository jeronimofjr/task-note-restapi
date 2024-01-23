# Endpoints para testes manuais

Para realizar os testes, é necessário a biblioteca `httpie`, informações mais profundas de uso e instalação podem ser encontradas aqui [httpie docs](https://httpie.io/docs/cli/installation):

### 1. Inserir uma task

##### Sintaxe
<!--MAIN_BEGIN-->
```bash
http POST http://localhost:8000/tasks title={title} description={description}
```
<!--MAIN_END-->

##### Exemplo
<!--MAIN_BEGIN-->
```bash
http POST http://localhost:8000/tasks title='ETL' description='Finalizar método de validação de schema'
```
<!--MAIN_END-->

### 2. Inserir tasks via upload de arquivo csv

##### Sintaxe
<!--MAIN_BEGIN-->
```bash
http --form POST http://localhost:8000/tasks/upload file@{filename}.csv
```
<!--MAIN_END-->

##### Exemplo
<!--MAIN_BEGIN-->
```bash
http --form POST http://localhost:8000/tasks/upload file@'/home/jr/Música/tasks'.csv
```
<!--MAIN_END-->

### 3. Recuperar todas as tasks

##### Sintaxe
<!--MAIN_BEGIN-->
```bash
http GET http://localhost:8000/tasks
```
<!--MAIN_END-->

### 4. Recuperar task por id

##### Sintaxe
<!--MAIN_BEGIN-->
```bash
http GET http://localhost:8000/tasks/{id}
```
<!--MAIN_END-->

### 5. Recuperar task por data

##### Sintaxe
<!--MAIN_BEGIN-->
```bash
http GET http://localhost:8000/tasks/date/{date}
```
<!--MAIN_END-->

### 6. Deletar task por id

##### Sintaxe
<!--MAIN_BEGIN-->
```bash
http DELETE http://localhost:8000/tasks/{id}
```
<!--MAIN_END-->

### 7. Deletar tasks que já foram completadas

##### Sintaxe
<!--MAIN_BEGIN-->
```bash
http DELETE http://localhost:8000/tasks/complete
```
<!--MAIN_END-->

### 8. Deletar todas as tasks

##### Sintaxe
<!--MAIN_BEGIN-->
```bash
http DELETE http://localhost:8000/tasks
```
<!--MAIN_END-->


### 9. Marcar task como completa

##### Sintaxe
<!--MAIN_BEGIN-->
```bash
http PATCH http://localhost:8000/tasks/{id}/complete
```
<!--MAIN_END-->

### 10. Atualizar task a partir do id

##### Sintaxe
<!--MAIN_BEGIN-->
```bash
http PUT http://localhost:8000/tasks/{id} title={title} description={description}
```
<!--MAIN_END-->

##### Exemplo
<!--MAIN_BEGIN-->
```bash
http PUT http://localhost:8000/tasks/3 title='Terminar tarefa de FUP' description=' Estudar conceitos de matrizes e sua sintaxe na Linguagem C'
```
<!--MAIN_END-->


### 11. Retornar stats relacionadas as tasks armazenadas

##### Sintaxe
<!--MAIN_BEGIN-->
```bash
http GET http://localhost:8000/tasks/resume/
```
<!--MAIN_END-->

### 12. Salvar tasks incompletas em arquivo CSV

##### Sintaxe
<!--MAIN_BEGIN-->
```bash
http GET http://localhost:8000/tasks/save?file_path={''}
```
<!--MAIN_END-->

##### Exemplo
<!--MAIN_BEGIN-->
```bash
http GET http://localhost:8000/tasks/save?file_path='/home/jr/Documentos/tasks.csv'
```
<!--MAIN_END-->

