# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = check_mk
VERSION = 1.2.4p5
GARTYPE = v2

DESCRIPTION = A new general purpose Nagios-plugin for retrieving data

MASTER_SITES = http://mathias-kettner.de/download/
DISTFILES += $(DISTNAME).tar.gz
DISTFILES += check_mk_setup.conf

PATCHFILES += 0001-Do-not-chown-during-package-building.patch
PATCHFILES += 0001-Allow-setting-SETUPCONF-externally.patch
PATCHFILES += 0001-Honour-SETUPCONF-even-when-DESTDIR-is-set.patch

VENDOR_URL = http://mathias-kettner.de/check_mk.html

PACKAGES += CSWnagios-plugin-checkmk
SPKG_DESC_CSWnagios-plugin-checkmk = A new general purpose Nagios-plugin for retrieving data
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWnagios-plugin-checkmk += CSWapache2
RUNTIME_DEP_PKGS_CSWnagios-plugin-checkmk += CSWperl

# This is a comment
CHECKPKG_OVERRIDES_CSWnagios-plugin-checkmk += file-with-bad-content|/usr/share|root/etc/opt/csw/check_mk/multisite.mk.CSW

GARCOMPILER = GCC4

# The configure/build/install phase is combined in setup.sh
CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

PRESERVECONF += $(sysconfdir)/check_mk/main.mk
PRESERVECONF += $(sysconfdir)/check_mk/multisite.mk

include gar/category.mk

#post-extract:
#	-cd $(WORKSRC) && gtar zxvf livestatus.tar.gz
#	@$(MAKECOOKIE)

install-custom:
	cd $(WORKSRC) && DESTDIR=$(DESTDIR) PATH=/opt/csw/gnu:/usr/xpg4/bin:$(PATH) SETUPCONF=$(abspath $(WORKDIR)/check_mk_setup.conf) CFLAGS="$(CFLAGS)" LDFLAGS="$(LDFLAGS)" LD_OPTIONS="$(LD_OPTIONS)" CC="$(CC)" ./setup.sh
	@# This crashes the python code around elfdump
	rm -f $(DESTDIR)/opt/csw/libexec/check_mk/livestatus.o
	@# WTF? Mixed binaries just deployed?!?
	@# CHECKPKG_OVERRIDES_CSWnagios-plugin-mk-livestatus += binary-architecture-does-not-match-placement|file=opt/csw/share/doc/check_mk/treasures/modbus/agent_modbus|arch_id=62|arch_name=amd64  
	@# CHECKPKG_OVERRIDES_CSWnagios-plugin-mk-livestatus += binary-architecture-does-not-match-placement|file=opt/csw/share/check_mk/agents/waitmax|arch_id=3|arch_name=i386  
	rm -f $(DESTDIR)/opt/csw/share/doc/check_mk/treasures/modbus/agent_modbus
	rm -f $(DESTDIR)/opt/csw/share/check_mk/agents/waitmax
	@# This is also present as multisite.mk, delete the versioned one as we use PRESERVECONF anyway
	rm -f $(DESTDIR)/etc/opt/csw/check_mk/multisite.mk-$(VERSION)
	rm -f $(DESTDIR)/etc/opt/csw/check_mk/main.mk-$(VERSION)
	@$(MAKECOOKIE)
