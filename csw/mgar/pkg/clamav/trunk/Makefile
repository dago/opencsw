GARNAME = clamav
GARVERSION = 0.95.1
#DISTNAME = $(GARNAME)-devel-latest
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
#MASTER_SITES = http://www.clamav.net/snapshot/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
#DISTFILES  = $(GARNAME)-devel-latest.tar.gz

PACKAGES = CSWclamav CSWlibclamav
CATALOGNAME_CSWclamav = clamav
SPKG_DESC_CSWclamav = $(DESCRIPTION)
CATALOGNAME_CSWlibclamav = libclamav
SPKG_DESC_CSWlibclamav = $(DESCRIPTION) Library

REQUIRED_PKGS_CSWclamav = CSWlibclamav CSWzlib CSWbzip2 CSWiconv CSWcswclassutils CSWncurses CSWlibtoolrt
REQUIRED_PKGS_CSWlibclamav = CSWzlib CSWbzip2 CSWiconv

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

# add usergroup class
SPKG_CLASSES_CSWclamav = none cswusergroup ugfiles cswcpsampleconf cswinitsmf

OPT_FLAGS_SOS = -xO2

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --disable-clamav
CONFIGURE_ARGS += --enable-milter
# unrecognized by 0.95rc1? CONFIGURE_ARGS += --with-sendmail=$(libdir)/sendmail
CONFIGURE_ARGS += --with-dbdir=/var/opt/csw/$(GARNAME)/db
CONFIGURE_ARGS += --localstatedir=/var/opt/csw/$(GARNAME)

EXTRA_MERGE_EXCLUDE_FILES = .*~ $(libdir)/.*\.a $(libdir)/.*\.la

PKGFILES_CSWlibclamav  = $(libdir)/.*
PKGFILES_CSWlibclamav += $(includedir)/.*
PKGFILES_CSWlibclamav += $(docdir)/libclamav/.*

PROTOTYPE_FILTER  = awk ' \
   $$$$3 ~ /\/init.d\/cswclamd$$$$/ { $$$$2 = "cswinitsmf" } \
   $$$$3 ~ /\/init.d\/cswclamav-milter$$$$/ { $$$$2 = "cswinitsmf" } \
   $$$$3 ~ /\/clamd.conf.CSW$$$$/ { $$$$2 = "cswcpsampleconf" } \
   $$$$3 ~ /\/clamav-milter.conf.CSW$$$$/ { $$$$2 = "cswcpsampleconf" } \
   $$$$3 ~ /\/freshclam.conf.CSW$$$$/ { $$$$2 = "cswcpsampleconf" } \
   $$$$3 ~ /\/var\/opt\/csw\/clamav/ { $$$$5 = "clamav" ; $$$$2 = "ugfiles" } \
   $$$$3 ~ /\/opt\/csw\/etc\/CSWclamav\/cswusergroup$$$$/ { $$$$2 = "cswusergroup" } \
   { print }'

SPKG_SOURCEURL = http://www.clamav.net

TEST_TARGET = check

# can not run checkpkg due to libs in separate package
ENABLE_CHECK=0

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
	@( cd $(DESTDIR)$(sysconfdir) ; \
	   gpatch < ../../../../../$(FILEDIR)/CSWclamav.clamd.conf.p )
	@mv $(DESTDIR)$(sysconfdir)/clamd.conf $(DESTDIR)$(sysconfdir)/clamd.conf.CSW
	@( cd $(DESTDIR)$(sysconfdir) ; \
	   gpatch < ../../../../../$(FILEDIR)/CSWclamav.freshclam.conf.p )
	@mv $(DESTDIR)$(sysconfdir)/freshclam.conf $(DESTDIR)$(sysconfdir)/freshclam.conf.CSW
	@mv $(DESTDIR)$(sysconfdir)/clamav-milter.conf $(DESTDIR)$(sysconfdir)/clamav-milter.conf.CSW
	@ginstall -d $(DESTDIR)$(sysconfdir)/CSWclamav
	@ginstall -m 644 $(FILEDIR)/CSWclamav.cswusergroup $(DESTDIR)$(sysconfdir)/CSWclamav/cswusergroup
	@ginstall -d $(DOCDEST)
	@$(foreach DOC,$(DOCS),ginstall -m 644 $(WORKSRC)/$(DOC) $(DOCDEST);)
	@ginstall -m 644 $(FILEDIR)/CSWclamav.INSTALL.clamav-milter.CSW $(DOCDEST)/INSTALL.clamav-milter.CSW
	@ginstall -m 644 $(FILEDIR)/CSWclamav.README.CSW $(DOCDEST)/README.CSW
	@ginstall -d $(DOCDEST)/contrib
	@ginstall -m 644 $(WORKSRC)/contrib/clamdwatch/* $(DOCDEST)/contrib
	@ginstall -m 644 $(WORKSRC)/contrib/cleanup-partial.pl $(DOCDEST)/contrib
	@ginstall -d $(DOCDEST)/html
	@ginstall -m 644 $(WORKSRC)/docs/html/* $(DOCDEST)/html
	@$(MAKECOOKIE)
