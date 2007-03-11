GARNAME = rlwrap
GARVERSION = 0.28
CATEGORIES = utils

DESCRIPTION = A readline wrapper
define BLURB
  rlwrap is a readline wrapper, a small utility that uses the GNU readline library to allow the editing of keyboard input for any other command. It maintains a separate input history for each command, and can TAB-expand words using all previously seen words and/or a user-specified file.
endef

MASTER_SITES = http://utopia.knoware.nl/~hlub/uck/rlwrap/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWrlwrap,depend prototpe)
DISTFILES += changelog.CSW

CONFIGURE_ARGS = $(DIRPATHS)

include ../category.mk

post-install:
	        @ginstall -D $(WORKDIR)/changelog.CSW $(DESTDIR)$(docdir)/$(GARNAME)/changelog.CSW
	        @( for FILE in AUTHORS BUGS INSTALL NEWS README TODO; do \
	                 ginstall -D $(WORKSRC)/$$FILE $(DESTDIR)$(docdir)/$(GARNAME)/`basename $$FILE`; \
	         done )
