GARNAME = rubygems
GARVERSION = 1.2.0
CATEGORIES = lang

DESCRIPTION = Ruby package manager
define BLURB
	RubyGems makes it really easy to install Rails and other libraries and to
	keep them up to date.
endef

SPKG_SOURCEURL = http://rubyforge.org/projects/rubygems/
MASTER_SITES   = http://rubyforge.org/frs/download.php/38646/

DISTFILES  = $(GARNAME)-$(GARVERSION).tgz
DISTFILES += $(call admfiles,CSWrubygems,depend copyright)

# Redirect Gem installation to $(DESTDIR)
#PATCHFILES += postinstall.diff

#CONFIGURE_SCRIPTS = $(WORKSRC)/setup.rb
CONFIGURE_SCRIPTS =
#BUILD_SCRIPTS = $(WORKSRC)/setup.rb
BUILD_SCRIPTS = 
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

include gar/category.mk

install-custom:
	( cd $(WORKSRC) ; ruby ./setup.rb --destdir=$(DESTDIR); )
	@$(MAKECOOKIE)

post-install: copy-contrib

copy-contrib:
	@mkdir -p $(DESTDIR)$(docdir)/$(GARNAME)
	@gcp -v  $(WORKSRC)/README $(DESTDIR)$(docdir)/$(GARNAME)
	@gcp -v  $(WORKSRC)/LICENSE.txt $(DESTDIR)$(docdir)/$(GARNAME)
	@gcp -v  $(WORKSRC)/GPL.txt $(DESTDIR)$(docdir)/$(GARNAME)
	@gcp -vr $(WORKSRC)/scripts $(DESTDIR)$(docdir)/$(GARNAME)
	@$(MAKECOOKIE)

