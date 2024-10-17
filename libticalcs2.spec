%define major 10
%define libname %mklibname ticacls2
%define develname %mklibname ticalcs2 -d

Name: libticalcs2
Version: 1.1.7
Release: 1
Url: https://sourceforge.net/projects/tilp
Source0: http://downloads.sourceforge.net/project/tilp/tilp2-linux/tilp2-1.16/%{name}-%{version}.tar.bz2
Group: System/Libraries
License: GPLv2+
BuildRequires: libusb1-devel, glib2-devel
BuildRequires: autoconf pkgconfig(ticonv) pkgconfig(libusb) pkgconfig(tifiles2)
Requires: udev >= 154
Summary: Library for communication with TI calculators
%description
Library for communication with TI calculators

%package  -n %develname
Summary: Development files for %{name}
Group: Development/C
Requires: %libname = %{version}-%{release}
Provides: ticalcs2-devel = %{version}-%{release} 

%description -n %develname
This package contains the files necessary to develop applications using the
%{name} library.

%package  -n %libname
Summary: Development files for %{name}
Group: System/Libraries

%description -n %libname
This package contains the files necessary to develop applications using the
%{name} library.

%prep
%setup -q
autoreconf -i -f

%build
%configure2_5x
%make

%install
%makeinstall_std
rm -f %buildroot%{_libdir}/*.la



%files -n %libname
%{_libdir}/libticalcs2.so.%{major}*

%files -n %develname
%{_includedir}/tilp2
%{_libdir}/libticalcs2.so
%{_libdir}/pkgconfig/ticalcs2.pc
%{_datadir}/locale/fr/LC_MESSAGES/libticalcs2.mo
