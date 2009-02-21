GARNAME = vsftpd
GARVERSION = 2.1.0
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

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWvsftpd,prototype preinstall depend csw_usrgrp_config)
DISTFILES += changelog.CSW README.CSW
DISTFILES += vsftpd.conf vsftpd.userlist
DISTFILES += cswvsftpd cswvsftpd.xml svc-cswvsftpd 
DISTFILES += i.conf r.conf

# adding configuration handling classes
# (init/smf classes are dynamically added in checkinstall)
SPKG_CLASSES = none conf

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

# patch to workaround the fact that 
# solaris libc doesn t have tm_gmtoff
# update: not useful anymore since 2.0.5
# PATCHFILES += tm_gmtoff.patch

# patch to add DESTDIR support to 
# vsftpd makfile
PATCHFILES += destdir.patch

# Documents
DOCFILES  = AUDIT BENCHMARKS BUGS COPYING COPYRIGHT Changelog FAQ INSTALL LICENSE REFS
DOCFILES += REWARD SIZE SPEED TODO TUNING README README.ssl README.security
DOCFILES += SECURITY/DESIGN SECURITY/IMPLEMENTATION SECURITY/OVERVIEW SECURITY/TRUST
DOCFILES += EXAMPLE/VIRTUAL_USERS_2/README EXAMPLE/PER_IP_CONFIG/README EXAMPLE/PER_IP_CONFIG/hosts.allow
DOCFILES += EXAMPLE/VIRTUAL_HOSTS/README EXAMPLE/VIRTUAL_USERS/logins.txt EXAMPLE/VIRTUAL_USERS/vsftpd.pam
DOCFILES += EXAMPLE/VIRTUAL_USERS/vsftpd.conf EXAMPLE/INTERNET_SITE/vsftpd.xinetd 
DOCFILES += EXAMPLE/INTERNET_SITE/README EXAMPLE/INTERNET_SITE/vsftpd.conf
DOCFILES += EXAMPLE/INTERNET_SITE_NOINETD/README EXAMPLE/INTERNET_SITE_NOINETD/vsftpd.conf


CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_SCRIPTS = fake

GARCOMPILER = SUN

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

# no configure step with vsftpd
configure-fake:
	$(MAKECOOKIE)

# we create the csw directory hierarchy 
pre-install:
	@echo "Creating csw directories"
	( install -d $(DESTDIR)$(sbindir); \
	 install -d $(DESTDIR)$(mandir)/man5; \
	 install -d $(DESTDIR)$(mandir)/man8; \
	 ln -sf $(DESTDIR)$(mandir) $(DESTDIR)$(prefix)/man; \
	 install -d $(DESTDIR)$(docdir)/vsftpd )



post-install:
	cd $(WORKSRC) && \
	for FILE in $(DOCFILES); do \
		ginstall -D $$FILE $(DESTDIR)$(docdir)/vsftpd/$$FILE; \
	done

