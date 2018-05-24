Summary: runit packaged for use with Docker
Name: docker-runit
Version: 2.1.2
Release: 1.lc%{?dist}
License: BSD
Source0: http://smarden.org/runit/runit-2.1.2.tar.gz
Source1: init.docker-runit
URL: http://smarden.org/runit/
Patch0: runit-fix-utmpset.patch
Patch1: runit-nostatic.patch

%description
A UNIX init scheme with service supervision.

%prep
%setup -q -n admin/runit-2.1.2
%patch0 -p2
%patch1 -p2

%build
./package/compile

%install
mkdir -p ${RPM_BUILD_ROOT}/usr/sbin
cp -av command/* ${RPM_BUILD_ROOT}/usr/sbin
cp -av %{SOURCE1} ${RPM_BUILD_ROOT}/usr/sbin

mkdir -p ${RPM_BUILD_ROOT}/usr/share/man/man8
cp -av man/* ${RPM_BUILD_ROOT}/usr/share/man/man8

mkdir -p ${RPM_BUILD_ROOT}/service

%files
%doc package/README
%license package/COPYING
%dir /service
/usr/sbin/chpst
/usr/sbin/runit
/usr/sbin/runit-init
/usr/sbin/runsv
/usr/sbin/runsvchdir
/usr/sbin/runsvdir
/usr/sbin/sv
/usr/sbin/svlogd
/usr/sbin/utmpset
/usr/sbin/init.docker-runit
/usr/share/man/man8/svlogd.8.gz
/usr/share/man/man8/runsvdir.8.gz
/usr/share/man/man8/runsv.8.gz
/usr/share/man/man8/chpst.8.gz
/usr/share/man/man8/runit.8.gz
/usr/share/man/man8/utmpset.8.gz
/usr/share/man/man8/runsvchdir.8.gz
/usr/share/man/man8/runit-init.8.gz
/usr/share/man/man8/sv.8.gz
