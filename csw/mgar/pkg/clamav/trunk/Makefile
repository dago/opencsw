# clamav, Peter Bonivart

# build with "ENABLE_CHECK=0 gmake package"
# check mantis bugs

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
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWclamav,checkinstall preinstall)
DISTFILES += $(call admfiles,CSWlibclamav,)

SPKG_DESC_CSWclamav = Clam AntiVirus
SPKG_DESC_CSWlibclamav = Clam AntiVirus Library

REQUIRED_PKGS_CSWclamav = CSWlibclamav CSWlibgmp CSWzlib CSWbzip2 CSWiconv CSWcswclassutils CSWtcpwrap
REQUIRED_PKGS_CSWlibclamav = CSWlibgmp CSWzlib CSWbzip2 CSWiconv

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

SPKG_CLASSES = none cswcpsampleconf cswinitsmf

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --disable-clamav
CONFIGURE_ARGS += --enable-milter
CONFIGURE_ARGS += --with-sendmail=$(libdir)/sendmail
CONFIGURE_ARGS += --with-dbdir=/var/opt/csw/$(GARNAME)/db
CONFIGURE_ARGS += --localstatedir=/var/opt/csw/$(GARNAME)

EXTRA_MERGE_EXCLUDE_FILES = .*~ $(libdir)/.*\.a $(libdir)/.*\.la

PKGFILES_CSWlibclamav  = $(libdir)/.*
PKGFILES_CSWlibclamav += $(includedir)/.*

PROTOTYPE_FILTER  = awk '$$$$3 ~ /\/init.d\/cswclamd$$$$/ { $$$$2 = "cswinitsmf" } $$$$3 ~ /\/init.d\/cswclamav-milter$$$$/ { $$$$2 = "cswinitsmf" } $$$$3 ~ /\/clamd.conf.CSW$$$$/ { $$$$2 = "cswcpsampleconf" } $$$$3 ~ /\/freshclam.conf.CSW$$$$/ { $$$$2 = "cswcpsampleconf" } $$$$3 ~ /\/var\/opt\/csw\/clamav/ { $$$$5 = "clamav" } { print }'

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
	@echo " ==> Post-install for $(GARNAME) (custom)"
	@ginstall -d $(DESTDIR)/etc/opt/csw/init.d
	@ginstall -m 755 $(FILEDIR)/CSWclamav.cswclamd $(DESTDIR)/etc/opt/csw/init.d/cswclamd
	@ginstall -m 755 $(FILEDIR)/CSWclamav.cswclamav-milter $(DESTDIR)/etc/opt/csw/init.d/cswclamav-milter
	@mv $(DESTDIR)$(sysconfdir)/clamd.conf $(DESTDIR)$(sysconfdir)/clamd.conf.CSW
	@mv $(DESTDIR)$(sysconfdir)/freshclam.conf $(DESTDIR)$(sysconfdir)/freshclam.conf.CSW
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
