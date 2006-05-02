GARNAME = mod_python
GARVERSION = 3.2.8
CATEGORIES = server

DESCRIPTION = an Apache/Python integration module
define BLURB
  Mod_python is an Apache module that embeds the Python language interpreter
  within the server, allowing for Apache handlers to be written in Python for
  faster and more powerful applications than plain CGI.
endef

MASTER_SITES = http://www.ibiblio.org/pub/mirrors/apache/httpd/modpython/
DISTFILES  = $(GARNAME)-$(GARVERSION).tgz
pkgfiles   = depend prototype postinstall preremove space
DISTFILES += $(call admfiles,CSWap2modpython,$(pkgfiles))

#DEPENDS += lang/python

# Fix refs to APR_STATUS_IS_SUCCESS
PATCHFILES += apr.diff

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-apxs=$(prefix)/apache2/sbin/apxs
CONFIGURE_ARGS += --with-python=$(bindir)/python
CONFIGURE_ARGS += --with-flex=$(prefix)/flex-2.5.31/bin/flex

include ../category.mk

pre-configure:
	@( cd $(WORKSRC) ; autoconf )
	@$(MAKECOOKIE)

