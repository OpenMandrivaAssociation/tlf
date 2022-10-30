Name:		tlf
License:	GPL
Group:		Communications
Url:		http://tlf.github.io/
Version:	1.4.1
Release:	1
Summary:	Contest logging program for Linux
Source0:	https://github.com/Tlf/tlf/releases/download/tlf-%{version}/tlf-%{version}.tar.gz
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
%autosetup -p1
%configure
#--enable-hamlib

%build
%make_build

%install
%make_install

%files
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README
%{_bindir}/tlf
%{_bindir}/play_vk
%{_mandir}/man1/tlf.1*
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
