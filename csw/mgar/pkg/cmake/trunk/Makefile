GARNAME = cmake
GARVERSION = 2.6.2
CATEGORIES = devel

DESCRIPTION = Cross-platform make
define BLURB
  CMake is used to control the software compilation process using simple
  platform and compiler independent configuration files. CMake generates
  native makefiles and workspaces that can be used in the compiler environment
  of your choice. CMake is quite sophisticated: it is possible to support
  complex environments requiring system configuration, pre-processor
  generation, code generation, and template instantiation. 
endef

MASTER_SITES = http://www.cmake.org/files/v2.6/
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWcmake)

datadir = /share/$(GARNAME)-$(GARVERSION)
sharedstatedir = /share
docdir = /share/doc/$(GARNAME)-$(GARVERSION)

CONFIGURE_ARGS = $(DIRPATHS) --docdir=$(docdir)

SKIPTEST = 1

include gar/category.mk

FIXCONFIG_DIRS += $(DESTDIR)$(prefix)/share/$(GARNAME)-$(GARVERSION)/Modules
FIXCONFIG_DIRS += $(DESTDIR)$(prefix)/share/$(GARNAME)-$(GARVERSION)/Templates
FIXCONFIG_DIRS += $(DESTDIR)$(prefix)$(docdir)
FIXCONFIG_DIRS += $(DESTDIR)$(prefix)/share/man/man1

pre-configure:
	@echo $(DIRPATHS)
	@echo "Docdir: $(docdir)"
	# Do NOT include the CSW include pathes here
	(cd $(WORKSRC); /usr/bin/env \
		CFLAGS="$($(GARCOMPILER)_CC_$(GARFLAVOR))" \
		CXXFLAGS="$($(GARCOMPILER)_CXX_$(GARFLAVOR))" \
		./bootstrap \
		--prefix=$(prefix)	\
		--datadir=$(datadir)	\
		--docdir=$(docdir)	\
		--mandir=/man		\
	)
	@$(MAKECOOKIE)
