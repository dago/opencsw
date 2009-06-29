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

GARNAME = vsftpd
GARVERSION = 2.1.2
CATEGORIES = server

DESCRIPTION = A very secure and fast FTP server.
define BLURB
  vsftpd is a secure and fast FTP server for UNIX-like systems
  that is used on many large and critical Internet sites. 
  Its rich feature set includes SSL encryption, IPv6, bandwidth
  throttling, PAM integration, virtual users, virtual IPs and 
  per-user / per-IP configuration. 
endef

MASTER_SITES = ftp://vsftpd.beasts.org/users/cevans/

PACKAGES = CSWvsftpd

REQUIRED_PKGS  = CSWtcpwrap 
REQUIRED_PKGS += CSWosslrt 
REQUIRED_PKGS += CSWcswclassutils

# adding configuration handling classes
# (init/smf classes are dynamically added in checkinstall)
SPKG_CLASSES = none cswpreserveconf cswusergroup cswinitsmf


###### Upstream and opencsw files information #######

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += CSWvsftpd.prototype CSWvsftpd.preinstall
DISTFILES += changelog.CSW README.CSW
DISTFILES += vsftpd.conf vsftpd.userlist
DISTFILES += cswvsftpd cswvsftpd.xml vsftpd.smf_wrapper
DISTFILES += cswusergroup 

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

# solaris doesn't have RLIMIT_NPROC
PATCHFILES += no_rlimit_nproc.patch

# Documentation files
DOCFILES  = AUDIT BENCHMARKS BUGS COPYING COPYRIGHT Changelog FAQ INSTALL LICENSE REFS
DOCFILES += REWARD SIZE SPEED TODO TUNING README README.ssl README.security
DOCFILES += SECURITY/DESIGN SECURITY/IMPLEMENTATION SECURITY/OVERVIEW SECURITY/TRUST
DOCFILES += EXAMPLE/VIRTUAL_USERS_2/README EXAMPLE/PER_IP_CONFIG/README EXAMPLE/PER_IP_CONFIG/hosts.allow
DOCFILES += EXAMPLE/VIRTUAL_HOSTS/README EXAMPLE/VIRTUAL_USERS/logins.txt EXAMPLE/VIRTUAL_USERS/vsftpd.pam
DOCFILES += EXAMPLE/VIRTUAL_USERS/vsftpd.conf EXAMPLE/INTERNET_SITE/vsftpd.xinetd 
DOCFILES += EXAMPLE/INTERNET_SITE/README EXAMPLE/INTERNET_SITE/vsftpd.conf
DOCFILES += EXAMPLE/INTERNET_SITE_NOINETD/README EXAMPLE/INTERNET_SITE_NOINETD/vsftpd.conf


##### Build and installation information #####

GARCOMPILER = SUN

CONFIGURE_ARGS = $(DIRPATHS)

CONFIGURE_SCRIPTS =
TEST_SCRIPTS =

include gar/category.mk

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
	 ln -sf $(DESTDIR)$(mandir) $(DESTDIR)$(prefix)/man; \
	 ginstall -d $(DESTDIR)$(docdir)/vsftpd )


post-merge: merge-doc-files merge-config-files merge-init-file

merge-init-file:
	ginstall -D "$(WORKDIR_FIRSTMOD)/cswvsftpd" "$(PKGROOT)/etc/init.d/cswvsftpd"
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
