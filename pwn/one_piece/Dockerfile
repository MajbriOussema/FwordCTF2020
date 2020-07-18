FROM ubuntu:19.10
#docker build -t one_piece .
#docker run -it -d -p 1234:4477 one_piece
RUN apt-get upgrade
RUN apt-get update

RUN useradd -d /home/fword/ -m -p fword -s /bin/bash fword
RUN echo "fword:fword" | chpasswd

RUN dpkg --add-architecture i386 && \
    apt-get -y update && \
    apt install -y \
    libc6:i386 \
    libc6-dbg:i386 \
    libc6-dbg \
    lib32stdc++6 \
    g++-multilib

WORKDIR /home/fword
COPY one_piece .
COPY flag.txt .
COPY ynetd .

RUN chown -R root:root /home/fword
USER fword
CMD ./ynetd -p 4477 ./one_piece
