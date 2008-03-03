
use strict;

my $r = shift;
$r->send_http_header('text/html');
$r->print("It worked!!!\n");

