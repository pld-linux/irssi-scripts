%include	/usr/lib/rpm/macros.perl
Summary:	Irssi scripts pack
Summary(pl.UTF-8):	Zestaw skryptów do Irssi
Name:		irssi-scripts
Version:	0.4
Release:	11
License:	distributable
Group:		Applications/Communications
Source0:	http://ep09.pld-linux.org/~domelu/pld/%{name}/irssi-scripts.tar.gz
# Source0-md5:	8614bea24b9683988e3336c23d38bc74
Source1:	http://www.irssi.org/scripts/scripts/amarok_ssh.pl
# Source1-md5:	073b81e7bb307883d6d67618bbd3b800
Source2:	http://www.irssi.org/scripts/scripts/autorealname.pl
# Source2-md5:	b9cee550addab8b9f0b15723ccb4676b
Source3:	http://www.irssi.org/scripts/scripts/chanact.pl
# Source3-md5:	65f33f53351432efe0932fc394027d3a
Source4:	http://www.irssi.org/scripts/scripts/charsetwars.pl
# Source4-md5:	dcb02583cf838445b99a0a8d7387f913
Source5:	http://www.irssi.org/scripts/scripts/dispatch.pl
# Source5-md5:	b52fec2c67c3088307bc6e7a2e2a464a
Source6:	http://www.irssi.org/scripts/scripts/hideauth.pl
# Source6-md5:	f9f35d8b14eb5db2a2e18eebc0938a62
Source7:	http://www.irssi.org/scripts/scripts/nocaps.pl
# Source7-md5:	b8aba206f9f4cfd159031cbda7397f74
Source8:	http://www.irssi.org/scripts/scripts/keepnick.pl
# Source8-md5:	e50707d22a9338df6fb9b39dcdefb7e2
Source9:	http://www.irssi.org/scripts/scripts/tab_stop.pl
# Source9-md5:	ffa8d8381c41521365cacf9b1bb13951
Source10:	http://netx.waw.pl/~agaran/forwardfix.pl
# Source10-md5:	8bf85f7368933a4e0cb4f875bac28733
Source11:	http://entermedia.pl/~shadzik/vtk/vtk.pl
# Source11-md5:	9e34c85f1084afaa71590bc544dd4e76
Patch0:		amarok_ssh-opt-user.patch
URL:		http://scripts.irssi.org/
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	sed >= 4.0
Requires:	irssi-script-amarok
Requires:	irssi-script-autorealname
Requires:	irssi-script-chanact
Requires:	irssi-script-charsetwars
Requires:	irssi-script-cp2iso
Requires:	irssi-script-dispatch
Requires:	irssi-script-forwardfix
Requires:	irssi-script-hideauth
Requires:	irssi-script-keepnick
Requires:	irssi-script-nocaps
Requires:	irssi-script-people
Requires:	irssi-script-seen
Requires:	irssi-script-tab_stop
Requires:	irssi-script-ziew
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_scriptdir	%{_prefix}/share/irssi/scripts
# requires perl(Irssi) >= 20020428, but Irssi provides only 0.9
%define		_noautoreq 'perl(Irssi)'

%description
This is a collection of useful scripts for the irssi IRC-client. Thus,
installing this package only makes sense if you intend to use irssi.

Almost all scripts can also be downloaded from
<http://scripts.irssi.org/>.

%description -l pl.UTF-8
Zestaw przydatnych skryptów do klienta IRC irssi.

Większość z nich jest dostępna pod adresem:
<http://scripts.irssi.org/>.

%package -n irssi-script-amarok
Summary:	amaroK (via ssh)
Summary(pl.UTF-8):	amaroK (po ssh)
Version:	1.0
License:	Public Domain
Group:		Applications/Communications
URL:		http://www.codeeye.de/irssi/
Requires:	irssi

%description -n irssi-script-amarok
Retrieves song infos and controls amaroK via dcop, optionally running
on another computer via ssh.

%description -n irssi-script-amarok -l pl.UTF-8
Skrypt uzyskujący informacje o utworze i sterujący odtwarzaczem amaroK
poprzez dcop, opcjonalnie działającym na innym komputerze po ssh.

%package -n irssi-script-autorealname
Summary:	autorealname script
Summary(pl.UTF-8):	Skrypt autorealname
Version:	0.8.5
License:	GPL v2 or later
Group:		Applications/Communications
Requires:	irssi

%description -n irssi-script-autorealname
Print realname of everyone who join to channels.

%description -n irssi-script-autorealname -l pl.UTF-8
Skrypt wypisujący prawdziwe nazwisko każdego dołączającego się do
kanałów.

%package -n irssi-script-chanact
Summary:	chanact script
Summary(pl.UTF-8):	Skrypt chanact
Version:	0.5.5
License:	GPL v2 or later
Group:		Applications/Communications
URL:		http://bc-bd.org/software.php3#irssi
Requires:	irssi

%description -n irssi-script-chanact
Adds new powerful and customizable [Act: ...] item
(channelnames, modes, alias).

Lets you give alias characters to windows so that you can select those
with meta-<char>.

%description -n irssi-script-chanact -l pl.UTF-8
Skrypt dodający potężny i konfigurowalny element [Act: ...]
(z nazwami kanałów, trybami, aliasami).

Pozwala nadać znaki aliasów do okien, dzięki czemu można wybierać okna
poprzez meta-<znak>.

%package -n irssi-script-charsetwars
Summary:	charsetwars
Summary(pl.UTF-8):	Skrypt charsetwars
Version:	0.69.1
License:	Public Domain
Group:		Applications/Communications
URL:		http://www.inf.ufsc.br/~nardin/irssi/
Requires:	irssi

%description -n irssi-script-charsetwars
Converts messages between charsets (utf-8 <=> iso-8859-1, etc.) by
nick/channel/ircnet. With "dumb" (regexp) guessing for any charset
(user configured).

%description -n irssi-script-charsetwars -l pl.UTF-8
Skrypt konwertujący wiadomości między zestawami znaków (utf-8 <=>
iso-8859-1 itp.) w zależności od nicka/kanału/sieci. Zawiera także
prymitywne zgadywanie (po wyrażeniu regularnym) dla dowolnego zestawu
znaków (konfigurowane przez użytkownika).

%package -n irssi-script-cp2iso
Summary:	cp2iso script
Summary(pl.UTF-8):	Skrypt cp2iso
Version:	1.3
Group:		Applications/Communications
Requires:	irssi

%description -n irssi-script-cp2iso
Translates CP1250 to ISO-8859-2 in incoming messages.

%description -n irssi-script-cp2iso -l pl.UTF-8
Skrypt cp2iso tłumaczący CP1250 na ISO-8859-2 w przychodzących
wiadomościach.

%package -n irssi-script-dispatch
Summary:	dispatch script
Summary(pl.UTF-8):	Skrypt dispatch
Version:	0.0.2
License:	GPL v2
Group:		Applications/Communications
Requires:	irssi

%description -n irssi-script-dispatch
This scripts sends unknown commands to the server.

%description -n irssi-script-dispatch -l pl.UTF-8
Ten skrypt wysyła nieznane polecenia do serwera.

%package -n irssi-script-forwardfix
Summary:	forwardfix script
Summary(pl.UTF-8):	Skrypt forwardfix
Version:	20060902
Group:		Applications/Communications
URL:		http://www.netx.waw.pl/~agaran/
Requires:	irssi

%description -n irssi-script-forwardfix
forwardfix script.

%description -n irssi-script-forwardfix -l pl.UTF-8
Skrypt forwardfix.

%package -n irssi-script-hideauth
Summary:	hideauth script
Summary(pl.UTF-8):	Skrypt hideauth
Version:	1.01
License:	Public Domain
Group:		Applications/Communications
URL:		http://www.jamesoff.net/
Requires:	irssi

%description -n irssi-script-hideauth
Stops eggdrop passwords from showing up in e.g. /msg botnick op
password [#channel].

%description -n irssi-script-hideauth -l pl.UTF-8
Skrypt zapobiegający pokazywaniu haseł eggdropa w np. /msg botnick op
password [#channel].

%package -n irssi-script-keepnick
Summary:	keepnick script
Summary(pl.UTF-8):	Skrypt keepnick
Version:	1.17
Group:		Applications/Communications
Requires:	irssi

%description -n irssi-script-keepnick
Try to get your nick back when it becomes available.

%description -n irssi-script-keepnick -l pl.UTF-8
Skrypt keepnick pozwala odzyskać swojego nicka kiedy stanie się
dostępny.

%package -n irssi-script-nocaps
Summary:	nocaps script
Summary(pl.UTF-8):	Skrypt nocaps
Version:	1.01
License:	Public Domain
Group:		Applications/Communications
URL:		http://www.jamesoff.net/
Requires:	irssi

%description -n irssi-script-nocaps
Replaces lines in ALL CAPS with something easier on the eyes.

%description -n irssi-script-nocaps -l pl.UTF-8
Skrypt zastępujący linie napisane w całości WIELKIMI LITERAMI czymś
łatwiejszym do przeczytania.

%package -n irssi-script-people
Summary:	people script
Summary(pl.UTF-8):	Skrypt people
Version:	1.4
Group:		Applications/Communications
Requires:	irssi

%description -n irssi-script-people
Userlist with autoopping, autokicking etc.

%description -n irssi-script-people -l pl.UTF-8
Skrypt people udostępnia listę użytkowników z opcjami autoop, autokick
itp.

%package -n irssi-script-seen
Summary:	seen script
Summary(pl.UTF-8):	Skrypt seen
Version:	1.11
Group:		Applications/Communications
Requires:	irssi

%description -n irssi-script-seen
Tell people when other people were online.

%description -n irssi-script-seen -l pl.UTF-8
Skrypt seen informuje ludzi o tym, że inni są online.

%package -n irssi-script-tab_stop
Summary:	tab_stop script
Summary(pl.UTF-8):	Skrypt tab_stop
Version:	0.2002123102
License:	GPL v2
Group:		Applications/Communications
Requires:	irssi

%description -n irssi-script-tab_stop
This script replaces the evil inverted 'I' with a configurable number
of whitespaces.

%description -n irssi-script-tab_stop -l pl.UTF-8
Ten skrypt zastępuje złe odwrócone 'I' konfigurowalną liczbą spacji.

%package -n irssi-script-vtk
Summary:	vtk script
Summary(pl.UTF-8):	Skrypt vtk
Version:	0.1
Group:		Applications/Communications
Requires:	irssi
Requires:	vtk-c

%description -n irssi-script-vtk
pl@TK for irssi.

%description -n irssi-script-vtk -l pl.UTF-8
pl@TK dla irssi.

%package -n irssi-script-ziew
Summary:	ziew script
Summary(pl.UTF-8):	Skrypt ziew
Version:	0.57
Group:		Applications/Communications
URL:		http://gj.pointblue.com.pl/projects/ziew/
Requires:	irssi

%description -n irssi-script-ziew
yawners toy.

%description -n irssi-script-ziew -l pl.UTF-8
Skrypt ziew.

%prep
%setup -q -n %{name}
cp -a %{SOURCE1} .
cp -a %{SOURCE2} .
cp -a %{SOURCE3} .
cp -a %{SOURCE4} .
cp -a %{SOURCE5} .
cp -a %{SOURCE6} .
cp -a %{SOURCE7} .
cp -a %{SOURCE8} .
cp -a %{SOURCE9} .
cp -a %{SOURCE10} .
cp -a %{SOURCE11} .
%patch0 -p1

# make rpm scan perl deps: add perl preamble
# if anyone has better idea/implementation, go ahead
sed -i -e '1{
	/perl/!i#!%{_bindir}/perl
}' *.pl

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_scriptdir}
install *.pl $RPM_BUILD_ROOT%{_scriptdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)

%files -n irssi-script-amarok
%defattr(644,root,root,755)
%{_scriptdir}/amarok_ssh.pl

%files -n irssi-script-autorealname
%defattr(644,root,root,755)
%{_scriptdir}/autorealname.pl

%files -n irssi-script-chanact
%defattr(644,root,root,755)
%{_scriptdir}/chanact.pl

%files -n irssi-script-charsetwars
%defattr(644,root,root,755)
%{_scriptdir}/charsetwars.pl

%files -n irssi-script-cp2iso
%defattr(644,root,root,755)
%{_scriptdir}/cp2iso.pl

%files -n irssi-script-dispatch
%defattr(644,root,root,755)
%{_scriptdir}/dispatch.pl

%files -n irssi-script-forwardfix
%defattr(644,root,root,755)
%{_scriptdir}/forwardfix.pl

%files -n irssi-script-hideauth
%defattr(644,root,root,755)
%{_scriptdir}/hideauth.pl

%files -n irssi-script-keepnick
%defattr(644,root,root,755)
%{_scriptdir}/keepnick.pl

%files -n irssi-script-nocaps
%defattr(644,root,root,755)
%{_scriptdir}/nocaps.pl

%files -n irssi-script-people
%defattr(644,root,root,755)
%{_scriptdir}/people.pl

%files -n irssi-script-seen
%defattr(644,root,root,755)
%{_scriptdir}/seen.pl

%files -n irssi-script-tab_stop
%defattr(644,root,root,755)
%{_scriptdir}/tab_stop.pl

%files -n irssi-script-vtk
%defattr(644,root,root,755)
%{_scriptdir}/vtk.pl

%files -n irssi-script-ziew
%defattr(644,root,root,755)
%{_scriptdir}/ziew.pl
