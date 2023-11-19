FROM ubuntu:22.04

RUN apt update
ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=Europe/Paris
RUN apt --yes upgrade \
&& apt --yes install software-properties-common \
&& add-apt-repository ppa:deadsnakes/ppa

RUN apt install -y --no-install-recommends build-essential checkinstall tzdata
RUN apt install -y python3-pip
RUN apt install -y python3.7 python3.7-distutils python3.7-dev 
RUN apt install -y python3.8 python3.8-distutils python3.8-dev 
RUN apt install -y python3.9 python3.9-distutils python3.9-dev 
RUN apt install -y python3.10 python3.10 python3.10-dev 
RUN apt install -y python3.11 python3.11 python3.11-dev 
RUN apt install -y python3.12 python3.12 python3.12-dev 

WORKDIR /app
COPY . .

RUN python3 -m pip install --upgrade pip
RUN python3 -m pip --no-cache-dir install tox pytest

ENTRYPOINT ["tox"]
