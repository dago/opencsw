GARNAME = slrn
GARVERSION = 0.9.8.1
CATEGORIES = net

DESCRIPTION = command-line news reader
define BLURB
  slrn (``s-lang read news'') is a newsreader, i.e. a program that accesses
  a newsserver to read messages from the Internet News service (also known
  as ``Usenet''). It runs in console mode on various Unix-like systems
  (including Linux), 32-bit Windows, OS/2, BeOS, Mac OS X and VMS. Beside
  the usual features of a newsreader, slrn supports scoring rules to
  highlight, sort or kill articles based on information from their header.
  It is highly customizable, allows free key-bindings and can easily be
  extended using the sophisticated s-lang macro language.
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
DISTFILES += $(call admfiles,CSWslrn,prototype depend)

LD_OPTIONS = -R/opt/csw/lib/\$$ISALIST -R/opt/csw/lib

CONFIGURE_ARGS = $(DIRPATHS) --with-ssl=/opt/csw
CONFIGURE_ARGS += --with-slang-library=/opt/csw/lib --with-slrnpull
CONFIGURE_ARGS += --enable-setgid-code --enable-spool
CONFIGURE_ARGS += --with-mta=/usr/lib/sendmail --enable-hardcode-libs

INSTALL_ARGS = install install-contrib

# slrn doesn't have a test target
TEST_TARGET =

# The homepage to show in pkginfo shouldn't be SourceForge
SPKG_SOURCEURL = http://www.slrn.org/

include gar/category.mk

#post-install:
#	(cd $(WORKSRC); make install-contrib)
