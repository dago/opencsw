GARNAME = indent
GARVERSION = 2.2.10
CATEGORIES = utils

DESCRIPTION = C language source code formatting program 
define BLURB
  The indent program can be used to make code easier to read. It can also convert
  from one style of writing C to another. indent understands a substantial amount
  about the syntax of C, but it also attempts to cope with incomplete and
  misformed syntax. 
endef

MASTER_SITES = $(GNU_MIRROR)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

# texinfo2man doesn't belong in the package
EXTRA_MERGE_EXCLUDE_FILES = /opt/csw/bin/texinfo2man

TEST_SCRIPTS =
CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

# Cosmetic stuff: 
# Get rid of the -R options derived by autoconfs "checking how to link with"
post-configure-modulated:
	perl -pi -e 's|-R/opt/csw/lib||' \
		$(WORKSRC)/Makefile $(WORKSRC)/src/Makefile
	@$(MAKECOOKIE)

# indent.1 (man page) comes with the tarball and is not a phony target
# As we don't want an empty man page, delete it to have it generated correctly
pre-build-modulated:
	rm $(WORKSRC)/man/indent.1
	@$(MAKECOOKIE)

post-install-modulated: DOCDEST=$(DESTDIR)$(docdir)/$(GARNAME)
post-install-modulated:
	@ginstall -d $(DOCDEST)
	@cp $(FILEDIR)/changelog.CSW $(DOCDEST)
	@$(MAKECOOKIE)
