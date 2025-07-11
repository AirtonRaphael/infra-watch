# infra-watch

**infra-watch** é uma aplicação para monitoramento de status de sites e endpoints. Através dela, usuários podem cadastrar e administrar endpoints que desejam monitorar, garantindo acompanhamento contínuo da disponibilidade e resposta dos serviços.

---

## Funcionalidades

- Cadastro e gerenciamento de endpoints para monitoramento
- Verificação automática do status dos sites/endpoints cadastrados
- Sistema de autenticação com JWT
- Notificação de ocorrencias via email ou whatsapp (em desenvolvimento)
- Sistema de log de ocorrencias (em desenvolvimento)
- Consumo do log de ocorrencias (em desenvolvimento)
- CLI para consumo da API (em desenvolvimento)

---

## Status do Projeto

O projeto esta em desenvolvimento mas usavel via swagger
---

## Como rodar
1. Clone o repositório:

    ```bash
    git clone https://github.com/seu-usuario/infra-watch.git
    cd infra-watch
    ```
2. Atualize o ```.env```
3. Crie a imagem
    ```bash
    docker build -t infra-watch .
    ```
4. Inicie o container
    ```bash
    docker run -p 8000:8000 infra-watch
    ```
