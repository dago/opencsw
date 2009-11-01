GARNAME = gsm
GARVERSION = 1.0.13
CATEGORIES = utils

DESCRIPTION = GSM 06.10 lossy speech compression
define BLURB
endef

MASTER_SITES = http://user.cs.tu-berlin.de/~jutta/gsm/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

SPKG_SOURCEURL = http://user.cs.tu-berlin.de/~jutta/toast.html

WORKSRC = $(WORKDIR)/gsm-1.0-pl13

# Stuff needed for Shared Library
#       @$(MAKE) REAL_DAEMON_DIR=$(REAL_DAEMON_DIR) STYLE=$(STYLE) \
#       LIBS="-lsocket -lnsl" RANLIB=/bin/true \
#       AR=ld ARFLAGS="-G -h libwrap.so.1 -o " \
#       LIB=libwrap.so.1 VSYSLOG= \
#       NETGROUP=-DNETGROUP AUX_OBJ="setenv.o sharedhack.o" TLI=-DTLI \
#       BUGS="$(BUGS) -DSOLARIS_24_GETHOSTBYNAME_BUG" IPV6="$(IPV6)" \
#       EXTRA_CFLAGS="-DUSE_STRERROR -Kpic" all

BUILD64 = 1

CONFIGURE_SCRIPTS =

BUILD_ARGS = CC="$(CC)" CFLAGS="-c $(CFLAGS) -Iinc"

TEST_TARGET = tst addtst misc
TEST_ARGS = $(BUILD_ARGS)

INSTALL_ARGS = TOAST_INSTALL_ROOT="$(DESTDIR)$(prefix)"
INSTALL_ARGS += GSM_INSTALL_ROOT="$(DESTDIR)$(prefix)"

include gar/category.mk

pre-install-modulated:
	ginstall -d $(DESTDIR)$(bindir)
	ginstall -d $(DESTDIR)$(libdir)
	ginstall -d $(DESTDIR)$(prefix)/inc
	ginstall -d $(DESTDIR)$(prefix)/man/man1
	@$(MAKECOOKIE)
