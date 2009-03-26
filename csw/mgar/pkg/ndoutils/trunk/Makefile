GARNAME = ndoutils
GARVERSION = 1.4b7
CATEGORIES = apps

SPKG_DESC_CSWndoutils2x = NDOutils for nagios 2.x
SPKG_DESC_CSWndoutils3x = NDOutils for nagios 3.x

define BLURB
  NDOUtils allows you to export current and historical data from one or more Nagios instances to a MySQL database. Several community addons use this as one of their data sources.
endef

SF_PROJ = nagios
MASTER_SITES = $(SF_MIRRORS)
#MASTER_SITES = http://mesh.dl.sourceforge.net/sourceforge/nagios/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWndoutils2x, prototype postinstall)
DISTFILES += $(call admfiles,CSWndoutils3x, prototype postinstall)
DISTFILES += cswndoutils

PATCHFILES += config.diff
PATCHFILES += installdb.diff

# We define upstream file regex so we can be notifed of new upstream software release
#UFILES_REGEX = -(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

REQUIRED_PKGS_CSWndoutils2x = CSWmysql5rt CSWzlib CSWnagios CSWcswclassutils
REQUIRED_PKGS_CSWndoutils3x = CSWmysql5rt CSWzlib CSWnagios CSWcswclassutils

SPKG_CLASSES_CSWndoutils2x = none cswpreserveconf cswinitsmf
SPKG_CLASSES_CSWndoutils3x = none cswpreserveconf cswinitsmf

ENABLE_CHECK = 0

EXTRA_INC += /opt/csw/mysql5/include
EXTRA_LIB += /opt/csw/mysql5/lib/mysql

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --disable-pgsql	# Postgres is not supported in the current version
CONFIGURE_ARGS += --with-mysql-lib=/opt/csw/mysql5/lib/mysql
CONFIGURE_ARGS += --with-mysql-inc=/opt/csw/mysql5/include

localstatedir=/opt/csw/nagios/ndoutils/var

SKIPTEST = 1
INSTALL_SCRIPTS = custom

CFGDIR = $(prefix)/nagios/ndoutils/etc
BINDIR = $(prefix)/nagios/ndoutils/bin
DOCDIR = $(prefix)/share/doc/ndoutils
CONTRIBDIR = $(prefix)/nagios/ndoutils/contrib
DOCS = Changelog README REQUIREMENTS TODO UPGRADING 

include gar/category.mk

install-custom:
	@cp $(WORKSRC)/docs/"NDOUtils Documentation.pdf" $(WORKSRC)/docs/NDOUtils_Documentation.pdf
	@cp $(WORKSRC)/docs/"NDOUTILS DB Model.pdf" $(WORKSRC)/docs/NDOUTILS_DB_Model.pdf
	@ginstall -m 755 -d $(DESTDIR)/$(CFGDIR)
	@ginstall -m 755 -d $(DESTDIR)/$(BINDIR)
	@ginstall -m 755 -d $(DESTDIR)/$(DOCDIR)
	@ginstall -m 755 -d $(DESTDIR)/$(localstatedir)
	@ginstall -m 755 -d $(DESTDIR)/$(CONTRIBDIR)/db
	@ginstall -m 644 $(WORKSRC)/config/ndo2db.cfg $(DESTDIR)/$(CFGDIR)/ndo2db.cfg.CSW
	@ginstall -m 644 $(WORKSRC)/config/ndomod.cfg $(DESTDIR)/$(CFGDIR)/ndomod.cfg.CSW
	@ginstall -m 644 $(WORKSRC)/config/nagios2.cfg $(DESTDIR)/$(CFGDIR)/nagios2.cfg.CSW
	@ginstall -m 644 $(WORKSRC)/config/nagios3.cfg $(DESTDIR)/$(CFGDIR)/nagios3.cfg.CSW
	@ginstall -m 644 $(WORKSRC)/config/misccommands.cfg $(DESTDIR)/$(CFGDIR)/ndomisccommands.cfg.CSW
	@ginstall -m 755 $(WORKSRC)/src/ndo2db-2x $(DESTDIR)/$(BINDIR)
	@ginstall -m 755 $(WORKSRC)/src/ndo2db-3x $(DESTDIR)/$(BINDIR)
	@ginstall -m 755 $(WORKSRC)/src/ndomod-2x.o $(DESTDIR)/$(BINDIR)
	@ginstall -m 755 $(WORKSRC)/src/ndomod-3x.o $(DESTDIR)/$(BINDIR)
	@ginstall -m 755 $(WORKSRC)/src/file2sock $(DESTDIR)/$(BINDIR)
	@ginstall -m 755 $(WORKSRC)/src/log2ndo $(DESTDIR)/$(BINDIR)
	cp -r $(WORKSRC)/db $(DESTDIR)/$(CONTRIBDIR)
	#@ginstall -m 744 $(WORKSRC)/db/installdb $(DESTDIR)/$(DOCDIR)/db
	@ginstall -m 644 $(WORKSRC)/docs/"NDOUTILS_DB_Model.pdf" $(DESTDIR)/$(DOCDIR)
	@ginstall -m 644 $(WORKSRC)/docs/"NDOUtils_Documentation.pdf" $(DESTDIR)/$(DOCDIR)
	@$(foreach DOC,$(DOCS), ginstall -m 644 $(WORKSRC)/$(DOC) $(DESTDIR)/$(DOCDIR);)
	@ginstall -d $(DESTDIR)/etc/opt/csw/init.d/
	@ginstall -m 755 $(FILEDIR)/cswndoutils $(DESTDIR)/etc/opt/csw/init.d/
	@$(MAKECOOKIE)
