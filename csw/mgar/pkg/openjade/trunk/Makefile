GARNAME = openjade
GARVERSION = 1.3.2
CATEGORIES = apps

PREREQUISITE_PKGS = CSWopenspdevel
REQUIRED_PKGS = CSWgcc3corert CSWgcc3g++rt
REQUIRED_PKGS += CSWggettextrt CSWiconv CSWopensprt CSWsgmlcommon
REQUIRED_PKGS += CSWxmlcommon

PACKAGES = CSWopenjade
LICENSE = COPYING

DESCRIPTION = A DSSSL implementation.
define BLURB
OpenJade is an implementation of the ISO/IEC 10179:1996 standard DSSSL
(Document Style Semantics and Specification Language). OpenJade is
based on James Clark's Jade implementation of DSSSL. OpenJade is a
command-line application and a set of components. The DSSSL engine
inputs an SGML or XML document and can output a variety of formats:
XML, RTF, TeX, MIF (FrameMaker), SGML, or XML.
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += CSWopenjade.postinstall CSWopenjade.preremove

PATCHFILES = openjade-1.3.1-nsl.patch

# Use gcc3 to build this.  a) it matches opensp b) the c++ used has
# some issues w/sun c++ and c) gcc4 generates object files that get
# the sun linker upset.  [we could likely force gld or a strip in the
# middle somewhere, but this works too.]
GARCOMPILER = GCC3

CONFIGURE_ARGS = $(DIRPATHS) --disable-static
CONFIGURE_ARGS += --datadir=$(datadir)/sgml/$(GARNAME)
CONFIGURE_ARGS += --enable-splibdir=$(libdir)
CONFIGURE_ARGS += --enable-default-catalog=/opt/csw/etc/sgml/catalog
CONFIGURE_ARGS += --disable-static

TEST_SCRIPTS = 

INSTALL_ARGS = install install-man

include gar/category.mk

sgmldir = $(DESTDIR)/$(datadir)/sgml/$(GARNAME)
sgmldoc = $(DESTDIR)/$(docdir)/$(GARNAME)
INSTALL = /opt/csw/bin/ginstall -c
INSTALL_DATA = $(INSTALL) -m 0644
INSTALL_DIR = $(INSTALL) -m 0755 -d

post-configure-modulated:
	@(cd $(WORKSRC); \
		mv libtool libtool.orig; \
		echo 'ARGS=`echo "$$@" | gsed "s#/opt/csw/lib/libosp.la#/opt/csw/lib/libosp.so#g"`' >> libtool; \
		echo $$PWD/$(WORKSRC)'/libtool.orig $$ARGS' >> libtool; \
		chmod 755 libtool; \
	 	echo '/opt/csw/lib/libosp.la:' > jade/Makefile.dep; \
		echo '	/bin/true' >> jade/Makefile.dep )
	@$(MAKECOOKIE)

post-install-modulated:
	@echo Installing catalog files.
	@( cd $(WORKSRC); \
		$(INSTALL_DIR) $(sgmldir)/; \
	  	$(INSTALL_DATA) dsssl/catalog $(sgmldir)/; \
		$(INSTALL_DATA) dsssl/dsssl.dtd $(sgmldir)/; \
		$(INSTALL_DATA) dsssl/fot.dtd $(sgmldir)/; \
		$(INSTALL_DATA) dsssl/style-sheet.dtd $(sgmldir); \
		$(INSTALL_DIR) $(DESTDIR)/$(sysconfdir)/sgml; \
		cd $(DESTDIR)/$(sysconfdir)/sgml; \
		touch $(GARNAME).soc)
	@echo Installing docs.
	@( cd $(WORKSRC); \
		$(INSTALL_DIR) $(sgmldoc); \
		$(INSTALL_DATA) jadedoc/*htm jadedoc/*txt $(sgmldoc)/; \
		$(INSTALL_DIR) $(sgmldoc)/images; \
		$(INSTALL_DATA) jadedoc/images/* $(sgmldoc)/images/; \
		$(INSTALL_DATA) dsssl/README.jadetex $(sgmldoc)/; \
		$(INSTALL_DATA) README COPYING VERSION $(sgmldoc)/; \
	)
	@$(MAKECOOKIE)
