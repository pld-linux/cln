Summary:	C++ Class Library for Numbers
Summary(pl):	Biblioteka klas C++ dla liczb
Name:		cln
Version:	1.1.7
Release:	1
License:	GPL
Group:		Libraries
Source0:	ftp://ftpthep.physik.uni-mainz.de/pub/gnu/%{name}-%{version}.tar.bz2
# Source0-md5:	b4a0ab4415281d2143edd44f2c8de136
URL:		http://www.ginac.de/CLN/
BuildRequires:	automake
BuildRequires:	gmp-devel
BuildRequires:	libstdc++-devel
Obsoletes:	libcln2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

%build
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
