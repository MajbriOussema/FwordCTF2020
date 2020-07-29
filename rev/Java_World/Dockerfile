FROM ubuntu:19.10

RUN useradd -d /home/fword/ -m -p fbi -s /bin/bash fword
RUN echo "fword:fword" | chpasswd

RUN apt-get upgrade && \
    apt-get update && \
    DEBIAN_FRONTEND=noninteractive \
    apt-get -y install default-jre-headless && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN chown -R root:root /home/fword
WORKDIR /home/fword
COPY run.sh .
COPY password.txt .
COPY flag.txt .
COPY java_world.class .
COPY run.sh .
COPY ynetd .

USER fword
CMD ./ynetd -p 4477 ./run.sh