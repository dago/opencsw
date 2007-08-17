GARNAME = openssh
GARVERSION = 4.6
RELEASE = p1
GSSKEX_VERSION = 20070312
CATEGORIES = server

DESCRIPTION = OpenSSH Secure Shell
define BLURB
  OpenSSH is a FREE version of the SSH connectivity tools that technical users 
  of the Internet rely on. Users of telnet, rlogin, and ftp may not realize that 
  their password is transmitted across the Internet unencrypted, but it is. 
  OpenSSH encrypts all traffic (including passwords) to effectively eliminate 
  eavesdropping, connection hijacking, and other attacks. Additionally, OpenSSH 
  provides secure tunneling capabilities and several authentication methods, 
  and supports all SSH protocol versions.
endef

MASTER_SITES = ftp://ftp.openbsd.org/pub/OpenBSD/OpenSSH/portable/ http://www.sxw.org.uk/computing/patches/

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*p\d+).tar.gz

DISTVERSION = $(GARVERSION)$(RELEASE)
DISTNAME = $(GARNAME)-$(DISTVERSION)

DISTFILES  = $(GARNAME)-$(DISTVERSION).tar.gz
DISTFILES += $(call admfiles,CSWossh,depend checkinstall preinstall prototype) 
DISTFILES += changelog.CSW
DISTFILES += sshd_config
DISTFILES += cswopenssh.init svc-cswopenssh cswopenssh.xml
DISTFILES += i.conf r.conf
DISTFILES += openssh

PATCHDIRLEVEL = 0
# The GSSAPI key exchange patch
PATCHFILES = openssh-$(GARVERSION)$(RELEASE)-gsskex-$(GSSKEX_VERSION).patch
# Fix mantis bug 2564 without waiting for 4.7 
# stolen from https://bugzilla.mindrot.org/show_bug.cgi?id=1306
PATCHFILES += spurious_log_fix.patch

SPKG_CLASSES = none conf

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-kerberos5=$(prefix)
CONFIGURE_ARGS += --sysconfdir=$(sysconfdir)/ssh
CONFIGURE_ARGS += --with-solaris-contracts
CONFIGURE_ARGS += --with-pam

include ../category.mk


# we re-run autoconf because of the GSSAPI key exchange patch
pre-configure:
	cd $(WORKSRC) && autoconf
	@$(MAKECOOKIE)

SPKG_REVSTAMP := $(SPKG_REVSTAMP)_rev=$(RELEASE)
