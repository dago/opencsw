NAME = duplicity
VERSION = 0.6.08b
CATEGORIES = python
GARTYPE = v2

DESCRIPTION = Encrypted bandwidth-efficient backup using the rsync algorithm
define BLURB
  Duplicity backs directories by producing encrypted tar-format volumes
  and uploading them to a remote or local file server. Because duplicity
  uses librsync, the incremental archives are space efficient and only
  record the parts of files that have changed since the last backup.
  Because duplicity uses GnuPG to encrypt and/or sign these archives, they
  will be safe from spying and/or modification by the server. 
endef

VENDOR_URL   = http://duplicity.nongnu.org/
MASTER_SITES = http://code.launchpad.net/duplicity/0.6-series/0.6.08b/+download/
DISTFILES    = $(NAME)-$(VERSION).tar.gz
# Couldn't find a parsable 'stable' releases page
# UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

RUNTIME_DEP_PKGS  = CSWpy-boto
RUNTIME_DEP_PKGS += CSWlibrsync
RUNTIME_DEP_PKGS += CSWgnupg
RUNTIME_DEP_PKGS += CSWncftp

TEST_SCRIPTS =
CONFIGURE_ARGS = $(DIRPATHS)

EXTRA_PAX_ARGS  = '-s,/doc/$(NAME)-$(VERSION),/doc/$(NAME),p'

CHECKPKG_OVERRIDES_CSWduplicity += pkgname-does-not-start-with-CSWpy-
CHECKPKG_OVERRIDES_CSWduplicity += catalogname-does-not-start-with-py_
CHECKPKG_OVERRIDES_CSWduplicity += surplus-dependency|CSWpy-boto
CHECKPKG_OVERRIDES_CSWduplicity += surplus-dependency|CSWgnupg
CHECKPKG_OVERRIDES_CSWduplicity += surplus-dependency|CSWncftp

include gar/category.mk

# Clean up the docdir a bit ... I wish pax wouldn't exit after the first match.
post-merge:
	( cd $(PKGROOT)$(docdir)/$(CATALOGNAME); \
		rm REPO-README COPYING tarfile-LICENSE; \
		mv CHANGELOG changelog; \
	)
	@$(MAKECOOKIE)
