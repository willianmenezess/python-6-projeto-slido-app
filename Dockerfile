# essa imagem é mais pesada, mas é mais completa e tem mais ferramentas
FROM python:3.10-slim

# para garantir que as saídas do Python sejam exibidas imediatamente no terminal
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# instalando as dependências do sistema operacional necessárias para instalar o mysqlclient
RUN apt update \
    && apt install -y python3-dev netcat-openbsd default-libmysqlclient-dev build-essential pkg-config \
    && pip install --upgrade pip

COPY ./requirements.txt ./

RUN pip install -r requirements.txt

COPY ./ ./

# Poderia ser: CMD ["python", "manage.py", "runserver"]
# parâmetro --bind do gunicorn para definir o endereço e porta que o servidor irá escutar
# CMD ["gunicorn", "slido_project.wsgi", "--bind", "0.0.0.0:8000"]

# Nesse caso, estamos definindo que o gunicorn irá escutar na porta 8000 de todas as interfaces de rede (0.0.0.0). Essa configuração será essencial para nossa aplicação ser acessível no Railway.

CMD ["sh", "entrypoint.sh"]