NAME = gnuplot
VERSION = 4.4.3
CATEGORIES = utils

DESCRIPTION = The Gnuplot Plotting Utility
define BLURB
  The Gnuplot Plotting Utility.
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(NAME)-$(VERSION).tar.gz

PATCHFILES = 0001-Remove-definition-unclear-why-leaving-it-in-causes-e.patch

VENDOR_URL = http://www.gnuplot.info/

LICENSE = Copyright

PACKAGES += CSWgnuplot
CATALOGNAME_CSWgnuplot = gnuplot
SPKG_DESC_CSWgnuplot = $(DESCRIPTION)
RUNTIME_DEP_PKGS_CSWgnuplot += CSWpng
RUNTIME_DEP_PKGS_CSWgnuplot += CSWemacscommon
RUNTIME_DEP_PKGS_CSWgnuplot += CSWfconfig
RUNTIME_DEP_PKGS_CSWgnuplot += CSWiconv
RUNTIME_DEP_PKGS_CSWgnuplot += CSWreadline
RUNTIME_DEP_PKGS_CSWgnuplot += CSWlibgd2
RUNTIME_DEP_PKGS_CSWgnuplot += CSWxpm
RUNTIME_DEP_PKGS_CSWgnuplot += CSWncurses
RUNTIME_DEP_PKGS_CSWgnuplot += CSWlua
RUNTIME_DEP_PKGS_CSWgnuplot += CSWftype2
RUNTIME_DEP_PKGS_CSWgnuplot += CSWzlib
RUNTIME_DEP_PKGS_CSWgnuplot += CSWjpeg

PACKAGES += CSWgnuplot-wx
CATALOGNAME_CSWgnuplot-wx = gnuplot_wx
SPKG_DESC_CSWgnuplot-wx = $(DESCRIPTION) (with WX-Widgets and Pango)
RUNTIME_DEP_PKGS_CSWgnuplot-wx = CSWgnuplot
RUNTIME_DEP_PKGS_CSWgnuplot-wx += CSWwxwidgetscommon
RUNTIME_DEP_PKGS_CSWgnuplot-wx += CSWlibatk
RUNTIME_DEP_PKGS_CSWgnuplot-wx += CSWpango
RUNTIME_DEP_PKGS_CSWgnuplot-wx += CSWlibintl8
RUNTIME_DEP_PKGS_CSWgnuplot-wx += CSWpng
RUNTIME_DEP_PKGS_CSWgnuplot-wx += CSWfconfig
RUNTIME_DEP_PKGS_CSWgnuplot-wx += CSWlibcairo
RUNTIME_DEP_PKGS_CSWgnuplot-wx += CSWiconv
RUNTIME_DEP_PKGS_CSWgnuplot-wx += CSWwxwidgetsgtk2
RUNTIME_DEP_PKGS_CSWgnuplot-wx += CSWreadline
RUNTIME_DEP_PKGS_CSWgnuplot-wx += CSWgtk2
RUNTIME_DEP_PKGS_CSWgnuplot-wx += CSWlibgd2
RUNTIME_DEP_PKGS_CSWgnuplot-wx += CSWxpm
RUNTIME_DEP_PKGS_CSWgnuplot-wx += CSWncurses
RUNTIME_DEP_PKGS_CSWgnuplot-wx += CSWlua
RUNTIME_DEP_PKGS_CSWgnuplot-wx += CSWsunmath
RUNTIME_DEP_PKGS_CSWgnuplot-wx += CSWftype2
RUNTIME_DEP_PKGS_CSWgnuplot-wx += CSWglib2
RUNTIME_DEP_PKGS_CSWgnuplot-wx += CSWzlib
RUNTIME_DEP_PKGS_CSWgnuplot-wx += CSWjpeg

BUILD_DEP_PKGS = $(RUNTIME_DEP_PKGS_CSWgnuplot-wx)

EXTRA_LINKER_FLAGS = -norunpath

EXTRA_MODULATORS = WXWIDGETS
MODULATIONS_WXWIDGETS = yes no

CONFIGURE_ARGS = $(DIRPATHS)

CONFIGURE_ARGS_wxwidgets-no += --without-cairo
CONFIGURE_ARGS_wxwidgets-no += --disable-wxwidgets
CONFIGURE_ARGS_wxwidgets-no += --without-x
CONFIGURE_ARGS += $(CONFIGURE_ARGS_wxwidgets-$(WXWIDGETS))

# Preset value until this is fixed:
#   https://sourceforge.net/tracker/?func=detail&aid=3129839&group_id=2055&atid=102055
CONFIGURE_ARGS += ac_cv_type__Bool=no

# Make sure we don't run the interactive displays from demo/
EXTRA_TEST_EXPORTS = DISPLAY
DISPLAY =

MERGE_SCRIPTS_isa-default-wxwidgets-yes = copy-all
MERGE_SCRIPTS_isa-default-wxwidgets-no = copy-all

# These are exactly the differing files between the install-directories
ALTERNATIVE_FILES += /opt/csw/bin/gnuplot
ALTERNATIVE_FILES += /opt/csw/libexec/gnuplot/4.4/gnuplot_x11
ALTERNATIVE_FILES += /opt/csw/share/emacs/site-lisp/gnuplot-gui.elc
ALTERNATIVE_FILES += /opt/csw/share/emacs/site-lisp/gnuplot.elc
ALTERNATIVE_FILES += /opt/csw/share/gnuplot/4.4/gnuplot.gih

WXSUFFIX-yes = wx
WXSUFFIX-no = nowx

EXTRA_PAX_ARGS = $(foreach A,$(ALTERNATIVE_FILES),-s ",^\.\($A\),\1-$(WXSUFFIX-$(WXWIDGETS)),p")

ALTERNATIVES_CSWgnuplot = basic
ALTERNATIVES_CSWgnuplot-wx = wxwidgets
ALTERNATIVE_basic = $(firstword $(ALTERNATIVE_FILES)) gnuplot $(firstword $(ALTERNATIVE_FILES))-$(WXSUFFIX-no) 100
ALTERNATIVE_basic += $(foreach A,$(wordlist 2,$(words $(ALTERNATIVE_FILES)),$(ALTERNATIVE_FILES)),$A $(notdir $A) $A-$(WXSUFFIX-no))
ALTERNATIVE_wxwidgets = $(firstword $(ALTERNATIVE_FILES)) gnuplot $(firstword $(ALTERNATIVE_FILES))-$(WXSUFFIX-yes) 200
ALTERNATIVE_wxwidgets += $(foreach A,$(wordlist 2,$(words $(ALTERNATIVE_FILES)),$(ALTERNATIVE_FILES)),$A $(notdir $A) $A-$(WXSUFFIX-yes))

PKGFILES_CSWgnuplot-wx = $(addsuffix -$(WXSUFFIX-yes),$(ALTERNATIVE_FILES))

# "Alternatives" are not properly checked yet
CHECKPKG_OVERRIDES_CSWgnuplot += surplus-dependency|CSWalternatives
CHECKPKG_OVERRIDES_CSWgnuplot-wx += surplus-dependency|CSWalternatives

# These are just examples
CHECKPKG_OVERRIDES_CSWgnuplot += file-with-bad-content|/usr/local|root/opt/csw/share/gnuplot/4.4/gnuplot.gih-nowx
CHECKPKG_OVERRIDES_CSWgnuplot-wx += file-with-bad-content|/usr/local|root/opt/csw/share/gnuplot/4.4/gnuplot.gih-wx
CHECKPKG_OVERRIDES_CSWgnuplot += file-with-bad-content|/usr/local|root/opt/csw/share/info/gnuplot.info

# Is this GDFONTPATH related? That would be bad... CHECK!!!
#CHECKPKG_OVERRIDES_CSWgnuplot += file-with-bad-content|/usr/local|root/opt/csw/bin/gnuplot-nowx
#CHECKPKG_OVERRIDES_CSWgnuplot-wx += file-with-bad-content|/usr/local|root/opt/csw/bin/gnuplot-wx
#CHECKPKG_OVERRIDES_CSWgnuplot += file-with-bad-content|/usr/share|root/opt/csw/bin/gnuplot-nowx
#CHECKPKG_OVERRIDES_CSWgnuplot-wx += file-with-bad-content|/usr/share|root/opt/csw/bin/gnuplot-wx

include gar/category.mk

# Adjust font pathes. /usr/sfw is just the last resort for a font, it could have been ommitted.
post-extract-modulated:
	perl -pi \
		-e 's,/usr/X11R6/lib/X11/fonts/Type1,/usr/openwin/lib/X11/fonts/Type1,;' \
		-e 's,/usr/X11R6/lib/X11/fonts/truetype,/usr/openwin/lib/X11/fonts/TrueType,;' \
		-e 's,/usr/share/ghostscript/fonts,/opt/csw/share/ghostscript/fonts,;' \
		-e 's,/usr/local/share/ghostscript/fonts,/usr/sfw/share/ghostscript/fonts,;' \
		$(WORKSRC)/src/variable.c
