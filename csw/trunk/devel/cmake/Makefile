GARNAME = cmake
GARVERSION = 2.4.6
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
DISTFILES += $(call admfiles,CSWcmake)

datadir = /share/$(GARNAME)-$(GARVERSION)
sharedstatedir = /share
docdir = /share/doc/$(GARNAME)-$(GARVERSION)

CONFIGURE_ARGS = $(DIRPATHS) --docdir=$(docdir)

include ../category.mk

pre-configure:
	@echo $(DIRPATHS)
	@echo "Docdir: $(docdir)"
	(cd $(WORKSRC); ./bootstrap	\
		-parallel=4		\
		--prefix=$(prefix)	\
		--datadir=$(datadir)	\
		--docdir=$(docdir)	\
		--mandir=/man		\
	)
	@$(MAKECOOKIE)
