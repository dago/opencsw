GARNAME = Frontier-RPC
DISTVERSION = 0.07b4
GARVERSION = $(subst b,.,$(DISTVERSION))
CATEGORIES = cpan
AUTHOR = KMACLEOD

DESCRIPTION = XML-RPC client interface
define BLURB
  Frontier::Client is an XML-RPC client over HTTP. Frontier::Client instances
  are used to make calls to XML-RPC servers and as shortcuts for creating
  XML-RPC special data types.
endef

MODDIST    = $(GARNAME)-$(DISTVERSION).tar.gz
DISTFILES += CSWpmfrontierrpc.gspec CSWpmfrontierrpc.depend

DEPENDS += cpan/HTML-Parser cpan/URI
DEPENDS += cpan/libwww-perl cpan/XML-Parser

PERL_PACKLIST = $(DESTDIR)$(perlpackroot)/Frontier/RPC/.packlist

include ../category.mk

post-install:
	@mkdir -p $(DESTDIR)$(docdir)/$(GARNAME)
	@( cd $(WORKSRC) ; \
		cp README COPYING $(DESTDIR)$(docdir)/$(GARNAME) ; \
		cp -r docs/* $(DESTDIR)$(docdir)/$(GARNAME) ; \
		cp -r examples $(DESTDIR)$(docdir)/$(GARNAME) )
	@$(MAKECOOKIE)

