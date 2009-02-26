
###  Configure Section  ###
CPPFLAGS = -I/opt/csw/include
CFLAGS   = -I/opt/csw/include
CXXFLAGS = -I/opt/csw/include
LDFLAGS  = -L/opt/csw/lib -R/opt/csw/lib/\\\\\\\$\$ISALIST -R/opt/csw/lib
OPTFLAGS =

OBJECT_DIR  = $(WORKDIR)/$(DISTNAME)/objdir
WORKSRC     = $(OBJECT_DIR)

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --prefix=$(prefix)/gcc4
CONFIGURE_ARGS += --exec-prefix=$(prefix)/gcc4
CONFIGURE_ARGS += --enable-libada
CONFIGURE_ARGS += --enable-libssp
CONFIGURE_ARGS += --enable-objc-gc
CONFIGURE_ARGS += --enable-threads=posix
CONFIGURE_ARGS += --enable-shared
CONFIGURE_ARGS += --with-mpfr=$(prefix)
CONFIGURE_ARGS += --with-gmp=$(prefix)
CONFIGURE_ARGS += --with-gnu-as
CONFIGURE_ARGS += --with-as=/opt/csw/bin/gas
CONFIGURE_ARGS += --without-gnu-ld
CONFIGURE_ARGS += --with-ld=/usr/ccs/bin/ld
CONFIGURE_ARGS += --with-build-time-tools=$(bindir)
## Do not try to build Ada
## Ada must be build with using GCC because the source uses some Ada Code
## Checkout gcc4ada* packages from svn if you wish to build Ada
CONFIGURE_ARGS += --enable-languages=c,c++,fortran,java,objc
CONFIGURE_ARGS += LDFLAGS=-R/opt/csw/lib
