NAME = gnuplot
VERSION = 4.4.2
CATEGORIES = utils

DESCRIPTION = The Gnuplot Plotting Utility
define BLURB
  The Gnuplot Plotting Utility.
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(NAME)-$(VERSION).tar.gz

PATCHFILES = 0001-Remove-definition-unclear-why-leaving-it-in-causes-e.patch

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

VENDOR_URL = http://www.gnuplot.info/

LICENSE = Copyright

RUNTIME_DEP_PKGS_CSWgnuplot += CSWwxwidgetscommon
RUNTIME_DEP_PKGS_CSWgnuplot += CSWlibatk
RUNTIME_DEP_PKGS_CSWgnuplot += CSWpango
RUNTIME_DEP_PKGS_CSWgnuplot += CSWggettextrt
RUNTIME_DEP_PKGS_CSWgnuplot += CSWpng
RUNTIME_DEP_PKGS_CSWgnuplot += CSWemacscommon
RUNTIME_DEP_PKGS_CSWgnuplot += CSWfconfig
RUNTIME_DEP_PKGS_CSWgnuplot += CSWlibcairo
RUNTIME_DEP_PKGS_CSWgnuplot += CSWiconv
RUNTIME_DEP_PKGS_CSWgnuplot += CSWwxwidgetsgtk2
RUNTIME_DEP_PKGS_CSWgnuplot += CSWreadline
RUNTIME_DEP_PKGS_CSWgnuplot += CSWgtk2
RUNTIME_DEP_PKGS_CSWgnuplot += CSWgd
RUNTIME_DEP_PKGS_CSWgnuplot += CSWxpm
RUNTIME_DEP_PKGS_CSWgnuplot += CSWncurses
RUNTIME_DEP_PKGS_CSWgnuplot += CSWlua
RUNTIME_DEP_PKGS_CSWgnuplot += CSWsunmath
RUNTIME_DEP_PKGS_CSWgnuplot += CSWftype2
RUNTIME_DEP_PKGS_CSWgnuplot += CSWglib2
RUNTIME_DEP_PKGS_CSWgnuplot += CSWzlib
RUNTIME_DEP_PKGS_CSWgnuplot += CSWjpeg

BUILD_DEP_PKGS = $(RUNTIME_DEP_PKGS_CSWgnuplot)

CONFIGURE_ARGS = $(DIRPATHS)

# Preset value until this is fixed:
#   https://sourceforge.net/tracker/?func=detail&aid=3129839&group_id=2055&atid=102055
CONFIGURE_ARGS += ac_cv_type__Bool=no

#CONFIGURE_ARGS += --with-texdir=

# Make sure we don't run the interactive displays from demo/
EXTRA_TEST_EXPORTS = DISPLAY
DISPLAY =

TEST_TARGET = check

include gar/category.mk
