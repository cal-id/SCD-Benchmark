#! /bin/bash

# Install IMB PingPong
sudo yum -y install openmpi-devel  # install OpenMPI
wget https://software.intel.com/sites/default/files/managed/a3/53/IMB_2017.tgz
tar -xvf IMB_2017.tgz
source /etc/profile.d/modules.sh   # enable environment-modules
module load openmpi-1.10-x86_64    # load the MPI module
cd imb/imb/src
make CC=mpicc                  # compile
cd -

# Install HPL
wget http://www.netlib.org/benchmark/hpl/hpl-2.2.tar.gz
tar -xvf hpl-2.2.tar.gz
sudo yum -y install openblas-devel openblas-static # install OpenBLAS
cd hpl-2.2/
# Copy in the makefile from the appendix now.
make arch=Linux_SL6_Intel64                        # compile
