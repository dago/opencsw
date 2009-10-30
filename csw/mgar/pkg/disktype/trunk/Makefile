GARNAME = disktype
GARVERSION = 9
CATEGORIES = utils

DESCRIPTION = Detection of content format of a disk or disk image
define BLURB
  The purpose of disktype is to detect the content format of a disk or
  disk image. It knows about common file systems, partition tables, and boot codes.
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

# The provided manpage doesn't work with Solaris nroff.
# See for details bug #1055:
#   http://www.opencsw.org/mantis/view.php?id=1055
DISTFILES += disktype.1

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

LICENSE = LICENSE

SPKG_SOURCEURL = http://disktype.sourceforge.net/

CONFIGURE_SCRIPTS =
BUILD_ARGS = CC="$(CC)" CFLAGS="$(CFLAGS)" LDFLAGS="$(LDFLAGS)"
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

include gar/category.mk

install-custom:
	ginstall -d $(DESTDIR)$(bindir)
	ginstall $(WORKSRC)/disktype $(DESTDIR)$(bindir)
	ginstall -d $(DESTDIR)$(mandir)/man1
	ginstall $(WORKDIR)/disktype.1 $(DESTDIR)$(mandir)/man1/
	@$(MAKECOOKIE)
