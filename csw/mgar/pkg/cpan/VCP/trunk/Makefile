NAME = VCP
DISTVERSION = 0.9-20050110
VERSION = $(subst -,.,$(DISTVERSION))
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = AUTRIJUS

DESCRIPTION = svk destination driver
define BLURB
	This driver allows vcp to insert revisions in to a Subversion repository via
	the svk interface. You could use the vcp command line interface or the
	integrated SVK mirror command.
endef

DISTFILES = $(call admfiles,CSWpmvcp,depend prototype)
MODDISTP  = $(NAME)-autrijus-snapshot-$(DISTVERSION)
MODDIST   = $(MODDISTP).tar.gz
WORKSRC   = $(WORKDIR)/$(MODDISTP)

UFILES_REGEX ?= $(NAME)-autrijus-snapshot-((\d+(?:\.\d+)*)(-\d+)?).tar.gz

DEPENDS += cpan/HTML-Tree
DEPENDS += cpan/IPC-Run3
DEPENDS += cpan/PodToHTML
DEPENDS += cpan/Regexp-Shellish
DEPENDS += cpan/Text-Diff
DEPENDS += cpan/XML-AutoWriter
DEPENDS += cpan/XML-Parser

include gar/category.mk
