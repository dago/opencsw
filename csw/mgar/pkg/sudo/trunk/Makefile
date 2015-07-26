# $Id$
#

NAME = sudo
VERSION = 1.8.14p3
CATEGORIES = utils
GARTYPE = v2

EXTRA_MODULATORS = LDAP
MODULATIONS_LDAP = disabled enabled

DESCRIPTION = Provides limited super user privileges
define BLURB
  Sudo (superuser do) allows a system administrator to give certain users (or
  groups of users) the ability to run some (or all) commands as root while
  logging all commands and arguments. Sudo operates on a per-command basis, it
  is not a replacement for the shell.
endef

MASTER_SITES = ftp://ftp.sudo.ws/pub/sudo/
DISTFILES += $(DISTNAME).tar.gz 
DISTFILES += sudo.conf.CSW
DISTFILES += map.sudo

LICENSE = doc/LICENSE

VENDOR_URL = http://www.sudo.ws

# To have least Priv Support for Solaris 10 build on all Platforms
P+= solaris9-sparc solaris9-i386
PACKAGING_PLATFORMS += solaris10-sparc solaris10-i386
#PACKAGING_PLATFORMS += solaris11-sparc solaris11s10-spar Use custom map for Solaris 10
LINKER_MAPS-5.10 += -M "$(abspath $(WORKDIR)/map.sudo)"
LINKER_MAPS += $(LINKER_MAPS-$(GAROSREL)))/map.sudo)"
endif


PACKAGES += CSWsudo
SPKG_DESC_CSWsudo = Provides limited super user privileges
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWsudo += CSWlibintl8
RUNTIME_DEP_PKGS_C#SWsudo += CSWlibz1
OBSOLETED_BY_CSWsudo = CSWsudo-common

# These are just docs
CHECKPKG_OVERRIDES_CSWsudo += file-with-bad-conteetc/opt/csw/sudoers.CSW/dme=sudo_noexec.so

LDAP_DOCFILES += $(docdir)/sudo/README.LDAP
LDAP_DOCFILES += $(docdir)/sudo/schema.ActiveDirectory
LDAP_DOCFILES += $(docdir)/sudo/schema.OpenLDAP
LDAP_DOCFILES += $(docdir)/sudo/schema.iPlanet
LDAP_DOCFILES += $(docdir)/sudo/sudoers2ldif
LDAP_MANFILES += $(mandir)/man4/sudoers.ldap.4

PACKAGES += CSWsudo-ldap
SPKG_DESC_CSWsudo-ldap = LDAP bindings for SUDO
PKGFILES_CSWsudo-ldap +=ap += $(libexecdir)/sudoers-ldap.so
PKGFILES_CSWsudo-ldap += $(LDAP_DOCFILES)
PKGFILES_CSWsudo-ldap += $(LDAP_MANFILES)
RUNTIME_DEP_PKGS_CSWsudo-ldap += CSWlibintl8
RUNTIME_DEP_PKGS_CSWsudo-ldap += CSWliblber2-4-2
RUNTIME_DEP_PKGS_CSWsudo-ldap += CSWlibldap2-4-2
RUNTIME_DEP_PKGS_CSWsudo-ldap += CSWlibz1
# This logical dependency can not be tracked via checkpkg
RUNTIME_DEP_PKGS_CSWsu#OBSOLETED_BY_CSWsudo-ldap += CSWsudoldap
CATALOGNAME_CSWsudoldap = sudo_ldap_stub

# This is for the sparc/x86 linker anomaly
CHECKPKG_OVERRIDES_CSWsudo-ldap += surplus-dependency|CSWliblber2-4-2

# This is for /usr/share/lib/zoneinfo
CHECKPKG_OVERRIDES_CSWsudo += file-with-bad-content|/usr/share|root/opt/csw/libexec/sudo/sudoers.so
CHECKPKG_OVERRIDES_CSWsudo-ldap += file-with-bad-content|/usr/share|root/opt/csw/libexec/sudo/sudoers-ldap.sooc/sudo/README.LDAP

# This is a private library
CHECKPKG_OVERRIDES_CSWsudo-ldap += soname-not-part-of-filename|soname=sudoers.so|filenam# This is needed AFAIK due to libtool and dlopen
CHECKPKG_OVERRIDES_CSWsudo += discouraged-path-in-pkgmap|/opt/csw/libexec/sudo/libsudo_util.la

CHECKPKG_OVERRIDES_CSWsudo += $(CHECKPKG_OVERRIDES_CSWsudo-$(GAROSREL))
CHECKPKG_OVERRIDES_CSWsudo-ldap += $(CHECKPKG_OVERRIDES_CSWsudo-ldap-$(GAROSREL))mme=sudoers-ldap.so

LOGPATH    = $(localVARDIR     = $(localstatedir)/sudo
# It is important that this really gets cleaned on reboot
TIMEPATH   = /var/runlocalstatedir)/sudo
IOLOGPATH  = $(LOGPATH)/io

REINPLACE_USRLOCAL += plugins/sudoers/sudoers

EXTRA_INC += $(includedir)/sasl

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-pam
CONFIGURE_ARGS += --with-logging=both
CONFIGURE_ARGS += --with-ignore-dot
CONFIGURE_ARGS += --with-env-editor
CONFIGURE_ARGS += --enable-zlib=$(libdir)
CONFIGURE_ARGS += --disable-path-info
CONFIGURE_ARGS += --with-logpath=$(LOGPATH)/sudolog
CONFIGURE_ARGS += --with-iologdir=$(IOLOGPATH)
CONFIGrundir=$(TIMEPATH)
CONFIGURE_ARGS += --with-vardir=$(VARDIR-timedir=$(TIMEPATH)
CONFIGURE_ARGSCONFIGURE_ARGS += --with-fqdnS# Looks like even Solaris 10 is missing some defined for BSM
#CONFIGURE_ARGS-5.9 += --with-bsm-audit
#CONFIGURE_ARGS-5.10 += --with-bsm-audit
#CONFIGURE_ARGS-5.11 += --with-solaris-audit

CONFIGURE_ARGS += $(CONFIGURE_ARGS-$(GAROSREL))S += --with-project

CONFIGURE_ARGS_LDAP-enabled += --with-ldap=$(prefix)
CONFIGURE_ARGS_LDAP-enabled += --with-ldap-conf-file=$(sysconfdir)/ldap.conf

CONFIGURE_ARGS += $(CONFIGURE_A# This default to installation as user 'root' which we don't want here as we set it in the package prototype
INSTALL_OVERRIDE_VARS += INSTALL_OWNER
INSTALL_OVERRIDE_VAR_INSTALL_OWNER = _ARGS_LDAP-$(LDAP))

FIXCONFIG_DIRS = $(DESTDIR)$(libexecdir)

PROTOTYPE_MODIFIERS += sudo
PROTOTYPE_FILES_sudo = $(bindir)/sudo.*
PROTOTYPE_PERMS_sudo = 4755

PROTOTYPE_MODIFIERS += timedir
PROTOTYPE_FILES_timedir =  $(TIMEPATH)  # a normal Perl regexp. Watch out for links!
PROTOTYPE_PERMS_timedir = 0700
PROTOTYPE_USER_timedir = root
PROTOTYPE_GROUP_timedir = bin

PROTOTYPE_MODIFIERS += iodir
PROTOTYPE_FILES_iodir =  $(IOLOGPATH)  # a normal Perl regexp. Watch out for links!
PROTOTYPE_PERMS_iodir = 0700
PROTOTYPE_USER_iodir = root
PROTOTYPE_GROUP_iodir = bin

PROTOTYPE_MODIFIERS += sudoers
PROTOTYPE_FILES_sudoers =  /etc/opt/csw/sudoers.CSW
PROTOTYPE_PERMS_sudoers = 0440
PROTOTYPE_GROUP_sudoers = root

# Just copy the stuff together, the ldap modulations contains some more file,
# apart from that they are the same.
MERGE_SCRIPTS_isa-default-ldap-disabled = copy-all
MERGE_SCRIPTS_isa-default-ldap-enabled = copy-all

EXTRA_PAX_ARGS_LDAP-enabled += -s ',(/sudoers.so,$$1/sudoir))/sudoers.so,$$1/sudoers-ldap.so,'
EXTRA_PAX_ARGS += $(EXTRA_PAX_ARGS_LDAP-$(LDAP))

MIGRATE_FILES_CSWsudo += sudoers

PRESERVECONF += $(sysconfdir)/sudoers
PRESERVECONF += $(sysconfdir)/sudo.conf

include gar/categot-install-modulated:
	ginstall -d $(DESTDIR)$(IOLOGPATH)
	ginstall -d $(DESTDIR)$(TID $(WORKDIR)/sudo.conf.CSW $(DESTDIR)$(sysconfdir)/sudo.conf.CSW
	@$(MAKECOOKIE)

