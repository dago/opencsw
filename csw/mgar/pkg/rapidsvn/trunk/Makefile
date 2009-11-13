GARNAME = rapidsvn
GARVERSION = 0.12.0-1
CATEGORIES = utils

DESCRIPTION = GUI front-end for the Subversion revision system
define BLURB
  This is the developer site for RapidSVN. You have access to the source code
  of RapidSVN, the issue tracker and the mailing lists. If you are a user of
  RapidSVN you might want to take a look at http://www.rapidsvn.org where we
  are working on the Documentation and Online Help of RapidSVN
endef

MASTER_SITES = http://www.rapidsvn.org/download/release/0.12/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
# DISTFILES += $(call admfiles,CSWrapidsvn,depend prototype)
# DISTFILES += $(call admfiles,CSWsvncpp,depend prototype)

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

SPKG_SOURCEURL = http://rapidsvn.tigris.org/

# RapidSVN 0.9.1 omits the manpage from the dist archive
# DISTFILES += rapidsvn.xml

# Remove gcc C/CXXFLAGS, and fix autoconf tests
# PATCHFILES += configure.diff

# This should be separated out of CSWkdelibsgcc
# KSGML = $(prefix)/kde-gcc/share/apps/ksgmltools2
# DOCBOOK_MANPAGE = $(KSGML)/docbook/xsl/manpages/docbook.xsl

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-apr-config=$(prefix)/apache2/bin/apr-1-config
CONFIGURE_ARGS += --with-apu-config=$(prefix)/apache2/bin/apu-1-config
CONFIGURE_ARGS += --with-svn-lib=$(libdir)/svn
CONFIGURE_ARGS += --with-svn-include=$(includedir)
# CONFIGURE_ARGS += --with-docbook-xsl-manpages=$(DOCBOOK_MANPAGE)

# EXTRA_LIB = $(prefix)/bdb43/lib $(SVNLIB)
# EXTRA_INC = $(prefix)/bdb43/include

TEST_TARGET = check

include gar/category.mk

# pre-configure:
# 	@echo " ==> Regenerating build tools..."
# 	@(cd $(WORKSRC) ; \
# 		aclocal                       && \
# 		autoconf                      && \
# 		libtoolize --automake --force && \
# 		aclocal                       && \
# 		automake -a )
# 	@$(MAKECOOKIE)

# pre-build:
# 	@cp $(WORKDIR)/rapidsvn.xml $(WORKSRC)/doc/manpage

# post-install:
# 	install -d $(DESTDIR)$(mandir)/man1
# 	( cd $(WORKSRC)/doc/manpage ; make manpage-yes )
# 	install $(WORKSRC)/doc/manpage/rapidsvn.1 $(DESTDIR)$(mandir)/man1
# 	@$(MAKECOOKIE)

