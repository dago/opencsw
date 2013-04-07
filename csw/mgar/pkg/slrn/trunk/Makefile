NAME = slrn
VERSION = 1.0.1
GARTYPE = v2

DESCRIPTION = C

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
DISTFILES  = $(NAMEgzprototype depend)

# We define upstream file regex so we can be notifed of new upstream software release
UPSTREAM_MASTER_SITES = $(SF_PROJECT_SHOWFILE)=7768
UPSTREAM_USE_SF = 1
UFILES_REGEX = $(NAME)-((\d+(?:\
CHECKPKG_OVERRIDES_CSWslrn += file-with-bad-content|/usr/local|root/opt/csw/share/doc/slrn/FAQ
CHECKPKG_OVERRIDES_CSWslrn += file-with-bad-content|/usr/local|root/opt/csw/share/doc/slrn/README.multiuser
CHECKPKG_OVERRIDES_CSWslrn += file-with-bad-content|/usr/local|root/opt/csw/share/doc/slrn/score.txt
CHECKPKG_OVERRIDES_CSWslrn += file-with-bad-content|/usr/local|root/opt/csw/share/doc/slrn/changes.txt
CHECKPKG_OVERRIDES_CSWslrn += file-with-bad-content|/usr/local|root/opt/csw/share/doc/slrn/manual.txt
CHECKPKG_OVERRIDES_CSWslrn += file-with-bad-content|/usr/local|root/opt/csw/share/doc/slrn/README.SSL
CHECKPKG_OVERRIDES_CSWslrn += file-with-bad-content|/usr/local|root/opt/csw/share/man/man1/slrn.1
CHECKPKG_OVERRIDES_CSWslrn += file-with-bad-content|/usr/local|root/opt/csw/share/slrn/slang/mailcap.sl
CHECKPKG_OVERRIDES_CSWslrn += file-with-bad-content|/usr/share|root/opt/csw/share/doc/slrn/FAQ
CHECKPKG_OVERRIDES_CSWslrn += file-with-bad-content|/usr/share|root/opt/csw/share/doc/slrn/changes.txt
CHECKPKG_OVERRIDES_CSWslrn += file-with-bad-content|/usr/share|root/opt/csw/share/doc/slrn/manual.txt

RUNTIME_DEP_PKGS = CSWlibintl8 CSWlibslang2 CSWlibiconv2 CSWlibssl1-0-0ST -R/opt/csw/lib

CONFIGURE_ARGS = $(DIRPATHS) --with-ssl=/opt/csw
CONFIGURE_ARGS += --with-slang-library=/opt/csw/lib --with-slrnpull
CONFIGURE_ARGS += --enable-setgid-code --enable-spool
CONFIGURE_ARGS += --with-mta=/usr/lib/sendmail --enable-hardcode-libs

INSTALl install-contrib

# slrn doesn't have a test target
TEST_TARGET =

# The homepage to show in pkginfo shouldn't be SourceForge
SPKG_SOURCEURL = http://www.slrn.org/

include gar/category.mk

#post-install:
#	(cd $(WORKSRC); make 