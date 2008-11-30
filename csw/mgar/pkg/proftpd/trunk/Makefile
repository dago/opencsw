GARNAME = proftpd
GARVERSION = 1.3.1
CATEGORIES = server

DESCRIPTION = Advanced, incredibly configurable and secure FTP daemon
define BLURB
  ProFTPD is a proven, high-performance, scalable FTP server written from
  scratch, with a focus toward simplicity, security, and ease of configuration.
  Naturally, ProFTPD powers some of the largest sites on the Internet. It
  features a very Apache-like configuration syntax, modules, and a highly
  customizable server infrastructure, including support for multiple 'virtual'
  FTP servers, anonymous FTP, and permission-based directory visibility.
endef

MASTER_SITES = ftp://ftp.proftpd.org/distrib/source/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
DISTFILES += $(call admfiles,CSWproftpd,)

CONFIGURE_ARGS = $(DIRPATHS)

# No test suite
TEST_SCRIPTS =

INSTALL_SCRIPTS = custom

PROFTPDBIN=ftpcount ftpdctl ftpshut ftptop ftpwho
PROFTPDDOC=doc sample-configurations
PROFTPDMAN1=utils/ftpcount.1 utils/ftptop.1 utils/ftpwho.1
PROFTPDMAN5=src/xferlog.5
PROFTPDMAN8=src/ftpdctl.8 src/proftpd.8

install-custom:
	ginstall -d $(DESTDIR)$(prefix)/etc
	ginstall -d $(DESTDIR)$(prefix)/bin
	ginstall -d $(DESTDIR)$(prefix)/sbin
	ginstall -d $(DESTDIR)$(prefix)/var/proftpd
	ginstall -d $(DESTDIR)$(prefix)/share/doc/proftpd
	ginstall -d $(DESTDIR)$(prefix)/share/man/man1
	ginstall -d $(DESTDIR)$(prefix)/share/man/man5
	ginstall -d $(DESTDIR)$(prefix)/share/man/man8
	cd $(WORKSRC); \
	cp sample-configurations/basic.conf proftpd.conf.CSW; \
	cp proftpd.conf.CSW $(DESTDIR)$(prefix)/etc; \
	cp $(PROFTPDBIN) $(DESTDIR)$(prefix)/bin; \
	cp proftpd $(DESTDIR)$(prefix)/sbin; \
	chmod 755 $(DESTDIR)$(prefix)/sbin/proftpd; \
	cp -r $(PROFTPDDOC) $(DESTDIR)$(prefix)/share/doc/proftpd; \
	cp -r $(PROFTPDDOC) $(DESTDIR)$(prefix)/share/doc/proftpd; \
	cp $(PROFTPDMAN1) $(DESTDIR)$(prefix)/share/man/man1; \
	cp $(PROFTPDMAN1) $(DESTDIR)$(prefix)/share/man/man5; \
	cp $(PROFTPDMAN1) $(DESTDIR)$(prefix)/share/man/man8 
	$(MAKECOOKIE)


include gar/category.mk
