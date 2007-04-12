%define oname esdl
%define erlangdir %{_libdir}/erlang-R11B

Summary:        Erlang OpenGL/SDL api and utilities
Name:           erlang-%{oname}
Version:        0.96.0626
Release:        %mkrel 1
Group:          Development/Other
License:        BSD
URL:            http://esdl.sourceforge.net
Source:		http://download.sourceforge.net/esdl/%{oname}-%{version}.src.tar.bz2
BuildRequires:  SDL-devel
BuildRequires:	mesa-common-devel
BuildRequires:	erlang-compiler = R11B
BuildRequires:	erlang-devel = R11B
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

%description
A library that gives you access to SDL and OpenGL functionality in
your Erlang program.

%package devel
Summary:	Development files for ESDL
Group:          Development/Other
Requires:	%{name} = %{version}-%{release}

%description devel
Development files for ESDL.

%prep
%setup -qn %{oname}-%{version}
perl -pi -e 's|INSTALLDIR = |INSTALLDIR = \$(DESTDIR)|' Makefile
perl -pi -e 's|^ERL_DIR.*|ERL_DIR:=%{erlangdir}|' Makefile

%build
%make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{erlangdir}/lib

%makeinstall_std
rm -rf  %{buildroot}%{erlangdir}/lib/esdl-%{version}/c_src

%clean
rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%doc %{erlangdir}/lib/esdl-%{version}/license.terms
%doc %{erlangdir}/lib/esdl-%{version}/Readme*
%dir %{erlangdir}/lib/esdl-%{version}
%dir %{erlangdir}/lib/esdl-%{version}/ebin
%dir %{erlangdir}/lib/esdl-%{version}/priv
%attr(755,root,root) %{erlangdir}/lib/esdl-%{version}/priv/*.so
%{erlangdir}/lib/esdl-%{version}/ebin/*.beam
%{erlangdir}/lib/esdl-%{version}/vsn
%exclude %{erlangdir}/lib/esdl-%{version}/include
%exclude %{erlangdir}/lib/esdl-%{version}/src

%files devel
%defattr(644,root,root,755)
%doc %{erlangdir}/lib/esdl-%{version}/doc
%{erlangdir}/lib/esdl-%{version}/include
%{erlangdir}/lib/esdl-%{version}/src


