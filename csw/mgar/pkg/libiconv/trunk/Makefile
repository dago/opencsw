GARNAME = libiconv
GARVERSION = 1.12
CATEGORIES = lib

GETTEXTNAME = gettext
GETTEXTVERSION = 0.17

DESCRIPTION = GNU iconv library
define BLURB
endef

MASTER_SITES = $(GNU_MIRROR)
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(GETTEXTNAME)-$(GETTEXTVERSION).tar.gz
DISTFILES += $(call admfiles,CSWlibiconv,)

UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

# Work around Sun Studio Preprocessor bug #6655406
#   http://sunsolve.sun.com/search/document.do?assetkey=1-1-6655406-1
PATCHFILES = patch-workaround-cc-bug-6655406.diff

# BUILD64 = 1

GETTEXTDISTNAME = $(GETTEXTNAME)-$(GETTEXTVERSION)

default: build
	$(DONADA)

# -- Bootstrap --
# There may not be a working gettext installation on the build system.
# For a fully working libiconv it must be compiled against gettext which
# itself has been compiled against libiconv. The bootstrap-compile is
# therefore done in three steps:
# 1. standalone libiconv
# 2. gettext with newly build libiconv
# 3. libiconv again with fully build gettext

BOOTSTRAPDIR = $(WORKDIR)/bootstrap
BOOTSTRAPCOOKIEDIR = $(BOOTSTRAPDIR)/cookies
BOOTSTRAPBUILDDIR = $(BOOTSTRAPDIR)/build
BOOTSTRAPINSTALLDIR = $(abspath $(BOOTSTRAPDIR)/instroot)

# Extract libiconv and gettext for bootstrap and apply patches
extract-bootstrap:
	COOKIEDIR=$(BOOTSTRAPCOOKIEDIR)							\
	EXTRACTDIR=$(BOOTSTRAPBUILDDIR)							\
		$(MAKE) extract
	$(MAKECOOKIE)

patch-libiconv: extract-bootstrap
	COOKIEDIR=$(BOOTSTRAPCOOKIEDIR)							\
	WORKSRC=$(BOOTSTRAPBUILDDIR)/$(DISTNAME)					\
		$(MAKE) patch
	$(MAKECOOKIE)

configure-libiconv: patch-libiconv
	COOKIEDIR=$(BOOTSTRAPCOOKIEDIR)							\
	CONFIGURE_ARGS="--prefix=$(BOOTSTRAPINSTALLDIR) --disable-nls"			\
		$(MAKE) configure-$(BOOTSTRAPBUILDDIR)/$(DISTNAME)/configure
	$(MAKECOOKIE)

build-libiconv: configure-libiconv
	COOKIEDIR=$(BOOTSTRAPCOOKIEDIR)							\
		$(MAKE) build-$(BOOTSTRAPBUILDDIR)/$(DISTNAME)/Makefile
	$(MAKECOOKIE)

test-libiconv: build-libiconv
	COOKIEDIR=$(BOOTSTRAPCOOKIEDIR)							\
		$(MAKE) test-$(BOOTSTRAPBUILDDIR)/$(DISTNAME)/Makefile
	$(MAKECOOKIE)

install-libiconv: test-libiconv
	cd $(BOOTSTRAPBUILDDIR)/$(DISTNAME) &&						\
	COOKIEDIR=$(BOOTSTRAPCOOKIEDIR)							\
		$(MAKE) install
	$(MAKECOOKIE)


patch-gettext: extract-bootstrap
	@$(MAKECOOKIE)

configure-gettext: install-libiconv patch-gettext
	@# Add -lsec, otherweise acl_trivial can not be found
	@# See gettext bug #21604 for details
	@#   http://savannah.gnu.org/bugs/?21604
	COOKIEDIR=$(BOOTSTRAPCOOKIEDIR)							\
		$(MAKE) configure-$(BOOTSTRAPBUILDDIR)/$(GETTEXTDISTNAME)/configure	\
			 LDFLAGS=-lsec base_prefix=$(BOOTSTRAPINSTALLDIR)
	@$(MAKECOOKIE)

build-gettext: configure-gettext
	COOKIEDIR=$(BOOTSTRAPCOOKIEDIR)							\
	$(MAKE) build-$(BOOTSTRAPBUILDDIR)/$(GETTEXTDISTNAME)/Makefile
	@$(MAKECOOKIE)

test-gettext: build-gettext
	if [ -z "${SKIPTEST}" ]; then							\
		cd $(BOOTSTRAPBUILDDIR)/$(GETTEXTDISTNAME) && gmake check;		\
	fi
	@$(MAKECOOKIE)

install-gettext: test-gettext
	cd $(BOOTSTRAPBUILDDIR)/$(GETTEXTDISTNAME) &&					\
	COOKIEDIR=$(BOOTSTRAPCOOKIEDIR)							\
		$(MAKE) install
	@$(MAKECOOKIE)

clean-source-gettext:
	cd $(BOOTSTRAPBUILDDIR)/$(GETTEXTDISTNAME) &&					\
	COOKIEDIR=$(BOOTSTRAPCOOKIEDIR)							\
		gmake clean
	-rm $(COOKIEDIR)/configure-gettext
	-rm $(BOOTSTRAPCOOKIEDIR)/configure-$(BOOTSTRAPBUILDDIR)/$(GETTEXTDISTNAME)/configure
	
bootstrap: install-libiconv install-gettext
	@$(MAKECOOKIE)

pre-configure: bootstrap

# Don't use libs in /opt/csw/lib or old libiconv.so will get picked up
EXT_LDFLAGS =
EXTRA_CFLAGS = -I$(BOOTSTRAPINSTALLDIR)/include
EXTRA_LDFLAGS = -L$(BOOTSTRAPINSTALLDIR)/lib
CONFIGURE_ARGS ?= $(DIRPATHS)

# 'gmake test' shows three errors of coredumping printf's
# This is due to bug #6550204
#   http://sunsolve.sun.com/search/document.do?assetkey=1-1-6550204-1
# and can safely be ignored as it is a failure in the testsuite.
TEST_TARGET = check

CLEAN_SCRIPTS = all bootstrap

clean-bootstrap:
	@echo " ==> Cleaning bootstrap"
	@rm -rf $(BOOTSTRAPDIR)

include gar/category.mk

# Bootstrap:
#   # Use gxgettext instead of xgettext, gmsgmerge instead of msgmerge
#   PATH=/opt/csw/gnu:$PATH
#   cd libiconv-1.12
#   ./configure --prefix=/root/automatic-multiarch-compile/lib/libiconv/tmp/instroot --disable-nls
#   gmake && gmake install
#   cd ../gettext-0.17
#   # Add -lsec, otherweise acl_trivial can not be found
#   # See bug #21604 for details
#   #   http://savannah.gnu.org/bugs/?21604
#   LDFLAGS=-lsec ./configure --prefix=/root/automatic-multiarch-compile/lib/libiconv/tmp/instroot
#   gmake && gmake install
