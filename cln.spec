Summary:	C++ Class Library for Numbers
Summary(pl):	Biblioteka klas C++ dla liczb
Name:		cln
Version:	1.1.8
Release:	1
License:	GPL
Group:		Libraries
Source0:	ftp://ftpthep.physik.uni-mainz.de/pub/gnu/%{name}-%{version}.tar.bz2
# Source0-md5:	490dd0697b3d16b2ba6a843829228cba
Patch0:		%{name}-info.patch
Patch1:		%{name}-link.patch
URL:		http://www.ginac.de/CLN/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	gmp-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
Obsoletes:	libcln2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# won't work with -O0 because of static const initialization loops
%define		debugcflags	-O1 -g

%description
A GPLed collection of C++ math classes and functions, that will bring
efficiency, type safety, algebraic syntax to everyone in a memory and
speed efficient library.

%description -l pl
Objêty licencj± GPL zbiór klas i funkcji matematycznych C++ daj±cy
wydajno¶æ, bezpieczne typy i sk³adniê algebraiczn±.

%package devel
Summary:	Development files for programs using the CLN library
Summary(pl):	Pliki do programowania z u¿yciem biblioteki CLN
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gmp-devel
Requires:	libstdc++-devel
Obsoletes:	libcln2-devel

%description devel
This package is necessary if you wish to develop software based on the
CLN library.

%description devel -l pl
Ten pakiet jest niezbêdny do tworzenia oprogramowania opartego na
bibliotece CLN.

%package static
Summary:	Static CLN library
Summary(pl):	Statyczna biblioteka CLN
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static CLN library.

%description static -l pl
Statyczna biblioteka CLN.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

# kill AC_PROG_LIBTOOL
head -n 423 autoconf/aclocal.m4 > acinclude.m4
tail -n +4045 autoconf/aclocal.m4 >> acinclude.m4

%build
%{__libtoolize}
%{__aclocal} -I . -I m4
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

%post devel
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%postun devel
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS README TODO*
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/cln-config
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/cln
%{_mandir}/man1/cln-config.1*
%{_infodir}/*.info*
%{_aclocaldir}/*.m4
%{_pkgconfigdir}/*.pc
%{_examplesdir}/%{name}-%{version}

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
