# $Id: Makefile 13420 2011-02-20 21:04:03Z bdwalton $
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = which
VERSION = 2.20
GARTYPE = v2

DESCRIPTION = Utility used to find which executable is executed when entered on the shell prompt.s pathname or alias
define BLURB
  GNU which - is a utility that is used to find which executable (or alias or shell function) is executed when entered .
endef

MASTER_SITES = http://ftp.gnu.org/gnu/which/
DISTFILES  = $(DISTNAME).tar.gz

VENDOR_URL = http://savannah.gnu.org/projects/which/

GARCOMPILER = GCC4

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --program-prefix=g

include gar/category.mk

post-install-modulated:
	ginstall -d $(DESTDIR)$(prefix)/gnu
	$(foreach G,$(notdir $(wildcard $(DESTDIR)$(bindir)/*)),ln -s ../bin/$G $(DESTDIR)$(prefix)/gnu/$(patsubst g%,%,$G);)
	@$(MAKECOOKIE)

