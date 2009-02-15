GARNAME = rubygems
GARVERSION = 1.3.1
CATEGORIES = xtra

DESCRIPTION = Ruby package manager
define BLURB
RubyGems makes it really easy to install Rails and other libraries and to
keep them up to date.
endef


SPKG_SOURCEURL = http://rubyforge.org/projects/rubygems/
MASTER_SITES   = http://rubyforge.org/frs/download.php/45905/

DISTFILES  = $(GARNAME)-$(GARVERSION).tgz

ARCHALL = 1
PREREQUISITE_PKGS = CSWruby
REQUIRED_PKGS_CSWrubygems = CSWruby

LICENSE_CSWrubygems = LICENSE.txt

# We define upstream file regex so we can be notifed of new upstream
# software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tgz

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = 
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

include gar/category.mk

install-custom:
	( cd $(WORKSRC) ; \
		ruby ./setup.rb --destdir=$(DESTDIR)/$(prefix); )
	@$(MAKECOOKIE)

post-install-modulated: copy-contrib

copy-contrib:
	@mkdir -p $(DESTDIR)$(docdir)/$(GARNAME)
	@gcp -v  $(WORKSRC)/README $(DESTDIR)$(docdir)/$(GARNAME)
	@gcp -v  $(WORKSRC)/LICENSE.txt $(DESTDIR)$(docdir)/$(GARNAME)
	@gcp -v  $(WORKSRC)/GPL.txt $(DESTDIR)$(docdir)/$(GARNAME)
	@gcp -vr $(WORKSRC)/scripts $(DESTDIR)$(docdir)/$(GARNAME)
	@$(MAKECOOKIE)

