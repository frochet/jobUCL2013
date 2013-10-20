#!/bin/sh
cat >> packetdrill.sh <<EOF
#!/bin/bash
cd /root
wget https://packetdrill.googlecode.com/archive/ea8f2fec724dfc0342dd007eac1c69bc3a2f0067.zip

unzip ea8f2fec724dfc0342dd007eac1c69bc3a2f0067.zip
mv packetdrill-ea8f2fec724d packetdrill
cd packetdrill/getests/net/packetdrill/
./configure
make
EOF
chmod +x packetdrill.sh



