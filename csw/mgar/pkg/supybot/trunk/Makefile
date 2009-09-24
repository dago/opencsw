# TODO
# - Check whether additional dependencies are needed
GARNAME = supybot
GARVERSION = 0.83.4.1
CATEGORIES = python

DESCRIPTION = Robust, user-friendly, and extensible IRC bot
define BLURB
endef

MASTER_SITES = $(SF_MIRRORS)
DISTNAME = Supybot-$(GARVERSION)
DISTFILES = $(DISTNAME).tar.gz

EXTRA_PAX_ARGS = '-s,ChangeLog$$,changelog,p'
TEST_SCRIPTS = 

include gar/category.mk

post-install-modulated: DOCDEST=$(DESTDIR)$(docdir)/$(CATALOGNAME)
post-install-modulated: DOCS=ChangeLog ACKS
post-install-modulated:
	ginstall -d $(DOCDEST)
	cp $(FILEDIR)/changelog.CSW $(DOCDEST)
	cp $(addprefix $(WORKSRC)/, $(DOCS)) $(DOCDEST)	
	@$(MAKECOOKIE)
