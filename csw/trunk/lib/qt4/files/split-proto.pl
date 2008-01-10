#!/usr/bin/perl

# This tiny perl script opens the file 'prototype' in the current
# directory and distributes the files to the main-, devel- and doc-
# package. It should only be run once if the prototypes need to be
# generated for a new version of Qt.

sub footer {
  my $pkg = shift;
  return "i copyright=${pkg}.copyright\n" .
	"i depend=${pkg}.depend\n" .
	"i pkginfo=${pkg}.pkginfo\n";
}

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
  if( $pathname =~ m!^/opt/csw/ignore! ) {
    # Ignore this line
  } elsif( $pathname =~ m!^/opt/csw/share/doc! ) {
    print DOC $_;
  } elsif( $pathname =~ m!^/opt/csw/include! ||
	$pathname =~ m!\.(la|prl)$! ||
	$pathname =~ m!^/opt/csw/bin/(sparcv9/)?qtconfig! ||
	$pathname =~ m!^/opt/csw/lib/(sparcv9/)?pkgconfig! ||
	$pathname =~ m!^/opt/csw/share/qt4/(demos|examples|mkspecs|q3porting.xml)! ) {
    print DEVEL_SPARC $_;
    $_ =~ s!/sparcv9!/amd64!;
    print DEVEL_I386 $_;
  } elsif( $pathname =~ m!^/opt/csw/(share/man|share/perl|lib/perl)! ) {
    # Ignore this line
  } elsif( $class =~ /^(copyright|depend|pkginfo)=/ ) {
    # Ignore this line
  } else {
    print MAIN_SPARC $_;
    $_ =~ s!/sparcv9!/amd64!;
    print MAIN_I386 $_;
  }
}
close P;

print MAIN_SPARC footer( "CSWqt4" );
print MAIN_I386 footer( "CSWqt4" );
print DEVEL_SPARC footer( "CSWqt4-devel" );
print DEVEL_I386 footer( "CSWqt4-devel" );
print DOC footer( "CSWqt4-docs" );
