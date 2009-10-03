GARNAME = supybot
GARVERSION = 0.83.4.1
CATEGORIES = python

DESCRIPTION = Robust, user-friendly, and extensible IRC bot
  Supybot is a robust (it doesn't crash), user friendly (it's easy to
  configure) and programmer friendly (plugins are *extremely* easy to
  write) Python IRC bot. It aims to be an adequate replacement for most
  existing IRC bots. It includes a very flexible and powerful ACL system
  for controlling access to commands, as well as more than 50 builtin
  plugins providing around 400 actual commands. 
endef

SPKG_SOURCEURL = http://sourceforge.net/projects/supybot/
MASTER_SITES = $(SF_MIRRORS)
DISTNAME = Supybot-$(GARVERSION)
DISTFILES = $(DISTNAME).tar.gz

REQUIRED_PKGS = CSWpysqlite CSWtwisted

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
