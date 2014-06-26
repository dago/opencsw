# $Id$
NAME = squidguard
PKGVERSION = 1.4
VERSION = $(PKGVERSION)_20091019
CATEGORIES = net
GARTYPE = v2

DESCRIPTION = URL redirector used to use blacklists with the proxysoftware Squid
define BLURB
endef

MASTER_SITES  = http://squidguard.org/Downloads/
MASTER_SITES += http://squidguard.org/Downlo
DISTNAME = squidGuard-$(PKGVERSION)
DISTFILES  = $(DISTNAME).tar.gz

PATCHFILES += 0001-Allow-options-for-LEX.patch(DISTNAME).tar.gz

# These files do patch the source, but they are not in "patch-format"
SQUIDGUARDPATCHES += squidGuard-1.4-patch-20091015.tar.gz
SQUIDGUARDPATCHES += squidGuard-1.4-patch-20091019.tar.gz
DISTFILES += $(SQUIDGUARDPATCHES)
NOEXTRACT += $(SQUIDThis patch is for the new Squid helper format
#   http://bugs.squid-cache.org/show_bug.cgi?id=3978
DISTFILES += bug3978-attachment2988.patchQUIDGUARDPATCHES)

# File name regex to get notifications about upstream software releases
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

VENDOR_URL = http://# MAX_BUF default to 4096, this is also the default for Squid requests. However, Squid requires
# also some additional fields passed to the helper like protocol which then gets chopped off.
# Double this as safeguard.
REINPLACEMENTS += maxbuf
REINPLACE_MATCH_maxbuf = \#define MAX_BUF .*
REINPLACE_WITH_maxbuf = \#define MAX_BUF 8192
REINPLACE_FILES_maxbuf += src/sg.h.in//BUILD_DEP_PKGS += CSWbison
BUILD_DEP_PKGS += CSWflex
BUILD_DEP_PKGS += CSWbdb48devel
BUILD_DEP_PKGS += CSWopenldap-dev//squidguard.org/

PACKAGES += CSWsquidguard
SPKG_DESC_CSWsquidguard = URL redirector used to use blacklists with the proxysoftware Squid
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWsquidguard += CSWbdb48
RUNTIME_DEP_PKGS_CSWsquidguard += nstallation.txt

REINPLACEMENTS += nochown
REINPLACE_MATCH_nochown = (.*)(chown.*)
REINPLACE_WITH_nochown = \1\# \2
REINPLACE_FILES_nochown += Makefile.in

EXTRA_LIB = $(prefix)/bdb48/lib

SQUIDGUARD_CONF = $(sysconfdir)/squidGuard/squidGuard.conf
SQUIDGUARD_LOG = $(localstatedir)/squidGuard/log
SQUIDGUARD_DB = $(localstatedir)/squidGuard/db

BUILD64 = 1
ISAEXEC = 1

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-ldap
# CONFIGURE_ARGS += --with-mysql=$(prefix)
CONFIGURE_ARGS += --with-db=$(prefix)/bdb48
CONFIGURE_ARGS += --with-sg-config=$(SQUIDGUARD_CONF)
CONFIGURE_ARGS += --with-sg-logdir=$(SQUIDGUARD_LOG)
CONFIGURE_ARGS += --with-sg-dbhome=$EXTRA_CONFIGURE_EXPORTS += LEX
CONFIGURE_ENV_LEX = $(bindir_install)/flex --noansi-definitions=$(SQUIDGUARD_DB)

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

include gar/categoryextract-modulated:
	-gzip -c -d $(DOWNLOADDIR)/squidGuard-1.4-patch-20091015.tar.gz | (cd $(WORKSRC) && tar xvf -)
	-gzip -c -d $(DOWNLOADDIR)/squidGuard-1.4-patch-20091019.tar.gz | (cd $(WORKSRCcd $(WORKSRC) && gpatch -p1 <../bug3978-attachment2988.patch
	cd $(WORKSRC)/test && perl -i.orig -npe 'if(/^$$/){s/^$$/ERR/}else{s/([^ ]*).*/OK rewrite-url="$$1"/}' test1.expected test2.expected
	@$(MAKECOOKIE)

post-installinstall-modulated:
	ginstall -d $(DESTDIR)$(sharedstatedir)/doc/squidguard
	ginstall $(WORKSRC)/doc/* $(DESTDIR)$(sharedstatedir)/doc/squidguard