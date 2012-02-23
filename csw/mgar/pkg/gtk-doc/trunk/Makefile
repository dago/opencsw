NAME = gtk-doc
VERSION = 1.18
CATEGORIES = gnome
GARTYPE = v2

DESCRIPTION = GTK-Doc is used to document C code.
define BLURB
	GTK-Doc is used to document C code. It is typically used to document the
	public API of libraries, such as the GTK+ and GNOME libraries. But it can
	also be used to document application code. 
endef

MASTER_SITES = $(GNOME_MIRROR)
DISTFILES += $(DISTNAME).tar.xz
DISTFILES += CSWgtk-doc.postinstall
DISTFILES += CSWgtk-doc.postremove

BUILD_DEP_PKGS += CSWsgmlcommon
BUILD_DEP_PKGS += CSWxmlcommon
BUILD_DEP_PKGS += CSWdocbookxsl
BUILD_DEP_PKGS += CSWopenjade
BUILD_DEP_PKGS += CSWgnomedocutils
BUILD_DEP_PKGS += CSWpy-libxml2

RUNTIME_DEP_PKGS += CSWperl
RUNTIME_DEP_PKGS += CSWpython
RUNTIME_DEP_PKGS += CSWsgmlcommon
RUNTIME_DEP_PKGS += CSWxmlcommon
RUNTIME_DEP_PKGS += CSWdocbookxsl
RUNTIME_DEP_PKGS += CSWopenjade
RUNTIME_DEP_PKGS += CSWgnomedocutils

# The dependencies can not be detected by checkpkg
CHECKPKG_OVERRIDES_CSWgtk-doc += surplus-dependency|CSWpython
CHECKPKG_OVERRIDES_CSWgtk-doc += surplus-dependency|CSWsgmlcommon
CHECKPKG_OVERRIDES_CSWgtk-doc += surplus-dependency|CSWxmlcommon
CHECKPKG_OVERRIDES_CSWgtk-doc += surplus-dependency|CSWdocbookxsl
CHECKPKG_OVERRIDES_CSWgtk-doc += surplus-dependency|CSWopenjade
CHECKPKG_OVERRIDES_CSWgtk-doc += surplus-dependency|CSWgnomedocutils

# These are just docs
CHECKPKG_OVERRIDES_CSWgtk-doc += file-with-bad-content|/usr/share|root/opt/csw/share/gnome/help/gtk-doc-manual/C/gtk-doc-manual.xml
CHECKPKG_OVERRIDES_CSWgtk-doc += file-with-bad-content|/usr/share|root/opt/csw/share/gnome/help/gtk-doc-manual/fr/gtk-doc-manual.xml
CHECKPKG_OVERRIDES_CSWgtk-doc += file-with-bad-content|/usr/share|root/opt/csw/share/gnome/help/gtk-doc-manual/bn_IN/gtk-doc-manual.xml
CHECKPKG_OVERRIDES_CSWgtk-doc += file-with-bad-content|/usr/share|root/opt/csw/share/gnome/help/gtk-doc-manual/gu/gtk-doc-manual.xml
CHECKPKG_OVERRIDES_CSWgtk-doc += file-with-bad-content|/usr/share|root/opt/csw/share/gnome/help/gtk-doc-manual/es/gtk-doc-manual.xml
CHECKPKG_OVERRIDES_CSWgtk-doc += file-with-bad-content|/usr/share|root/opt/csw/share/gnome/help/gtk-doc-manual/sl/gtk-doc-manual.xml
CHECKPKG_OVERRIDES_CSWgtk-doc += file-with-bad-content|/usr/share|root/opt/csw/share/gnome/help/gtk-doc-manual/ta/gtk-doc-manual.xml
CHECKPKG_OVERRIDES_CSWgtk-doc += file-with-bad-content|/usr/share|root/opt/csw/share/gnome/help/gtk-doc-manual/en_GB/gtk-doc-manual.xml
CHECKPKG_OVERRIDES_CSWgtk-doc += file-with-bad-content|/usr/share|root/opt/csw/share/gnome/help/gtk-doc-manual/el/gtk-doc-manual.xml
CHECKPKG_OVERRIDES_CSWgtk-doc += file-with-bad-content|/usr/share|root/opt/csw/share/gnome/help/gtk-doc-manual/de/gtk-doc-manual.xml
CHECKPKG_OVERRIDES_CSWgtk-doc += file-with-bad-content|/usr/share|root/opt/csw/share/gnome/help/gtk-doc-manual/sv/gtk-doc-manual.xml
CHECKPKG_OVERRIDES_CSWgtk-doc += file-with-bad-content|/usr/share|root/opt/csw/share/gnome/help/gtk-doc-manual/te/gtk-doc-manual.xml

ARCHALL = 1

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-xml-catalog=/etc/opt/csw/xml/catalog
CONFIGURE_ARGS += --disable-scrollkeeper

# xmllint test fail on buildfarm due to proxy requirement
# some other tests fail due to gtk-doc not installed (doh!)
SKIPTEST ?= 1

include gar/category.mk
