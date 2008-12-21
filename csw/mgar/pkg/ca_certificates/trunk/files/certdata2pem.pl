#!/usr/bin/perl

sub encode_base64
{
	my $string = shift;
	my $res = pack("u", $string);
	# Remove first character of each line, remove newlines
	$res =~ s/^.//mg;
	$res =~ s/\n//g;

	$res =~ tr|` -_|AA-Za-z0-9+/|;               # `# help emacs
	# fix padding at the end
	my $padding = (3 - length($string) % 3) % 3;
	$res =~ s/.{$padding}$/'=' x $padding/e if $padding;
	# break encoded string into lines of no more than 76 characters each
	$res =~ s/(.{1,60})/$1\n/g;
	
	return $res;
}


while (my $line = <STDIN>) {
	next if $line =~ /^#/;
	
	if ($line =~ /^\s*$/) {
		undef $fname;
		next;
	}

	chomp ($line);

	if ($line =~ /CKA_LABEL/) {
		my ($label, $type, $val) = split (/ /, $line, 3);
		$val =~ s/^"//;
		$val =~ s/"$//;
		$val =~ s/[\/\s,]/_/g;
		$val =~ s/[()]//g;
		$fname = $val . ".crt";
		next;
	}

	if ($line =~ /CKA_VALUE MULTILINE_OCTAL/) {
		if (not $fname) {
			print "ERROR: unexpected CKA_VALUE MULTILINE_OCTAL\n";
			next;
		}
		my @cert_data;
		while ($line = <STDIN>) {
			last if $line =~ /^END/;
			chomp ($line);
			my @data = split (/\\/, $line);
			shift (@data);
			push (@cert_data, @data);
		}
		@cert_data = map (oct, @cert_data);
		@cert_data = map (chr, @cert_data);
		open (FH, "> $fname");
		print FH "-----BEGIN CERTIFICATE-----\n";
		print FH encode_base64 (join ("", @cert_data));
		print FH "-----END CERTIFICATE-----\n";
		close (FH);
		print "Created $fname certificate\n";
	}
} 
