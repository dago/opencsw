NAME = mtx
VERSION = 1.3.12
CATEGORIES = utils
GARTYPE = v2

DESCRIPTION = Control tape autoloaders
define BLURB
  mtx is a set of low level driver programs to control features of SCSI backup
  related devices such as autoloaders, tape changers, media jukeboxes, and tape drives.
  It can also report much data, including serial numbers, maximum block sizes, and
  TapeAlert messages that most modern tape drives implement (to tell you the exact
  reason why a backup or restore failed), as well as do raw SCSI READ and WRITE commands
  to tape drives (not important on Linux, but important on Solaris due to the fact that
  the Solaris tape driver supports none of the additional features of tape drives invented
  after 1988). mtx is designed to be a low level driver in a larger scripted backup solution,
  such as Bacula or Amanda. mtx is not supposed to itself be a high level interface to the
  SCSI devices that it controls.
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(NAME)-$(VERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

LICENSE = LICENSE
LICENSE_CSWmtxcontrib = contrib/README

PACKAGES = CSWmtx CSWmtxcontrib

CATALOGNAME_CSWmtx = mtx
CATALOGNAME_CSWmtxcontrib = mtx_contrib

SPKG_DESC_CSWmtx = Control tape autoloaders
SPKG_DESC_CSWmtxcontrib = MTX contributed scripts

RUNTIME_DEP_PKGS_CSWmtxcontrib = CSWmtx CSWtk

VENDOR_URL = http://mtx.opensource-sw.net/

CONTRIBDIR = $(sharedstatedir)/mtx/contrib

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET =

INSTALL_OVERRIDE_DIRS = sbindir mandir

ARCHALL_CSWmtxcontrib = 1

PKGFILES_CSWmtxcontrib = $(CONTRIBDIR)/.*

CHECKPKG_OVERRIDES_CSWmtxcontrib += surplus-dependency|CSWtk
CHECKPKG_OVERRIDES_CSWmtxcontrib += surplus-dependency|CSWmtx

include gar/category.mk

post-extract-modulated:
	-cd $(WORKSRC)/contrib; gzip -c -d mtxctl-0.0.2.tar.gz | tar xvf -
	@$(MAKECOOKIE)

post-install-modulated:
	ginstall -d $(DESTDIR)$(CONTRIBDIR)
	ginstall $(WORKSRC)/contrib/config_sgen_solaris.sh $(DESTDIR)$(CONTRIBDIR)/
	ginstall $(WORKSRC)/contrib/mtxctl/mtxctl.tk $(DESTDIR)$(CONTRIBDIR)/mtxctl
	ginstall $(WORKSRC)/contrib/mtxctl/README $(DESTDIR)$(CONTRIBDIR)/README.mtxctl
	perl -pi -e 's,#!/usr/freeware/bin/wish -f,#!/opt/csw/bin/wish -f,; s,/usr/freeware/bin/mtx,/opt/csw/sbin/mtx,' $(DESTDIR)$(CONTRIBDIR)/mtxctl
	@$(MAKECOOKIE)
