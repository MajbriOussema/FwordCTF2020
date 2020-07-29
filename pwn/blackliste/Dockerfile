FROM ubuntu:19.10
#docker build -t blacklist .
#docker run -it -d -p 1234:4477 blacklist
RUN apt-get upgrade
RUN apt-get update

RUN useradd -d /home/fbi/ -m -p fbi -s /bin/bash fbi

RUN echo "fbi:fbi" | chpasswd

WORKDIR /home/fbi
COPY ynetd .
COPY blacklist .
COPY aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaanaaaoaaapaaaqaaaraaasaaataaauaaavaaawaaaxaaayaaazaabbaabcaabdaabeaabfaabgaabhaabiaabjaabkaablaabmaabnaaboaabpaabqaabraabsaabtaabuaabvaabwaabxaabyaabzaacbaaccaacdaaceaacfaacgaachaaciaacjaackaaclaacma.txt .

RUN chown -R root:root /home/fbi

USER fbi
CMD ./ynetd -p 4477 ./blacklist 
