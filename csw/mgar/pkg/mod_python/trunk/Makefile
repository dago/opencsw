GARNAME = mod_python
GARVERSION = 3.3.1
CATEGORIES = server

DESCRIPTION = an Apache/Python integration module
define BLURB
  Mod_python is an Apache module that embeds the Python language interpreter
  within the server, allowing for Apache handlers to be written in Python for
  faster and more powerful applications than plain CGI.
endef

MASTER_SITES = http://www.ibiblio.org/pub/mirrors/apache/httpd/modpython/
DISTFILES  = $(GARNAME)-$(GARVERSION).tgz
DISTFILES += postinstall preremove space

PACKAGES = CSWap2modpython

REQUIRED_PKGS_CSWap2modpython = CSWap2prefork CSWpython
CATALOGNAME_CSWap2modpython   = ap2_modpython
SPKG_DESC_CSWap2modpython     = an Apache/Python integration module

STRIP_LIBTOOL = 1
PATCHFILES += connobject.diff

EXTRA_MERGE_EXCLUDE_FILES = .*\.pyo .*\.pyc
PROTOTYPE_FILTER = awk '$$$$3 ~ /.*\.py$$$$/ { $$$$2 = "cswpycompile" } { print }'
SPKG_CLASSES = none cswpycompile
REQUIRED_PKGS += CSWcswclassutils

# We define upstream file regex so we can be notifed of 
# new upstream software release
UFILES_REGEX = (\d+(?:\.\d+)*)

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-apxs=$(prefix)/apache2/sbin/apxs
CONFIGURE_ARGS += --with-python=$(bindir)/python
CONFIGURE_ARGS += --with-flex=$(bindir)/flex-2.5.35
CONFIGURE_ARGS += --with-python-src=../python

include gar/category.mk

DESTDOC = $(DESTDIR)$(docdir)/ap2_modpython

post-install-modulated:
	@install -d $(DESTDOC)
	@for file in COPYRIGHT CREDITS LICENSE NEWS NOTICE README ; do \
	  ginstall -m 0644 $(WORKSRC)/$$file $(DESTDOC) ; \
	done
	@( cd $(WORKSRC) ; gcp -vR examples doc-html $(DESTDOC) )
	@$(DONADA)

