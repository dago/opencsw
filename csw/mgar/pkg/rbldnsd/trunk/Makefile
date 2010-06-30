GARNAME = rbldnsd
GARVERSION = 0.996b
CATEGORIES = net

DESCRIPTION = Small and fast DNS daemon which is especially made to serve DNSBL zones
define BLURB
  Small and fast DNS daemon which is especially made to serve DNSBL zones
endef

MASTER_SITES = http://www.corpit.ru/mjt/rbldnsd/
DISTFILES  = $(GARNAME)_$(GARVERSION).tar.gz
DISTFILES += COPYING
DISTFILES += rbldnsd
DISTFILES += test

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

RUNTIME_DEP_PKGS_CSWrbldnsd += CSWzlib

INSTALL_SCRIPTS = custom

SKIPTEST = 1

INITSMF = /etc/opt/csw/init.d/cswrbldnsd
SAMPLECONF = /etc/opt/csw/rbldnsd
USERGROUP = /etc/opt/csw/pkg/CSWrbldnsd/cswusergroup

include gar/category.mk

DOCLIST = CHANGES-0.81 NEWS README.user TODO

install-custom:
	@echo " ==> Installing $(GARNAME) (custom)"
	@ginstall -m 755 -d $(DESTDIR)/opt/csw/sbin
	@ginstall -m 755 $(WORKSRC)/$(GARNAME) $(DESTDIR)/opt/csw/sbin
	@ginstall -m 755 -d $(DESTDIR)$(docdir)/$(GARNAME)
	@$(foreach DOC,$(DOCLIST),cp $(WORKSRC)/$(DOC) $(DESTDIR)$(docdir)/$(GARNAME);)
	@ginstall -m 755 -d $(DESTDIR)$(mandir)/man8
	@ginstall -m 755 $(WORKSRC)/$(GARNAME).8 $(DESTDIR)$(mandir)/man8
	@ginstall -m 755 -d $(DESTDIR)/etc/opt/csw/init.d
	@ginstall -m 755 $(FILEDIR)/cswrbldnsd $(DESTDIR)/etc/opt/csw/init.d
	@ginstall -m 755 -d $(DESTDIR)/etc/opt/csw/pkg/CSW$(GARNAME)
	@ginstall -m 644 $(FILEDIR)/rbldnsd $(DESTDIR)/etc/opt/csw
	@ginstall -m 444 $(FILEDIR)/cswusergroup $(DESTDIR)/etc/opt/csw/pkg/CSW$(GARNAME)
	@ginstall -m 755 -d $(DESTDIR)/var/opt/csw/$(GARNAME)
	@ginstall -m 644 $(FILEDIR)/test $(DESTDIR)/var/opt/csw/$(GARNAME)
	@$(MAKECOOKIE)
