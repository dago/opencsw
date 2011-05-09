NAME = scala
VERSION = 2.8.1
CATEGORIES = java

DESCRIPTION = The Scala programming language
define BLURB
  Scala is a general purpose programming language designed to express
  common programming patterns in a concise, elegant, and type-safe way. It
  smoothly integrates features of object-oriented and functional
  languages. It is also fully interoperable with Java.
endef

MASTER_SITES = http://www.scala-lang.org/downloads/distrib/files/
DISTFILES  = $(NAME)-$(VERSION).final.tgz
DISTNAME = $(NAME)-$(VERSION).final

SPKG_SOURCEURL = http://www.scala-lang.org/
ARCHALL = 1

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).final.tgz
UPSTREAM_MASTER_SITES = http://www.scala-lang.org/downloads

BUILD_SCRIPTS =
CONFIGURE_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

PRESERVECONF = .*/meta/[^/]+ .*/config/[^/]+

CHECKPKG_OVERRIDES_CSWscala += file-with-bad-content|/usr/share|root/opt/csw/share/scala/misc/scala-tool-support/scite/README
CHECKPKG_OVERRIDES_CSWscala += file-with-bad-content|/usr/share|root/opt/csw/share/scala/misc/scala-tool-support/kate/README
CHECKPKG_OVERRIDES_CSWscala += file-with-bad-content|/usr/share|root/opt/csw/share/scala/misc/scala-tool-support/gedit/README
CHECKPKG_OVERRIDES_CSWscala += file-with-bad-content|/usr/share|root/opt/csw/share/scala/misc/scala-tool-support/a2ps/README
CHECKPKG_OVERRIDES_CSWscala += file-with-bad-content|/usr/local|root/opt/csw/share/scala/misc/scala-tool-support/jedit/console/commando/scala.xml
CHECKPKG_OVERRIDES_CSWscala += file-with-bad-content|/usr/local|root/opt/csw/share/scala/misc/scala-tool-support/jedit/console/commando/scalac.xml
CHECKPKG_OVERRIDES_CSWscala += file-with-bad-content|/usr/local|root/opt/csw/share/man/man1/scala.1
CHECKPKG_OVERRIDES_CSWscala += file-with-bad-content|/usr/local|root/opt/csw/share/man/man1/scalac.1
CHECKPKG_OVERRIDES_CSWscala += file-with-bad-content|/usr/share|root/opt/csw/share/scala/misc/scala-tool-support/gedit/scala.lang
CHECKPKG_OVERRIDES_CSWscala += missing-dependency|CSWemacscommon

include gar/category.mk

install-dirs: 
	@ginstall -d $(DESTDIR)$(datadir)/vim/vimfiles
	@ginstall -d $(DESTDIR)$(datadir)/$(NAME)/config
	@ginstall -d $(DESTDIR)$(datadir)/$(NAME)/bin
	@ginstall -d $(DESTDIR)$(docdir)/$(NAME)
	@ginstall -d $(DESTDIR)$(mandir)
	@ginstall -d $(DESTDIR)$(bindir)
	$(MAKECOOKIE)

# Binaries go to /opt/csw/share/scala/bin and are then linked to /opt/csw/bin
# XXX: Where did you source the $(FILEDIR) binaries?
install-bin: SCALA_LINKS = scalac fsc scaladoc sbaz
install-bin:
	@ginstall -m 0755 $(FILEDIR)/scala.csw $(DESTDIR)$(datadir)/scala/bin/scala
	@cd $(DESTDIR)$(datadir)/scala/bin; \
		$(foreach L,$(SCALA_LINKS), ln scala $(L);)
	@ginstall -m 0755 $(WORKSRC)/bin/sbaz-setup $(DESTDIR)$(datadir)/scala/bin
	@cd $(DESTDIR)$(bindir); for i in ../share/scala/bin/*; do ln -s $$i; done
	@rm -rf $(WORKSRC)/bin
	$(MAKECOOKIE)

# Most of the installation goes to /opt/csw/share/scala
install-data:
	@mv $(WORKSRC)/misc/scala-tool-support/vim/syntax \
		$(WORKSRC)/misc/scala-tool-support/vim/indent \
		$(WORKSRC)/misc/scala-tool-support/vim/ftdetect \
		$(DESTDIR)$(datadir)/vim
	@rm -rf $(WORKSRC)/misc/scala-tool-support/vim
	@rm -rf \
		$(WORKSRC)/misc/scala-tool-support/notepad-plus \
		$(WORKSRC)/misc/scala-tool-support/subethaedit \
		$(WORKSRC)/misc/scala-tool-support/textmate \
		$(WORKSRC)/misc/scala-tool-support/xcode \
		$(WORKSRC)/misc/scala-tool-support/textwrangler

	@mv $(WORKSRC)/man/man1 $(DESTDIR)$(mandir); rm -rf $(WORKSRC)/man
	@mv $(WORKSRC)/doc/* $(DESTDIR)$(docdir)/$(NAME); rm -rf $(WORKSRC)/doc
	@mv $(WORKSRC)/* $(DESTDIR)$(datadir)/$(NAME)
	@$(MAKECOOKIE)

install-config:
	@cp $(FILEDIR)/sbaz.properties \
		$(DESTDIR)$(datadir)/$(NAME)/config/sbaz.properties.CSW
	@$(foreach F,available description installed universe, \
		mv $(DESTDIR)$(datadir)/$(NAME)/meta/$(F) \
			$(DESTDIR)$(datadir)/$(NAME)/meta/$(F).CSW; )
	@$(MAKECOOKIE)

install-custom: install-dirs install-bin install-data install-config
	@$(MAKECOOKIE)
