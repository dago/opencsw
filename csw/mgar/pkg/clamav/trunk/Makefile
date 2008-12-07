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

pre-package:
	@echo "  ==> Pre-package for $(GARNAME)"
	@find $(DESTDIR) -type f -name "*~" -exec rm {} \;
	@ginstall -d $(DESTDIR)$(docdir)/$(GARNAME)
	@ginstall -m 644 $(WORKSRC)/AUTHORS $(DESTDIR)$(docdir)/$(GARNAME)
	@ginstall -m 644 $(WORKSRC)/COPYING $(DESTDIR)$(docdir)/$(GARNAME)/LICENSE
	@ginstall -m 644 $(WORKSRC)/FAQ $(DESTDIR)$(docdir)/$(GARNAME)
	@ginstall -m 644 $(WORKSRC)/NEWS $(DESTDIR)$(docdir)/$(GARNAME)
	@ginstall -m 644 $(WORKSRC)/README $(DESTDIR)$(docdir)/$(GARNAME)
	@$(MAKECOOKIE)
