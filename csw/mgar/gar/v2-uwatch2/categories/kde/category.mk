
# KDE
KDE_ROOT      = http://download.kde.org
KDE_VERSION   = 3.5.10
KDE_DIST      = stable
KDE_MIRROR    = $(KDE_ROOT)/$(KDE_DIST)/$(KDE_VERSION)/src/

MASTER_SITES ?= $(KDE_MIRROR)
VERSION   ?= $(KDE_VERSION)
PKGDIST      ?= $(NAME)-$(VERSION).tar.bz2
DISTFILES    += $(PKGDIST)

# Compiler
GARCOMPILER = GNU

include gar/gar.mk
