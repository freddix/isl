Summary:	Library for manipulating sets and relations of integer points bounded by linear constraints
Name:		isl
Version:	0.12.1
Release:	3
License:	MIT
Group:		Libraries
Source0:	http://isl.gforge.inria.fr/%{name}-%{version}.tar.lzma
# Source0-md5:	d7a723a508056b9dc5a25c5ca7d1d74f
URL:		http://isl.gforge.inria.fr/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gmp-devel
BuildRequires:	libtool
BuildRequires:	rpm-pythonprov
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
isl is a library for manipulating sets and relations of integer points
bounded by linear constraints. Supported operations on sets include
intersection, union, set difference, emptiness check, convex hull,
(integer) affine hull, integer projection, and computing the
lexicographic minimum using parametric integer programming. It also
includes an ILP solver based on generalized basis reduction.

%package devel
Summary:	Header files for isl library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gmp-devel

%description devel
Header files for isl library.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__automake}
%{__autoconf}
%configure \
	--disable-silent-rules \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%attr(755,root,root) %ghost %{_libdir}/libisl.so.10
%attr(755,root,root) %{_libdir}/libisl.so.*.*.*
%exclude %{_libdir}/*.py

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libisl.so
%{_includedir}/isl
%{_pkgconfigdir}/isl.pc

