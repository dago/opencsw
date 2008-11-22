GARNAME = rapidsvn
GARVERSION = 0.9.1
CATEGORIES = utils

DESCRIPTION = Subversion GUI
define BLURB
  # TODO: Insert Blurb
endef

MASTER_SITES = http://www.rapidsvn.org/download/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWrapidsvn,depend prototype)
DISTFILES += $(call admfiles,CSWsvncpp,depend prototype)

# RapidSVN 0.9.1 omits the manpage from the dist archive
DISTFILES += rapidsvn.xml

# Remove gcc C/CXXFLAGS, and fix autoconf tests
PATCHFILES += configure.diff

# This should be separated out of CSWkdelibsgcc
KSGML = $(prefix)/kde-gcc/share/apps/ksgmltools2
DOCBOOK_MANPAGE = $(KSGML)/docbook/xsl/manpages/docbook.xsl

SVNLIB = $(prefix)/lib/svn

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-apr-config=$(prefix)/apache2/bin/apr-1-config
CONFIGURE_ARGS += --with-apu-config=$(prefix)/apache2/bin/apu-1-config
CONFIGURE_ARGS += --with-svn-lib=$(SVNLIB)
CONFIGURE_ARGS += --with-svn-include=$(includedir)
CONFIGURE_ARGS += --with-docbook-xsl-manpages=$(DOCBOOK_MANPAGE)

EXTRA_LIB = $(prefix)/bdb43/lib $(SVNLIB)
EXTRA_INC = $(prefix)/bdb43/include

TEST_TARGET = check

include ../category.mk

pre-configure:
	@echo " ==> Regenerating build tools..."
	@(cd $(WORKSRC) ; \
		aclocal                       && \
		autoconf                      && \
		libtoolize --automake --force && \
		aclocal                       && \
		automake -a )
	@$(MAKECOOKIE)

pre-build:
	@cp $(WORKDIR)/rapidsvn.xml $(WORKSRC)/doc/manpage

post-install:
	install -d $(DESTDIR)$(mandir)/man1
	( cd $(WORKSRC)/doc/manpage ; make manpage-yes )
	install $(WORKSRC)/doc/manpage/rapidsvn.1 $(DESTDIR)$(mandir)/man1
	@$(MAKECOOKIE)

