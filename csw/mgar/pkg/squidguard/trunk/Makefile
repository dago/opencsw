# $Id$
NAME = squidguard
PKGVERSION = 1.4
VERSION = $(PKGVERSION),20091019
CATEGORIES = net
GARTYPE = v2

DESCRIPTION = URL redirector used to use blacklists with the proxysoftware Squid
define BLURB
endef

MASTER_SITES  = http://squidguard.org/Downloads/
MASTER_SITES += http://squidguard.org/Downloads/Patches/1.4/
DISTNAME = squidGuard-$(PKGVERSION)
DISTFILES  = $(DISTNAME).tar.gz

# These files do patch the source, but they are not in "patch-format"
SQUIDGUARDPATCHES += squidGuard-1.4-patch-20091015.tar.gz
SQUIDGUARDPATCHES += squidGuard-1.4-patch-20091019.tar.gz
DISTFILES += $(SQUIDGUARDPATCHES)
NOEXTRACT += $(SQUIDGUARDPATCHES)

# File name regex to get notifications about upstream software releases
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

VENDOR_URL = http://squidguard.org/

PACKAGES += CSWsquidguard
SPKG_DESC_CSWsquidguard = URL redirector used to use blacklists with the proxysoftware Squid
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWsquidguard += CSWbdb48

# Just docs, leave for now
CHECKPKG_OVERRIDES_CSWsquidguard += file-with-bad-content|/usr/local|root/opt/csw/share/doc/squidguard/configure.txt
CHECKPKG_OVERRIDES_CSWsquidguard += file-with-bad-content|/usr/local|root/opt/csw/share/doc/squidguard/features.txt
CHECKPKG_OVERRIDES_CSWsquidguard += file-with-bad-content|/usr/local|root/opt/csw/share/doc/squidguard/features.html
CHECKPKG_OVERRIDES_CSWsquidguard += file-with-bad-content|/usr/local|root/opt/csw/share/doc/squidguard/faq.txt
CHECKPKG_OVERRIDES_CSWsquidguard += file-with-bad-content|/usr/local|root/opt/csw/share/doc/squidguard/installation.html
CHECKPKG_OVERRIDES_CSWsquidguard += file-with-bad-content|/usr/local|root/opt/csw/share/doc/squidguard/configuration.txt
CHECKPKG_OVERRIDES_CSWsquidguard += file-with-bad-content|/usr/local|root/opt/csw/share/doc/squidguard/install.txt
CHECKPKG_OVERRIDES_CSWsquidguard += file-with-bad-content|/usr/local|root/opt/csw/share/doc/squidguard/configure.html
CHECKPKG_OVERRIDES_CSWsquidguard += file-with-bad-content|/usr/local|root/opt/csw/share/doc/squidguard/configuration.html
CHECKPKG_OVERRIDES_CSWsquidguard += file-with-bad-content|/usr/local|root/opt/csw/share/doc/squidguard/install.html
CHECKPKG_OVERRIDES_CSWsquidguard += file-with-bad-content|/usr/local|root/opt/csw/share/doc/squidguard/faq.html
CHECKPKG_OVERRIDES_CSWsquidguard += file-with-bad-content|/usr/local|root/opt/csw/share/doc/squidguard/installation.txt

REINPLACEMENTS += nochown
REINPLACE_MATCH_nochown = (.*)(chown.*)
REINPLACE_WITH_nochown = \1\# \2
REINPLACE_FILES_nochown += Makefile.in

EXTRA_LIB = $(prefix)/bdb48/lib

SQUIDGUARD_CONF = $(sysconfdir)/squidGuard/squidGuard.conf
SQUIDGUARD_LOG = $(localstatedir)/squidGuard/log
SQUIDGUARD_DB = $(localstatedir)/squidGuard/db

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS +=  --with-db=$(prefix)/bdb48
CONFIGURE_ARGS += --with-sg-config=$(SQUIDGUARD_CONF)
CONFIGURE_ARGS += --with-sg-logdir=$(SQUIDGUARD_LOG)
CONFIGURE_ARGS += --with-sg-dbhome=$(SQUIDGUARD_DB)

PRESERVECONF += $(SQUIDGUARD_CONF)

MIGRATE_FILES += squidGuard.conf
MIGRATE_DEST_DIR_squidGuard.conf = $(sysconfdir)/squidGuard

TEST_TARGET = test

INSTALL_OVERRIDE_DIRS += prefix
INSTALL_OVERRIDE_DIRS += bindir

INSTALL_OVERRIDE_VARS += configfile
INSTALL_OVERRIDE_VARS += logdir
INSTALL_OVERRIDE_VARS += dbhomedir
INSTALL_OVERRIDE_VAR_configfile = $(DESTDIR)$(SQUIDGUARD_CONF)
INSTALL_OVERRIDE_VAR_logdir = $(DESTDIR)$(SQUIDGUARD_LOG)
INSTALL_OVERRIDE_VAR_dbhomedir = $(DESTDIR)$(SQUIDGUARD_DB)

include gar/category.mk

post-extract-modulated:
	-gzip -c -d $(DOWNLOADDIR)/squidGuard-1.4-patch-20091015.tar.gz | (cd $(WORKSRC) && tar xvf -)
	-gzip -c -d $(DOWNLOADDIR)/squidGuard-1.4-patch-20091019.tar.gz | (cd $(WORKSRC) && tar xvf -)
	@$(MAKECOOKIE)

post-install-modulated:
	ginstall -d $(DESTDIR)$(sharedstatedir)/doc/squidguard
	ginstall $(WORKSRC)/doc/* $(DESTDIR)$(sharedstatedir)/doc/squidguard
	@$(MAKECOOKIE)
