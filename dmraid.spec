Summary:	Device-mapper RAID tool and library
Name:		dmraid
Version:	1.0.0
Release:	0.1
License:	GPL
Group:		Base
Source0:	http://people.redhat.com/~heinzm/sw/dmraid/src/%{name}-%{version}-rc4.tar.bz2
# Source0-md5:	96ab9ad2891045a28688f84c5329cedc
URL:		http://people.redhat.com/~heinzm/sw/dmraid/
BuildRequires:	autoconf
BuildRequires:	device-mapper-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DMRAID supports device discovery, set activation and display of
properties for ATARAID on Linux >= 2.4 using device-mapper.

%prep
%setup -q -n %{name}
mv */* ./

%build

%{__gettextize}
%{__aclocal}
%{__autoconf}

%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -D tools/dmraid $RPM_BUILD_ROOT%{_sbindir}/dmraid
install -D man/dmraid.8 $RPM_BUILD_ROOT%{_mandir}/man8/dmraid.8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO doc/dmraid_design.txt
%attr(755,root,root) %{_sbindir}/*
%attr(644,root,root) %{_mandir}/man8/*
