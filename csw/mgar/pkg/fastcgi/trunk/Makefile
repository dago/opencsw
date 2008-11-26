GARNAME = fastcgi
GARVERSION = 2.4.0
CATEGORIES = lib

DESCRIPTION = A FastCGI Library
define BLURB
  FastCGI is a language independent, scalable, open extension to CGI
  that provides high performance without the limitations of server
  specific APIs.
endef

DLNAME = fcgi-$(GARVERSION)

#note that this project is named fastcgi, but the tarball is filed as fcgi.
#i'm preserving the name fastcgi (since it shows up in the package listing,
#etc, as there is a reimplementation (binary compatibly) project called fcgi.
MASTER_SITES = http://www.fastcgi.com/dist/
DISTFILES  = $(DLNAME).tar.gz
DISTFILES += CSWfastcgi.gspec CSWfastcgi.depend CSWfastcgi.prototype
#DISTFILES += CSWfastcgidoc.gspec CSWfastcgidoc.depend CSWfastcgidoc.prototype

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

WORKSRC ?= $(WORKDIR)/$(DLNAME)

datadir = $(docdir)/$(GARNAME)

# Remove the following rules and uncomment the
# include before building.
all: .DEFAULT
.DEFAULT:
	@true

PI_TARGETS = instdocs

instdocs:
	@mkdir -p $(DESTDIR)$(datadir)
	@mkdir -p $(DESTDIR)$(mandir)/man1
	@mkdir -p $(DESTDIR)$(mandir)/man3
	@cp -R $(WORKSRC)/doc/* $(DESTDIR)$(datadir)
	@for m3 in Accept Finish SetExitStatus StartFilterData; do \
		cp $(WORKSRC)/doc/FCGI_$$m3.3 $(DESTDIR)$(mandir)/man3/; \
	done
	@cp $(WORKSRC)/doc/*1 $(DESTDIR)$(mandir)/man1/
	@cp $(WORKSRC)/LICENSE.TERMS $(DESTDIR)$(datadir)/
	@$(MAKECOOKIE)
	
post-install: $(PI_TARGETS)
	@$(MAKECOOKIE)

#include gar/category.mk
include gar/category.mk
