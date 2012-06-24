Summary:	A serial port to TCP/IP bridge
Summary(pl):	Most pomi�dzy portem szeregowym a TCP/IP
Name:		tcpser
Version:	1.0rc9
Release:	1
License:	GPL
Group:		Networking
Source0:	http://www.jbrain.com/pub/linux/serial/%{name}-%{version}.tar.gz
# Source0-md5:	37770b332c403b7999f149accbd1353b
Patch0:		%{name}-Makefile.patch
URL:		http://www.jbrain.com/pub/linux/serial/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
TCPSER is a utility that turns a PC serial port into an emulated
Hayes(TM) compatible modem, with the phone connection replaced by
TCP/IP for both inbound and outbound connections. TCPSER is used as a
low-cost way to put older computing systems (like 8-bit BBSes) on the
Internet.

%description -l pl
TCPSER to program zamieniaj�cy port szeregowy PC w emulowany modem
zgodny ze standardem Hayes(TM). Lini� telefoniczn� zast�puje protok�
TCP/IP zapewniaj�cy obs�ug� po��cze� przychodz�cych i wychodz�cych.
TCPSER jest u�ywany jako tani spos�b na udost�pnienie starszych
system�w (np. 8-bitowych BBS-�w) w Internecie.

%prep
%setup -q
%patch0 -p1

%build
CFLAGS="%{rpmcflags}" \
%{__make} all \
	CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT
install -D tcpmdm $RPM_BUILD_ROOT%{_bindir}/tcpmdm
install -D tcpser $RPM_BUILD_ROOT%{_bindir}/tcpser

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES
%attr(755,root,root) %{_bindir}/*
