# infra-watch

**infra-watch** é uma aplicação para monitoramento de status de sites e endpoints. Através dela, usuários podem cadastrar e administrar endpoints que desejam monitorar, garantindo acompanhamento contínuo da disponibilidade e resposta dos serviços.

---

## Funcionalidades

- Cadastro e gerenciamento de endpoints para monitoramento (em desenvolvimento)
- Verificação automática do status dos sites/endpoints cadastrados (em desenvolvimento)
- Dashboard simples para visualização dos resultados (em desenvolvimento)
- Sistema de autenticação com JWT
- API RESTful para integração com clientes externos, incluindo CLI (em desenvolvimento)

---

## Status do Projeto

O projeto ainda esta em desenvolvimento

---

## Como rodar?
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
