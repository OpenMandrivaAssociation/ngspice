%define __libtoolize	/bin/true

%define major		0
%define	docname		ngspice-doc
%define libname		%mklibname %{name} %{major}
%define develname	%mklibname %{name} -d

Summary:	Mixed Mode - Mixed Level Circuit Simulator Based On Berkley's spice3f5
Name:		ngspice
Version:	30
Release:	2
License:	GPL and GPLv2 and LGPLv2 and BSD
Group:		System/Libraries
Url:		http://ngspice.sourceforge.net/index.html
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source1:	http://downloads.sourceforge.net/%{name}/%{docname}-%{version}.tar.gz
Source100:	%{name}.rpmlintrc

BuildRequires:	xaw-devel
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	readline-devel

%description
Ngspice is a mixed-level/mixed-signal circuit simulator. Its code is 
based on three open source software packages: Spice3f5, Cider1b1 and
Xspice. It is the open source successor of these venerable packages.
Many, many modifications, bug fixes and improvements have been added
to the code, yielding a stable and reliable simulator. Therefore,
besides being used as a standalone simulator, Ngspice has been
incorporated into many projects, see our simulation environments
page.

%package -n %{libname}
Summary:	Main library for %{name}
Group:		System/Libraries

%description -n %{libname}
This package contains the library needed to run programs dynamically
linked with %{name}.

%package -n %{develname}
Summary:	Headers for developing programs that will use %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}
Provides:	%{name}%{major}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{develname}
This package contains the headers that programmers will need to develop
applications which will use %{name}.

%prep
%setup -q -a 1

%build
# Cannot enable CIDER and adms due to there licences
# see https://sourceforge.net/p/ngspice/ngspice/ci/master/tree/COPYING
%configure \
	--with-ngshared \
	--enable-xspice \
	--with-readline=yes \
	--disable-cider \
	--disable-adms \
	--disable-debug
%make_build

%install
%make_install

%files
%{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/ngspice/scripts/*
%{_datadir}/ngspice/dlmain.c

%files -n %{libname}
%{_libdir}/lib*.so.%{major}*
%{_libdir}/ngspice/*

%files -n %{develname}
%{_libdir}/lib*.so
%{_includedir}/*
%{_libdir}/pkgconfig/*.pc
