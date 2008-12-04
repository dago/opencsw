GARNAME = openjade
GARVERSION = 1.3.2
PATCHLEVEL = 27
CATEGORIES = apps

PREREQUISITES = CSWopensp

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
DISTFILES += $(call admfiles,CSWopenjade,depend postinstall preremove)

PATCHFILES = openjade-1.3.1-nsl.patch

# use gnu c/c++ for this one...(matches opensp and the c++ doesn't want to
# play with sun_cc...)
GARCOMPILER = GNU
GNU_CC_HOME = /opt/csw/gcc3

CONFIGURE_ARGS = $(DIRPATHS) --disable-static
CONFIGURE_ARGS += --datadir=$(datadir)/sgml/$(GARNAME)-$(GARVERSION)
CONFIGURE_ARGS += --enable-splibdir=$(libdir)

TEST_SCRIPTS = 

INSTALL_ARGS = install install-man

include gar/category.mk

sgmldir = $(DESTDIR)/$(datadir)/sgml/$(GARNAME)-$(GARVERSION)
sgmldoc = $(DESTDIR)/$(docdir)/$(GARNAME)
INSTALL = /opt/csw/bin/ginstall -c
INSTALL_DATA = $(INSTALL) -m 0644
INSTALL_DIR = $(INSTALL) -m 0755 -d

post-install:
	@echo Installing catalog files.
	@( cd $(WORKSRC); \
		$(INSTALL_DIR) $(sgmldir)/; \
	  	$(INSTALL_DATA) dsssl/catalog $(sgmldir)/; \
		$(INSTALL_DATA) dsssl/dsssl.dtd $(sgmldir)/; \
		$(INSTALL_DATA) dsssl/fot.dtd $(sgmldir)/; \
		$(INSTALL_DATA) dsssl/style-sheet.dtd $(sgmldir); \
		$(INSTALL_DIR) $(DESTDIR)/$(sysconfdir)/sgml; \
		cd $(DESTDIR)/$(sysconfdir)/sgml; \
		touch $(GARNAME)-$(GARVERSION)-$(PATCHLEVEL).soc; \
		ln -s $(GARNAME)-$(GARVERSION)-$(PATCHLEVEL).soc $(GARNAME).soc; \
	)
	
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