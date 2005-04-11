# TODO:
# - longer descriptions
# - the package versions don't reflect the script version.
#   create separate .specs? (brr)
Summary:	Irssi scripts pack
Summary(pl):	Zestaw skryptów do Irssi
Name:		irssi-scripts
Version:	0.4
Release:	2
License:	distributable
Group:		Applications/Communications
Source0:	http://ep09.pld-linux.org/~domelu/pld/irssi-scripts/%{name}.tar.gz
# Source0-md5:	8614bea24b9683988e3336c23d38bc74
Source1:	http://www.irssi.org/scripts/scripts/amarok_ssh.pl
# Source1-md5:	073b81e7bb307883d6d67618bbd3b800
Requires:	irssi
Obsoletes:	irssi-script
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_scriptdir	%{_prefix}/share/irssi/scripts

%description
Irssi scripts pack.

%description -l pl
Zestaw skryptów do Irssi.

%package -n irssi-script-forwardfix
Summary:	forwardfix script
Summary(pl):	Skrypt forwardfix
Group:		Applications/Communications
URL:		http://vorlon.icpnet.pl/~agaran/
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
URL:		http://gj.pointblue.com.pl/projects/ziew/
Requires:	irssi
Provides:	irssi-script
Obsoletes:	irssi-scripts

%description -n irssi-script-ziew
ziew script.

%description -n irssi-script-ziew -l pl
Skrypt ziew.

%package -n irssi-script-seen
Summary:	seen script
Summary(pl):	Skrypt seen
Group:		Applications/Communications
Requires:	irssi
Provides:	irssi-script
Obsoletes:	irssi-scripts

%description -n irssi-script-seen
seen scripts.

%description -n irssi-script-seen -l pl
Skrypt seen.

%package -n irssi-script-cp2iso
Summary:	cp2iso script
Summary(pl):	Skrypt cp2iso
Group:		Applications/Communications
Requires:	irssi
Provides:	irssi-script
Obsoletes:	irssi-scripts

%description -n irssi-script-cp2iso
cp2iso script.

%description -n irssi-script-cp2iso -l pl
Skrypt cp2iso.

%package -n irssi-script-keepnick
Summary:	keepnick script
Summary(pl):	Skrypt keepnick
Group:		Applications/Communications
Requires:	irssi
Provides:	irssi-script
Obsoletes:	irssi-scripts

%description -n irssi-script-keepnick
keepnick script.

%description -n irssi-script-keepnick -l pl
Skrypt keepnick.

%package -n irssi-script-people
Summary:	people script
Summary(pl):	Skrypt people
Group:		Applications/Communications
Requires:	irssi
Provides:	irssi-script
Obsoletes:	irssi-scripts

%description -n irssi-script-people
people script.

%description -n irssi-script-people -l pl
Skrypt people.

%package -n irssi-script-amarok
Summary:	amaroK (via ssh)
Group:		Applications/Communications
URL:		http://www.codeeye.de/irssi/
License:	Public Domain
Requires:	irssi
Provides:	irssi-script
Obsoletes:	irssi-scripts

%description -n irssi-script-amarok
Retrievs song infos and controls amaroK via dcop, optionally running
on another computer via ssh.

%prep
%setup -q -n %{name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_scriptdir}

install *.pl $RPM_BUILD_ROOT%{_scriptdir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_scriptdir}

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

%files -n irssi-script-seen
%defattr(644,root,root,755)
%{_scriptdir}/seen.pl

%files -n irssi-script-cp2iso
%defattr(644,root,root,755)
%{_scriptdir}/cp2iso.pl

%files -n irssi-script-keepnick
%defattr(644,root,root,755)
%{_scriptdir}/keepnick.pl

%files -n irssi-script-people
%defattr(644,root,root,755)
%{_scriptdir}/people.pl

%files -n irssi-script-amarok
%defattr(644,root,root,755)
%{_scriptdir}/amarok_ssh.pl
