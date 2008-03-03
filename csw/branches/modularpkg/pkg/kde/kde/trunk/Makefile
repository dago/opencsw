GARNAME = kde
CATEGORIES = kde

DESCRIPTION = The K Desktop Environment (KDE) (gcc3)
define BLURB
  LONG DESCRIPTION
endef

PKGDIST    =
DISTFILES += $(call admfiles,CSWkdegcc,depend)
DISTFILES += $(call admfiles,CSWkdegccdtlogin,)

DEPENDS += lib/qt-gcc kde/arts
DEPENDS += kde/kdelibs kde/kdebase kde/kdeutils kde/kdenetwork kde/kdeadmin
DEPENDS += kde/kdegraphics kde/kdeartwork kde/kdemultimedia kde/kdeaddons
DEPENDS += kde/kdetoys kde/kdeedu kde/kdegames
DEPENDS += kde/kdepim
#DEPENDS += kde/koffice kde/kdevelop kde/kdewebdev kde/quanta

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk
