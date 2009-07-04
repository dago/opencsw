GARNAME = nano
GARVERSION = 2.0.9
CATEGORIES = utils

DESCRIPTION = Enhanced clone of the Pico text editor
define BLURB
  GNU nano is designed to be a free replacement for the Pico text editor,
  part of the Pine email suite from The University of Washington. It aims
  to "emulate Pico as closely as possible and perhaps include extra
  functionality".
endef

MASTER_SITES = http://www.nano-editor.org/dist/v2.0/
SPKG_SOURCEURL = http://www.nano-editor.org/
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += CSWnano.postinstall CSWnano.postremove

UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

REQUIRED_PKGS = CSWggettextrt CSWncurses

EXTRA_INC = /opt/csw/include/ncurses

TEST_SCRIPTS =

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --enable-all 

# Disable automatic line wraps when running as root. See 
# http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=513443 for 
# some background info
CONFIGURE_ARGS += --disable-wrapping-as-root

include gar/category.mk

post-install-modulated: DOCS=AUTHORS THANKS UPGRADE
post-install-modulated: DOCDEST=$(DESTDIR)$(docdir)/$(GARNAME)
post-install-modulated:
	ginstall -d $(DOCDEST)/examples
	cp $(FILEDIR)/changelog.CSW $(DOCDEST)
	cp $(WORKSRC)/doc/nanorc.sample $(DOCDEST)/examples
	cp $(addprefix $(WORKSRC)/, $(DOCS)) $(DOCDEST)
	perl -pi -e 's|/usr/share/doc|$(docdir)|' \
		$(addprefix $(DESTDIR)$(mandir)/, \
			man1/nano.1 \
			man5/nanorc.5 \
			fr/man1/nano.1 \
			fr/man5/nanorc.5 \
		)
	@$(MAKECOOKIE)
