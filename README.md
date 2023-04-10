# backend-python-creditcard
Desafio para vaga de backend na MaisTodos

### Pré-requisitos

Instale [Docker Compose standalone](https://docs.docker.com/compose/install/other/) ou [Docker Compose plugin](https://docs.docker.com/compose/install/)

execute o programa com Compose standalone

```
docker compose up
```

ou execute o programa com Compose plugin

```
docker-compose up
```

### Teste Unitarios
Com Docker Compose standalone:
```
docker compose exec -it app pytest
```

Com Docker Compose plugin:
```
docker-compose exec -it app pytest
```

### Uso via Curl
- endpoint cadastrar um novo cartão de crédito
```
curl --location 'http://127.0.0.1:8080/api/v1/credit-card' \
--header 'Content-Type: application/json' \
--data '{
    "exp_date": "04/2023",
    "holder": "DVL",
    "number": "4539578763621486",
    "cvv": "123"
}'
```

- endpoint listar os cartões de crédito
```
curl --location 'http://127.0.0.1:8080/api/v1/credit-card'
```

- endpoint detalhe do cartão de crédito
```
curl --location 'http://127.0.0.1:8080/api/v1/credit-card/<id_card>'
```

- endpoint de autenticação e autorização - obter token.
```
curl --location 'http://127.0.0.1:8080/api/v1/auth/token' \
--header 'Content-Type: application/json' \
--data '{
    "username": "admin",
    "password": "admin123"
}'
```

- endpoint de autenticação e autorização - validar token.
```
curl --location 'http://127.0.0.1:8080/api/v1/auth/token/verify' \
--header 'Content-Type: application/json' \
--data '{
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZF91c2VyIjoiMjk5ODQ1YzAtNWQwNy00NmFlLTg2M2ItZDRlOTBkOGVhOTM0IiwidXNlcm5hbWUiOiJhZG1pbiIsImlzX3N0YWZmIjpmYWxzZX0.YUxDsHQMVhOKa2HwMByL-D9JKxLorFooZf3ew7l4c-I"
}'
```

## Author

* **David Lucas** - *Linkedin* - [david-luk4s](https://www.linkedin.com/in/david-lucas-souz4/)