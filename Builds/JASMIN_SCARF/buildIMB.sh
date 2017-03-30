#! /bin/bash

# Install IMB PingPong
wget https://software.intel.com/sites/default/files/managed/a3/53/IMB_2017.tgz
tar -xvf IMB_2017.tgz
cd imb/imb/src
gmake CC=mpicc
