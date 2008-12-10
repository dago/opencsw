# clamav, Peter Bonivart

# files outside /opt/csw are not included, need to fix gspec and cswproto
# put libs in lib/32?
# add rc/smf support. cswclassutils?
# add pre/post scripts
# add etc/clamav-milter?
# add etc/clamd?
# check mantis bugs
# + add doc/README.CSW, INSTALL.clamav-milter.CSW
# + split into multiple packages: clamav, libclamav
# + add re for update notification
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

SF_PROJ = clamav
MASTER_SITES = $(SF_MIRRORS)
#MASTER_SITES = http://freshmeat.net/redir/clamav/29355/url_tgz/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWclamav,checkinstall preinstall postinstall preremove)
DISTFILES += $(call admfiles,CSWlibclamav,)

SPKG_DESC_CSWclamav = Clam AntiVirus
SPKG_DESC_CSWlibclamav = Clam AntiVirus Library

REQUIRED_PKGS_CSWclamav = CSWlibclamav CSWlibgmp CSWzlib CSWbzip2 CSWiconv CSWcswclassutils
REQUIRED_PKGS_CSWlibclamav = CSWlibgmp CSWzlib CSWbzip2 CSWiconv

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

SPKG_CLASSES = none cswinitsmf

#GARCOMPILER = GCC3

CONFIGURE_ARGS  = $(DIRPATHS)
#CONFIGURE_ARGS += --with-user=nobody
#CONFIGURE_ARGS += --with-group=nobody
CONFIGURE_ARGS += --disable-clamav
CONFIGURE_ARGS += --enable-milter
CONFIGURE_ARGS += --with-sendmail=$(libdir)/sendmail
CONFIGURE_ARGS += --with-dbdir=/var/opt/csw/$(GARNAME)/db
CONFIGURE_ARGS += --localstatedir=/var/opt/csw/$(GARNAME)

EXTRA_MERGE_EXCLUDE_FILES = .*~ $(libdir)/.*\.a $(libdir)/.*\.la

PKGFILES_CSWlibclamav  = $(libdir)/.*
PKGFILES_CSWlibclamav += $(includedir)/.*

SPKG_SOURCEURL = http://www.clamav.net/

include gar/category.mk

DOCS  = AUTHORS BUGS ChangeLog
DOCS += FAQ NEWS README UPGRADE
DOCS += docs/clamav-mirror-howto.pdf
DOCS += docs/clamdoc.pdf
DOCS += docs/phishsigs_howto.pdf
DOCS += docs/signatures.pdf

DOCDEST = $(DESTDIR)$(docdir)/$(GARNAME)

post-install-modulated:
	@echo " ==> Post-install for $(GARNAME)"
	@ginstall -d $(DESTDIR)/etc/opt/csw/init.d
	@ginstall -m 755 $(FILEDIR)/CSWclamav.cswclamd $(DESTDIR)/etc/opt/csw/init.d/cswclamd
	@ginstall -d $(DOCDEST)
	@$(foreach DOC,$(DOCS),ginstall -m 644 $(WORKSRC)/$(DOC) $(DOCDEST);)
	@ginstall -m 644 $(WORKSRC)/COPYING $(DOCDEST)/LICENSE
	@ginstall -m 644 $(FILEDIR)/CSWclamav.INSTALL.clamav-milter.CSW $(DOCDEST)/INSTALL.clamav-milter.CSW
	@ginstall -m 644 $(FILEDIR)/CSWclamav.README.CSW $(DOCDEST)/README.CSW
	@ginstall -d $(DOCDEST)/contrib
	@ginstall -m 644 $(WORKSRC)/contrib/clamdwatch/* $(DOCDEST)/contrib
	@ginstall -m 644 $(WORKSRC)/contrib/init/Solaris10/* $(DOCDEST)/contrib
	@ginstall -m 644 $(WORKSRC)/contrib/cleanup-partial.pl $(DOCDEST)/contrib
	@ginstall -d $(DOCDEST)/html
	@ginstall -m 644 $(WORKSRC)/docs/html/* $(DOCDEST)/html
	@ginstall -d $(DESTDIR)$(docdir)/libclamav
	@ginstall -m 644 $(WORKSRC)/COPYING $(DESTDIR)$(docdir)/libclamav/LICENSE
	@$(MAKECOOKIE)
