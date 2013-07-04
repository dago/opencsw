# vim: ft=perl

$progname        = 'lrzsz';
$version         = '0.12.20';

$buildroot = "${builddir}/${progname}-${version}-buildroot";

$category  = 'application';
$vendor    = 'http://www.ohse.de/uwe/software/lrzsz.html packaged for CSW by Thomas Glanzmann';

@sources   = ("${progname}-${version}.tar.gz");
@packages  = ({
		pkgname      => ${progname},
		filename     => ${progname},
		name         => "${progname} - X/Y/Zmodem suite",
		dependencies => ['CSWcommon'],
		filelist     => [qw(opt)]
		});
$copyright = "${progname}-${version}/COPYING";

$build     = <<"EOF";
export CC=gcc
export PATH="/opt/csw/bin:/usr/ccs/bin:/usr/bin:/usr/openwin/bin"
export LD_OPTIONS='-R/opt/csw/lib -L/opt/csw/lib'
export LD_LIBRARY_PATH=/opt/csw/lib
export CFLAGS="-I/opt/csw/include -O"
cd ${progname}-${version}
./configure --prefix=/opt/csw --mandir=/opt/csw/share/man
gmake LIBS="-lnsl -lsocket -lintl"
gmake DESTDIR=${buildroot} install
ln ${buildroot}/opt/csw/bin/lrb ${buildroot}/opt/csw/bin/rz
ln ${buildroot}/opt/csw/bin/lrb ${buildroot}/opt/csw/bin/rx
ln ${buildroot}/opt/csw/bin/lrb ${buildroot}/opt/csw/bin/rb
ln ${buildroot}/opt/csw/bin/lsb ${buildroot}/opt/csw/bin/sz
ln ${buildroot}/opt/csw/bin/lsb ${buildroot}/opt/csw/bin/sx
ln ${buildroot}/opt/csw/bin/lsb ${buildroot}/opt/csw/bin/sb
ln ${buildroot}/opt/csw/share/man/man1/lrz.1 ${buildroot}/opt/csw/share/man/man1/rz.1
ln ${buildroot}/opt/csw/share/man/man1/lrz.1 ${buildroot}/opt/csw/share/man/man1/rx.1
ln ${buildroot}/opt/csw/share/man/man1/lrz.1 ${buildroot}/opt/csw/share/man/man1/rb.1
ln ${buildroot}/opt/csw/share/man/man1/lsz.1 ${buildroot}/opt/csw/share/man/man1/sz.1
ln ${buildroot}/opt/csw/share/man/man1/lsz.1 ${buildroot}/opt/csw/share/man/man1/sx.1
ln ${buildroot}/opt/csw/share/man/man1/lsz.1 ${buildroot}/opt/csw/share/man/man1/sb.1
EOF
