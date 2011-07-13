NAME = enscript
VERSION = 1.6.5.2
CATEGORIES = utils

DESCRIPTION = GNU enscript converts ASCII files to PostScript
define BLURB
  GNU enscript is a free replacement for the Adobe's enscript program.
  Enscript converts ASCII files to PostScript and spools generated PostScript
  output to the specified printer or leaves it to file. Enscript can be easily
  extended to handle different output media and it has many options that can
  be used to customize printouts.
endef

MASTER_SITES = $(GNU_MIRROR)
DISTFILES  = $(DISTNAME).tar.gz

VENDOR_URL = http://www.gnu.org/s/enscript/

RUNTIME_DEP_PKGS_CSWenscript += CSWlibintl8

PRESERVECONF = $(sysconfdir)/enscript.cfg
MIGRATE_FILES = enscript.cfg

# This is the location where the font was taken from
CHECKPKG_OVERRIDES_CSWenscript += file-with-bad-content|/usr/share|root/opt/csw/share/enscript/afm/matrix.pfa

include gar/category.mk

# Adjust font pathes
post-extract-modulated:
	-perl -pi -e 's,/usr/local/lib/ps:/usr/lib/ps,/usr/openwin/lib/X11/fonts/F3/afm:/usr/openwin/lib/X11/fonts/Type1/afm:/usr/openwin/lib/X11/fonts/Type1/sun/afm,' \
		$(WORKSRC)/afmlib/afm.c \
		$(WORKSRC)/lib/enscript.cfg.in

