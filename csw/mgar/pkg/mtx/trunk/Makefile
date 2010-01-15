GARNAME = mtx
GARVERSION = 1.3.12
CATEGORIES = utils

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
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

# TODO:
# - Add stuff from contrib

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

SPKG_SOURCEURL = http://mtx.opensource-sw.net/

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET =

INSTALL_OVERRIDE_DIRS = sbindir mandir

include gar/category.mk

post-install-modulated:
	ginstall $(WORKSRC)/contrib/config_sgen_solaris.sh $(DESTDIR)$(sbindir)
	@$(MAKECOOKIE)
