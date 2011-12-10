#!/usr/bin/env perl
#
# This is a minimal example how to read a process catalog data via the
# REST interface. The idea is that you fetch data from a specific URL,
# which is a JSON representation of a data structure. You decode the
# structure, and you're ready to process it.
#
# In this example, the data structure read is one package catalog.

use warnings;

use LWP::Simple;
use JSON;
use Data::Dumper;

my $url = 'http://buildfarm.opencsw.org/pkgdb/rest/catalogs/unstable/sparc/SunOS5.9/';
# More URL patterns at: http://buildfarm.opencsw.org/pkgdb/
my $json_string = get $url;
die "Couldn't get $url" unless defined $json_string;
my $catalog_data = decode_json $json_string;
# You can process the catalog data here.
print Dumper($catalog_data);
