#!/bin/sh -e
docker build -t docker-runit-rpm .
docker run --name docker-runit-rpm docker-runit-rpm:latest /bin/true
docker cp docker-runit-rpm:/root/rpmbuild/RPMS/x86_64/docker-runit-2.1.2-2.lc.el7.x86_64.rpm .
docker rm docker-runit-rpm
