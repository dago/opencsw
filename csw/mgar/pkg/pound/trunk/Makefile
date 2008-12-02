GARNAME = Pound
GARVERSION = 2.0.4
CATEGORIES = net

DESCRIPTION = reverse proxy load balancer
define BLURB
	The Pound program is a reverse proxy, load balancer and HTTPS front-end for
	Web server(s). Pound was developed to enable distributing the load among
	several Web-servers and to allow for a convenient SSL wrapper for those Web
	servers that do not offer it natively. Pound is distributed under the GPL -
	no warranty, it's free to use, copy and give away.
endef

MASTER_SITES = http://www.apsis.ch/pound/
DISTFILES  = $(GARNAME)-$(GARVERSION).tgz
DISTFILES += $(call admfiles,CSWpound,)

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tgz

# Install properly when
#    (a) destdir does not exist, and
#    (b) installing as non root.
PATCHFILES += install.diff

# Look for regcomp() instead of pcreposix_regcomp()
PATCHFILES += pcre.diff

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --enable-super
CONFIGURE_ARGS += --enable-msdav
CONFIGURE_ARGS += --with-ssl=$(prefix)

# No test suite available
TEST_SCRIPTS =

include gar/category.mk
