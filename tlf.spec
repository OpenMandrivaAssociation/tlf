Name:		tlf
License:	GPL
Group:		Communications
Url:		http://home.iae.nl/users/reinc/TLF-0.2.html
Version:	1.1.2
Release:	3
Summary:	Contest logging program for Linux
Source0:	https://github.com/downloads/Tlf/%{name}/%{name}-%{version}.tar.gz
BuildRequires:	ncurses-devel
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gnuradio-core)
BuildRequires:	hamlib-devel

%description
Tlf is developed by Rein Couperus, PA0R. Hamlib is used here to get the rig's 
frequency and track dx spots when logged in to a DX-cluser. 
Tlf is a contest logging program with networking support, partially based on 
TRLOG (but much better of course).

%prep
%setup -q

%build
%configure2_5x 
#--enable-hamlib
%make

%install
%makeinstall_std

%files
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README
%{_bindir}/tlf
%{_bindir}/play_vk
%{_datadir}/man/man1/tlf.1.*
%{_bindir}/soundlog
%{_datadir}/tlf/arrlsections
%{_datadir}/tlf/callmaster
%{_datadir}/tlf/cty.dat
%{_datadir}/tlf/ssamults
#%{_datadir}/tlf/usa_canada_states
%{_datadir}/tlf/spdxmults
%{_datadir}/tlf/paccmults
%{_datadir}/tlf/ea_sections
%{_datadir}/tlf/logcfg.dat
%{_datadir}/tlf/rules/*
%{_datadir}/tlf/arrl10m_mults
%{_datadir}/tlf/arrldx_mults


%changelog
* Thu May 10 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.1.2-1
+ Revision: 798019
- hamlib-devel
- version update 2.48
- version update 1.1.2
- BR: gnuradio-devel

* Thu Jan 19 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.1.1-1
+ Revision: 762812
- version update

* Mon Dec 26 2011 Alexander Khrukin <akhrukin@mandriva.org> 1.1.0-1
+ Revision: 745396
- so strange it was built on my test cooker and want into cluster
- br fixes
- glib2.0-devel BR
- imported package tlf

