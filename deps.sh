#!/bin/sh -ex

# disable fastestmirror plugin
cat <<EOF > /etc/yum/pluginconf.d/fastestmirror.conf
[main]
enabled=0
EOF

# add CentOS 7 GPG key
rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7

# pull in latest updates
yum -y update

# install build dependencies
yum install -y gcc make rpm-build
