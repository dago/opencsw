GARNAME = apr
GARVERSION = 1.2.2
CATEGORIES = lib

DESCRIPTION = Apache Portable Runtime
define BLURB
  The mission of the Apache Portable Runtime (APR) project is to create and
  maintain software libraries that provide a predictable and consistent
  interface to underlying platform-specific implementations.
endef

MASTER_SITES = http://apache.mirrored.ca/apr/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWapr,depend prototype)
DISTFILES += $(call admfiles,CSWapr-devel,depend prototype)
DISTFILES += config.layout

CONFIGURE_ARGS  = --prefix=$(prefix)
CONFIGURE_ARGS += --enable-layout=csw
CONFIGURE_ARGS += --enable-threads
CONFIGURE_ARGS += --enable-other-child

# Tests verified: 1.2.2
TEST_SCRIPTS =

include ../category.mk

pre-configure:
	@sed -e s,INSTALL_PREFIX,$(prefix),g \
		$(WORKDIR)/config.layout > $(WORKSRC)/config.layout
	@$(MAKECOOKIE)

post-install: create-link fix-libtool

create-link:
	@( cd $(DESTDIR)$(bindir) ; ln -s apr-1-config apr-config )
	@$(MAKECOOKIE)

fix-libtool:
	@sed -i -e s,/export/home/comand/bin/sed,$(bindir)/gsed,g \
		$(DESTDIR)$(datadir)/apr/build-1/libtool
	@$(MAKECOOKIE)

