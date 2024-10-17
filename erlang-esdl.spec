%define oname esdl
%define erlang_libdir %{_libdir}/erlang/addons

Summary:	Erlang OpenGL/SDL api and utilities
Name:		erlang-%{oname}
Version:	1.2
Release:	3
Group:		Development/Other
License:	BSD
URL:		https://esdl.sourceforge.net
Source0:	http://downloads.sourceforge.net/project/esdl/esdl/%{oname}-%{version}/%{oname}-%{version}.src.tar.gz
Patch0:		esdl-1.0.1-optflags.patch
Patch1:		esdl-1.0.1-makefile.patch
BuildRequires:  SDL-devel
BuildRequires:	SDL_ttf-devel
BuildRequires:	SDL_image-devel
BuildRequires:	mesa-common-devel
BuildRequires:	erlang-compiler		>= R11B-7
BuildRequires:	erlang-devel		>= R11B-7
Requires:	erlang-base		>= R11B-7

%description
A library that gives you access to SDL and OpenGL functionality in
your Erlang program.

%package devel
Summary:	Development files for ESDL
Group:		Development/Other
Requires:	%{name} = %{version}-%{release}
Requires:	erlang-devel >= R11B-6
Requires:	SDL-devel
Requires:	mesa-common-devel

%description devel
Development files for ESDL.

%prep
%setup -qn %{oname}-%{version}
#% patch0 -p1

%patch1 -p1

perl -pi -e 's|INSTALLDIR = |INSTALLDIR = \$(DESTDIR)|' Makefile

%build
%define _disable_ld_no_undefined 1
export CFLAGS="%{optflags}"
export CLINKFLAGS="%{ldflags}"
%make

%install
%makeinstall_std

pushd test
mv -f *.beam %{buildroot}%{erlang_libdir}/esdl-%{version}/ebin
popd

rm -f %{buildroot}%{erlang_libdir}/esdl-%{version}/Readme.MacOSX-Cocoa
rm -f %{buildroot}%{erlang_libdir}/esdl-%{version}/Readme.win32

%files
%defattr(644,root,root,755)
%doc %{erlang_libdir}/esdl-%{version}/license.terms
%doc %{erlang_libdir}/esdl-%{version}/Readme
%dir %{erlang_libdir}/esdl-%{version}
%dir %{erlang_libdir}/esdl-%{version}/ebin
%dir %{erlang_libdir}/esdl-%{version}/priv
%attr(755,root,root) %{erlang_libdir}/esdl-%{version}/priv/*.so
%{erlang_libdir}/esdl-%{version}/ebin/*.beam
%{erlang_libdir}/esdl-%{version}/vsn.mk
%exclude %{erlang_libdir}/esdl-%{version}/include
%exclude %{erlang_libdir}/esdl-%{version}/src

%files devel
%defattr(644,root,root,755)
%doc %{erlang_libdir}/esdl-%{version}/doc
%{erlang_libdir}/esdl-%{version}/include
%{erlang_libdir}/esdl-%{version}/src
%{erlang_libdir}/esdl-%{version}/c_src
