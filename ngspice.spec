%define __libtoolize	/bin/true

%define major 44	
%define minor 2
%define	docname		ngspice-doc
%define libname		%mklibname %{name}  
%define develname	%mklibname %{name} -d
%define _disable_ld_no_undefined 1

Summary:	Mixed Mode - Mixed Level Circuit Simulator Based On Berkley's spice3f5
Name:		ngspice
Version:    %{major}%{?minor:.%minor}	
Release:	2
# See COPYING for more detail concerning license
License:	GPL and GPLv2 and LGPLv2 and BSD
Group:		System/Libraries
Url:		https://ngspice.sourceforge.net/index.html
Source0:    https://downloads.sourceforge.net/project/ngspice/ng-spice-rework/%{major}%{?minor:.%minor}/ngspice-%{major}%{?minor:.%minor}.tar.gz
Source100:	%{name}.rpmlintrc

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
%setup -a 0 
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
%{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/ngspice/scripts/*
%exclude %{_datadir}/ngspice/scripts/src/*

%files -n %{libname}
%{_libdir}/lib*.so.*
%{_libdir}/ngspice/*

%files -n %{develname}
%{_libdir}/lib*.so
%{_includedir}/*
%{_libdir}/pkgconfig/*.pc
%{_datadir}/ngspice/scripts/src/*


