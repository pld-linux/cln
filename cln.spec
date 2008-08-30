Summary:	C++ Class Library for Numbers
Summary(pl.UTF-8):	Biblioteka klas C++ dla liczb
Name:		cln
Version:	1.2.2
Release:	1
License:	GPL
Group:		Libraries
Source0:	ftp://ftpthep.physik.uni-mainz.de/pub/gnu/%{name}-%{version}.tar.bz2
# Source0-md5:	6b479281fec86314b4c7a9357bd83ef8
Patch0:		%{name}-info.patch
URL:		http://www.ginac.de/CLN/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	gmp-devel >= 3.0
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
BuildRequires:	tetex-dvips
BuildRequires:	tetex-fonts-latex
BuildRequires:	tetex-format-plain
BuildRequires:	tetex-metafont
BuildRequires:	texinfo
BuildRequires:	texinfo-texi2dvi
Requires:	gmp >= 3.0
Obsoletes:	libcln2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# won't work with -O0 because of static const initialization loops
%define		debugcflags	-O1 -g

%description
A GPLed collection of C++ math classes and functions, that will bring
efficiency, type safety, algebraic syntax to everyone in a memory and
speed efficient library.

%description -l pl.UTF-8
Objęty licencją GPL zbiór klas i funkcji matematycznych C++ dający
wydajność, bezpieczne typy i składnię algebraiczną.

%package devel
Summary:	Development files for programs using the CLN library
Summary(pl.UTF-8):	Pliki do programowania z użyciem biblioteki CLN
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gmp-devel >= 3.0
Requires:	libstdc++-devel
Obsoletes:	libcln2-devel

%description devel
This package is necessary if you wish to develop software based on the
CLN library.

%description devel -l pl.UTF-8
Ten pakiet jest niezbędny do tworzenia oprogramowania opartego na
bibliotece CLN.

%package static
Summary:	Static CLN library
Summary(pl.UTF-8):	Statyczna biblioteka CLN
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static CLN library.

%description static -l pl.UTF-8
Statyczna biblioteka CLN.

%prep
%setup -q
%patch0 -p1

rm -f m4/libtool.m4

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install examples/{Makefile,*.cc} $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	devel -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	devel -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS README TODO*
%attr(755,root,root) %{_libdir}/libcln.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcln.so.5

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcln.so
%{_libdir}/libcln.la
%{_includedir}/cln
%{_infodir}/cln.info*
%{_pkgconfigdir}/cln.pc
%{_examplesdir}/%{name}-%{version}

%files static
%defattr(644,root,root,755)
%{_libdir}/libcln.a
