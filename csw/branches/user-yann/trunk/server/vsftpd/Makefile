GARNAME = vsftpd
GARVERSION = 2.0.4
CATEGORIES = server

DESCRIPTION = A very secure and fast GPL'd FTP server.
define BLURB
  vsftpd is a secure and fast FTP server for UNIX-like systems
  that is used on many large and critical Internet sites. 
  Its rich feature set includes SSL encryption, IPv6, bandwidth
  throttling, PAM integration, virtual users, virtual IPs and 
  per-user / per-IP configuration. 
endef

MASTER_SITES = ftp://vsftpd.beasts.org/users/cevans/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWvsftpd,prototype checkinstall preinstall postinstall preremove)
DISTFILES += changelog.CSW README.CSW
DISTFILES += vsftpd.conf.CSW vsftpd.userlist.CSW
DISTFILES += cswvsftpd vsftpd.xml svc-vsftpd i.smfyes i.smfno

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
# solaris libc doesn't have tm_gmtoff
PATCHFILES += tm_gmtoff.patch

# patch to add DESTDIR support to 
# vsftpd makfile
PATCHFILES += destdir.patch


CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_SCRIPTS = fake

ENABLE_TEST = 0

include ../category.mk

CFLAGS += -I/usr/include -Idummyinc
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
	ginstall -d $(DESTDIR)/etc/rc2.d
	ginstall -d $(DESTDIR)/etc/rc1.d
	ginstall -d $(DESTDIR)/etc/rc0.d
	( cd $(DESTDIR)/etc/rc2.d; rm -f S85cswvsftpd; ln -sf ../init.d/cswvsftpd S85cswvsftpd; \
	cd $(DESTDIR)/etc/rc1.d; rm -f K15cswvsftpd; ln -sf ../init.d/cswvsftpd K15cswvsftpd; \
	cd $(DESTDIR)/etc/rc0.d; rm -f K15cswvsftpd; ln -sf ../init.d/cswvsftpd K15cswvsftpd )
	ginstall -D $(WORKDIR)/README.CSW $(DESTDIR)$(docdir)/$(GARNAME)/README.CSW
	ginstall -D $(WORKDIR)/changelog.CSW $(DESTDIR)$(docdir)/$(GARNAME)/changelog.CSW
	ginstall -D $(WORKDIR)/i.smfyes $(DESTDIR)/i.smfyes
	ginstall -D $(WORKDIR)/i.smfno $(DESTDIR)/i/smfno
	ginstall -D $(WORKDIR)/vsftpd.conf.CSW $(DESTDIR)$(sysconfdir)/$(GARNAME)/vsftpd.conf.CSW
	ginstall -D $(WORKDIR)/vsftpd.userlist.CSW $(DESTDIR)$(sysconfdir)/$(GARNAME)/vsftpd.userlist.CSW
	ginstall -D $(WORKDIR)/vsftpd.xml $(DESTDIR)$(localstatedir)/svc/manifest/network/vsftpd.xml
	ginstall -D $(WORKDIR)/svc-vsftpd $(DESTDIR)$(libdir)/svc/method/svc-vsftpd
	

