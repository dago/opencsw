

CONFIGURE_ARGS  = --prefix=/opt/csw/gcc4
CONFIGURE_ARGS += --exec-prefix=/opt/csw/gcc4
CONFIGURE_ARGS += --with-gnu-as
CONFIGURE_ARGS += --with-as=/opt/csw/bin/gas
CONFIGURE_ARGS += --without-gnu-ld
CONFIGURE_ARGS += --with-ld=/usr/ccs/bin/ld
CONFIGURE_ARGS += --enable-nls
CONFIGURE_ARGS += --with-included-gettext
CONFIGURE_ARGS += --with-libiconv-prefix=/opt/csw
CONFIGURE_ARGS += --with-x
CONFIGURE_ARGS += --with-mpfr=/opt/csw
CONFIGURE_ARGS += --with-gmp=/opt/csw
CONFIGURE_ARGS += --enable-java-awt=xlib
CONFIGURE_ARGS += --enable-libada
CONFIGURE_ARGS += --enable-libssp
CONFIGURE_ARGS += --enable-objc-gc
CONFIGURE_ARGS += --enable-threads=posix
CONFIGURE_ARGS += --enable-stage1-languages=c
CONFIGURE_ARGS += --enable-languages=c,c++,fortran,java,objc

