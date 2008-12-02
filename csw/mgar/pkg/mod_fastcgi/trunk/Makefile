GARNAME = mod_fastcgi
GARVERSION = 2.4.6
CATEGORIES = server

DESCRIPTION = Apache 2.x FastCGI module
define BLURB
  FastCGI  is a language independent, scalable, open extension to CGI that
  provides high performance without the limitations of server specific APIs.
endef

MASTER_SITES = http://www.fastcgi.com/dist/
DISTFILES += $(GARNAME)-$(GARVERSION).tar.gz
ADMFILES   = depend prototype postinstall preremove copyright
DISTFILES += $(call admfiles,CSWap2modfastcgi,$(ADMFILES))

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

# Allow fcgi to compile against Apache 2.2.  From
# http://www.fastcgi.com/archives/fastcgi-developers/2005-December/004060.html
# with blastwave modifications.
PATCHFILES += apr_compat.diff

CONFIGURE_SCRIPTS =

# No test suite
TEST_SCRIPTS =

STRIP_DIRS = $(DESTDIR)$(prefix)/apache2/libexec

include gar/category.mk

pre-build:
	@( cd $(WORKSRC) ; cp Makefile.AP2 Makefile )
	@$(MAKECOOKIE)

pkgdocs = $(DESTDIR)$(docdir)/$(GARNAME)
post-install:
	@install -d $(pkgdocs)
	@cp $(WORKSRC)/docs/* $(WORKSRC)/README $(WORKSRC)/CHANGES $(pkgdocs)
	@$(MAKECOOKIE)

