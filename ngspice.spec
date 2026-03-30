%define __libtoolize	/bin/true

%define major 46
#%%define minor 0
%define	docname		ngspice-doc
%define libname		%mklibname %{name}  
%define develname	%mklibname %{name} -d
%define _disable_ld_no_undefined 1

Summary:	Mixed Mode - Mixed Level Circuit Simulator Based On Berkley's spice3f5
Name:		ngspice
Version:    %{major}%{?minor:.%minor}
Release:	1
# See COPYING for more detail concerning license
License:	BSD-3-Clause AND GPL-2.0-or-later AND LGPL-2.1-or-later
Group:		System/Libraries
URL:		https://ngspice.sourceforge.net/index.html
Source0:    https://downloads.sourceforge.net/project/ngspice/ng-spice-rework/%{major}%{?minor:.%minor}/ngspice-%{major}%{?minor:.%minor}.tar.gz
Source100:	%{name}.rpmlintrc

BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool-base
BuildRequires:	slibtool
BuildRequires:	make
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:	pkgconfig(readline)
BuildRequires:  pkgconfig(x11)
BuildRequires:	pkgconfig(xaw7)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xft)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(xrender)

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
Provides:   %{libname} = %{version}-%{release}
Obsoletes:  %{libname}0 <= 30

%description -n %{libname}
This package contains the library needed to run programs dynamically
linked with %{name}

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
%autosetup -a 0
echo "The build directory is %{builddir}"

%build
mkdir _build
mkdir _build_lib
#
cd %{builddir}/%{name}-%{version}/_build
#
CONFIGURE_TOP=%{builddir}/%{name}-%{version} 
%configure \
    --with-x                                \
    --enable-xspice                         \
    --enable-openmp                         \
    --enable-cider      
#
%make_build 
#
cd %{builddir}/%{name}-%{version}/_build_lib
#
%configure                                  \
    --with-ngshared                         \
    --enable-xspice                         \
    --enable-openmp                         \
    --enable-cider
%make_build 

%install
cd /%{builddir}/%{name}-%{version}/_build
%make_install
cd /%{builddir}/%{name}-%{version}/_build_lib
%make_install


%files
%{_bindir}/%{name}
%{_mandir}/man1/ngspice.*
%{_datadir}/ngspice/scripts/*
%exclude %{_datadir}/ngspice/scripts/src/*

%files -n %{libname}
%{_libdir}/libngspice.so.*
%{_libdir}/ngspice/*

%files -n %{develname}
%{_includedir}/ngspice/*
%{_libdir}/libngspice.so
%{_libdir}/pkgconfig/ngspice.pc
%{_datadir}/ngspice/scripts/src/*


