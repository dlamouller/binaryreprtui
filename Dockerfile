FROM ubuntu:22.04

RUN apt update
ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=Europe/Paris
RUN apt --yes upgrade \
&& apt --yes install software-properties-common \
&& add-apt-repository ppa:deadsnakes/ppa

RUN apt install -y --no-install-recommends build-essential checkinstall tzdata curl
RUN apt install -y python3-pip
RUN apt install -y python3.7 python3.7-distutils python3.7-dev 
RUN apt install -y python3.8 python3.8-distutils python3.8-dev 
RUN apt install -y python3.9 python3.9-distutils python3.9-dev 
RUN apt install -y python3.10 python3.10-distutils python3.10-dev
RUN apt install -y python3.11 python3.11-distutils python3.11-dev
RUN apt install -y python3.12 python3-setuptools python3.12-dev

# Download and execute get-pip.py for installing pip et setuptools
RUN curl https://bootstrap.pypa.io/pip/3.7/get-pip.py -o get-pip.py && \
    python3.7 get-pip.py && \
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py && \
    python3.8 get-pip.py && \
    python3.9 get-pip.py && \
    python3.10 get-pip.py && \
    python3.11 get-pip.py && \
    python3.12 get-pip.py && \
    rm get-pip.py

# update pip
RUN python3.7 -m pip install --upgrade pip setuptools && \
    python3.8 -m pip install --upgrade pip setuptools && \
    python3.9 -m pip install --upgrade pip setuptools && \
    python3.10 -m pip install --upgrade pip setuptools && \
    python3.11 -m pip install --upgrade pip setuptools && \
    python3.12 -m pip install --upgrade pip setuptools

WORKDIR /app
COPY . .

# pyhton3 is python3.10
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip --no-cache-dir install tox pytest flake8 typing-extensions


# Install tox end dependency with pip Python 3.7
RUN python3.7 -m pip --no-cache-dir install tox "typing-extensions<4.6.0" pytest flake8
RUN python3.7 -m pip install --upgrade importlib-metadata

RUN python3.8 -m pip --no-cache-dir install flake8 && \
    python3.9 -m pip --no-cache-dir install flake8 && \
    python3.11 -m pip --no-cache-dir install flake8 && \
    python3.12 -m pip --no-cache-dir install flake8

ENTRYPOINT ["tox"]
