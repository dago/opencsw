GARNAME = aide
GARVERSION = 0.13.1
CATEGORIES = utils

DESCRIPTION = Advanced Intrusion Detection Environment
define BLURB
  AIDE (Advanced Intrusion Detection Environment) is a free
  replacement for Tripwire. It does the same things as the
  semi-free Tripwire and more.
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += aide.conf

# Disable Sun ACLs for now until bug #2887984 is fixed:
#   http://sourceforge.net/tracker/?func=detail&aid=2887984&group_id=86976&atid=581579
#PATCHFILES = 0001-Fix-ACL-ifdef-logic.patch

# Add patch until bug #2888035 is fixed:
#   http://sourceforge.net/tracker/?func=detail&aid=2888035&group_id=86976&atid=581579
PATCHFILES += 0002-Add-missing-prototypes-for-db_sql.patch

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

REQUIRED_PKGS = CSWcurlrt CSWgcrypt CSWgpgerr CSWlibidn CSWlibmhash CSWlibpq
REQUIRED_PKGS += CSWoldaprt CSWosslrt CSWzlib

sysconfdir = /etc/opt/csw/aide
PRESERVECONF = $(sysconfdir)/aide.conf

EXTRA_LIB = $(prefix)/postgresql/lib
EXTRA_INC = $(prefix)/postgresql/include

EXTRA_CPPFLAGS = -D__const=const

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-curl

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
