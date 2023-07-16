FROM python:3.8.10-slim-buster
ENV DOCKER_CONTAINER true
COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY . ./checknews_backend
USER root
WORKDIR /checknews_backend
EXPOSE 9001
RUN chmod +x docker_entrypoint.sh
ENTRYPOINT ["./docker_entrypoint.sh"]
