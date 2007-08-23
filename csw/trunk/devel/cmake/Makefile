GARNAME = cmake
GARVERSION = 2.4.7
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

MASTER_SITES = http://www.cmake.org/files/v2.4/
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWcmake,prototype)

datadir = /share/$(GARNAME)-$(GARVERSION)
sharedstatedir = /share
docdir = /share/doc/$(GARNAME)-$(GARVERSION)

CONFIGURE_ARGS = $(DIRPATHS) --docdir=$(docdir)

include ../category.mk

FIXCONFIG_DIRS += $(DESTDIR)$(prefix)/share/$(GARNAME)-$(GARVERSION)/Modules
FIXCONFIG_DIRS += $(DESTDIR)$(prefix)/share/$(GARNAME)-$(GARVERSION)/Templates
FIXCONFIG_DIRS += $(DESTDIR)$(prefix)$(docdir)
FIXCONFIG_DIRS += $(DESTDIR)$(prefix)/share/man/man1

pre-configure:
	@echo $(DIRPATHS)
	@echo "Docdir: $(docdir)"
	(cd $(WORKSRC); CFLAGS="$(CFLAGS)" CXXFLAGS="$(CXXFLAGS)" ./bootstrap	\
		--prefix=$(prefix)	\
		--datadir=$(datadir)	\
		--docdir=$(docdir)	\
		--mandir=/man		\
	)
	@$(MAKECOOKIE)
