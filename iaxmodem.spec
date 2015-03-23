# force _smp_mflags to -j1
%define _smp_mflags -j1
Summary: Software modem for interfacing Asterisk and Hylafax via IAX2
Name: iaxmodem
Version: 1.2.0
Release: 1%{?dist}
License: GPL
Group: Applications/Communications
Url: https://sourceforge.net/projects/iaxmodem
Source0: http://prdownloads.sourceforge.net/iaxmodem/iaxmodem-%{version}.tar.gz
Vendor: Lee Howard <faxguy@howardsilvan.com>
Packager: Laimbock Consulting <asterisk@laimbock.com>
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: libtiff-devel

%description
IAXmodem is a software modem written in C that uses an IAX channel
(commonly provided by an Asterisk PBX system) instead of a traditional
phone line and uses a DSP library instead of DSP hardware chipsets.

To accomplish this, then, IAXmodem interfaces an IAX library known as
libiax2 with a DSP library known as spandsp, and then IAXmodem interfaces
the DSP library with a tty device node for interfacing with modem
applications.

%prep
%setup

%build
[ "%{buildroot}" != '/' ] && rm -rf %{buildroot}

# build static version
./build static

%install
# install the bunch manually
%{__install} -D -m 755 iaxmodem %{buildroot}%{_sbindir}/iaxmodem
%{__install} -D -m 644 iaxmodem.1 %{buildroot}%{_mandir}/man1/iaxmodem.1
%{__install} -D -m 660 config.ttyIAX %{buildroot}%{_localstatedir}/spool/hylafax/etc/config.ttyIAX
perl -pi -e 's,/usr/local/,/usr/,g' iaxmodem.init.fedora
%{__install} -D -m 755 iaxmodem.init.fedora %{buildroot}%{_initrddir}/iaxmodem
mkdir -p %{buildroot}%{_localstatedir}/log/iaxmodem
mkdir -p %{buildroot}%{_sysconfdir}/iaxmodem/

%clean
[ "%{buildroot}" != '/' ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGES FAQ README TODO VERSION
%attr(750,root,root)				%{_sbindir}/iaxmodem
%attr(0644,root,root)					%{_mandir}/man1/iaxmodem.1.gz
%attr(0660,root,uucp)	%config(noreplace)	%{_localstatedir}/spool/hylafax/etc/config.ttyIAX
%attr(0660,root,uucp)	%config(noreplace)	%{_sysconfdir}/iaxmodem/
%attr(0755,root,root)					%{_initrddir}/iaxmodem
%attr(0770,root,uucp)	%dir			%{_localstatedir}/log/iaxmodem


%changelog
* Mon Mar 18 2013 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.2.0-1
- First release for NethServer - CentOS 6.4
