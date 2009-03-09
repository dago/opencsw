
## Install everythong /opt/csw/gcc4 instead of /opt/csw
prefix = /opt/csw/gcc4

CONFIGURE_ARGS  = --prefix=$(prefix)
CONFIGURE_ARGS += --exec-prefix=$(prefix)
CONFIGURE_ARGS += --enable-libada
CONFIGURE_ARGS += --enable-libssp
CONFIGURE_ARGS += --enable-objc-gc
CONFIGURE_ARGS += --enable-threads=posix
CONFIGURE_ARGS += --enable-shared
CONFIGURE_ARGS += --with-mpfr=/opt/csw
CONFIGURE_ARGS += --with-gmp=/opt/csw
CONFIGURE_ARGS += --with-gnu-as
CONFIGURE_ARGS += --with-as=/opt/csw/bin/gas
CONFIGURE_ARGS += --without-gnu-ld
CONFIGURE_ARGS += --with-ld=/usr/ccs/bin/ld
CONFIGURE_ARGS += --with-build-time-tools=/opt/csw/bin
## Do not try to build Ada
## Ada must be build with using GCC because the source uses some Ada Code
## Checkout gcc4ada* packages from svn if you wish to build Ada
CONFIGURE_ARGS += --enable-languages=c,c++,fortran,java,objc

