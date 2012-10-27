#####################################################################
# OpenCSW build recipe for vsftpd
#
# Copyright 2009 Yann Rouillard <yann@pleiades.fr.eu.org>
# All rights reserved.  Use is subject to license terms.
#
# Redistribution and/or use, with or without modification, is
# permitted.  This software is without warranty of any kind.  The
# author(s) shall not be liable in the event that use of the
# software causes damage.
#####################################################################

###### Package information #######

NAME = vsftpd
VERSION = 3.0.2
CATEGORIES = server
GARTYPE = v2

DESCRIPTION = A very secure and fast FTP server.
define BLURB
  vsftpd is a secure and fast FTP server for UNIX-like systems
  that is used on many large and critical Internet sites. 
  Its rich feature set includes SSL encryption, IPv6, bandwidth
  throttling, PAM integration, virtual users, virtual IPs and 
  per-user / per-IP configuration. 
endef

MASTER_SITES = https://security.appspot.com/downloads/
UPSTREAM_MASTER_SITES = https://security.appspot.com/vsftpd.html

PACKAGES = CSWvsftpd

RUNTIME_DEP_PKGS  = CSWlibwrap1
RUNTIME_DEP_PKGS += CSWlibssl1-0-0

# Reference to DTD path, can be safely ignored
CHECKPKG_OVERRIDES_CSWvsftpd += file-with-bad-content|/usr/share|root/var/opt/csw/svc/manifest/network/cswvsftpd.xml

# Various reference to default vsftpd path in documentation files, can be safely ignored
CHECKPKG_OVERRIDES_CSWvsftpd += file-with-bad-content|/usr/local|root/opt/csw/share/doc/vsftpd/EXAMPLE/INTERNET_SITE/vsftpd.xinetd
CHECKPKG_OVERRIDES_CSWvsftpd += file-with-bad-content|/usr/local|root/opt/csw/share/doc/vsftpd/EXAMPLE/INTERNET_SITE/README
CHECKPKG_OVERRIDES_CSWvsftpd += file-with-bad-content|/usr/local|root/opt/csw/share/doc/vsftpd/INSTALL
CHECKPKG_OVERRIDES_CSWvsftpd += file-with-bad-content|/usr/local|root/opt/csw/share/doc/vsftpd/Changelog
CHECKPKG_OVERRIDES_CSWvsftpd += file-with-bad-content|/usr/share|root/opt/csw/share/doc/vsftpd/INSTALL
CHECKPKG_OVERRIDES_CSWvsftpd += file-with-bad-content|/usr/share|root/opt/csw/share/doc/vsftpd/README.ssl


###### Upstream and opencsw files information #######

DISTFILES  = $(NAME)-$(VERSION).tar.gz
DISTFILES += CSWvsftpd.preinstall
DISTFILES += changelog.CSW README.CSW
DISTFILES += vsftpd.conf vsftpd.userlist
DISTFILES += cswvsftpd cswvsftpd.xml vsftpd.smf_wrapper
DISTFILES += cswusergroup 

PRESERVECONF = $(sysconfdir)/vsftpd/vsftpd.conf $(sysconfdir)/vsftpd/vsftpd.userlist
USERGROUP = /etc/opt/csw/pkg/CSWvsftpd/cswusergroup
INITSMF = /etc/opt/csw/init.d/cswvsftpd

MIGRATE_FILES = vsftpd.conf vsftpd.chroot_list vsftpd.banned_emails vsftpd.email_passwords vsftpd.user_list
MIGRATE_SOURCE_DIR = $(prefix)/etc/vsftpd
MIGRATE_DEST_DIR = $(sysconfdir)/vsftpd

# The vsftpd user home directory has special rights
PROTOTYPE_MODIFIERS = empty
PROTOTYPE_FILES_empty = \/opt\/csw\/var\/empty\/vsftpd
PROTOTYPE_PERMS_empty = 0700
PROTOTYPE_USER_empty = root
PROTOTYPE_GROUP_empty = sys

# build options are set by modifying 
# builddefs.h, so we patch it to enable
# ssl and tcp wrapper support
PATCHFILES = build_options.patch

# patch to have vsftpd use standard
# csw paths
PATCHFILES += csw_paths.patch

# patch to integrate vsftpd Makefile
# with csw build system
PATCHFILES += csw_build_system.patch

# Use vsftpd instead of nobody as the
# privilege separation user
PATCHFILES += set_priv_sep_user.patch

# patch to add DESTDIR support to 
# vsftpd makfile
PATCHFILES += destdir.patch

# patch to avoid an incompatible pointer type
# error when compiling under Solaris with -Werror
PATCHFILES += avoid_pam_conv_warning.patch

# vsftpd need to be linked against resolv.so
# only in Solaris 5.9 but not for Solaris >= 5.10
PATCHFILES += removed-resolv.so-dependency.patch

# Documentation files
DOCFILES  = AUDIT BENCHMARKS BUGS COPYING COPYRIGHT Changelog FAQ INSTALL LICENSE REFS
DOCFILES += REWARD SIZE SPEED TODO TUNING README README.ssl README.security
DOCFILES += SECURITY/DESIGN SECURITY/IMPLEMENTATION SECURITY/OVERVIEW SECURITY/TRUST
DOCFILES += EXAMPLE/VIRTUAL_USERS_2/README EXAMPLE/PER_IP_CONFIG/README EXAMPLE/PER_IP_CONFIG/hosts.allow
DOCFILES += EXAMPLE/VIRTUAL_HOSTS/README EXAMPLE/VIRTUAL_USERS/logins.txt EXAMPLE/VIRTUAL_USERS/vsftpd.pam
DOCFILES += EXAMPLE/VIRTUAL_USERS/vsftpd.conf EXAMPLE/INTERNET_SITE/vsftpd.xinetd 
DOCFILES += EXAMPLE/INTERNET_SITE/README EXAMPLE/INTERNET_SITE/vsftpd.conf
DOCFILES += EXAMPLE/INTERNET_SITE_NOINETD/README EXAMPLE/INTERNET_SITE_NOINETD/vsftpd.conf

PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386


##### Build and installation information #####

GARCOMPILER = SUN

CONFIGURE_ARGS = $(DIRPATHS)

CONFIGURE_SCRIPTS =
TEST_SCRIPTS =

include gar/category.mk

# to support shared /opt/csw setup
# see http://wiki.opencsw.org/shared-opt-csw-setup
localstatedir   = /var$(prefix)
sysconfdir      = /etc$(prefix)

# /opt/csw/include is not take in account 
# by vsftp build system
CFLAGS += -I$(includedir)

# dummyinc must be the last include directory
# to search
ifeq ($(GARCOMPILER),GNU)
CFLAGS += -idirafter dummyinc
else
CFLAGS += -I/usr/include -Idummyinc 
endif

INSTALL_ENV += INSTALL="ginstall"


# we create the csw directory hierarchy 
pre-install-modulated:
	@echo "Creating csw directories"
	( ginstall -d $(DESTDIR)$(sbindir); \
	 ginstall -d $(DESTDIR)$(mandir)/man5; \
	 ginstall -d $(DESTDIR)$(mandir)/man8; \
	 ginstall -d $(DESTDIR)$(docdir)/vsftpd )


post-merge: merge-doc-files merge-config-files merge-init-file merge-special-directories

merge-init-file:
	ginstall -D "$(WORKDIR_FIRSTMOD)/cswvsftpd" "$(PKGROOT)/etc/opt/csw/init.d/cswvsftpd"
	ginstall -D "$(WORKDIR_FIRSTMOD)/cswvsftpd.xml" "$(PKGROOT)/var/opt/csw/svc/manifest/network/cswvsftpd.xml"
	ginstall -D "$(WORKDIR_FIRSTMOD)/vsftpd.smf_wrapper" "$(PKGROOT)/$(sbindir)/vsftpd.smf_wrapper"

merge-config-files:
	ginstall -D "$(WORKDIR_FIRSTMOD)/vsftpd.conf" "$(PKGROOT)$(sysconfdir)/vsftpd/vsftpd.conf.CSW"
	ginstall -D "$(WORKDIR_FIRSTMOD)/vsftpd.userlist" "$(PKGROOT)$(sysconfdir)/vsftpd/vsftpd.userlist.CSW"
	ginstall -D "$(WORKDIR_FIRSTMOD)/cswusergroup" "$(PKGROOT)$(sysconfdir)/pkg/CSWvsftpd/cswusergroup"

merge-doc-files:
	for FILE in $(DOCFILES); do \
		ginstall -D "$(WORKSRC_FIRSTMOD)/$$FILE" "$(PKGROOT)$(docdir)/vsftpd/$$FILE"; \
	done
	ginstall -D "$(WORKDIR_FIRSTMOD)/changelog.CSW" "$(PKGROOT)$(docdir)/vsftpd/changelog.CSW"
	ginstall -D "$(WORKDIR_FIRSTMOD)/README.CSW" "$(PKGROOT)$(docdir)/vsftpd/README.CSW"

merge-special-directories:
	ginstall -d "$(PKGROOT)/var/opt/csw/empty/vsftpd"
	ginstall -d "$(PKGROOT)/var/opt/csw/ftp"
	
