FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y ffmpeg && \
    apt-get clean && \
    sudo apt install python3.12

RUN pip install -r requirements.txt

CMD tail -f /dev/null
