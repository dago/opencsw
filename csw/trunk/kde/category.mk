
MASTER_SITES ?= $(KDE_MIRROR)
PKGDIST      ?= $(GARNAME)-$(GARVERSION).tar.bz2
DISTFILES    += $(PKGDIST)

# Compiler
GARCOMPILER = GNU

include ../../gar.mk
