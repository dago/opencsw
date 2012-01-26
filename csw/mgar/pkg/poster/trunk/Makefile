NAME = poster
VERSION = 20050907
CATEGORIES = apps
GARTYPE = v2

DESCRIPTION = Create large posters out of PostScript pages
define BLURB
  Poster takes a one-page PostScript file and scales it to a specified
  size. It can tile the resulting image into multiple smaller pages that
  can be pasted together to form the big poster. Poster prefers EPS as its
  input although freer forms of PostScript are also understood. 
endef

VENDOR_URL   = http://packages.debian.org/lenny/poster
MASTER_SITES = http://ftp.debian.org/debian/pool/main/p/poster/
DISTFILES    = $(NAME)_$(VERSION).orig.tar.gz
UFILES_REGEX = $(NAME)_(\d+(?:\.\d+)*).orig.tar.gz

# Trivial build w/o configure and test
CONFIGURE_SCRIPTS =
TEST_SCRIPTS      = 
INSTALL_SCRIPTS   = custom

include gar/category.mk

# Get rid of gcc'isms
pre-build-modulated:
	gsed -i \
		-e '/^CFLAGS/d' \
		-e 's/gcc/$$(CC)/' \
		$(WORKSRC)/Makefile
	@$(MAKECOOKIE)

install-custom:
	ginstall -Dm755 $(WORKSRC)/poster $(DESTDIR)$(bindir)/poster
	ginstall -Dm755 $(WORKSRC)/poster.1 $(DESTDIR)$(mandir)/man1/poster.1
	@$(MAKECOOKIE)

# Instsall changelog.CSW
post-merge: $(foreach P,$(_PKG_SPECS),install-changelog-$P)

install-changelog-%:
	ginstall -D $(FILEDIR)/changelog.CSW \
		$(PKGROOT)$(docdir)/$(call catalogname,$*)/changelog.CSW
	@$(MAKECOOKIE)
