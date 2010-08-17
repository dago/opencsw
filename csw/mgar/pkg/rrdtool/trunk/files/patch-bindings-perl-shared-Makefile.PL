--- rrdtool-1.4.2.orig/bindings/perl-shared/Makefile.PL	2008-12-05 16:39:55.000000000 +0100
+++ rrdtool-1.4.2/bindings/perl-shared/Makefile.PL	2010-03-04 16:15:30.877275566 +0100
@@ -37,6 +37,7 @@
     'VERSION_FROM' => 'RRDs.pm', # finds $VERSION
     'DEFINE'	   => "-DPERLPATCHLEVEL=$Config{PATCHLEVEL}",
     'INC'          => '-I../../src',
+    'LIBS'         => '-lperl',
     # Perl will figure out which one is valid
     #'dynamic_lib'  => {'OTHERLDFLAGS' => "$librrd -lm"},
     'depend'       => {'RRDs.c' => "../../src/librrd.la"},
