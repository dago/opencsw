# dep to perl?

GARNAME = dcc
GARVERSION = 1.3.116
CATEGORIES = net

DESCRIPTION = E-mail greylisting and a cooperative, distributed system to identify spam

MASTER_SITES = http://www.rhyolite.com/dcc/source/
DISTFILES  = $(GARNAME).tar.Z

LICENSE = LICENSE

# Upstream watch
#UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.Z

#CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS  =
CONFIGURE_ARGS += --homedir=/var/opt/csw/dcc
CONFIGURE_ARGS += --bindir=/opt/csw/bin
CONFIGURE_ARGS += --libexecdir=/opt/csw/libexec/dcc
CONFIGURE_ARGS += --mandir=/opt/csw/share/man
CONFIGURE_ARGS += --with-installroot=$(DESTDIR)
CONFIGURE_ARGS += --with-DCC-MD5
#CONFIGURE_ARGS += --with-uid=dcc
CONFIGURE_ARGS += --with-uid=bonivart
#CONFIGURE_ARGS += --with-cgibin=/var/opt/csw/dcc/cgi-bin
CONFIGURE_ARGS += --with-cgibin=/opt/csw/dcc/cgi-bin
CONFIGURE_ARGS += --with-rundir=/var/opt/csw/dcc/run
CONFIGURE_ARGS += --with-sendmail=/home/bonivart/tmp/sendmail-8.14.2/include/libmilter

GARCOMPILER = GNU

# dcc has no tests
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

SAMPLECONF  = /var/opt/csw/dcc/dcc_conf
SAMPLECONF += /var/opt/csw/dcc/flod
SAMPLECONF += /var/opt/csw/dcc/grey_flod
SAMPLECONF += /var/opt/csw/dcc/grey_whitelist
SAMPLECONF += /var/opt/csw/dcc/ids
SAMPLECONF += /var/opt/csw/dcc/map.txt
SAMPLECONF += /var/opt/csw/dcc/whiteclnt
SAMPLECONF += /var/opt/csw/dcc/whitecommon
SAMPLECONF += /var/opt/csw/dcc/whitelist

SPKG_SOURCEURL = http://www.rhyolite.com/dcc/
CONFFILES =  dcc_conf flod grey_flod grey_whitelist ids map.txt whiteclnt whitecommon whitelist
DOCFILES = CHANGES FAQ.txt INSTALL.txt RESTRICTIONS misc/README misc/dcc.m4 misc/dccdnsbl.m4 misc/site.config.m4

include gar/category.mk

install-custom:
	@echo " ==> Installing $(GARNAME) (custom)"
	@rm -rf $(DESTDIR)
	@( cd $(WORKSRC) ; \
	   sed 's/DCC_GRP.*=bin/DCC_GRP     =csw/' Makefile.inc > tmp.sed ; \
	   mv tmp.sed Makefile.inc ; \
	   cd cgi-bin ; \
	   sed 's/\/opt\/csw\/dcc\/cgi-bin/\/var\/opt\/csw\/dcc\/cgi-bin/' Makefile > tmp.sed ; \
	   mv tmp.sed Makefile ; \
	   cd .. ; \
	   gmake install )
	@( cd $(DESTDIR)/var/opt/csw/$(GARNAME) ; \
	  sed 's/bonivart/dcc/' dcc_conf > tmp.sed ; \
	  mv tmp.sed dcc_conf )
#	@$(foreach FILE, $(CONFFILES), mv $(DESTDIR)/var/opt/csw/$(GARNAME)/$(FILE) $(DESTDIR)/var/opt/csw/$(GARNAME) ;)
	@ginstall -d $(DESTDIR)$(docdir)/$(GARNAME)/misc
	@$(foreach FILE, $(DOCFILES), cp $(WORKSRC)/$(FILE) $(DESTDIR)$(docdir)/$(GARNAME)/$(FILE) ;)
	@cp $(FILEDIR)/CSWdcc.INSTALL.CSW.txt $(DESTDIR)$(docdir)/$(GARNAME)/INSTALL.CSW.txt
	@cp $(FILEDIR)/CSWdcc.dcc.xml $(DESTDIR)$(docdir)/$(GARNAME)/dcc.xml
	@cp $(FILEDIR)/CSWdcc.svc-dcc $(DESTDIR)$(docdir)/$(GARNAME)/svc-dcc
	@$(MAKECOOKIE)
