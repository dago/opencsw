GARNAME = Frontier-RPC
GARVERSION = 0.07b4
CATEGORIES = cpan
AUTHOR = KMACLEOD

DESCRIPTION = XML-RPC client interface
define BLURB
  Frontier::Client is an XML-RPC client over HTTP. Frontier::Client instances
  are used to make calls to XML-RPC servers and as shortcuts for creating
  XML-RPC special data types.
endef

DISTFILES += $(call admfiles,CSWpmfrontierrpc,depend prototype)

# See http://rt.cpan.org/Public/Bug/Display.html?id=18299
PATCHFILES += XMLRPC-mp2.diff

DEPENDS += cpan/HTML-Parser cpan/URI
DEPENDS += cpan/libwww-perl cpan/XML-Parser

PERL_PACKLIST = $(DESTDIR)$(perlpackroot)/Frontier/RPC/.packlist

include gar/category.mk

post-install:
	@mkdir -p $(DESTDIR)$(docdir)/$(GARNAME)
	@( cd $(WORKSRC) ; \
		cp README COPYING $(DESTDIR)$(docdir)/$(GARNAME) ; \
		cp -r docs/* $(DESTDIR)$(docdir)/$(GARNAME) ; \
		cp -r examples $(DESTDIR)$(docdir)/$(GARNAME) )
	@$(MAKECOOKIE)

