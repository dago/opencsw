NAME = Frontier-RPC
VERSION = 0.07b4
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = KMACLEOD

DESCRIPTION = XML-RPC client interface
define BLURB
  Frontier::Client is an XML-RPC client over HTTP. Frontier::Client instances
  are used to make calls to XML-RPC servers and as shortcuts for creating
  XML-RPC special data types.
endef

DISTFILES += $(call admfiles,CSWpmfrontierrpc,depend prototype)

UFILES_REGEX ?= $(NAME)-((\d+(?:\.\d+)*)(b\d+)?).tar.gz

# See http://rt.cpan.org/Public/Bug/Display.html?id=18299
PATCHFILES += XMLRPC-mp2.diff

DEPENDS += cpan/HTML-Parser cpan/URI
DEPENDS += cpan/libwww-perl cpan/XML-Parser

PERL_PACKLIST = $(DESTDIR)$(perlpackroot)/Frontier/RPC/.packlist

include gar/category.mk

post-install:
	@mkdir -p $(DESTDIR)$(docdir)/$(NAME)
	@( cd $(WORKSRC) ; \
		cp README COPYING $(DESTDIR)$(docdir)/$(NAME) ; \
		cp -r docs/* $(DESTDIR)$(docdir)/$(NAME) ; \
		cp -r examples $(DESTDIR)$(docdir)/$(NAME) )
	@$(MAKECOOKIE)

