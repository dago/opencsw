GARNAME = rubygems
GARVERSION = 0.8.11
CATEGORIES = lang

DESCRIPTION = Ruby package manager
define BLURB
	RubyGems makes it really easy to install Rails and other libraries and to
	keep them up to date.
endef

SPKG_SOURCEURL = http://rubyforge.org/projects/rubygems/
MASTER_SITES   = http://rubyforge.org/frs/download.php/5207/

DISTFILES  = $(GARNAME)-$(GARVERSION).tgz
DISTFILES += $(call admfiles,CSWrubygems,depend copyright)

# Redirect Gem installation to $(DESTDIR)
PATCHFILES += postinstall.diff

CONFIGURE_SCRIPTS = rbsetup
BUILD_SCRIPTS = rbsetup
TEST_SCRIPTS =
INSTALL_SCRIPTS = rbsetup

include ../category.mk

post-install: copy-contrib

copy-contrib:
	@mkdir -p $(DESTDIR)$(docdir)/$(GARNAME)
	@cp -v  $(WORKSRC)/README $(DESTDIR)$(docdir)/$(GARNAME)
	@cp -vr $(WORKSRC)/examples $(DESTDIR)$(docdir)/$(GARNAME)
	@cp -vr $(WORKSRC)/scripts $(DESTDIR)$(docdir)/$(GARNAME)
	@$(MAKECOOKIE)

