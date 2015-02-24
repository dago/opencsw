NAME = ratom
VERSION = 0.6.7
CATEGORIES = rbgems
GARTYPE = v2

DESCRIPTION = RAtom is a library for working with the Atom Syndication Format and the Atom Publishing Protocol

define BLURB
rAtom was originally built to support the communication between a number of applications built by Peerworks, via the Atom Publishing protocol. However, it supports, or aims to support, all the Atom Syndication Format and Publication Protocol and can be used to access Atom feeds or to script publishing entries to a blog supporting APP.
endef

GEM_DEPS = CSWrb18-libxml-1-1-4
GEM_DEPS =

LICENSE = LICENSE

ARCHALL = 1

RUNTIME_DEP_PKGS_CSWrb18-ratom-0-6-7 = $(GEM_DEPS)

include gar/category.mk

post-merge:
	@rm $(PKGROOT)$(libdir)/ruby/gems/1.8/gems/$(DISTNAME)/.gitignore
	@$(MAKECOOKIE)
