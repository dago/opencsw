NAME = gnuplot
VERSION = 4.6.1

DESCRIPTION = The Gnuplot Plotting Utilityting Utility.
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(NAME)-$(VERSION).tar.gz

PATCHFILES = 0001-Remove-definition-unclear-why-leaving-it-rc solaris10-i386

VENDOR_URL = http://www.gnuplot.info/

LICENSE = Copyright

PACKAGES += CSWgnuplot
CATALOGNAME_CSWgnuplot = gnuplot
SPKG_DESC_CSWgnuplot = $(DESCRIPTION)
RUNTIME_DEP_PKGS_CSWgnuplot += CSWlibpng12-0
RUNTIME_DEP_PKGS_CSWgnuplot += CSWlibfontconfig1
RUNTIME_DEP_PKGS_CSWgnuplot += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWgnuplot += CSWlibreadline6
RUNTIME_DEP_PKGS_CSWgnuplot += CSWlibgd2
RUNTIME_DEP_PKGS_CSWgnuplot += CSWlibxpm4
RUNTIME_DEP_PKGS_CSWgnuplot += CSWlibncurses5
RUNTIME_DEP_PKGS_CSWgnuplot += CSWliblua5-2
RUNTIME_DEP_PKGS_CSWgnuplot += CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWgnuplot += CSWlibz1
RUNTIME_DEP_PKGS_CSWgnupRUNTIME_DEP_PKGS_CSWgnuplot += CSWlibpdf6
RUNTIME_DEP_PKGS_CSWgnuplot += CSWlibpng15-15

# There is just an emacs style in it, do not depend on it
CHECKPKG_OVERRIDES_CSWgnuplot += missing-dependency|CSWemacscommonplot += CSWlibjpeg7

PACKAGES += CSWgnuplot-wx
CATALOGNAME_CSWgnuplot-wx = gnuplot_wx
SPKG_DESC_CSWgnuplot-wx = $(DESCRIPTION) (with WX-Widgets and Pango)
RUNTIME_DEP_PKGS_CSWgnuplot-wx = CSWgnuplot
RUNTIME_DEP_PKGS_CSWgnuplot-wx += CSWwxwidgetscommon
RUNTIME_DEP_PKGS_CSWgnuplot-wx += CSWlibatk1-0-0
RUNTIME_DEP_PKGS_CSWgnuplot-wx += CSWpango
RUNTIME_DEP_PKGS_CSWgnuplot-wx += CSWlibintl8
RUNTIME_DEP_PKGS_CSWgnuplot-wx += CSWlibpng12-0
RUNTIME_DEP_PKGS_CSWgnuplot-wx += CSWlibfontconfig1
RUNTIME_DEP_PKGS_CSWgnuplot-wx += CSWlibcairo2
RUNTIME_DEP_PKGS_CSWgnuplot-wx += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWgnuplot-wx += CSWwxwidgetsgtk2
RUNTIME_DEP_PKGS_CSWgnuplot-wx += CSWlibreadline6
RUNTIME_DEP_PKGS_CSWgnuplot-wx += CSWlibgd2
RUNTIME_DEP_PKGS_CSWgnuplot-wx += CSWlibxpm4
RUNTIME_DEP_PKGS_CSWgnuplot-wx += CSWlibncurses5
RUNTIME_DEP_PKGS_CSWgnuplot-wx += CSWlibncursesw5
RUNTIME_DEP_PKGS_CSWgnuplot-wx += CSWliblua5-2
RUNTIME_DEP_PKGS_CSWgnuplot-wx += CSWsunmath
RUNTIME_DEP_PKGS_CSWgnuplot-wx += CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWgnuplot-wx += CSWlibz1
RUNTIME_DEP_PKGS_CSWgnuplot-wx += CSWlibjpeg7
RUNTIME_DEP_PKGS_CSWgnuplot-wx += CSWlibgdk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWgnuplot-wx += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWgnuplot-wx += CSWlibgtk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWgnuplot-wx += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWgnuplot-wx += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWgnuplot-wx += CSWlibgdk-pixbuf2-0-0
RUNTIME_DEP_PKGS_CSWgnuplot-wxRUNTIME_DEP_PKGS_CSWgnuplot-wx += CSWlibpdf6
RUNTIME_DEP_PKGS_CSWgnuplot-wx += CSWlibpng15-15

# This is pulled in from Wx, take out if that has been redone
CHECKPKG_OVERRIDES_CSWgnuplot-wx += bad-rpath-entry|/opt/csw/lib/|opt/csw/libexec/gnuplot/4.6/gnuplot_x11-wx

# TBD: Add all build deps += CSWlibgio2-0-0

BUILD_DEP_PKGS = $(RUNTIME_DEP_PKGS_CSWgnuplot-wx)

REINPLACE_USRLOCAL += share/gnuplotrc

+= -norunpath

# Gnuplot automatically pulls in libCstd which is needed by libwx_gtk2u_core-2.8.so.0.6.0 because
# the library is wrong self-contained (ldd -r on that throws unresolved symbol errors).
# Gnuplot itself does not need libCstd leading to stripped NEEDED and then linking in libwx
# fails. Long-term should be a fix to libwx to be self-contained, but add libs unconditionally
# for now.
LINKER_IGNORE =_FLAGS = -norunpath

EXTRA_MODULATORS = WXWIDGETS
MODULATIONS_WXWIDGETS = yes no

CONFIGURE_ARGS = $(DIRPATHS)

CONFIGURE_ARGS_wxwidgets-no += --without-cairo
CONFIGURE_ARGS_wxwidgets-no += --disable-wxwidgets
#CONFIGURE_ARGS_wxwidgets-no += --without-x
CONFIGURE_ARGS += $(CONFIGURE_ARGS_wxwidgets-$(WXWIDGETS))

# Preset value until this is fixed:
#   https://sourceforge.net/tracker/?func=detail&aid=3129839&group_id=2055&atid=102055 (closed)
#   https://sourceforge.net/tracker/?func=detail&atid=102055&aid=3538084&group_id=2055 (heads up)
CONFIGURE_ARGS += ac_cv_type__Bool=no

# Make sure we don't run the interactive displays from demo/
EXTRA_TEST_EXPORTS = # The testsuite does not work without DISPLAY any more, I tested it manually for 4.6.1 with DISPLAY
# without errors. Please retest on major new versions.
SKIPTEST ?= 1= DISPLAY
DISPLAY =

MERGE_SCRIPTS_isa-default-wxwidgets-yes = copy-all
MERGE_SCRIPTS_isa-default-wxwidgets-no = copy-all

# These are exactly the differing files between the install-directories
ALTERNATIVE_FILES += /opt/csw/bin/gnuplot
ALTERNATIVE_FILES += /opt/csw/libexec/gnuplot/4.6/gnuplot_x11
ALTERNATIVE_FILES += /opt/csw/share/emacs/site-lisp/gnuplot-gui.elc
ALTERNATIVE_FILES += /opt/csw/share/emacs/site-lisp/gnuplot.elc
ALTERNATIVE_FILES += /opt/csw/share/gnuplot/4.6/gnuplot.gih

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
CHECKPKG_OVERRIDES_CSWgnuplot += file-with-bad-content|/usr/local|root/opt/csw/share/gnuplot/4.6/gnuplot.gih-nowx
CHECKPKG_OVERRIDES_CSWgnuplot-wx += file-with-bad-content|/usr/local|root/opt/csw/share/gnuplot/4.6/gnuplot.gih-wx
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
		$(WORKS