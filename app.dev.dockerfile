FROM debian

RUN apt update
RUN apt install -y python3 python3-pip python3-venv
