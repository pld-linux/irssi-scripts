# This script is possibly buggy, but i haven't got much time
# to test it. Use at your own risk.
# a g a r a n   a t   p l d   d a s h   l i n u x   d o t   o r g


use strict;
use Irssi;
use vars qw($VERSION %IRSSI);

$VERSION = '0.01';

%IRSSI = (
		authors => 'Maciej \'agaran\' Pijanka',
		contact => 'agaran@pld-linux.org',
		name => 'forwardfix',
		description => 'hides crossnetwork channel joining',
		license => 'GPL',
		url => 'http://netx.waw.pl/~agaran/forwardfix.pl'
);

#### Interface ###
#
#
#

# /upgrade_ffix
# dont do it, may harm your childrens, blow your drives and so on

# VARIABLES
# =========

Irssi::settings_add_str("forward", "forward_chanset","#pld:abw,#pldhelp:abw,#pldlivecd:abw");
Irssi::settings_add_str("forward", "forward_netmap","IRCnet:IN,FreeNode:FN,PLDNet:PN");
Irssi::settings_add_bool("forward","forward_dash",1);
Irssi::settings_add_int("forward", "forward_transmod",0);
Irssi::settings_add_bool("forward","forward_addnet",1);
Irssi::settings_add_str("forward", "forward_sep",'$');

Irssi::print("Its, beta, dont rely on it \nif something like forwardfix-debug: [something]\nhappens, please let me know");
Irssi::print("-- agaran (20060902-2050) ");

our %crude_hack = ();

Irssi::signal_add "event privmsg", sub {
	my ($server, $data, $nick, $address) = @_;
	my ($target, $text) = split(/ :/, $data, 2);
	my ($fwd,$p,$q,$fn);
	my ($chanset,$netmap,$fn) = ({},{},'');
	my $transmod = Irssi::settings_get_int("forward_transmod");
	my $addnet = Irssi::settings_get_bool("forward_addnet");
	my $sep = Irssi::settings_get_str("forward_sep");
	my $dash = Irssi::settings_get_bool("forward_dash");
	my $targetl = lc $target;

	map { split /:/,$_; $chanset->{lc $_[0]} = lc $_[1]; } split /[ ,]+/,Irssi::settings_get_str("forward_chanset");
	map { split /:/,$_; $netmap->{lc $_[0]} = $_[1]; } split /[ ,]+/,Irssi::settings_get_str("forward_netmap");

	my $now = time(); # yep compute foreach net, just to scope var
	foreach my $n (keys %crude_hack) {
		foreach my $m (keys %{$crude_hack{$n}}) {
			delete $crude_hack{$n}{$m} if($crude_hack{$n}{$m} + 30 < $now);
		}
	}

	if (defined $chanset->{$targetl} && (lc $nick eq $chanset->{$targetl} || ($dash && lc $nick eq $chanset->{$targetl}.'-' ))) {
		if($text =~ /^\(?([a-zA-Z\-_0-9\`\^|]+)?\@([A-Z]+)\) (.*)$/) { # maska maska maska
			($nick,$fwd,$text) = ($1,$2,$3);
			$text .= " [$fwd]" if($addnet);

			if($transmod == 2) { # convert to quasinormal stream;
				Irssi::signal_stop();
				Irssi::signal_emit("event privmsg", $server, "$target :$text", $nick.$sep.$fwd, $nick.'@'.$fwd);
			} else {
				Irssi::signal_stop();
				Irssi::signal_emit("event privmsg", $server, "$target :$text", $nick, $nick.'@'.$fwd);
			}

		} elsif ($text =~ /^\* \(?([a-zA-Z\-_0-9\`\^\|]+)?\@([A-Z]+)\) (.*)$/) { 
			($nick,$fwd,$text) = ($1,$2,$3);
			$text .= " [$fwd]" if($addnet);
			Irssi::signal_stop();
			Irssi::signal_emit("event privmsg", $server, "$target :ACTION $text", $nick, $nick.'@'.$fwd);
			
		} elsif ($text =~ /^\*\*\* Join ([a-zA-Z\-_0-9\`\]\[\^\|]+) \(([a-z\/\=+\~^A-Z\[\-_0-9\^:\@\.]+)\) on (.*)$/ ) {
			($nick,$text,$fwd) = ($1,$2,$3);

			$fn = $netmap->{lc $fwd} if(defined $netmap->{lc $fwd});

			if(($transmod == 1 || $transmod == 2) && $fn ne '') { # convert to quasinormal stream;
				Irssi::signal_stop();
				delete $crude_hack{$fn}{$nick} if(defined $crude_hack{$fn}{$nick});
				Irssi::signal_emit("event join", $server, ":$target", $nick.$sep.$fn, $text);
			}
			
		} elsif ($text =~ /^\*\*\* Part ([a-zA-Z\-_0-9\`\]\[\^\|]+) \(([a-z\/\=+\~^A-Z\[\-_0-9\^:\@\.]+)\) on (.*)$/ ) {
			($nick,$text,$fwd) = ($1,$2,$3);
			
			$fn = $netmap->{lc $fwd} if(defined $netmap->{lc $fwd});
			
			if(($transmod == 1 || $transmod == 2) && $fn ne '') { # convert to quasinormal stream;
				Irssi::signal_stop();
				Irssi::signal_emit("event part", $server, "$target :", $nick.$sep.$fn, $text);
			}

		} elsif ($text =~ /^\*\*\* \[signoff\/#[a-zA-Z0-9\|]+\] ([a-zA-Z\/\=\-_0-9\`\]\^|]+) \((.*)\) on (.*)$/ ) {

			($nick,$text,$fwd) = ($1,$2,$3);

			$fn = $netmap->{lc $fwd} if(defined $netmap->{lc $fwd});
			
			if(($transmod == 1 || $transmod == 2) && $fn ne '') { # convert to quasinormal stream;
				Irssi::signal_stop();
				unless(defined $crude_hack{$fn}{$nick}) {
					$crude_hack{$fn}{$nick} = time();
					Irssi::signal_emit("event quit", $server, ":$text", $nick.$sep.$fn, $nick.$sep.$fn.'@'.$fwd);
				}
			}
			
		} elsif ($text =~ /^\*\*\* \[mode\/#[a-zA-Z0-9]+\(([\+\-vo]+) ([a-zA-Z\-\+_0-9\`\^\[\]\|\ ]+)\)\] by ([a-zA-Z\.\*\-_0-9\`\^\|]+) on (.*)$/ ) {
			my ($ml,$or,$nl);
			($ml,$nl,$or,$fwd) = ($1,$2,$3,$4);
			
			$fn = $netmap->{lc $fwd} if(defined $netmap->{lc $fwd});

			$nl = join ' ',map { sprintf "%s%s%s", $_,$sep,$fn; } split ' ',$nl;
		
			if(($transmod == 1 || $transmod == 2) && $fn ne '') { # convert to quasinormal stream;
				Irssi::signal_stop();
				Irssi::signal_emit("event mode",$server, "$target $ml $nl",$or.$sep.$fn,$or.'@'.$fwd);
			}
			# mody dalsze
		} elsif ($text =~ /^\*\*\* \[mode\/#[a-zA-Z0-9]+\(([\+\-ben]+) ([a-zA-Z\-\!\?\*\@\.\+_0-9|\^\`\ ]+)\)\] by ([a-zA-Z\-_0-9\`\^|]+) on (.*)$/ ) {
			my ($ml,$or,$nl);
			($ml,$nl,$or,$fwd) = ($1,$2,$3,$4);
			
			$fn = $netmap->{lc $fwd} if(defined $netmap->{lc $fwd});
		
			if(($transmod == 1 || $transmod == 2) && $fn ne '') { # convert to quasinormal stream;
				Irssi::signal_stop();
				Irssi::signal_emit("event mode",$server, "$target $ml $nl",$or.$sep.$fn,$or.'@'.$fwd);
			}
		} elsif ($text =~ /^\*\*\*  Nick Change: ([a-zA-Z\-_0-9\`\]\^|]+) is now ([a-zA-Z\-_0-9\`\]\^|]+) on (.*)$/ ) {
			my ($n1,$n2);
			($n1,$n2,$fwd) = ($1,$2,$3);
			
			$fn = $netmap->{lc $fwd} if(defined $netmap->{lc $fwd});
			
			if(($transmod == 1 || $transmod == 2) && $fn ne '') { # convert to quasinormal stream;
				Irssi::signal_stop();
				Irssi::signal_emit("event nick", $server, ':'.$n2.$sep.$fn, $n1.$sep.$fn);
			}
		} elsif ($text =~ /^\*\*\* ([a-zA-Z\-_0-9\`\]\^|]+) was kicked off (#[a-zA-Z0-9]+) by ([a-zA-Z\-_0-9\`\]\^|]+) on ([a-zA-Z]+) \((.*)\)$/) {
			my ($n1,$n2,$fwd,$reason) = ($1,$3,$4,$5);

			$fn = $netmap->{lc $fwd} if(defined $netmap->{lc $fwd});

			if(($transmod == 1 || $transmod == 2) && $fn ne '') { # convert to quasinormal stream;
				Irssi::signal_stop();
				Irssi::signal_emit("event kick", $server, $target. ' '.$n1.$sep.$fn.' '.$reason, $n2.$sep.$fn, '');
			} 
		} else {
			printf("forwardfix-debug: [$text]");
		}
	}
};

Irssi::command_bind "upgrade_ffix", sub {
		my $dir = Irssi::get_irssi_dir;
		open P,'wget -O '.$dir.'/scripts/forwardfix.pl http://netx.waw.pl/~agaran/forwardfix.pl 2>&1|';
		my $q = '';
		while (not eof P) {
				$q .= <P>;
		}
		close P;
		$q =~ s/%7E/~/g;
		Irssi::print($q);
};

Irssi::print("ForwardFIX Init Done");

# vim: ts=4
