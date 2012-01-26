NAME = rubygems
VERSION = 1.7.2
CATEGORIES = xtra
GARTYPE = v2

DESCRIPTION = Ruby package manager
define BLURB
RubyGems makes it really easy to install Rails and other libraries and to
keep them up to date.
endef


SPKG_SOURCEURL = http://rubyforge.org/projects/rubygems/
MASTER_SITES   = http://production.cf.rubygems.org/rubygems/

DISTFILES  = $(NAME)-$(VERSION).tgz
DISTFILES += CSWrubygems.cswreleasenotes

ARCHALL = 1
BUILD_DEP_PKGS = CSWruby18
RUNTIME_DEP_PKGS_CSWrubygems = CSWruby18

LICENSE_CSWrubygems = LICENSE.txt

# We define upstream file regex so we can be notifed of new upstream
# software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tgz

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = 
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

CHECKPKG_OVERRIDES_CSWrubygems += file-with-bad-content|/usr/local|root/opt/csw/lib/ruby/site_ruby/1.8/rubygems/gem_path_searcher.rb
CHECKPKG_OVERRIDES_CSWrubygems += surplus-dependency|CSWalternatives

ALTERNATIVE = $(bindir)/gem gem $(bindir)/gem18 5

include gar/category.mk

install-custom:
	( cd $(WORKSRC) ; \
		ruby ./setup.rb --destdir=$(DESTDIR); )
	@$(MAKECOOKIE)

post-install-modulated: copy-contrib
	@$(MAKECOOKIE)

copy-contrib:
	@mkdir -p $(DESTDIR)$(docdir)/$(NAME)
	@gcp -v  $(WORKSRC)/README.rdoc $(DESTDIR)$(docdir)/$(NAME)
	@gcp -v  $(WORKSRC)/LICENSE.txt $(DESTDIR)$(docdir)/$(NAME)
	@gcp -v  $(WORKSRC)/GPL.txt $(DESTDIR)$(docdir)/$(NAME)
	@$(MAKECOOKIE)
