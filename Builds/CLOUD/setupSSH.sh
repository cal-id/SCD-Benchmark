# On both VMs
sudo chown $USER:root ~/.ssh # Cloud VMs start with root:root, allow yourself access

# On one
ssh-keygen -t rsa # create key pair
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys # allow access to key
scp ~/.ssh/* <other VM hostname>:~/.ssh/ # copy this setup to the other machine
