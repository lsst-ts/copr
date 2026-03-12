Name:           gphoto2
Version:        2.5.27
Release:        1%{?dist}
Summary:        Command line interface to libgphoto2
License:        LGPL
URL:            http://www.gphoto.org/

Source0:        http://github.com/gphoto/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.bz2

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  libgphoto2-devel
BuildRequires:  popt-devel
BuildRequires:  libjpeg-devel
BuildRequires:  pkgconfig(libexif)

%description
gphoto2 is a command line client to for the libgphoto2. It allows to
use gPhoto software from a terminal or from a script shell to perform
any camera operation that can be done. This is the main user interface.

%prep
rm -rf "${RPM_BUILD_DIR}/%{name}-%{version}"

%setup -q -n %{name}-%{version}

%build
%configure
make

%install
rm -rf "${RPM_BUILD_ROOT}"
make DESTDIR=%{?buildroot:%{buildroot}} install

%files
%defattr(-,root,root)
%{_bindir}/gphoto2
%{_mandir}/man1/*
%{_datadir}/locale/*
/usr/share/doc/%{name}/test-hook.sh
