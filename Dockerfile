FROM python:3
USER root
WORKDIR /dotctrl
ENV LOCAL_BIN=/root/.local/bin
RUN apt-get update \
&& apt-get install zsh vim -y \
&& export PATH=$PATH:$LOCAL_BIN \
&& pip install poetry \
&& rm -rf /var/cache/apt/*
ADD . /dotctrl
RUN cd /dotctrl \
&& poetry install \
&& chmod +x docker.sh
CMD poetry shell
