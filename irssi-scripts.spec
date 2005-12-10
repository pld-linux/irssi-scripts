%include	/usr/lib/rpm/macros.perl
Summary:	Irssi scripts pack
Summary(pl):	Zestaw skryptów do Irssi
Name:		irssi-scripts
Version:	0.4
Release:	4.6
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
Patch0:		amarok_ssh-opt-user.patch
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

%description
This is a collection of useful scripts for the irssi IRC-client. Thus,
installing this package only makes sense if you intend to use irssi.

Almost all scripts can also be downloaded from
<http://scripts.irssi.org/>.

%description -l pl
Zestaw skryptów do Irssi.

%package -n irssi-script-amarok
Summary:	amaroK (via ssh)
Summary(pl):	amaroK (po ssh)
Version:	1.0
License:	Public Domain
Group:		Applications/Communications
URL:		http://www.codeeye.de/irssi/
Requires:	irssi

%description -n irssi-script-amarok
Retrieves song infos and controls amaroK via dcop, optionally running
on another computer via ssh.

%description -n irssi-script-amarok -l pl
Skrypt uzyskuj±cy informacje o utworze i steruj±cy odtwarzaczem amaroK
poprzez dcop, opcjonalnie dzia³aj±cym na innym komputerze po ssh.

%package -n irssi-script-autorealname
Summary:	autorealname script
Version:	0.8.5
License:	GPL v2 or later
Group:		Applications/Communications
Requires:	irssi

%description -n irssi-script-autorealname
Print realname of everyone who join to channels.

%package -n irssi-script-chanact
Summary:	chanact script
Version:	0.5.5
License:	GPL v2 or later
Group:		Applications/Communications
URL:		http://bc-bd.org/software.php3#irssi
Requires:	irssi

%description -n irssi-script-chanact
Adds new powerful and customizable [Act: ...] item
(chanelnames,modes,alias).
Lets you give alias characters to windows so that you can select those
with meta-<char>.

%package -n irssi-script-charsetwars
Summary:	charsetwars
Summary(pl):	Skrypt charsetwars
Version:	0.69.1
License:	Public Domain
Group:		Applications/Communications
URL:		http://www.inf.ufsc.br/~nardin/irssi/
Requires:	irssi
Requires:	perl-Text-Iconv

%description -n irssi-script-charsetwars
Converts messages between charsets (utf-8 <=> iso-8859-1, etc.) by
nick/channel/ircnet. With "dumb" (regexp) guessing for any charset
(user configured).

%description -n irssi-script-charsetwars -l pl
Skrypt konwertuj±cy wiadomo¶ci miêdzy zestawami znaków (utf-8 <=>
iso-8859-1 itp.) w zale¿no¶ci od nicka/kana³u/sieci. Zawiera tak¿e
prymitywne zgadywanie (po wyra¿eniu regularnym) dla dowolnego zestawu
znaków (konfigurowane przez u¿ytkownika).

%package -n irssi-script-cp2iso
Summary:	cp2iso script
Summary(pl):	Skrypt cp2iso
Version:	1.3
Group:		Applications/Communications
Requires:	irssi

%description -n irssi-script-cp2iso
Translates CP1250 to ISO8859-2 in incoming messages.

%description -n irssi-script-cp2iso -l pl
Skrypt cp2iso.

%package -n irssi-script-dispatch
Summary:	dispatch script
Version:	0.0.2
License:	GPL v2
Group:		Applications/Communications
Requires:	irssi

%description -n irssi-script-dispatch
This scripts sends unknown commands to the server.

%package -n irssi-script-forwardfix
Summary:	forwardfix script
Summary(pl):	Skrypt forwardfix
Group:		Applications/Communications
URL:		http://vorlon.icpnet.pl/~agaran/
Requires:	irssi

%description -n irssi-script-forwardfix
forwardfix script.

%description -n irssi-script-forwardfix -l pl
Skrypt forwardfix.

%package -n irssi-script-hideauth
Summary:	hideauth script
Version:	1.01
License:	Public Domain
Group:		Applications/Communications
URL:		http://www.jamesoff.net
Requires:	irssi

%description -n irssi-script-hideauth
Stops eggdrop passwords from showing up in e.g. /msg botnick op
password [#channel].

%package -n irssi-script-keepnick
Summary:	keepnick script
Summary(pl):	Skrypt keepnick
Version:	1.17
Group:		Applications/Communications
Requires:	irssi

%description -n irssi-script-keepnick
Try to get your nick back when it becomes available.

%description -n irssi-script-keepnick -l pl
Skrypt keepnick.

%package -n irssi-script-nocaps
Summary:	nocaps script
Version:	1.01
License:	Public Domain
Group:		Applications/Communications
URL:		http://www.jamesoff.net
Requires:	irssi

%description -n irssi-script-nocaps
Replaces lines in ALL CAPS with something easier on the eyes.

%package -n irssi-script-people
Summary:	people script
Summary(pl):	Skrypt people
Version:	1.4
Group:		Applications/Communications
Requires:	irssi

%description -n irssi-script-people
Userlist with autoopping, autokicking etc.

%description -n irssi-script-people -l pl
Skrypt people.

%package -n irssi-script-seen
Summary:	seen script
Summary(pl):	Skrypt seen
Version:	1.11
Group:		Applications/Communications
Requires:	irssi

%description -n irssi-script-seen
Tell people when other people were online.

%description -n irssi-script-seen -l pl
Skrypt seen.

%package -n irssi-script-tab_stop
Summary:	tab_stop script
Version:	0.2002123102
License:	GPL v2
Group:		Applications/Communications
Requires:	irssi

%description -n irssi-script-tab_stop
This script replaces the evil inverted 'I' with a configurable number
of whitespaces.

%package -n irssi-script-ziew
Summary:	ziew script
Summary(pl):	Skrypt ziew
Version:	0.57
Group:		Applications/Communications
URL:		http://gj.pointblue.com.pl/projects/ziew/
Requires:	irssi

%description -n irssi-script-ziew
yawners toy.

%description -n irssi-script-ziew -l pl
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
%patch0 -p1

# make rpm scan perl deps: add perl preamble
# if anyone has better idea/implementation, go ahead
sed -i -e '1{
	/perl/!i#!/usr/bin/perl
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

%files -n irssi-script-ziew
%defattr(644,root,root,755)
%{_scriptdir}/ziew.pl
