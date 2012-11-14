# $Id$

NAME = openjade
VERSION = 1.3.2
CATEGORIES = apps
GARTYPE = v2

BUILD_DE-dev
AGES = CSWopenjade
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
DISTFILES  = $(NAME)-$(VERSION).tar.gz
DISTFILES += CSWopenjade.postinstall CSWopenjade.preremove

PATCHFILES = openjadPATCHFILES += 0002-adjust-types-in-a-pow-call.patch

GARCOMPILER = GNUGARCOMPILER = GCC3

CONFIGURE_ARGS = $(DIRPATHS) --disable-static
CONFIGURE_ARGS += --datadir=$(datadir)/sgml/$(NAME)
CONFIGURE_ARGS += --enable-splibdir=$(libdir)
CONFIGURE_ARGS += --enable-default-catalog=$(sysconfdir)/sgml/catalog
CONFIGURE_ARGS += --disable-stat

INSTALL_ARGS = install install-man

sysconfdir = /etc/opt/csw

PACKAGES += CSWlibogrove0
PKGFILES_CSWlibogrove0 += $(call baseisadirs,$(libdir),libogrove\.so\.0(\.\d+)*)
SPKG_DESC_CSWlibogrove0 += $(DESCRIPTION), libogrove.so.0

PACKAGES += CSWlibospgrove0
PKGFILES_CSWlibospgrove0 += $(call baseisadirs,$(libdir),libospgrove\.so\.0(\.\d+)*)
SPKG_DESC_CSWlibospgrove0 += $(DESCRIPTION), libospgrove.so.0

PACKAGES += CSWlibostyle0
PKGFILES_CSWlibostyle0 += $(call baseisadirs,$(libdir),libostyle\.so\.0(\.\d+)*)
SPKG_DESC_CSWlibostyle0 += $(DESCRIPTION), libostyle.so.0

PACKAGES += CSWopenjade-dev
SPKG_DESC_CSWopenjade-dev += $(DESCRIPTION), development files
PKGFILES_CSWopenjade-dev += $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWopenjade-dev += CSWlibospgrove0
RUNTIME_DEP_PKGS_CSWopenjade-dev += CSWlibostyle0
RUNTIME_DEP_PKGS_CSWopenjade-dev += CSWlibogrove0

PACKAGES += CSWopenjade
SPKG_DESC_CSWopenjade += $(DESCRIPTION)
RUNTIME_DEP_PKGS_CSWopenjade += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWopenjade += CSWlibosp5
RUNTIME_DEP_PKGS_CSWopenjade += CSWlibospgrove0
RUNTIME_DEP_PKGS_CSWopenjade += CSWlibostyle0
RUNTIME_DEP_PKGS_CSWopenjade += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWopenjade += CSWsgmlcommon
RUNTIME_DEP_PKGS_CSWopenjade += CSWxmlcommon

CHECKPKG_OVERRIDES_CSWopenjade += surplus-dependency|CSWxmlcommon
CHECKPKG_OVERRIDES_CSWopenjade += surplus-dependency|CSWsgmlcommondir = /etc/opt/csw

include gar/category.mk

sgmldir = $(DESTDIR)/$(datadir)/sgml/$(NAME)
sgmldoc = $(DESTDIR)/$(docdir)/$(NAME)
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
		touch $(NAME).soc)
	@echo Installing docs.
	@( cd $(WORKSRC); \
		$(INSTALL_DIR) $(sgmldoc); \
		$(INSTALL_DATA) jadedoc/*htm jadedoc/*txt $(sgmldoc)/; \
		$(INSTALL_DIR) $(sgmldoc)/images; \
		$(INSTALL_DATA) jadedoc/images/* $(sgmldoc)/images/; \
		$(INSTALL_DATA) dsssl/README.jadetex $(sgmldoc)/; \
		$(INSTALL_DATA) README COPYING VERSION $(sgmldoc)/; \
	