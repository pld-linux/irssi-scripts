Summary:	Irssi scripts pack
Summary(pl):	Zestaw skrypt�w do Irssi.
Name:		irssi-scripts
Version:	0.1
Release:	0.1
License:	distributable
Group:		Applications/Communications
Source0:	http://ep09.pld-linux.org/~domelu/pld/irssi-scripts/%{name}.tar.gz
# Source0-md5:	a9e7bbcc841a27984394a09d0f11edf1
Requires:	irssi
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:      irssi-script

%define		_scriptdir	%{_prefix}/share/irssi/scripts

%description
Irssi scripts pack.
 
%description -l pl
Zestaw skrypt�w do Irssi.

%package -n irssi-script-forwardfix
Summary:	forwardfix script
Summary(pl):	Skrypt forwardfix
Group:		Applications/Communications
Requires:	irssi
Provides:	irssi-script
Obsoletes:	irssi-scripts

%description -n irssi-script-forwardfix
forwardfix script.

%description -n irssi-script-forwardfix -l pl
Skrypt forwardfix.

%package -n irssi-script-ziew
Summary:	ziew script
Summary(pl):	Skrypt ziew
Group:		Applications/Communications
Requires:	irssi
Provides:	irssi-script
Obsoletes:	irssi-scripts

%description -n irssi-script-ziew
forwardfix ziew.

%description -n irssi-script-ziew -l pl
Skrypt ziew.

%prep
%setup -q -n %{name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_scriptdir}

install *.pl $RPM_BUILD_ROOT%{_scriptdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_scriptdir}/*

%files -n irssi-script-forwardfix
%defattr(644,root,root,755)
%{_scriptdir}/forwardfix.pl

%files -n irssi-script-ziew
%defattr(644,root,root,755)
%{_scriptdir}/ziew.pl
