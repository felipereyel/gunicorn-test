FROM --platform=linux/x86_64 debian:11.3-slim AS base

ENV DEBIAN_FRONTEND noninteractive
ENV PORT 8002
ENV WORKERS 2
ENV THREADS 20

# Install system dependencies
RUN apt-get update -y --fix-missing
RUN apt-get install -y python3 python3-pip python3-venv python3-distutils git curl

# Install extra dependencies before implementing presets
RUN apt-get install --no-install-suggests --no-install-recommends -y poppler-utils ffmpeg libsm6 libxext6

# Setup Python
ENV VIRTUAL_ENV=/opt/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN ln -sf python3 /usr/bin/python && ln -sf pip3 /usr/bin/pip
RUN pip install --no-cache-dir --upgrade pip
RUN python -m venv $VIRTUAL_ENV

# Setup user
RUN groupadd -r -g 3000 python-group
RUN useradd --no-log-init --create-home -r -g python-group -u 3000 python-user

COPY ./atest-lib /atest-lib
RUN pip install --no-cache-dir --compile /atest-lib

COPY consume.py .

CMD exec python -u -m atest.cloud
