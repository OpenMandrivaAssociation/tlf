Name:		tlf
License:	GPL
Group:		Communications
Url:		http://home.iae.nl/users/reinc/TLF-0.2.html
Version:	1.1.0	
Release:	1
Summary:	TLF is a contest logging program for Linux
Source0:	tlf-%{version}.tar.gz
BuildRequires:	libhamlib-devel ncurses-devel glib2-devel

%description
Tlf is developed by Rein Couperus, PA0R. Hamlib is used here to get the rig's 
frequency and track dx spots when logged in to a DX-cluser. 
Tlf is a contest logging program with networking support, partially based on 
TRLOG (but much better of course).

%prep
%setup -q

%build
%configure --enable-hamlib
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
%{_datadir}/tlf/usa_canada_states
%{_datadir}/tlf/spdxmults
%{_datadir}/tlf/paccmults
%{_datadir}/tlf/ea_sections
%{_datadir}/tlf/logcfg.dat
%{_datadir}/tlf/rules/*
