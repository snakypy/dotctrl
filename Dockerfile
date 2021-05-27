FROM python:3
USER root
WORKDIR /snakypy/dotctrl
ENV LOCAL_BIN=/root/.local/bin
RUN apt-get update \
&& apt-get install zsh vim -y \
&& export PATH=$PATH:$LOCAL_BIN \
&& pip install poetry \
&& rm -rf /var/cache/apt/*
ADD . /snakypy/dotctrl
RUN cd /snakypy/dotctrl \
&& poetry install
CMD poetry shell
