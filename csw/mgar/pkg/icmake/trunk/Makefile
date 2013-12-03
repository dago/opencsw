# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = icmake
VERSION = 7.21.00
GARTYPE = v2

DESCRIPTION = Make system

MASTER_SITES = $(SF_MIRROR)
DISTFILES += $(NAME)_$(VERSION).orig.tar.gz
DISTFILES += INSTALL.im

PATCHFILES += 0001-Use-the-correct-dir-for-etc.patch

VENDOR_URL = http://icmake.sourceforge.net

PACKAGES += CSWicmake
SPKG_DESC_CSWicmake = Make system
# PKGFILES is catchall

# We should take care of this, but I really want to get some experience with icmake first
CHECKPKG_OVERRIDES_CSWicmake += file-with-bad-content|/usr/share|root/etc/opt/csw/icmake/icmake.rc

# Default "usr/bin"
ICMAKE_BINDIR = $(patsubst /%,%,$(bindir))
# Default "usr/share/icmake"
ICMAKE_SKELDIR = $(patsubst /%,%,$(sharedstatedir)/icmake)
# Default "usr/share/man"
ICMAKE_MANDIR = $(patsubst /%,%,$(mandir))
# Default "usr/lib/icmake"
ICMAKE_LIBDIR = $(patsubst /%,%,$(libdir)/icmake)
# Default "etc/icmake"
ICMAKE_CONFDIR = $(patsubst /%,%,$(sysconfdir)/icmake)
# Default "etc/icmake"
ICMAKE_DOCDIR = $(patsubst /%,%,$(docdir)/icmake)
# Default "usr/share/doc/icmake"
ICMAKE_DOCDOCDIR = $(patsubst /%,%,$(docdir)/icmake)

EXPANDVARS += INSTALL.im

GARCOMPILER = GNU

EXTRA_CFLAGS += -std=c99

CONFIGURE_SCRIPTS = custom
BUILD_SCRIPTS = custom
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

include gar/category.mk

configure-custom:
	cp $(WORKDIR)/INSTALL.im $(WORKSRC)/INSTALL.im
	@$(MAKECOOKIE)

build-custom:
	cd $(WORKSRC) && PATH=/opt/csw/gnu:$(PATH) CFLAGS="$(CFLAGS)" ./icm_bootstrap /
	@$(MAKECOOKIE)

install-custom:
	cd $(WORKSRC) && PATH=/opt/csw/gnu:$(PATH) ./icm_install all $(DESTDIR)
	@$(MAKECOOKIE)
