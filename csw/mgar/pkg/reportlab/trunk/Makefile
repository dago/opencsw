NAME = reportlab
VERSION = 2.4
CATEGORIES = python
DISTNAME = ReportLab_2_4

DESCRIPTION = industry-strength PDF generating solution
define BLURB
  Free Open Source PDF library is suitable for web publishers, developers
  or creative design professionals who need to quickly and easily create
  or automate complex (even data-driven) documents. It lets you create
  professional documents programmatically without being locked into one
  special technology and/or platform. It has grown over years in response
  to the real-world requirements of large financial institutions'
  reporting needs, making it the trusted proven foundation of existing
  enterprise solutions rather than a just a fancy gimmick or interesting
  library.
endef

MASTER_SITES = http://www.reportlab.org/ftp/
DISTFILES  = $(DISTNAME).tar.gz

RUNTIME_DEP_PKGS_CSWreportlab = CSWpil

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = ReportLab_(\d+(?:\_\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =

include gar/category.mk

