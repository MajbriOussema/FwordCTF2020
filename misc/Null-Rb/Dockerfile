FROM ubuntu:14.04

RUN apt-get update
#RUN apt-get upgrade

RUN useradd -d /home/fword/ -m -p fword -s /bin/bash fword
RUN echo "fword:fword" | chpasswd
RUN DEBIAN_FRONTEND='noninteractive' apt-get install -y Ruby1.9.1-full
RUN apt-get install -y rubygems1.9.1
RUN apt-get install -y Ruby1.9.1-dev
#RUN update-alternatives --install /usr/bin/Ruby ruby /usr/bin/Ruby1.9.1 1

WORKDIR /home/fword
COPY Nil.rb .

RUN chown -R root:root /home/fword
USER fword
CMD /bin/bash