NAME = dcc
VERSION = 1.3.140
CATEGORIES = net
GARTYPE = v2

DESCRIPTION = E-mail greylisting and a cooperative, distributed system to identify spam

#MASTER_SITES = http://www.rhyolite.com/src/dcc/old/
MASTER_SITES = http://www.dcc-servers.net/dcc/source/old/
DISTFILES  = $(NAME)-$(VERSION).tar.Z

LICENSE = LICENSE

RUNTIME_DEP_PKGS += CSWperl

CHECKPKG_OVERRIDES_CSWdcc += file-with-bad-content

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
# This obviously needs a better solution
CONFIGURE_ARGS += --with-sendmail=/home/bonivart/tmp/sendmail-8.14.5/include/libmilter

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
USERGROUP   = /etc/opt/csw/pkg/CSWdcc/cswusergroup

# Fix ownership of map file
PROTOTYPE_MODIFIERS = 1
PROTOTYPE_FILES_1   = /var/opt/csw/dcc/map
PROTOTYPE_USER_1    = dcc
PROTOTYPE_CLASS_1   = ugfiles

SPKG_SOURCEURL = http://www.rhyolite.com/dcc/
CONFFILES = dcc_conf flod grey_flod grey_whitelist ids map.txt whiteclnt whitecommon whitelist
DOCFILES = CHANGES FAQ.html INSTALL.html RESTRICTIONS misc/README misc/dcc.m4 misc/dccdnsbl.m4 misc/site.config.m4

include gar/category.mk

install-custom:
	@echo " ==> Installing $(NAME) (custom)"
	@rm -rf $(DESTDIR)
	@( cd $(WORKSRC) ; \
	   sed 's/DCC_GRP.*=bin/DCC_GRP     =csw/' Makefile.inc > tmp.sed ; \
	   mv tmp.sed Makefile.inc ; \
	   cd cgi-bin ; \
	   sed 's/\/opt\/csw\/dcc\/cgi-bin/\/var\/opt\/csw\/dcc\/cgi-bin/' Makefile > tmp.sed ; \
	   mv tmp.sed Makefile ; \
	   cd .. ; \
	   gmake install )
	@( cd $(DESTDIR)/var/opt/csw/$(NAME) ; \
	   sed 's/bonivart/dcc/' dcc_conf > tmp.sed ; \
	   mv tmp.sed dcc_conf )
	@( cd $(DESTDIR)/opt/csw/libexec/$(NAME) ; \
	   sed 's/bonivart/dcc/' fix-map > tmp.sed ; \
	   mv tmp.sed fix-map )
#	@$(foreach FILE, $(CONFFILES), mv $(DESTDIR)/var/opt/csw/$(NAME)/$(FILE) $(DESTDIR)/var/opt/csw/$(NAME) ;)
	@ginstall -d $(DESTDIR)$(docdir)/$(NAME)/misc
	@$(foreach FILE, $(DOCFILES), cp $(WORKSRC)/$(FILE) $(DESTDIR)$(docdir)/$(NAME)/$(FILE) ;)
	@cp $(FILEDIR)/CSWdcc.INSTALL.CSW.txt $(DESTDIR)$(docdir)/$(NAME)/INSTALL.CSW.txt
	@cp $(FILEDIR)/CSWdcc.dcc.xml $(DESTDIR)$(docdir)/$(NAME)/dcc.xml
	@cp $(FILEDIR)/CSWdcc.svc-dcc $(DESTDIR)$(docdir)/$(NAME)/svc-dcc
	@ginstall -m 755 -d $(DESTDIR)/etc/opt/csw/pkg/CSWdcc
	@ginstall -m 444 $(FILEDIR)/cswusergroup $(DESTDIR)/etc/opt/csw/pkg/CSWdcc
	@$(MAKECOOKIE)
