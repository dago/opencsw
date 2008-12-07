# add re for update notification
# split into multiple packages: clamav, libclamav
# put libs in lib/32?
# add depend files
# add rc/smf support
# add pre/post scripts
# add etc/clamav-milter
# add etc/clamd?
# add doc/README.CSW, INSTALL.clamav-milter.CSW
# check mantis bugs
# + add contrib
# + add html docs and some pdf:s
# + remove *.a, *.la from libs

GARNAME = clamav
GARVERSION = 0.94.2
CATEGORIES = apps

DESCRIPTION = Clam AntiVirus
define BLURB
  Clam AntiVirus is an open source (GPL) anti-virus toolkit for UNIX, designed 
  especially for e-mail scanning on mail gateways. It provides a number of 
  utilities including a flexible and scalable multi-threaded daemon, a command 
  line scanner and advanced tool for automatic database updates. The core of 
  the package is an anti-virus engine available in a form of shared library.
endef

MASTER_SITES = http://freshmeat.net/redir/clamav/29355/url_tgz/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWclamav,)
#DISTFILES += $(call admfiles,CSWlibclamav,)

GARCOMPILER = GNU
GNU_CC_HOME = /opt/csw/gcc3

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-user=nobody
CONFIGURE_ARGS += --with-group=nobody
CONFIGURE_ARGS += --enable-milter
CONFIGURE_ARGS += --with-sendmail=/opt/csw/lib/sendmail
CONFIGURE_ARGS += --with-dbdir=/var/opt/csw/$(GARNAME)/db
CONFIGURE_ARGS += --localstatedir=/var/opt/csw/$(GARNAME)

include gar/category.mk

SPKG_SOURCEURL = http://www.clamav.net/

pre-package:
	@echo " ==> Pre-package for $(GARNAME)"
	@find $(DESTDIR) -type f -name "*~" -exec rm {} \;
	@find $(DESTDIR)/opt/csw/lib -type f -name "*.a" -exec rm {} \;
	@find $(DESTDIR)/opt/csw/lib -type f -name "*.la" -exec rm {} \;
	@ginstall -d $(DESTDIR)$(docdir)/$(GARNAME)/html
	@ginstall -d $(DESTDIR)$(docdir)/$(GARNAME)/contrib
	@ginstall -m 644 $(WORKSRC)/AUTHORS $(DESTDIR)$(docdir)/$(GARNAME)
	@ginstall -m 644 $(WORKSRC)/BUGS $(DESTDIR)$(docdir)/$(GARNAME)
	@ginstall -m 644 $(WORKSRC)/ChangeLog $(DESTDIR)$(docdir)/$(GARNAME)
	@ginstall -m 644 $(WORKSRC)/docs/clamav-mirror-howto.pdf $(DESTDIR)$(docdir)/$(GARNAME)
	@ginstall -m 644 $(WORKSRC)/docs/clamdoc.pdf $(DESTDIR)$(docdir)/$(GARNAME)
	@ginstall -m 644 $(WORKSRC)/COPYING $(DESTDIR)$(docdir)/$(GARNAME)/LICENSE
	@ginstall -m 644 $(WORKSRC)/FAQ $(DESTDIR)$(docdir)/$(GARNAME)
	@ginstall -m 644 $(WORKSRC)/NEWS $(DESTDIR)$(docdir)/$(GARNAME)
	@ginstall -m 644 $(WORKSRC)/docs/phishsigs_howto.pdf $(DESTDIR)$(docdir)/$(GARNAME)
	@ginstall -m 644 $(WORKSRC)/README $(DESTDIR)$(docdir)/$(GARNAME)
	@ginstall -m 644 $(WORKSRC)/docs/signatures.pdf $(DESTDIR)$(docdir)/$(GARNAME)
	@ginstall -m 644 $(WORKSRC)/UPGRADE $(DESTDIR)$(docdir)/$(GARNAME)
	@ginstall -m 644 $(WORKSRC)/contrib/clamdwatch/* $(DESTDIR)$(docdir)/$(GARNAME)/contrib
	@ginstall -m 644 $(WORKSRC)/contrib/init/Solaris10/* $(DESTDIR)$(docdir)/$(GARNAME)/contrib
	@ginstall -m 644 $(WORKSRC)/contrib/cleanup-partial.pl $(DESTDIR)$(docdir)/$(GARNAME)/contrib
	@for file in $(WORKSRC)/docs/html/*; do \
	   cp $$file $(DESTDIR)$(docdir)/$(GARNAME)/html ; \
	 done
	@$(MAKECOOKIE)
