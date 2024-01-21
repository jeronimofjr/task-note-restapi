
### Recuperar todas as tasks

http GET http://localhost:8000/tasks

### Recuperar task por id

http GET http://localhost:8000/tasks/{id}

### Deletar task por id

http DELETE http://localhost:8000/tasks/{id}

### Deletar tasks que já foram completadas

http DELETE http://localhost:8000/tasks/complete

### Marcar task como completada

http PATCH http://localhost:8000/tasks/{id}/complete

### Inserir uma task

http POST http://localhost:8000/tasks title={title} description={description}

### Inserir tasks via upload de arquivo csv

http --form POST http://localhost:8000/tasks/upload file@{filename}.csv

### Atualizar Task com ID

http PUT http://localhost:8000/tasks/id title={title} description={description}

### Recuperar task por data

http GET http://localhost:8000/tasks/date/{date}




