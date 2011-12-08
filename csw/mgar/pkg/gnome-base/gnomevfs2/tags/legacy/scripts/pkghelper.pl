#!/opt/csw/bin/perl -w
use strict;
use warnings FATAL => 'uninitialized';

use FindBin qw($RealBin $RealScript);
use File::Basename;
use Getopt::Long;

my @csw_ignore = qw(
opt/csw
opt/csw/bin
opt/csw/bin/sparcv8
opt/csw/bin/sparcv8plus
opt/csw/bin/sparcv8plus+vis
opt/csw/bin/sparcv9
opt/csw/lib
opt/csw/lib/X11
opt/csw/lib/X11/app-defaults
opt/csw/lib/sparcv8plus
opt/csw/lib/sparcv8plus+vis
opt/csw/lib/sparcv9
opt/csw/sbin
opt/csw/share
opt/csw/share/doc
opt/csw/share/info
opt/csw/share/locale
opt/csw/share/locale/az
opt/csw/share/locale/az/LC_MESSAGES
opt/csw/share/locale/be
opt/csw/share/locale/be/LC_MESSAGES
opt/csw/share/locale/bg
opt/csw/share/locale/bg/LC_MESSAGES
opt/csw/share/locale/ca
opt/csw/share/locale/ca/LC_MESSAGES
opt/csw/share/locale/cs
opt/csw/share/locale/cs/LC_MESSAGES
opt/csw/share/locale/da
opt/csw/share/locale/da/LC_MESSAGES
opt/csw/share/locale/de
opt/csw/share/locale/de/LC_MESSAGES
opt/csw/share/locale/el
opt/csw/share/locale/el/LC_MESSAGES
opt/csw/share/locale/en@boldquot
opt/csw/share/locale/en@boldquot/LC_MESSAGES
opt/csw/share/locale/en@quot
opt/csw/share/locale/en@quot/LC_MESSAGES
opt/csw/share/locale/es
opt/csw/share/locale/es/LC_MESSAGES
opt/csw/share/locale/et
opt/csw/share/locale/et/LC_MESSAGES
opt/csw/share/locale/eu
opt/csw/share/locale/eu/LC_MESSAGES
opt/csw/share/locale/fi
opt/csw/share/locale/fi/LC_MESSAGES
opt/csw/share/locale/fr
opt/csw/share/locale/fr/LC_MESSAGES
opt/csw/share/locale/ga
opt/csw/share/locale/ga/LC_MESSAGES
opt/csw/share/locale/gl
opt/csw/share/locale/gl/LC_MESSAGES
opt/csw/share/locale/he
opt/csw/share/locale/he/LC_MESSAGES
opt/csw/share/locale/hr
opt/csw/share/locale/hr/LC_MESSAGES
opt/csw/share/locale/hu
opt/csw/share/locale/hu/LC_MESSAGES
opt/csw/share/locale/id
opt/csw/share/locale/id/LC_MESSAGES
opt/csw/share/locale/it
opt/csw/share/locale/it/LC_MESSAGES
opt/csw/share/locale/ja
opt/csw/share/locale/ja/LC_MESSAGES
opt/csw/share/locale/ko
opt/csw/share/locale/ko/LC_MESSAGES
opt/csw/share/locale/locale.alias
opt/csw/share/locale/lt
opt/csw/share/locale/lt/LC_MESSAGES
opt/csw/share/locale/nl
opt/csw/share/locale/nl/LC_MESSAGES
opt/csw/share/locale/nn
opt/csw/share/locale/nn/LC_MESSAGES
opt/csw/share/locale/no
opt/csw/share/locale/no/LC_MESSAGES
opt/csw/share/locale/pl
opt/csw/share/locale/pl/LC_MESSAGES
opt/csw/share/locale/pt
opt/csw/share/locale/pt/LC_MESSAGES
opt/csw/share/locale/pt_BR
opt/csw/share/locale/pt_BR/LC_MESSAGES
opt/csw/share/locale/ro
opt/csw/share/locale/ro/LC_MESSAGES
opt/csw/share/locale/ru
opt/csw/share/locale/ru/LC_MESSAGES
opt/csw/share/locale/sk
opt/csw/share/locale/sk/LC_MESSAGES
opt/csw/share/locale/sl
opt/csw/share/locale/sl/LC_MESSAGES
opt/csw/share/locale/sp
opt/csw/share/locale/sp/LC_MESSAGES
opt/csw/share/locale/sr
opt/csw/share/locale/sr/LC_MESSAGES
opt/csw/share/locale/sv
opt/csw/share/locale/sv/LC_MESSAGES
opt/csw/share/locale/tr
opt/csw/share/locale/tr/LC_MESSAGES
opt/csw/share/locale/uk
opt/csw/share/locale/uk/LC_MESSAGES
opt/csw/share/locale/vi
opt/csw/share/locale/vi/LC_MESSAGES
opt/csw/share/locale/wa
opt/csw/share/locale/wa/LC_MESSAGES
opt/csw/share/locale/zh
opt/csw/share/locale/zh/LC_MESSAGES
opt/csw/share/locale/zh_CN
opt/csw/share/locale/zh_CN/LC_MESSAGES
opt/csw/share/locale/zh_CN.GB2312
opt/csw/share/locale/zh_CN.GB2312/LC_MESSAGES
opt/csw/share/locale/zh_TW
opt/csw/share/locale/zh_TW/LC_MESSAGES
opt/csw/share/locale/zh_TW.Big5
opt/csw/share/locale/zh_TW.Big5/LC_MESSAGES
opt/csw/share/man
);

my @csw_dirs = qw();
#my @csw_dirs = qw(
#etc/init.d
#etc/rc0.d
#etc/rc1.d
#etc/rc2.d
#etc/rc3.d
#etc/rcS.d
#opt/csw
#opt/csw/etc
#opt/csw/bin
#opt/csw/bin/sparcv8
#opt/csw/bin/sparcv8plus
#opt/csw/bin/sparcv8plus+vis
#opt/csw/bin/sparcv9
#opt/csw/sbin
#opt/csw/share
#opt/csw/share/doc
#opt/csw/share/locale
#opt/csw/share/man
#opt/csw/share/man/man1
#opt/csw/share/man/man2
#opt/csw/share/man/man3
#opt/csw/share/man/man4
#opt/csw/share/man/man5
#opt/csw/share/man/man6
#opt/csw/share/man/man7
#opt/csw/share/man/man8
#opt/csw/share/info
#opt/csw/lib
#opt/csw/lib/X11
#opt/csw/lib/X11/app-defaults
#opt/csw/include
#opt/csw/libexec
#opt/csw/var
#);

my @possible_scripts = qw(request checkinstall preinstall postinstall preremove postremove);

my @sunwsprolocs = ('/opt/forte11x86/SUNWspro/bin', '/opt/forte11/SUNWspro/bin', '/opt/studio/SOS11/SUNWspro/bin', '/opt/studio/SOS10/SUNWspro/bin', '/opt/forte8/SUNWspro/bin', '/opt/SUNWspro/bin');
my $builddir     = $ENV{'BUILDDIR'} || '/opt/build/michael';
my $packagedir   = $ENV{'PACKAGEDIR'} || "${RealBin}/../packages";
my $content      = "/var/sadm/install/contents";
my %options; # getopt

# variables defined via eval
my $progname     = undef;
my $version      = undef;
my $buildroot    = undef;
my $category     = undef;
my $vendor       = undef;
my $hotline      = 'http://www.opencsw.org/bugtrack/';
my $email        = 'michael@opencsw.org';
my @sources      = undef;
my $prepatch     = undef;
my @patches      = (); # default to no patches
my $copyright    = undef;
my $build        = undef;
my $suffix       = undef;
my $rev          = undef;
my $arch         = undef;
my $osversion    = undef;
my @packages     = undef;
my @isaexecs     = ();
my $sunwspropath = undef;
my %attributes   = ();
my %seenpaths    = ();
my %contents     = ();

# helper applications
my $tar = '/opt/csw/bin/gtar';

sub
prepare
{
	chdir($builddir) || die("can't change to $builddir");

	foreach my $source (@sources) {
		if      (($source =~ /tar\.gz$/)
		       ||($source =~ /tgz$/)
		       ||($source =~ /tar\.Z$/)) {
			system("/bin/gzcat ${RealBin}/../sources/${source} | ${tar} xf -");

		} elsif ($source =~ /tar\.bz2$/) {
			system("/bin/bzcat ${RealBin}/../sources/${source} | ${tar} xf -");

		} elsif ($source =~ /tar$/) {
			system("${tar} xf ${RealBin}/../sources/${source}");

		} else {
			die("don't know how to extrace ${source}");
		}
	}

	if (defined($prepatch)) {
		open(PREPATCH, "> $builddir/prepatch") || die ("can't create $builddir/prepatch: $!");
		print PREPATCH $prepatch;
		close(PREPATCH);
		system("chmod +x $builddir/prepatch");
		system("/bin/bash -x $builddir/prepatch");
		unlink("$builddir/prepatch");
	}

	foreach my $patch (@patches) {
		chdir("$builddir/@{$patch}[1]") || die("can't change to $builddir/@{$patch}[1]");
		system("gpatch @{$patch}[2] < ${RealBin}/../sources/@{$patch}[0]");
	}
}

sub probe_directory
{
        while (my $dir = shift) {
                -d $dir && return $dir;
        }

        return undef;
}


sub
isaexec
{
	foreach my $exec (@isaexecs) {
		open(ISA, "> ${builddir}/isaexec.c") || die("can't create ${builddir}/isaexec.c for overwrite: $!");
		print ISA <<"EOF";
#include <unistd.h>

int
main(int argc, char *argv[], char *envp[])
{
	return (isaexec("${exec}", argv, envp));
}
EOF
		close(ISA);
		system("${sunwspropath}/cc -o ${buildroot}${exec} ${builddir}/isaexec.c");
		unlink("${builddir}/isaexec.c");
	}
}

sub
build
{
	chdir($builddir) || die("can't change to $builddir");

	open(BUILD, "> $builddir/build") || die ("can't create $builddir/build: $!");
	print BUILD $build;
	close(BUILD);
	system("chmod +x $builddir/build");
	system("/bin/bash -x $builddir/build");
	unlink("$builddir/build");
	isaexec();
	strip();
}

sub
compute_ownership
{
	my $path  = shift;
	my $perm  = shift;
	my $user  = 'root';
	my $group = 'bin';

	if (%attributes) {
		$perm  = $attributes{$path}->{perm}   || $perm;
		$user  = $attributes{$path}->{user}   || $user;
		$group = $attributes{$path}->{group} || $group;
	}

	return "$perm $user $group\n";
}

# This functions purpose is to get sure that all directories in /path/to/file
# are also in file list. It also accounts which filename was packaged in what
# package. So that it possible to warn the user if a file has been packaed in
# more than one package.

sub
verify_path
{
	my $r = shift;
	my $prototype = shift;
	my $path      = shift;

	push(@{$seenpaths{$path}}, "CSW$r->{pkgname}");

	# Handle symlinks in the art of etc/rcS.d/K03cswsamba=../init.d
	$path =~ s/=.*$//;

	while ('.' ne ($path = dirname($path))) {
		if (! grep($_ =~ /^d none \/\Q${path}\E\s+/, @$prototype)) {
			pkgproto($r, $prototype, `echo ${path} | pkgproto`);
		}
	}
}

sub
pkgproto
{
	my $r = shift;
	my $prototype = shift;

	while (my $line = shift) {
		my @fields = split(/\s+/, $line);
		if ($fields[0] eq 'd') {
			# d none opt/csw 0755 sithglan icipguru
			if ((! ($fields[2] =~ /\//)) || (grep($fields[2] eq $_, @csw_ignore)) ) {
				# skip toplevel dirs (opt, etc, ...)

			} elsif (grep($fields[2] eq $_, @csw_dirs)) {
				unshift(@$prototype, "$fields[0] $fields[1] /$fields[2] ? ? ?\n");
			} else {
				unshift(@$prototype, "$fields[0] $fields[1] /$fields[2] " . compute_ownership("/$fields[2]", "$fields[3]"));
			}

		} elsif ($fields[0] eq 'f') {
			# f none opt/csw 0755 sithglan icipguru
			push(@$prototype, "$fields[0] $fields[1] /$fields[2] " . compute_ownership("/$fields[2]", "$fields[3]"));
			verify_path($r, $prototype, $fields[2]);

		} elsif ( ($fields[0] eq 's')
			||($fields[0] eq 'l')) {
			push(@$prototype, "$fields[0] $fields[1] /$fields[2]\n");
			verify_path($r, $prototype, $fields[2]);
		} else {
			die ("unknown line: <$line>");
		}
	}
}

sub
generate_prototype
{
	my $r = shift;

	my @prototype = ();

	chdir($buildroot) || die("can't change to ${buildroot}: $!");
	push(@prototype, "i pkginfo\n");
	push(@prototype, "i depend\n");
	if (defined(${copyright})) {
		-f "$builddir/${copyright}" || die("can't find copyrightfile: $!");
		system("cp $builddir/${copyright} copyright");
		push(@prototype, "i copyright\n");
	}
	foreach my $file (@possible_scripts) {
		if (defined($r->{"$file"})) {
			-f "${RealBin}/../sources/$r->{$file}" || die("can't find $file: $!");
			system("cp -f ${RealBin}/../sources/$r->{$file} $file");
			push(@prototype, "i $file\n");
		}
	}

	my @dirs  = `gfind @{$r->{filelist}} -type d | sort | uniq | pkgproto`;
	pkgproto($r, \@prototype, @dirs);
	my @links = `gfind @{$r->{filelist}} -type l | sort | uniq | pkgproto`;
	pkgproto($r, \@prototype, @links);
	my @files = `gfind @{$r->{filelist}} -type f | sort | uniq | pkgproto`;
	pkgproto($r, \@prototype, @files);

	open(PROTOTYPE, "> ${buildroot}/prototype") || die("can't open ${buildroot}/prototype for overwrite: $!");
	print PROTOTYPE @prototype;
	close(PROTOTYPE);
}

sub
uniq
{
	my %hash; @hash{@_} = ();
	return sort keys %hash;
}

sub
write_dependencies
{
	my $r = shift || die("one reference expected");

	my @out = `pkginfo`;
	my %pkg = ();
	foreach my $line (@out) {
		if ($line =~ /^[^\s]+\s+([^\s]+)\s+([^\s].*)/) {
			$pkg{$1} = "$2";
		}
	}

	open(DEP, '> depend') || die("can't open depend file: $!");

	foreach my $dep (@{$r->{dependencies}}) {
		if (! defined($pkg{$dep})) {
			print STDERR "WARNING: FAKEING dependency for <$dep>\n";
			$pkg{$dep} = 'common - THIS IS A FAKE DEPENDENCY';
		}
		print DEP "P $dep $pkg{$dep}\n";
	}

	if (defined($r->{incompatibilities})) {
		foreach my $inc (@{$r->{incompatibilities}}) {
			if (! defined($pkg{$inc})) {
				print STDERR "WARNING: FAKEING incompatibiltie for <$inc>\n";
				$pkg{$inc} = 'common - THIS IS A FAKE INCOMPATIBILTY';
			}
			print DEP "I $inc $pkg{$inc}\n";
		}
	}

	close(DEP);
}

sub
resolve_link
{
	my $file = shift || die ("one argument expected");
	my $count = 0;

	chomp($file);

	while ((-l $file)
	    && ($count < 10)) {
		my $dirname = dirname($file);
		$file = readlink($file);
		if(! ($file =~ /^\//)) {
			$file = $dirname . '/' . $file;
		} 
		$count++;
	}

	return $file;
}

sub
a1minusa2
{
	my ($a1,$a2) = @_;
	my %h;
	@h{@$a2} = (1) x @$a2;
	return grep {!exists $h{$_}} @$a1;
}

sub
populate_contents
{
	open(FILE, ${content}) || die("can't open ${content}: $!");
	for my $line (<FILE>) {
		# /etc/cron.d/queuedefs f none 0644 root sys 17 1164 1018133064 SUNWcsr
		# 0                     1 2    3    4    5   6  7    8          9
		my @array = split(/\s+/, $line);
		my ($file, $type, @packages) = @array[0, 1, 9 ... $#array];
		if ($type =~ /^f$/) {
			push(@{$contents{$file}}, @packages);
		}
	}
	close(FILE);
}

sub
find_dependencies
{
	my $r = shift || die("one reference expected");
	populate_contents();

	chdir(${buildroot}) || die("can't change to ${buildroot}: $!");
	# look for shared libaries
	my @deps = `gfind @{$r->{filelist}} \\( -type f -perm +111 \\) -o -path opt/csw/lib/\\*.so\\* | xargs ldd 2> /dev/null | grep -v 'file not found' 2> /dev/null | grep '=>' | awk '{print \$3}'`;

	# look for bangs
	my @files = `gfind @{$r->{filelist}} -type f -perm +111`;
	foreach my $file (@possible_scripts) {
		-f "${buildroot}/${file}" && push(@files, "${buildroot}/${file}");
	}
	foreach my $file (@files) {
		chomp($file);
		open(FILE, $file) || die("can't open ${file}: $!");
		my $firstline = <FILE>;
		if ($firstline =~ /^#!\s?([^\s]+)/) {
			push(@deps, "$1\n");
		}
		close(FILE);
	}
	
	# resolve symlinks / substitute
	@deps = uniq(@deps);
	for my $element (@deps) {
		# /bin and /lib are packages in /usr/{bin,lib}
		$element =~ s#^/bin#/usr/bin#;
		$element =~ s#^/lib#/usr/lib#;
		# /opt/csw/lib/sparcv8 is a symlink to .
		$element =~ s#^/opt/csw/lib/sparcv8#/opt/csw/lib#;
		# Resolve links if necessary
		$element = resolve_link($element);
	}

	# get dependencies
	foreach my $dep (@deps) {
		# </usr/lib/../openwin/lib/libX11.so.4>
		$dep =~ s#\w+\/\.\.##g;

		if (defined($contents{$dep})) {
			push(@{$r->{dependencies}}, @{$contents{$dep}});
		}
	}

	# make them uniq and don't include a dependency to the packet itself
	@{$r->{dependencies}} = grep("CSW$r->{pkgname}" ne $_, uniq(@{$r->{dependencies}}));

	if (defined($r->{exclude_dependencies})) {
		@{$r->{dependencies}} = a1minusa2($r->{dependencies}, $r->{exclude_dependencies});
	}

	write_dependencies($r);
}

sub
strip
{
	system("/usr/ccs/bin/strip ${buildroot}/opt/csw/bin/* ${buildroot}/opt/csw/bin/sparcv8/* ${buildroot}/opt/csw/bin/sparcv8plus/* ${buildroot}/opt/csw/bin/sparcv8plus+vis/* ${buildroot}/opt/csw/bin/sparcv9/* 2> /dev/null");
}

sub
generate_pkginfo
{
	my $r = shift || die("one reference expected");

	chdir(${buildroot}) || die("can't change to ${buildroot}: $!");
	open(PKGINFO, '> pkginfo');

print PKGINFO <<"EOF";
PKG=CSW$r->{pkgname}
NAME=$r->{name}
ARCH=${arch}
CATEGORY=${category}
VERSION=${version}
VENDOR=${vendor}
HOTLINE=${hotline}
EMAIL=${email}
EOF
# DESC=[Optional extra info about software. Omit this line if you wish]
	close(PKGINFO);
}

sub
actually_package
{
	my $r = shift || die("one reference expected");

	my $filename="$r->{filename}-${version}-SunOS${osversion}-${arch}-CSW.pkg";

	chdir(${buildroot}) || die("can't change to ${buildroot}: $!");
	system("/usr/bin/pkgmk -o -r ${buildroot}");
	system("/usr/bin/pkgtrans -s /var/spool/pkg ${packagedir}/$filename CSW$r->{pkgname}");
	unlink("${packagedir}/${filename}.gz");
	system("/usr/bin/gzip ${packagedir}/$filename");
	system("rm -rf /var/spool/pkg/CSW$r->{pkgname}");
}

# This function makes all files not readable by me readable. This is because
# the bang checker and pkgmk needs this. The correct permissions are allready
# in pkginfo file so everything is as it should be.

sub
make_all_files_readable_by_user
{ 
	my $r = shift || die("one reference expected");

	chdir(${buildroot}) || die("can't change to ${buildroot}: $!");
	system("gfind @{$r->{filelist}} -perm -400 -o -print | xargs -x -n 1 chmod u+r");
}

sub
mkpackage
{
	foreach my $r (@packages) {
		generate_prototype($r);
		make_all_files_readable_by_user($r);
		generate_pkginfo($r);
		find_dependencies($r);
		actually_package($r);
	}

	foreach my $key (keys(%seenpaths)) {
		if (1 < @{$seenpaths{$key}}) {
			print "$key -> @{$seenpaths{$key}}\n";
		}
	}
}

if (! (-d $builddir)) {
	mkdir("$builddir", 0755) || die("can't create $builddir: $!");
}

#main
# {

if (! GetOptions(\%options, "p", "b", "c", "s", "u", "rev=s")) {
	print <<"__EOF__";
${RealBin}/${RealScript} [-p] [-b] [-c] [-s] specfile ...

	-p    prepare:  extract and patch sources
	-b    build:    build and install sources into destenation
	-c    create:   create package
	-s    show:     show build script and exit (high precedence!)
	-u    cleanUp:  remove ${builddir}
	-rev  <rev>     use <rev> instead of current date

	If no parameter is specified. The given specfile is processed. (eg.
	prepared, build and packaged)
__EOF__
	exit(1);
}

# Unset makeflags
$ENV{'MFLAGS'} = '';
$ENV{'MAKEFLAGS'} = '';

my $infile = shift || die('one argument expected');

if (! defined($arch)) {
	$arch = `/bin/uname -p` || die("can't get arch: $!");
	chomp($arch);
}

$sunwspropath = probe_directory(@sunwsprolocs) || die ("couldn't find SUNWspro");

eval `/bin/cat $infile`;

if (! defined($rev)) {
	$rev = $options{'rev'} || $ENV{'REV'} || `/bin/date '+20%y.%m.%d'`;
}
chomp ($rev);

$version .= ',REV=' . ${rev};

if (defined($suffix)) {
	$version .= $suffix;
}

if (! defined($osversion)) {
	$osversion = `/bin/uname -r`;
	chomp($osversion);
}

if (! -d "${packagedir}") {
	system("/bin/mkdir -p ${packagedir}");
}

if (! keys(%options)) {
	prepare();
	build();
	mkpackage();
	exit();
}

if (defined($options{'s'})) {
	print $build;
	exit();
}

if (defined($options{'p'})) {
	prepare();
}

if (defined($options{'b'})) {
	build();
}

if (defined($options{'c'})) {
	mkpackage();
}

if (defined($options{'u'})) {
	system("/bin/rm -rf ${builddir}");
}

# }
