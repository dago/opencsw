--- rrdtool-1.4.2.orig/bindings/perl-piped/Makefile.PL	2008-03-15 11:39:48.000000000 +0100
+++ rrdtool-1.4.2/bindings/perl-piped/Makefile.PL	2010-03-04 16:15:51.013159708 +0100
@@ -5,6 +5,7 @@
 WriteMakefile(
     'NAME'         => 'RRDp',
     'VERSION'      => '0.99.0', # finds $VERSION
+    'LIBS'         => '-lperl',
     'linkext'   => {LINKTYPE => ''},
     'dist'    =>    {COMPRESS=>'gzip', SUFFIX=>'gz'},
 );
