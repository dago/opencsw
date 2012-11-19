NAME = corkscrew
VERSION = 2.0

DESCRIPTION = A tool for tunneling SSH through HTTP proxies

MASTER_SITES = http://www.agroman.net/corkscrew/

DISTFILES += $(DISTNAME).tar.gz

REINPLACE_USRLOCAL += README

include gar/category.mk

post-install-modulated:
	ginstall -d $(DESTDIR)$(docdir)/corkscrew
	ginstall $(WORKSRC)/README $(DESTDIR)$(docdir)/corkscrew
	@$(MAKECOOKIE)
