#!/usr/bin/perl -w

use strict;

#  $Id: editconf.perl,v 1.1 2000/05/19 22:44:34 rusty Exp $
#
#  This edits configuration files during software install/uninstall.
#  Run with --help or see the text of the usage subroutine below for
#  more information.
#
#  Examples:
#
#      Add fam to /etc/inetd.conf during install:
#      editconf inetd.conf add '\bfam\b' \
#          "#  fam, the File Alteration Monitor" \
#          "sgi_fam/1-2 stream rpc/tcp wait root /usr/local/bin/fam fam"
#
#      Remove fam from /etc/inetd.conf during uninstall:
#      editconf inetd.conf remove '\bfam\b'
#
#      Add /usr/sysadm/lib to /etc/ld.so.conf#
#      editconf ld.so.conf add '\bsysadm\b' /usr/sysadm/lib
#
#      Add sysadmd to /usr/local/etc/tcpmux.conf:
#      editconf tcpmux.conf add '\bsysadm\b' \
#          "#  sysadmd, for system administration applications" \
#          "sgi_sysadm root /usr/sysadm/bin/sysadmd sysadmd"
#
#  The main goal of this script is to "do no harm."  We don't
#  modify any files if it looks like we're going to mess with
#  lines which have been edited by the user.  The only time we
#  change a file is when we're confident that we're adding new
#  lines, or messing with lines which we ourselves added or
#  removed during a previous invocation of the script.
#
#  Well... that's not entirely true; the "remove" operation comments
#  out any line that matches the given regexp.  But it makes a backup!
#
#  USING EDITCONF WITH AUTOMAKE AND RPM
#
#  This prepends DESTDIR to the files it operates on (unless you pass
#  it a file starting with \.{0,2}/, so it can be used during an
#  automake "make install" into a non-root directory (as you would do
#  while building an RPM package).  Note that the file it attempts to
#  operate on probably won't be present, though, so you'll probably
#  need to ignore errors during the make install:
#
#      make-install-hook:
#              -$(EDITCONF) ld.so.conf add '\bsysadm\b' /usr/sysadm/lib
#
#  This will probably fail when DESTDIR is set, as ld.so.conf probably
#  doesn't exist under DESTDIR; the only reason to have this line in the
#  Makefile.am is so that a normal "make install" will update the
#  configuration files.
#
#  In order to have your configuration files updated during the install/
#  uninstall of an rpm package, you'll need to add something like this
#  to your spec file:
#
#      #  this is %preun rather than %postun because we want to use our
#      #  script before it gets uninstalled.
#      %preun
#      perl /usr/local/lib/fam/editconf.perl ld.so.conf remove '\bsysadm\b'
#
#
sub usage {
    my($msg) = @_;
    $msg && ($msg ne "help") && print STDERR "$msg\n\n";
    print STDERR <<"EOF";
Usage:
  $0 [options] file \"add\" regexp lines...
  $0 [options] file \"remove\" regexp [comment]
  $0 --help

Options:
  -n  No-exec (don't change any files)
  -v  Verbose
  -s  Silent
  --  End argument processing (in case your new config file lines
      start with -)
EOF

    if($msg eq "help") {
        print STDERR <<"EOF";

This edits configuration files.  Given a file name, it looks
in a list of directories (see below) for the file.  (If the file
name starts with "/" or ".", the path list is not searched.)
Once the file is found, the given regular expression is searched
for in the file to determine whether the option or service we're
adding/removing already exists.

If we're adding new lines to the file, there are four possible
outcomes:

  - If the regexp isn't found in the file, we figure our lines
    haven't been added before, and we add them.

  - If the regexp is found in the file, and indeed the exact lines
    we were going to add are already there, we're happy, and we
    don't change the file.

  - If the regexp is found in the file, and the lines we were going
    to add are present but commented out, we uncomment them.

  - If the regexp is found in the file, but in lines which are
    different than the lines we were going to add, we figure the
    option or service we were going to add has already been configured
    differently; in this case, we make our changes in a new copy
    of the file and print a warning message saying that someone
    should compare the two files.  (We don't change the
    configuration of the system in this case.) 

If we're removing lines from the file, there are two possible
outcomes:

  - If the regexp isn't found in the file, we're happy, and we
    don't change the file.

  - If the regexp is found in the file, we make a backup of the
    file, and comment out the lines containing the regexp in the
    original file.

EOF
        print STDERR "Configuration file paths:\n";
        foreach (@::paths) { print STDERR "  $_\n"; }
    }

    exit 1;
}


#  See if DESTDIR is set, to have us operate on files not in /
my $DESTDIR = $ENV{'DESTDIR'} ? $ENV{'DESTDIR'} : "";

#  This is the list of places we'll look for the configuration file
#  if we weren't given an absolute path.
@::paths = ("$DESTDIR/etc", "$DESTDIR/usr/etc", "$DESTDIR/usr/local/etc");

my $comment = '#';
my $verbose = &splicegrep('^-v$', \@ARGV, '^--$');
my $noexec = &splicegrep('^-n$', \@ARGV, '^--$');
my $silent = &splicegrep('^-s$', \@ARGV, '^--$');
&splicegrep('^--?h', \@ARGV, '^--$') && &usage("help");
&splicegrep('^-', \@ARGV, '^--$') && &usage();
&splicegrep('^--$', \@ARGV);

my $file; # the name of the file passed on the command line
my $regexp; # the pattern passed on the command line
my $op; # the operation being performed (add|remove)

($file = shift) || &usage("The config file name is required!");
(($op = shift) && ($op =~ /^(add|remove)$/)) || &usage("\"add\" or \"remove\" is required!");
($regexp = shift) || &usage("The regexp to search for is required!");
my @lines = @ARGV;


#
#  Does the file name start with /, ./, or ../?
#
if ($file =~ m#^\.{0,2}/#) {
    #  Danger!  Not applying $DESTDIR to $path here!
    &shaketh_thy_booty($op, $file, $regexp, @lines);
    exit 0;
}
#
#  No, so we'll search for the file name in the list of paths.
#
$verbose && $DESTDIR && print "Using DESTDIR \"$DESTDIR\"\n";
my($p, $path);
foreach $p (@::paths) {
    $path = "$p/$file";
    $verbose && print STDERR "Looking for $path...\n";
    if (-f $path) {
        &shaketh_thy_booty($op, $path, $regexp, @lines);
        exit 0;
    }
}
die("Couldn't find $file in " . join(" ", @::paths) . "\n");


#
#  Once we know what file we're attacking, this does the actual work.
#
sub shaketh_thy_booty {  #  or is it "thine"?
    my($op, $path, $regexp, @lines) = @_;
    $noexec || -w $path || die("I don't have write permission on $path!\n");
    #  Might as well snort it into memory.  Hopefully it's a small file, ha ha.
    open(CFG, "<$path") || die("Couldn't open $path for input!\n");
    my @wholefile = <CFG>;
    close(CFG);

    my $matched = 0;
    if (!grep /$regexp/, @wholefile) {
        if ($op eq 'add') {
            #  It doesn't contain our regexp, so append our lines and
            #  exit happily.
            if ($noexec) {
                print "I would have added the following lines to $path:\n";
                foreach (@lines) { print "$_\n"; }
            } else {
                open(CFG, ">>$path") || die("Couldn't open $path for append!\n");
                $silent || print "Added the following lines to $path:\n";
                foreach (@lines) {
                    $silent || print "$_\n";
                    print CFG "$_\n";
                }
                $silent || print "(end of lines added to $path)\n";
            }
            exit 0;
        } elsif ($op eq 'remove') {
            #  It doesn't contain our regexp, so we don't need to remove it,
            #  so we're happy.
            exit 0;
        } else { die("bad op \"$op\""); }
    }

    if ($op eq "remove") {
        #  Since we're still here, and we're removing this entry, comment out
        #  all lines matching our regexp.
        if ($noexec) {
            print "I would have commented out the following lines in $path:\n";
            grep {
                /$regexp/ && print;
            } @wholefile;
        } else {
            my $tmpnm = &tmpnam("$path.$$");
            my $comment_re = quotemeta $comment;
            my @commented_out;
            open(CFG, ">$tmpnm") || die("Couldn't open $tmpnm for output!\n");
            foreach (@wholefile) {
                #  We care if it matches, and isn't already commented out.
                if ((/$regexp/) && (!/^$comment_re/)) {
                    push @commented_out, $_;
                    print CFG $comment;
                }
                print CFG;
            }
            if ($#commented_out == -1) {
                #  We didn't actually need to comment anything out!
                #  Apparently all the lines that matched our regexp were
                #  already commented out.
                $verbose && print "All the lines matching our regexp were ",
                                  "already commented out, so we're not doing ",
                                  "anything!\n";
                unlink $tmpnm;
                exit 0;
            }
#            $silent || print "Commented out the following lines in $path:\n";
#            $silent || grep { print; } @commented_out;
#            $silent || print "(end of lines commented out in $path)\n";
            my $bak = &tmpnam("$path.O");
            rename($path, $bak) || die("Couldn't rename $path to $bak!\n");
            rename($tmpnm, $path) || die("Couldn't rename $tmpnm to $path!\n");
            $silent || print "Original file saved as $bak\n";
        }
        exit 0;
    }

    #  just a sanity check...
    ($op eq "add") || die("bad op \"\$op\"");

    #  We're still here, so we found our regexp, which suggests that the
    #  entry we're adding might already be in the file.  Do our new lines
    #  match existing lines exactly?
    $verbose && print "The file contains our regular expression, so let's see ",
                      "if it has our lines...\n";
    $matched = 1;
    my $re;
    foreach (@lines) {
        $re = quotemeta $_;
        $verbose && print "  Looking for \"$re\"\n";
        if (! grep /^$re$/, @wholefile) {
            $verbose && print "  Didn't find it!\n";
            $matched = 0;
            last;
        }
    }
    if ($matched) {
        #  The lines we would have added are already in the file, so
        #  we can all go home early.
        $verbose && print "$path already contains the lines we would have ",
                          "added.\n";
        exit 0;
    }

    #  All right, we're still here, so let's see if the lines we would have
    #  added are in the file, but commented out.  This is slightly complicated
    #  by the possibility that lines we're adding start with comments; if so,
    #  we don't want to require that they be preceded by another comment
    #  character.
    $verbose && print "Let's see if it has our lines, but commented out...\n";
    $re = quotemeta $comment;
    my @linesre = @lines;
    grep {
        #  If it starts with a comment, require make an additional starting
        #  comment optional.  (the ($re.*)? as opposed to $re.*)
        $_ = (/^$re/) ? "^($re.*)?" . quotemeta $_ : "^$re.*" . quotemeta $_;
    } @linesre;
    $matched = 1;
    foreach $re (@linesre) {
        #  This loop through @linesre isn't done in the grep above because
        #  we want that to iterate through every element, while this loop
        #  can bail as soon as it fails to find a line it's looking for.
        $verbose && print "  Looking for \"$re\"\n";
        #  If you change this next line, make sure you make the same changes
        #  in the substitution below.
        if (! grep /$re$/, @wholefile) {
            $verbose && print "  Didn't find it!\n";
            $matched = 0;
            last;
        }
    }
    if ($matched) {
        #  The lines we would have added are already in the file, but
        #  commented out.  Let's uncomment them into a temp file, and then
        #  replace the existing file with the temp file.
        if ($noexec) {
            print "I would have uncommented the following lines in $path:\n";
            foreach (@lines) { print "$_\n"; }
            exit 0;
        }
        #  This is crude.  For every line in the file, if it matches the
        #  commented-out version of any of the lines we're adding, replace
        #  it with the corresponding non-commented-out line.
        my $idx;
        foreach (@wholefile) {
            foreach $idx (0..$#lines) {
                s/$linesre[$idx]$/$lines[$idx]/ && last;
            }
        }
        #  isn't there a perl tmpnam?  this open/die is stupid.
        my $tmpnm = &tmpnam("$path.$$");
        open(CFG, ">$tmpnm") || die("Couldn't open $tmpnm for output!\n");
        print CFG @wholefile;
        close(CFG) || die("Couldn't close $tmpnm after writing!\n");
        rename($tmpnm, $path) || die("Couldn't replace $path with $tmpnm " .
                                     "after writing!\n");
        exit 0;
    }

    #  We're still here, so it looks like our configuration lines are in the
    #  file, but they're different than what we would have added.  Nuts!
    #  Comment out everything matching our regexp and append our new lines,
    #  but do it into a new file so that we don't stomp any existing
    #  configuration.
    my $tmpnm = &tmpnam("$path.N");
    if ($noexec) {
        print "I would have copied $path to $tmpnm and commented out the following lines in $tmpnm:\n";
        grep {
            /$regexp/ && print;
        } @wholefile;
        print "...and added the following lines to $tmpnm:\n";
        foreach (@lines) { print "$_\n"; }
        exit 0;
    }
    grep {
        /$regexp/ && ($_ = ($comment . $_));
    } @wholefile;
    #  Now append our new stuff
    foreach (@lines) {
        push @wholefile, "$_\n";
    }
    open(CFG, ">$tmpnm") || die("Couldn't open $tmpnm for output!\n");
    print CFG @wholefile;
    close(CFG) || die("Couldn't close $tmpnm after writing!\n");
    #  Just for fun, if $path.N already existed, let's see if it's the
    #  same as what we just wrote.
    &diff($tmpnm, "$path.N", \@wholefile) || ($tmpnm = "$path.N");  

    print STDERR <<"EOF";

**********************************************************************
Configuration changes to $file have not been made
automatically because there appears to be a conflict between the
file's current contents and the lines which would have been added.

Original file: $path
New file:      $tmpnm

Please compare these two files and update the original file as needed.
**********************************************************************

EOF
    exit 0;
}


#  Returns the array of elements matching the given re in the given array,
#  and removes those elements from the array.  If $bre is set, we only
#  search through the array until an element matching $bre is encountered.
sub splicegrep {
    my($re, $a, $bre) = @_;
    my @ta = ();
    my @ra = ();
    my $skip = 0;
    $a || ($a = \@ARGV);
    #  sub-optimal but our argv should be short
    grep {
        $bre && /$bre/ && ($skip = 1);
        ((!$skip) && /$re/) ? push @ra, $_ : push @ta, $_;
    } @{$a};
    @{$a} = @ta;
    return @ra;
}


#  This is kind of stupid.
sub tmpnam {
    my($base) = @_;
    my $hope = $base;
    my $count = 0;
    while(-e $hope) {
        $hope = "$base$count";
        ++$count;
    }
    return $hope;
}


#  Returns 0 if we know the two files are the same, 1 if we're not sure.
sub diff {
    my($fn1, $fn2, $fc1) = @_;
    ($fn1 eq $fn2) && return 0;  # same file name!
    my $sz1 = (stat $fn1)[7];  # size $sstuff[7];  #  size
    my $sz2 = (stat $fn2)[7];  # size  $sstuff[7];  #  size
    $sz1 && ($sz1 != $sz2) && return 1;  # different sizes; they're different
    #  Nuts, they're the same size, so we have to compare them.
    open(FH2, "<$fn2") || return 1;
    my @snort2 = <FH2>;
    close(FH2);
    #  Same number of lines?
    ($#snort2 == $#{$fc1}) || return 1;
    my $i = $#snort2;
    while ($i >= 0) {
        ($snort2[$i] eq $fc1->[$i]) || return 1;
        --$i;
    }
    return 0;
}
