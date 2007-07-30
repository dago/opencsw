GARNAME = openssh
GARVERSION = 4.6
RELEASE = p1
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

MASTER_SITES = ftp://ftp.openbsd.org/pub/OpenBSD/OpenSSH/portable/

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*p\d+).tar.gz

DISTVERSION = $(GARVERSION)$(RELEASE)
DISTNAME = $(GARNAME)-$(DISTVERSION)

DISTFILES  = $(GARNAME)-$(DISTVERSION).tar.gz
DISTFILES += $(call admfiles,CSWossh,depend checkinstall preinstall prototype) 
DISTFILES += sshd_config
DISTFILES += cswopenssh.init svc-cswopenssh cswopenssh.xml
DISTFILES += i.conf r.conf
DISTFILES += openssh


SPKG_CLASSES = none conf

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-kerberos5=$(prefix)
CONFIGURE_ARGS += --sysconfdir=$(sysconfdir)/ssh
CONFIGURE_ARGS += --with-solaris-contracts
CONFIGURE_ARGS += --with-pam

include ../category.mk

SPKG_REVSTAMP := $(SPKG_REVSTAMP)_rev=$(RELEASE)
