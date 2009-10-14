GARNAME = miltergreylist
GARVERSION = 4.2.3
#RELEASE = rc1
#DISTVERSION = $(GARVERSION)$(RELEASE)
DISTVERSION = $(GARVERSION)
DISTNAME = milter-greylist-$(DISTVERSION)
WORKSRC = $(WORKDIR)/$(DISTNAME)
CATEGORIES = net

DESCRIPTION = Greylist mail filtering method
define BLURB
   Greylist mail filtering method
endef

MASTER_SITES = http://ftp.espci.fr/pub/milter-greylist/
DISTFILES  = milter-greylist-$(DISTVERSION).tgz
DISTFILES += COPYING

REQUIRED_PKGS = CSWsendmail CSWcurlrt CSWgeoip

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tgz

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS  = --prefix=/opt/csw
CONFIGURE_ARGS += --sysconfdir=/etc/opt/csw
#CONFIGURE_ARGS += --with-user=greylist
CONFIGURE_ARGS += --with-user=`/usr/xpg4/bin/id -u`
CONFIGURE_ARGS += --with-conffile=/etc/opt/csw/greylist.conf
CONFIGURE_ARGS += --enable-dnsrbl
CONFIGURE_ARGS += --enable-stdio-hack
CONFIGURE_ARGS += --localstatedir=/var/opt/csw/milter-greylist
CONFIGURE_ARGS += --with-libGeoIP=/opt/csw/lib
CONFIGURE_ARGS += --with-libcurl=/opt/csw/lib
CONFIGURE_ARGS += --mandir=/opt/csw/share/man

#SPKG_CLASSES = none cswusergroup cswcpsampleconf cswinitsmf

TEST_SCRIPTS = 
INSTALL_SCRIPTS = custom
USERGROUP = /opt/csw/etc/pkg/miltergreylist/cswusergroup
SAMPLECONF = /etc/opt/csw/greylist.conf.CSW
INITSMF = /etc/opt/csw/init.d/cswmiltergreylist

PROTOTYPE_FILTER  = awk ' \
  $$$$3 ~ /\/var\/opt\/csw\/miltergreylist/ { $$$$4 = "0700" ; $$$$5 = "greylist" } \
  { print }'

include gar/category.mk

#WORKSRC := $(WORKDIR)/$(GARNAME)-$(GARVERSION)b1
SPKG_SOURCEURL = http://hcpnet.free.fr/milter-greylist
#SPKG_REVSTAMP := $(SPKG_REVSTAMP)_rev=$(RELEASE)

DOCLIST = README ChangeLog greylist.conf greylist2.conf milter-greylist.m4

install-custom:
	@echo " ==> Installing $(GARNAME) (custom)"
	@( cd $(WORKSRC) ; \
	   gmake DESTDIR=$(DESTDIR) install )
	@ginstall -d -m 755 $(DESTDIR)/etc/opt/csw
	@mv $(DESTDIR)/etc/mail/greylist.conf $(DESTDIR)/etc/opt/csw/greylist.conf.CSW
	@rmdir $(DESTDIR)/etc/mail
	@ginstall -d -m 755 $(DESTDIR)$(docdir)/$(GARNAME)
	@$(foreach DOC,$(DOCLIST),cp $(WORKSRC)/$(DOC) $(DESTDIR)$(docdir)/$(GARNAME);)
	@ginstall -d -m 755 $(DESTDIR)/var/opt/csw/$(GARNAME)
	@rmdir $(DESTDIR)/var/milter-greylist
	@ginstall -d -m 755 $(DESTDIR)/opt/csw/etc/pkg/$(GARNAME)
	@cp $(FILEDIR)/CSWmiltergreylist.ug $(DESTDIR)/opt/csw/etc/pkg/$(GARNAME)/cswusergroup
	@ginstall -d -m 755 $(DESTDIR)/etc/opt/csw/init.d
	@cp $(FILEDIR)/CSWmiltergreylist.init $(DESTDIR)/etc/opt/csw/init.d/cswmiltergreylist
	@cp $(FILEDIR)/README.CSW $(DESTDIR)$(docdir)$(GARNAME)
	@$(MAKECOOKIE)
