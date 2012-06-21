NAME = aide
VERSION = 0.15.1
CATEGORIES = utils
GARTYPE = v2

DESCRIPTION = Advanced Intrusion Detection Environment
define BLURB
  AIDE (Advanced Intrusion Detection Environment) is a free
  replacement for Tripwire. It does the same things as the
  semi-free Tripwire and more.
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(NAME)-$(VERSION).tar.gz
DISTFILES += aide.conf

GARCOMPILER = GNU

PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

# Disable Sun ACLs for now until bug #2887984 is fixed:
#   http://sourceforge.net/tracker/?func=detail&aid=2887984&group_id=86976&atid=581579
#PATCHFILES = 0001-Fix-ACL-ifdef-logic.patch

# Add patch until bug #2888035 is fixed:
#   http://sourceforge.net/tracker/?func=detail&aid=2888035&group_id=86976&atid=581579
# PATCHFILES += 0002-Add-missing-prototypes-for-db_sql.patch
# PATCHFILES += 0003-fix-zlib-test_configure.in.patch
PATCHFILES += 0004-fix-_FILE_OFFSET_BITS_configure.in.patch

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

sysconfdir = /etc/opt/csw/aide
PRESERVECONF = $(sysconfdir)/aide.conf

CHECKPKG_OVERRIDES_CSWaide += file-with-bad-content|/usr/local|root/etc/opt/csw/aide/aide.conf.CSW

RUNTIME_DEP_PKGS_CSWaide += CSWlibgcrypt11
RUNTIME_DEP_PKGS_CSWaide += CSWlibz1
RUNTIME_DEP_PKGS_CSWaide += CSWlibssl1-0-0
RUNTIME_DEP_PKGS_CSWaide += CSWlibgpg-error0
RUNTIME_DEP_PKGS_CSWaide += CSWlibcurl4
RUNTIME_DEP_PKGS_CSWaide += CSWlibmhash
RUNTIME_DEP_PKGS_CSWaide += CSWlibidn11
RUNTIME_DEP_PKGS_CSWaide += CSWlibpq5


EXTRA_LIB = $(prefix)/postgresql/lib
EXTRA_INC = $(prefix)/postgresql/include

EXTRA_CPPFLAGS = -D__const=const

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-curl
# we have no libs.a
CONFIGURE_ARGS += --disable-static

# Disable Sun ACLs for now until bug #2887984 is fixed (see above)
#CONFIGURE_ARGS += --with-sun-acl

CONFIGURE_ARGS += --with-psql
# Add extra libraries until bug #2888028 is fixed:
#   http://sourceforge.net/tracker/?func=detail&aid=2888028&group_id=86976&atid=581579
EXTRA_LINKER_FLAGS = -lgcrypt -lgpg-error

# Disable tests until bug #2888084 is fixed
#   http://sourceforge.net/tracker/?func=detail&aid=2888084&group_id=86976&atid=581579
#TEST_TARGET = check
TEST_SCRIPTS =

include gar/category.mk

post-install-modulated:
	ginstall -d $(DESTDIR)/etc/opt/csw/aide
	ginstall $(WORKDIR)/aide.conf $(DESTDIR)/etc/opt/csw/aide/
