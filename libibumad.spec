#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libibumad
Version  : 1.3.10.2
Release  : 3
URL      : https://www.openfabrics.org/downloads/management/libibumad-1.3.10.2.tar.gz
Source0  : https://www.openfabrics.org/downloads/management/libibumad-1.3.10.2.tar.gz
Summary  : OpenFabrics Alliance InfiniBand umad (user MAD) library
Group    : Development/Tools
License  : BSD-2-Clause GPL-2.0
Requires: libibumad-lib
Requires: libibumad-doc

%description
libibumad provides the user MAD library functions which sit on top of
the user MAD modules in the kernel. These are used by the IB diagnostic
and management tools, including OpenSM.

%package dev
Summary: dev components for the libibumad package.
Group: Development
Requires: libibumad-lib
Provides: libibumad-devel

%description dev
dev components for the libibumad package.


%package doc
Summary: doc components for the libibumad package.
Group: Documentation

%description doc
doc components for the libibumad package.


%package lib
Summary: lib components for the libibumad package.
Group: Libraries

%description lib
lib components for the libibumad package.


%prep
%setup -q -n libibumad-1.3.10.2

%build
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/infiniband/umad.h
/usr/include/infiniband/umad_cm.h
/usr/include/infiniband/umad_sa.h
/usr/include/infiniband/umad_sm.h
/usr/include/infiniband/umad_str.h
/usr/include/infiniband/umad_types.h
/usr/lib64/*.so

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man3/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/*.so.*
