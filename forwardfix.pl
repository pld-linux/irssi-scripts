# This script is possibly buggy, but i haven't got much time
# to test it. Use at your own risk.
# a g a r a n   a t   p l d   d a s h   l i n u x   d o t   o r g
#
# Now maintained at http://cvs.pld-linux.org/cgi-bin/cvsweb/packages/irssi-scripts/forwardfix.pl


use strict;
use Irssi;
use vars qw($VERSION %IRSSI);

$VERSION = '0.02';

%IRSSI = (
		authors => 'Maciej \'agaran\' Pijanka',
		contact => 'agaran@pld-linux.org',
		name => 'forwardfix',
		description => 'hides crossnetwork channel joining',
		license => 'GPL'
);

#### Interface ###
#
#
#

# VARIABLES
# =========

Irssi::settings_add_str("forward", "forward_chanset","#pld:abw,#pldhelp:abw,#pldlivecd:abw");
Irssi::settings_add_str("forward", "forward_netmap","IRCnet:IN,FreeNode:FN,PLDNet:PN");
Irssi::settings_add_bool("forward","forward_dash",1);
Irssi::settings_add_int("forward", "forward_transmod",0);
Irssi::settings_add_bool("forward","forward_addnet",1);
Irssi::settings_add_str("forward", "forward_sep",'$');

Irssi::print("Its, beta, dont rely on it \nif something like forwardfix-debug: [something]\nhappens report at http://bugs.pld-linux.org");
Irssi::print("-- agaran ");

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
	# RFC2812
	#  nickname   =  ( letter / special ) *8( letter / digit / special / "-" )
	#  letter     =  %x41-5A / %x61-7A       ; A-Z / a-z
	#  digit      =  %x30-39                 ; 0-9
	#  special    =  %x5B-60 / %x7B-7D       ; "[", "]", "\", "`", "_", "^", "{", "|", "}"
	my $re_nick = qr/[A-Za-z0-9\[\]\\\`\_\^\{\|\}\-]+/o;

	my @forward_chanset = split(/[ ,]+/,Irssi::settings_get_str("forward_chanset"));
	map { my @a=split /:/,$_; $chanset->{lc $a[0]} = lc $a[1]; } @forward_chanset;
	my @forward_netmap = split(/[ ,]+/,Irssi::settings_get_str("forward_netmap"));
	map { my @a=split /:/,$_; $netmap->{lc $a[0]} = $a[1]; } @forward_netmap;

	my $now = time(); # yep compute foreach net, just to scope var
	foreach my $n (keys %crude_hack) {
		foreach my $m (keys %{$crude_hack{$n}}) {
			delete $crude_hack{$n}{$m} if($crude_hack{$n}{$m} + 30 < $now);
		}
	}

	if (defined $chanset->{$targetl} && (lc $nick eq $chanset->{$targetl} || ($dash && lc $nick eq $chanset->{$targetl}.'-' ))) {
		if($text =~ /^\(?($re_nick)?\@([A-Z]+)\) (.*)$/) { # maska maska maska
			($nick,$fwd,$text) = ($1,$2,$3);
			$text .= " [$fwd]" if($addnet);

			if($transmod == 2) { # convert to quasinormal stream;
				Irssi::signal_stop();
				Irssi::signal_emit("event privmsg", $server, "$target :$text", $nick.$sep.$fwd, $nick.'@'.$fwd);
			} else {
				Irssi::signal_stop();
				Irssi::signal_emit("event privmsg", $server, "$target :$text", $nick, $nick.'@'.$fwd);
			}

		} elsif ($text =~ /^\* \(?($re_nick)?\@([A-Z]+)\) (.*)$/) { 
			($nick,$fwd,$text) = ($1,$2,$3);
			$text .= " [$fwd]" if($addnet);
			Irssi::signal_stop();
			Irssi::signal_emit("event privmsg", $server, "$target :ACTION $text", $nick, $nick.'@'.$fwd);
			
		} elsif ($text =~ /^\*\*\* Join ($re_nick) \(([a-z\/\=+\~^A-Z\[\-_0-9\^:\@\.]+)\) on (.*)$/ ) {
			($nick,$text,$fwd) = ($1,$2,$3);

			$fn = $netmap->{lc $fwd} if(defined $netmap->{lc $fwd});

			if(($transmod == 1 || $transmod == 2) && $fn ne '') { # convert to quasinormal stream;
				Irssi::signal_stop();
				delete $crude_hack{$fn}{$nick} if(defined $crude_hack{$fn}{$nick});
				Irssi::signal_emit("event join", $server, ":$target", $nick.$sep.$fn, $text);
			}
			
		} elsif ($text =~ /^\*\*\* Part ($re_nick) \(([a-z\/\=+\~^A-Z\[\-_0-9\^:\@\.]+)\) on (.*)$/ ) {
			($nick,$text,$fwd) = ($1,$2,$3);
			
			$fn = $netmap->{lc $fwd} if(defined $netmap->{lc $fwd});
			
			if(($transmod == 1 || $transmod == 2) && $fn ne '') { # convert to quasinormal stream;
				Irssi::signal_stop();
				Irssi::signal_emit("event part", $server, "$target :", $nick.$sep.$fn, $text);
			}

		} elsif ($text =~ /^\*\*\* \[signoff\/#$re_nick\] ([a-zA-Z\/\=\-_0-9\`\]\^|]+) \((.*)\) on (.*)$/ ) {

			($nick,$text,$fwd) = ($1,$2,$3);

			$fn = $netmap->{lc $fwd} if(defined $netmap->{lc $fwd});
			
			if(($transmod == 1 || $transmod == 2) && $fn ne '') { # convert to quasinormal stream;
				Irssi::signal_stop();
				unless(defined $crude_hack{$fn}{$nick}) {
					$crude_hack{$fn}{$nick} = time();
					Irssi::signal_emit("event quit", $server, ":$text", $nick.$sep.$fn, $nick.$sep.$fn.'@'.$fwd);
				}
			}
			
		} elsif ($text =~ /^\*\*\* \[mode\/#[a-zA-Z0-9]+\(([\+\-vo]+) ($re_nick)\)\] by ($re_nick) on (.*)$/ ) {
			my ($ml,$or,$nl);
			($ml,$nl,$or,$fwd) = ($1,$2,$3,$4);
			
			$fn = $netmap->{lc $fwd} if(defined $netmap->{lc $fwd});

			$nl = join ' ',map { sprintf "%s%s%s", $_,$sep,$fn; } split ' ',$nl;
		
			if(($transmod == 1 || $transmod == 2) && $fn ne '') { # convert to quasinormal stream;
				Irssi::signal_stop();
				Irssi::signal_emit("event mode",$server, "$target $ml $nl",$or.$sep.$fn,$or.'@'.$fwd);
			}
			# mody dalsze
		} elsif ($text =~ /^\*\*\* \[mode\/#[a-zA-Z0-9]+\(([\+\-ben]+) ($re_nick)\)\] by ($re_nick) on (.*)$/ ) {
			my ($ml,$or,$nl);
			($ml,$nl,$or,$fwd) = ($1,$2,$3,$4);
			
			$fn = $netmap->{lc $fwd} if(defined $netmap->{lc $fwd});
		
			if(($transmod == 1 || $transmod == 2) && $fn ne '') { # convert to quasinormal stream;
				Irssi::signal_stop();
				Irssi::signal_emit("event mode",$server, "$target $ml $nl",$or.$sep.$fn,$or.'@'.$fwd);
			}
		} elsif ($text =~ /^\*\*\*  Nick Change: ($re_nick) is now ($re_nick) on (.*)$/ ) {
			my ($n1,$n2);
			($n1,$n2,$fwd) = ($1,$2,$3);
			
			$fn = $netmap->{lc $fwd} if(defined $netmap->{lc $fwd});
			
			if(($transmod == 1 || $transmod == 2) && $fn ne '') { # convert to quasinormal stream;
				Irssi::signal_stop();
				Irssi::signal_emit("event nick", $server, ':'.$n2.$sep.$fn, $n1.$sep.$fn);
			}
		} elsif ($text =~ /^\*\*\* ($re_nick) was kicked off (#[a-zA-Z0-9]+) by ($re_nick) on ([a-zA-Z]+) \((.*)\)$/) {
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

Irssi::print("ForwardFIX Init Done");

# vim: ts=4
