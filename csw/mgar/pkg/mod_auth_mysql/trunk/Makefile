GARNAME = mod_auth_mysql
GARVERSION = 3.0.0
CATEGORIES = server

DESCRIPTION = Implements basic authentication on top of MySQL
define BLURB
	# TODO: Add blurb
endef

SF_PROJ = modauthmysql
MASTER_SITES = $(SF_MIRRORS)
DISTFILES += $(GARNAME)-$(GARVERSION).tar.gz
ADMFILES   = depend prototype postinstall preremove copyright
DISTFILES += $(call admfiles,CSWap2modauthmysql,$(ADMFILES))

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

# Restore deprecated (removed) macros
PATCHFILES += apr.diff

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = custom
INSTALL_SCRIPTS = custom

# No test suite
TEST_SCRIPTS =

STRIP_DIRS = $(DESTDIR)$(prefix)/apache2/libexec

include gar/category.mk

# Apache paths
AP2_ROOT      = $(prefix)/apache2
AP2_LIBEXEC   = $(DESTDIR)$(AP2_ROOT)/libexec
AP2_EXTRACONF = $(DESTDIR)$(AP2_ROOT)/etc/extra
AP2_SBIN      = $(AP2_ROOT)/sbin
APXS          = $(AP2_SBIN)/apxs

# MySQL paths
MYSQL_VERSION = mysql5
MYSQL_ROOT    = $(prefix)/$(MYSQL_VERSION)
MYSQL_BIN     = $(MYSQL_ROOT)/bin
MYSQL_CONFIG  = $(MYSQL_BIN)/mysql_config

build-custom:
	( cd $(WORKSRC) ; \
		$(APXS) -c `$(MYSQL_CONFIG) --libs --include` mod_auth_mysql.c )
	$(DONADA)

install-custom:
	mkdir -p $(AP2_LIBEXEC)
	( cd $(WORKSRC) ; \
	  $(APXS) -S LIBEXECDIR=$(AP2_LIBEXEC) -i mod_auth_mysql.la )
	$(DONADA)

COPYFILES = CONFIGURE CHANGES README
DOCDEST   = $(DESTDIR)$(docdir)/$(GARNAME)

post-install:
	@mkdir -p $(DOCDEST)
	@ginstall $(foreach S,$(COPYFILES),$(WORKSRC)/$(S)) $(DOCDEST)
	$(DONADA)

