NAME = svnstat
VERSION = 1.0
CATEGORIES = apps
GARTYPE = v2

DESCRIPTION = Statistic reports and report graphs similar to StatCvs from Subversion
define BLURB
endef

MASTER_SITES = $(SF_MIRROR)
DISTNAME = SvnStat-$(VERSION)
DISTFILES  = $(DISTNAME).zip

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = SvnStat-(\d+(?:\.\d+)*).zip

VENDOR_URL = http://svnstat.sourceforge.net/

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk
