GARNAME = rapidsvn
GARVERSION = 0.9.0
CATEGORIES = utils

DESCRIPTION = Subversion GUI
define BLURB
  # TODO: Insert Blurb
endef

MASTER_SITES = http://www.rapidsvn.org/download/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWrapidsvn,depend prototype)
DISTFILES += $(call admfiles,CSWsvncpp,depend prototype)

# Don't hardcode antisocial CFLAGS/CXXFLAGS!
PATCHFILES += flags.diff

# no generated Makefile in manpage dir, so install it manually
PATCHFILES += manpage.diff

SVNLIB = $(prefix)/lib/svn

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-apr-config=$(prefix)/apache2/bin/apr-1-config
CONFIGURE_ARGS += --with-apu-config=$(prefix)/apache2/bin/apu-1-config
CONFIGURE_ARGS += --with-svn-lib=$(SVNLIB)
CONFIGURE_ARGS += --with-svn-include=$(includedir)

EXTRA_LIB = $(prefix)/bdb4/lib $(SVNLIB)
EXTRA_INC = $(prefix)/bdb4/include

TEST_TARGET = check

include ../category.mk

# Libdir is a bit non-standard
#LDFLAGS += -L$(DESTDIR)$(prefix)/lib/svn

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
	@echo " ==> Compensating for NEONLIBS + CC.."
	@( cd $(WORKSRC) ; \
		gsed -i.bak -e 's/-fast -xarch=v8 -xstrconst -xildoff/$(OPTFLAGS)/g' \
			Makefile src/Makefile )
	@$(MAKECOOKIE)

post-install:
	@install -d $(DESTDIR)$(mandir)/man1
	@install $(WORKSRC)/doc/manpage/rapidsvn.1 $(DESTDIR)$(mandir)/man1

