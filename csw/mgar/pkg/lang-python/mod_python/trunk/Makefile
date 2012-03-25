# $Id$

NAME = mod_python
VERSION = 3.3.1
CATEGORIES = server
GARTYPE = v2

DESCRIPTION = Apache/Python integration module
define BLURB
  Mod_python is an Apache module that embeds the Python language interpreter
  within the server, allowing for Apache handlers to be written in Python for
  faster and more powerful applications than plain CGI.
endef

MASTER_SITES = http://archive.apache.org/dist/httpd/modpython/
DISTFILES  = $(NAME)-$(VERSION).tgz
DISTFILES += postinstall preremove space

STRIP_LIBTOOL = 1
PATCHFILES += connobject.diff

EXTRA_MERGE_EXCLUDE_FILES = .*\.pyo .*\.pyc
PYCOMPILE = 1

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-apxs=$(prefix)/apache2/sbin/apxs
CONFIGURE_ARGS += --with-python=$(bindir)/python
CONFIGURE_ARGS += --with-flex=$(bindir)/flex-2.5.35
CONFIGURE_ARGS += --with-python-src=../python

LICENSE = LICENSE

PACKAGES = CSWap2modpython
SPKG_DESC_CSWap2modpython     = an Apache/Python integration module
CATALOGNAME_CSWap2modpython = ap2_modpython
RUNTIME_DEP_PKGS_CSWap2modpython += CSWpython
RUNTIME_DEP_PKGS_CSWap2modpython += CSWlibpython2-6-1-0
RUNTIME_DEP_PKGS_CSWap2modpython += CSWapache2

CHECKPKG_OVERRIDES_CSWap2modpython += file-with-bad-content|/usr/local|root/opt/csw/share/doc/ap2_modpython/README
CHECKPKG_OVERRIDES_CSWap2modpython += file-with-bad-content|/usr/local|root/opt/csw/share/doc/ap2_modpython/doc-html/dir-other-pp.html
CHECKPKG_OVERRIDES_CSWap2modpython += file-with-bad-content|/usr/local|root/opt/csw/share/doc/ap2_modpython/doc-html/inst-configure.html
CHECKPKG_OVERRIDES_CSWap2modpython += file-with-bad-content|/usr/share|root/opt/csw/share/doc/ap2_modpython/README

CHECKPKG_OVERRIDES_CSWap2modpython += catalogname-does-not-match-pkgname|pkgname=CSWap2modpython|catalogname=ap2_modpython|expected-catalogname=ap2modpython

CHECKPKG_OVERRIDES_CSWap2modpython += pkginfo-description-not-starting-with-uppercase|an|Apache/Python|integration|module
CHECKPKG_OVERRIDES_CSWap2modpython += pkgname-does-not-start-with-CSWpy-
CHECKPKG_OVERRIDES_CSWap2modpython += catalogname-does-not-start-with-py_

CHECKPKG_OVERRIDES_CSWap2modpython += missing-dependency|CSWapache2

include gar/category.mk

DESTDOC = $(DESTDIR)$(docdir)/ap2_modpython

post-install-modulated:
	@install -d $(DESTDOC)
	@for file in COPYRIGHT CREDITS LICENSE NEWS NOTICE README ; do \
	  ginstall -m 0644 $(WORKSRC)/$$file $(DESTDOC) ; \
	done
	@( cd $(WORKSRC) ; gcp -vR examples doc-html $(DESTDOC) )
	@$(DONADA)

