#!/usr/bin/perl -w

use strict;

my %counter;

while (<>) {
	if (/\"GET (\/csw\/.*) HTTP\/.\..\"/) {
		# print "match: $1\n";
		my $path = $1;

		if ($path =~ /\/csw\/(unstable|stable)\/(sparc|i386)\/5\.(8|9|10)\/([^-]*)-.*\.pkg.gz/) {
			# print "real match: $1 $2 $3 $4\n";
			$counter{$4}++;
		}

	}
}

foreach my $pkg (reverse(sort {$counter{$a} <=> $counter{$b} or $b cmp $a} (keys(%counter)))) {
	printf "% 20.20s -> %d\n", $pkg, $counter{$pkg};
}
