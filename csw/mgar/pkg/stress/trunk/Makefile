# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = stress
VERSION = 1.0.4
CATEGORIES = apps
GARTYPE = v2

DESCRIPTION = A deliberately simple workload generator for POSIX systems
define BLURB
  The tool started out as a very simple way to generate work on a
  computer. It has pretty much stayed as simple as reasonably possible. It
  is a single file called stress.c whose internal organization is in
  essence a loop that forks worker processes and then waits for them to
  either complete normally or exit with an error. It has been used in a
  lot of product development labs as well as in research projects. 
endef

MASTER_SITES = http://weather.ou.edu/~apw/projects/stress/
DISTFILES    = $(NAME)-$(VERSION).tar.gz
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

# Install changelog.CSW
post-merge: $(foreach P,$(_PKG_SPECS),install-changelog-$P)
install-changelog-%:
	ginstall -D $(FILEDIR)/changelog.CSW \
		$(PKGROOT)$(docdir)/$(call catalogname,$*)/changelog.CSW
	@$(MAKECOOKIE)
