# $Id$
#

NAME = svn-client
VERSION = 1.6.16
DISTNAME = subversion-$(VERSION)
CATEGORIES = utils

DESCRIPTION = subversion version control, client
define BLURB
    The goal of the Subversion project is to build a version control system 
    that is a compelling replacement for CVS in the open source community.
endef

VENDOR_URL   = http://subversion.apache.org/
MASTER_SITES = http://subversion.tigris.org/downloads/
#MASTER_SITES = http://orac.ece.utexas.edu/pub/svn/1.6.7/yuletide-eggnog/
DISTFILES    = $(DISTNAME).tar.bz2
DISTFILES   += fixme.sh

UFILES_REGEX = subversion-(\d+(?:\.\d+)*).tar.bz2


PACKAGES  = CSWsvn-client
SPKG_DESC_CSWsvn           = subversion version control client
CATALOGNAME_CSWsvn         = svn-client
RUNTIME_DEP_PKGS_CSWsvn      += CSWexpat
RUNTIME_DEP_PKGS_CSWsvn      += CSWggettextrt
RUNTIME_DEP_PKGS_CSWsvn      += CSWiconv
RUNTIME_DEP_PKGS_CSWsvn      += CSWneon
RUNTIME_DEP_PKGS_CSWsvn      += CSWlibserf0-0
RUNTIME_DEP_PKGS_CSWsvn      += CSWoldaprt
RUNTIME_DEP_PKGS_CSWsvn      += CSWsasl
RUNTIME_DEP_PKGS_CSWsvn      += CSWsqlite3rt
RUNTIME_DEP_PKGS_CSWsvn      += CSWzlib
RUNTIME_DEP_PKGS_CSWsvn      += CSWapr
RUNTIME_DEP_PKGS_CSWsvn      += CSWapr-util

EXTRA_LINKER_FLAGS = -lintl -liconv

# Only add $ISALIST to dirs which ship optimized versions (done by explicitly
# excluding those lib dirs which are known not to ship optimized versions).
RUNPATH_ISALIST  = $(libdir)

STRIP_LIBTOOL = 1

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --without-apxs
CONFIGURE_ARGS += --without-berkeley-db
CONFIGURE_ARGS += --with-neon=$(prefix)
CONFIGURE_ARGS += --with-serf=$(prefix)
CONFIGURE_ARGS += --with-ssl=$(PREFIX)
CONFIGURE_ARGS += --disable-static
CONFIGURE_ARGS += --without-swig
CONFIGURE_ARGS += --with-zlib=$(prefix)

TEST_TARGET  = check

include gar/category.mk

post-configure-modulated:
	@echo "~~~ Fixing Libtool ~~~"
	$(DOWNLOADDIR)/fixme.sh $(WORKSRC)

