NAME = supybot
VERSION = 0.83.4.1
CATEGORIES = python

DESCRIPTION = Robust, user-friendly, and extensible IRC bot
define BLURB
  Supybot is a robust (it doesn't crash), user friendly (it's easy to
  configure) and programmer friendly (plugins are *extremely* easy to
  write) Python IRC bot. It aims to be an adequate replacement for most
  existing IRC bots. It includes a very flexible and powerful ACL system
  for controlling access to commands, as well as more than 50 builtin
  plugins providing around 400 actual commands. 
endef

VENDOR_URL   = http://supybot.com/
MASTER_SITES = $(SF_MIRRORS)
DISTFILES    = $(DISTNAME).tar.gz
DISTNAME     = Supybot-$(VERSION)

ARCHALL = 1
RUNTIME_DEP_PKGS = CSWpysqlite CSWtwisted

EXTRA_PAX_ARGS = '-s,ChangeLog$$,changelog,p'
TEST_SCRIPTS = 

include gar/category.mk

post-install-modulated: DOCDEST=$(DESTDIR)$(docdir)/$(NAME)
post-install-modulated: DOCS=ChangeLog ACKS docs/*
post-install-modulated: MANDEST=$(DESTDIR)$(mandir)/man1
post-install-modulated:
	ginstall -d $(DOCDEST)
	-cp $(addprefix $(WORKSRC)/, $(DOCS)) $(DOCDEST)	
	ginstall -d $(MANDEST) && cp $(WORKSRC)/docs/man/* $(MANDEST)
	@$(MAKECOOKIE)

# Install changelog.CSW
post-merge: $(foreach P,$(_PKG_SPECS),install-changelog-$P)
install-changelog-%:
	ginstall -D $(FILEDIR)/changelog.CSW \
		$(PKGROOT)$(docdir)/$(call catalogname,$*)/changelog.CSW
	@$(MAKECOOKIE)
