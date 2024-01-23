# Endpoints para testes manuais

Para realizar os testes, é necessário a biblioteca `httpie`, informações mais profundas de uso e instalação podem ser encontradas aqui [httpie docs](https://httpie.io/docs/cli/installation):

### 1. Inserir uma task

<!--MAIN_BEGIN-->
```bash
http POST http://localhost:8000/tasks title={title} description={description}
```
<!--MAIN_END-->

### 2. Inserir tasks via upload de arquivo csv

<!--MAIN_BEGIN-->
```bash
http --form POST http://localhost:8000/tasks/upload file@{filename}.csv
```
<!--MAIN_END-->


### 3. Recuperar todas as tasks

<!--MAIN_BEGIN-->
```bash
http GET http://localhost:8000/tasks
```
<!--MAIN_END-->

### 4. Recuperar task por id

<!--MAIN_BEGIN-->
```bash
http GET http://localhost:8000/tasks/{id}
```
<!--MAIN_END-->

### 5. Recuperar task por data

<!--MAIN_BEGIN-->
```bash
http GET http://localhost:8000/tasks/date/{date}
```
<!--MAIN_END-->

### 6. Deletar task por id

<!--MAIN_BEGIN-->
```bash
http DELETE http://localhost:8000/tasks/{id}
```
<!--MAIN_END-->

### 7. Deletar tasks que já foram completadas

<!--MAIN_BEGIN-->
```bash
http DELETE http://localhost:8000/tasks/complete
```
<!--MAIN_END-->

### 8. Deletar todas as tasks

<!--MAIN_BEGIN-->
```bash
http DELETE http://localhost:8000/tasks
```
<!--MAIN_END-->


### 9. Marcar task como completa

<!--MAIN_BEGIN-->
```bash
http PATCH http://localhost:8000/tasks/{id}/complete
```
<!--MAIN_END-->

### 10. Atualizar task a partir do id

<!--MAIN_BEGIN-->
```bash
http PUT http://localhost:8000/tasks/id title={title} description={description}
```
<!--MAIN_END-->

### 11. Retornar stats relacionadas as tasks armazenadas

<!--MAIN_BEGIN-->
```bash
http GET http://localhost:8000/tasks/resume/
```
<!--MAIN_END-->

### 12. Salvar tasks incompletas em arquivo CSV

<!--MAIN_BEGIN-->
```bash
http GET http://localhost:8000/tasks/save?file_path={''}
```
<!--MAIN_END-->


