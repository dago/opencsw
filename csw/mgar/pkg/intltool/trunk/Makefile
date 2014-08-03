# $Id$

NAME = intltool
MAJOR_VER = 0.50
MINOR_VER = 2
VERSION = $(MAJOR_VER).$(MINOR_VER)
GNOME_SUBV = $(MAJOR_VER)
CATEGORIES = utils
GARTYPE = v2
ARCHALL_CSWintltool = 1

DESCRIPTION =  A collection of tools for internationaliz	The intltool package is a set of tools for translating the contents of data
	e contents of data files using the gettext translation framework.
endhttps://launchpad.net/$(NAME)/trunk/$(VERSION)/+download/
DISTFILES  = $(DISTNAMEAME)-(\d+(PACKAGING_PLATFORMS = solaris9-sparc solaris9-i386

RUNTIME_DEP_PKGS_CSWintltool  = CSWperl
RUNTIME_DEP_PKGS_CSWintltool += CSWpm-xml-parser

CONFIGURE_ARGS = $(DIRPATHS)

CHECKPKG_OVERRIDES_CSWintltool += surplus-dependency|CSWpm-xml-parser
CHECKPKG_OVERRIDES_CSWintltool += surplus-dependency|CSWperl

include gar/category.mk
