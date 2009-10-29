GARNAME = apr
GARVERSION = 1.3.8
CATEGORIES = lib

DESCRIPTION = Apache Portable Runtime
define BLURB
  The mission of the Apache Portable Runtime (APR) project is to create and
  maintain software libraries that provide a predictable and consistent
  interface to underlying platform-specific implementations.
endef

MASTER_SITES = http://apache.crihan.fr/dist/apr/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
#DISTFILES += $(call admfiles,CSWapr,depend prototype)
#DISTFILES += $(call admfiles,CSWapr-devel,depend prototype)
DISTFILES += config.layout

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

BUILD64 = 1

CONFIGURE_ARGS  = --prefix=$(prefix)
CONFIGURE_ARGS += --enable-layout=csw
CONFIGURE_ARGS += --enable-threads
CONFIGURE_ARGS += --enable-other-child

# Tests verified: 1.3.8
TEST_SCRIPTS =

include gar/category.mk

pre-configure-modulated:	install-layout

install-layout:
	@sed -e s,INSTALL_PREFIX,$(prefix),g \
		$(WORKDIR)/config.layout > $(WORKDIR)/$(GARNAME)-$(GARVERSION)/config.layout
	@$(MAKECOOKIE)

post-install: create-link fix-libtool

create-link:
	@( cd $(DESTDIR)$(bindir) ; ln -s apr-1-config apr-config )
	@$(MAKECOOKIE)

fix-libtool:
	@sed -i -e s,/export/home/comand/bin/sed,$(bindir)/gsed,g \
		$(DESTDIR)$(datadir)/apr/build-1/libtool
	@$(MAKECOOKIE)

