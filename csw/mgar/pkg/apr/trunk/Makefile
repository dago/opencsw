GARNAME = apr
GARVERSION = 1.3.9
CATEGORIES = lib

DESCRIPTION = Apache Portable Runtime
define BLURB
  The mission of the Apache Portable Runtime (APR) project is to create and
  maintain software libraries that provide a predictable and consistent
  interface to underlying platform-specific implementations.
endef

MASTER_SITES = http://apache.crihan.fr/dist/apr/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

BUILD64 = 1

CONFIGURE_ARGS  = --prefix=$(prefix)
CONFIGURE_ARGS += --enable-layout=csw
CONFIGURE_ARGS += --enable-threads
CONFIGURE_ARGS += --enable-other-child

TEST_TARGET = check

include gar/category.mk

post-extract-modulated:
	ginstall -d $(WORKSRC)
	(echo "# csw layout";\
	echo "<Layout csw>";\
	echo "    prefix:        $(prefix)";\
	echo "    exec_prefix:   $(exec_prefix)";\
	echo "    bindir:        $(bindir)";\
	echo "    sbindir:       $(sbindir)";\
	echo "    libdir:        $(libdir)";\
	echo "    libexecdir:    $(libdir)/apr/modules";\
	echo "    mandir:        $(mandir)";\
	echo "    datadir:       $(datadir)/apr";\
	echo "    includedir:    $(includedir)/apr-$${APR_MAJOR_VERSION}";\
	echo "    localstatedir: /var/run";\
	echo "    runtimedir:    /var/run";\
	echo "    infodir:       $(infodir)";\
	echo "    libsuffix:    -$${APR_MAJOR_VERSION}";\
	echo "</Layout>") >$(WORKSRC)/config.layout
	@$(MAKECOOKIE)

post-install-modulated:
	gln -s apr-1-config $(DESTDIR)$(bindir)/apr-config
	@$(MAKECOOKIE)
