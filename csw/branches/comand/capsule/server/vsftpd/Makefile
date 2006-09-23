GARNAME = vsftpd
GARVERSION = 2.0.5
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
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWvsftpd,prototype preinstall)
DISTFILES += changelog.CSW README.CSW
DISTFILES += vsftpd.conf vsftpd.userlist
DISTFILES += cswvsftpd vsftpd.xml svc-vsftpd 
DISTFILES += i.init r.init i.smf r.smf i.conf r.conf
DISTFILES += csw_smf csw_smf_postinstall csw_smf_preremove csw_smf_checkinstall

#CONF_FILES = /opt/csw/etc/vsftpd/vsftpd.conf
#INIT_FILES = /etc/init.d/cswvsftpd
#MANIFEST_FILES = /opt/csw/var/svc/manifest/network/vsftpd.xml

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

# patch to workaround the fact that 
# solaris libc doesn t have tm_gmtoff
# update: not useful anymore since 2.0.5
# PATCHFILES += tm_gmtoff.patch

# patch to add DESTDIR support to 
# vsftpd makfile
PATCHFILES += destdir.patch

# 
#
CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_SCRIPTS = fake

GARCOMPILER = SUN

TEST_SCRIPTS =

include ../category.mk

PKG_EXPORTS += INIT_FILES MANIFEST_FILES 

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
	@( install -d $(DESTDIR)$(sbindir); \
	 install -d $(DESTDIR)$(mandir)/man5; \
	 install -d $(DESTDIR)$(mandir)/man8; \
	 ln -sf $(DESTDIR)$(mandir) $(DESTDIR)$(prefix)/man; \
	 install -d $(DESTDIR)$(docdir)/vsftpd )

# we install additionnal files
post-install:
	ginstall -D $(WORKDIR)/cswvsftpd $(DESTDIR)/etc/init.d/cswvsftpd
	ginstall -D $(WORKDIR)/README.CSW $(DESTDIR)$(docdir)/$(GARNAME)/README.CSW
	ginstall -D $(WORKDIR)/changelog.CSW $(DESTDIR)$(docdir)/$(GARNAME)/changelog.CSW
	ginstall -D $(WORKDIR)/i.smf $(DESTDIR)/i.smf
	ginstall -D $(WORKDIR)/r.smf $(DESTDIR)/r.smf
	ginstall -D $(WORKDIR)/i.init $(DESTDIR)/i.init
	ginstall -D $(WORKDIR)/r.init $(DESTDIR)/r.init
	ginstall -D $(WORKDIR)/i.conf $(DESTDIR)/i.conf
	ginstall -D $(WORKDIR)/r.conf $(DESTDIR)/r.conf
	ginstall -D $(WORKDIR)/vsftpd.conf $(DESTDIR)$(sysconfdir)/$(GARNAME)/vsftpd.conf.CSW
	ginstall -D $(WORKDIR)/vsftpd.userlist $(DESTDIR)$(sysconfdir)/$(GARNAME)/vsftpd.userlist
	ginstall -D $(WORKDIR)/vsftpd.xml $(DESTDIR)$(localstatedir)/svc/manifest/network/vsftpd.xml
	ginstall -D $(WORKDIR)/svc-vsftpd $(DESTDIR)$(libdir)/svc/method/svc-vsftpd
	

