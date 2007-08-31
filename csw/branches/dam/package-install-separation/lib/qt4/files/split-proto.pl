#!/usr/bin/perl

open MAIN_SPARC, ">CSWqt4.prototype-sparc";
open MAIN_I386, ">CSWqt4.prototype-i386";
open DEVEL_SPARC, ">CSWqt4-devel.prototype-sparc";
open DEVEL_I386, ">CSWqt4-devel.prototype-i386";
open DOC, ">CSWqt4-docs.prototype";

print DOC "d none /opt/csw/share 0755 root bin\n";
open P, "prototype";
while( <P> ) {
  $_ =~ s/\? \? \?/0755 root bin/;
  my ($type, $class, $pathname, $mode, $owner, $group, $rest) = split( /\s+/, $_, 7 );
  if( $pathname =~ m!^/opt/csw/share/doc! ) {
    print DOC $_;
  } elsif( $pathname =~ m!^/opt/csw/include! ||
	$pathname =~ m!\.(la|prl)$! ||
	$pathname =~ m!^/opt/csw/lib/(sparcv9/)?pkgconfig! ||
	$pathname =~ m!^/opt/csw/share/qt4/(demos|examples|mkspecs|q3porting.xml)! ) {
    print DEVEL_SPARC $_;
    $_ =~ s!/sparcv9!/amd64!;
    print DEVEL_I386 $_;
  } elsif( $pathname =~ m!^/opt/csw/(ignore|share/man|share/perl|lib/perl)! ) {
  } else {
    print MAIN_SPARC $_;
    $_ =~ s!/sparcv9!/amd64!;
    print MAIN_I386 $_;
  }
}
close P;
