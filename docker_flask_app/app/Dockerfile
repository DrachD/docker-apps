FROM ubuntu:latest
LABEL maintainer="drachdmitriy21@gmail.com"
RUN apt-get update -y && \
    apt-get install -y \
    python3-pip \
    python3-dev \
    python3-venv \
    build-essential
RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
RUN mkdir -p /tmp
COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt
COPY app.py .
WORKDIR /app
EXPOSE 5000
CMD ["python3", "/app.py"]