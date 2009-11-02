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

INSTALL_SCRIPTS = custom
#INSTALL_ARGS = TOAST_INSTALL_ROOT="$(DESTDIR)$(prefix)"
#INSTALL_ARGS += GSM_INSTALL_ROOT="$(DESTDIR)$(prefix)"

include gar/category.mk

post-build-modulated:

install-custom:
	ginstall -d $(DESTDIR)$(bindir)
	ginstall $(WORKSRC)/bin/toast $(DESTDIR)$(bindir)
	gln untoast $(DESTDIR)$(bindir)/toast
	gln tcat $(DESTDIR)$(bindir)/toast
	ginstall -d $(DESTDIR)$(libdir)
	ginstall $(WORKSRC)/lib/libgsm.a $(DESTDIR)$(libdir)
	ginstall -d $(DESTDIR)$(includedir)
	ginstall $(WORKSRC)/inc/gsm.h $(DESTDIR)$(includedir)
	ginstall -d $(DESTDIR)$(mandir)/man1
	ginstall $(WORKSRC)/man/toast.1 $(DESTDIR)$(mandir)/man1
	ginstall -d $(DESTDIR)$(mandir)/man3
	ginstall $(WORKSRC)/man/*.3 $(DESTDIR)$(mandir)/man3
	@$(MAKECOOKIE)
