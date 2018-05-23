#!/bin/sh -ex

# download source
mkdir -p /root/rpmbuild/SOURCES
cd /root/rpmbuild/SOURCES
curl -O http://smarden.org/runit/runit-2.1.2.tar.gz
echo '398f7bf995acd58797c1d4a7bcd75cc1fc83aa66  runit-2.1.2.tar.gz' | sha1sum -c

# build package
rpmbuild -bb /root/rpmbuild/SPECS/docker-runit.spec
