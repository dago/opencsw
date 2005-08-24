GARNAME = mod_python
GARVERSION = 3.1.4
CATEGORIES = server

DESCRIPTION = an Apache/Python integration module
define BLURB
  Mod_python is an Apache module that embeds the Python language interpreter
  within the server, allowing for Apache handlers to be written in Python for
  faster and more powerful applications than plain CGI.
endef

MASTER_SITES = http://www.ibiblio.org/pub/mirrors/apache/httpd/modpython/
DISTFILES  = $(GARNAME)-$(GARVERSION).tgz
DISTFILES += CSWap2modpython.gspec
DISTFILES += CSWap2modpython.depend
DISTFILES += CSWap2modpython.prototype
DISTFILES += CSWap2modpython.postinstall
DISTFILES += CSWap2modpython.preremove
DISTFILES += CSWap2modpython.space

# Source hard codes path to flex
PATCHFILES += lex.diff

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-apxs=$(prefix)/apache2/sbin/apxs
CONFIGURE_ARGS += --with-python=$(bindir)/python
CONFIGURE_ARGS += --with-flex=$(prefix)/flex-2.5.31/bin/flex

include ../category.mk

pre-configure:
	@( cd $(WORKSRC) ; autoconf )
