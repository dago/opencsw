#!/usr/bin/perl

use strict;

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

require Encode;
use Unicode::Normalize;

sub strip_diacritics
{
	my $string = shift;

	my $sub = sub { 
		my $val = shift;
		return (chr(hex($val)));
	};

	$string =~ s/\\x([0-9a-fA-F]{2})/$sub->($1)/ge;
	$string =~ s/\xe4/ae/g; 
	$string =~ s/\xf1/ny/g;
	$string =~ s/\xf6/oe/g;
	$string =~ s/\xfc/ue/g;
	$string =~ s/\xff/yu/g;

	$string = NFD( $string );
	$string =~ s/\pM//g;     
	$string =~ s/[^\0-\x80]//g;

	return ($string);
}


sub label_to_filename
{
	my $label = shift;

	$label =~ s/^"//;
	$label =~ s/"$//;
	$label =~ s/[\/\s,]/_/g;
	$label =~ s/[()]//g;
	$label = strip_diacritics ($label);
	return ($label . ".pem");
}


sub parse_multiline_octal
{
	my $lines = shift;

	my $sub = sub { 
		my $val = shift;
		return (chr(oct($val)));
	};

	my $string = join ("", @{$lines});
	$string =~ s/\\([0-9]{3})/$sub->($1)/ge;

	return ($string);
}


my $certificates_list = {};
my $certdata_object;

while (my $line = <STDIN>) {
	next if $line =~ /^#/;
	chomp ($line);
	
	if ($line =~ /^\s*$/) {

		if (exists ($certdata_object->{"ISSUER"}) and exists ($certdata_object->{"SERIAL_NUMBER"})) {

			my $serial_number = $certdata_object->{"SERIAL_NUMBER"};
			my $issuer = $certdata_object->{"ISSUER"};

			$certificates_list->{$issuer} = {} if (not exists ($certificates_list->{$issuer}));

			if (exists ($certificates_list->{$issuer}->{$serial_number})) {

				my $certificate = $certificates_list->{$issuer}->{$serial_number};
				@{$certificate}{ keys (%{$certdata_object}) } = values (%{$certdata_object});

			} else {
				$certificates_list->{$issuer}->{$serial_number} = $certdata_object;
			}
		}
		$certdata_object = {};
		next;
	}

	my ($field, $type, $value) = split (/ /, $line, 3);

	$field =~ s/^CKA_//;

	next if ($field eq "CLASS" or $field eq "TOKEN" 
		or $field eq "PRIVATE" or $field eq "MODIFIABLE");

	if ($type eq "MULTILINE_OCTAL") {
		my @multilines;
		while ($line = <STDIN>) {
			last if $line =~ /^END/;
			chomp ($line);
			push (@multilines, $line);
		}
		$value = parse_multiline_octal (\@multilines);
	} 

	$certdata_object->{$field} = $value;
}


foreach my $certificates_by_issuer (values (%{$certificates_list})) {

	foreach my $certificate (values (%{$certificates_by_issuer})) {

		my $trusted = 1;
		foreach my $trust ("TRUST_SERVER_AUTH", 
				   "TRUST_EMAIL_PROTECTION",
				   "TRUST_CODE_SIGNING") {
			if ($certificate->{$trust} eq "CKT_NSS_NOT_TRUSTED") {
				$trusted = 0;
			}
		}
		if ($trusted) {

			my $filename = label_to_filename ($certificate->{"LABEL"});

			open (FH, "> $filename");
			print FH "-----BEGIN CERTIFICATE-----\n";
			print FH encode_base64 ($certificate->{"VALUE"});
			print FH "-----END CERTIFICATE-----\n";
			close (FH);
			print "Created $filename certificate\n";

		} else {

			print "Certificate " . $certificate->{"LABEL"} . " Not trusted\n";
		}
	}
}

