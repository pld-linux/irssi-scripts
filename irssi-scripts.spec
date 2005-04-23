# TODO:
# - longer descriptions
# - the package versions don't reflect the script version.
#   create separate .specs? (brr)
Summary:	Irssi scripts pack
Summary(pl):	Zestaw skryptów do Irssi
Name:		irssi-scripts
Version:	0.4
Release:	4
License:	distributable
Group:		Applications/Communications
Source0:	http://ep09.pld-linux.org/~domelu/pld/irssi-scripts/%{name}.tar.gz
# Source0-md5:	8614bea24b9683988e3336c23d38bc74
Source1:	http://www.irssi.org/scripts/scripts/amarok_ssh.pl
# Source1-md5:	073b81e7bb307883d6d67618bbd3b800
Source2:	http://www.irssi.org/scripts/scripts/charsetwars.pl
# Source2-md5:	dcb02583cf838445b99a0a8d7387f913
Patch0:		amarok_ssh-opt-user.patch
Requires:	irssi
Requires:	perl-Text-Iconv
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
Summary(pl):	amaroK (po ssh)
License:	Public Domain
Group:		Applications/Communications
URL:		http://www.codeeye.de/irssi/
Requires:	irssi
Provides:	irssi-script
Obsoletes:	irssi-scripts

%description -n irssi-script-amarok
Retrieves song infos and controls amaroK via dcop, optionally running
on another computer via ssh.

%description -n irssi-script-amarok -l pl
Skrypt uzyskuj±cy informacje o utworze i steruj±cy odtwarzaczem amaroK
poprzez dcop, opcjonalnie dzia³aj±cym na innym komputerze po ssh.

%package -n irssi-script-charsetwars
Summary:	charsetwars
Summary(pl):	Skrypt charsetwars
License:	Public Domain
Group:		Applications/Communications
URL:		http://www.inf.ufsc.br/~nardin/irssi/
Requires:	irssi
Requires:	perl-Text-Iconv
Provides:	irssi-script
Obsoletes:	irssi-scripts

%description -n irssi-script-charsetwars
Converts messages between charsets (utf-8 <=> iso-8859-1, etc.) by
nick/channel/ircnet. With "dumb" (regexp) guessing for any charset
(user configured).

%description -n irssi-script-charsetwars -l pl
Skrypt konwertuj±cy wiadomo¶ci miêdzy zestawami znaków (utf-8 <=>
iso-8859-1 itp.) w zale¿no¶ci od nicka/kana³u/sieci. Zawiera tak¿e
prymitywne zgadywanie (po wyra¿eniu regularnym) dla dowolnego zestawu
znaków (konfigurowane przez u¿ytkownika).

%prep
%setup -q -n %{name}
install %{SOURCE1} .
install %{SOURCE2} .
%patch0 -p1

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

%files -n irssi-script-charsetwars
%defattr(644,root,root,755)
%{_scriptdir}/charsetwars.pl
