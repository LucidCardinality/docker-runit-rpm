FROM centos:7

COPY deps.sh /
RUN sh -ex /deps.sh && rm -v /deps.sh

COPY docker-runit.spec /root/rpmbuild/SPECS/

COPY runit-fix-utmpset.patch /root/rpmbuild/SOURCES/
COPY runit-nostatic.patch /root/rpmbuild/SOURCES/
COPY init.docker-runit /root/rpmbuild/SOURCES/

COPY build.sh /
RUN sh -ex /build.sh && rm -v /build.sh
