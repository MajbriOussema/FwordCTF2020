FROM ubuntu:19.10
#docker build -t blacklist .
#docker run -it -d -p 1234:4477 blacklist
RUN apt-get upgrade
RUN apt-get update

RUN useradd -d /home/elizabeth/ -m -p elizabeth -s /bin/bash elizabeth
RUN useradd -d /home/fbi/ -m -p fbi -s /bin/bash fbi

RUN echo "fbi:fbi" | chpasswd

RUN dpkg --add-architecture i386 && \
    apt-get -y update && \
    apt install -y \
    libc6:i386 \
    libc6-dbg:i386 \
    libc6-dbg \
    lib32stdc++6 \
    g++-multilib
    
WORKDIR /home/fbi
COPY ynetd .
COPY blacklist .
COPY flag.txt .

RUN chown -R root:root /home/fbi

USER fbi
CMD ./ynetd -p 4477 ./blacklist
