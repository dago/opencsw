GARNAME = openoffice
GARVERSION = 2.2.1
SRCNUM=680
MILESTONE=m18
CATEGORIES = apps

DESCRIPTION = An Open Source version of StarOffice.
define BLURB
	OpenOffice.org is the Open Source project through which Sun Microsystems is releasing the technology for the popular StarOffice productivity suite.
endef


MASTER_SITES = ftp://openoffice.cict.fr/openoffice/stable/$(GARVERSION)/
DISTFILES  = OOo_$(GARVERSION)_src_core.tar.bz2
DISTFILES += OOo_$(GARVERSION)_src_system.tar.bz2
DISTFILES += OOo_$(GARVERSION)_src_binfilter.tar.bz2
DISTFILES += OOo_$(GARVERSION)_src_l10n.tar.bz2

# Mozilla prebuild libraries 
DISTFILES += SOLARISC52Iinc SOLARISC52Ilib SOLARISC52Iruntime SOLARISC52Sinc SOLARISC52Slib SOLARISC52Sruntime

# Base packages
DISTFILES += $(call admfiles,CSWooocommon,prototype)
DISTFILES += $(call admfiles,CSWooocore,prototype)

# Localized packages 
OOO_LANGS = af bg ca cs cy da de el en-GB en-US es et fr gl hr hu it lt nb nl nn pl pt pt-BR sk sl sv zu
LANG_DISTFILES = $(call admfiles, CSWoooui$(shell echo $(lang) | tr '[A-Z]' '[a-z]' | tr -d '-'),prototype depend)
DISTFILES += $(foreach lang, $(OOO_LANGS), $(LANG_DISTFILES))

# This file add CSW paths to Openoffice Build environment variables
DISTFILES += SolarisCSWEnv.Set.sh

DISTNAME = OOF$(SRCNUM)_$(MILESTONE)


# Patches
#
# Fix a missing -lXt option when linking with libaudio
# and an incorrect libjpeg linking option
PATCHFILES = csw_build_env.patch

# Fix a missing X include in cairo_cairo.cxx
PATCHFILES += cairo_x_include.patch

# the round function is defined in C99 and is not available
# in solaris 8/9, this patch replace round (x) by floor (x+0.5)
PATCHFILES += no_round.patch

#####################################################################
# Configure parameters and build environment 
#####################################################################

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-ant-home=$(libdir)/ant/

CONFIGURE_ARGS += --enable-cairo
CONFIGURE_ARGS += --with-java=java
CONFIGURE_ARGS += --with-jdk-home=$(ls -1d /usr/jdk/j2sdk1.4.2_* | sort | tail -1)
CONFIGURE_ARGS += --with-lang="$(OOO_LANGS)"

# for now we disable some stuff to build successfully
# (will have to be enabled later)
CONFIGURE_ARGS += --disable-odk
#CONFIGURE_ARGS += --disable-mozilla
CONFIGURE_ARGS += --disable-build-mozilla
CONFIGURE_ARGS += --disable-pasf

# neon_devel not yet installed on isis
CONFIGURE_ARGS += --disable-neon

# configure needs some gnu tools
CONFIGURE_ARGS += --with-gnu-patch=/bin/gpatch
CONFIGURE_ARGS += --with-gnu-cp=$(bindir)/gcp

# We use csw libraries instead of 
CONFIGURE_ARGS += --with-system-libxml
CONFIGURE_ARGS += --with-system-python
CONFIGURE_ARGS += --with-system-zlib
CONFIGURE_ARGS += --with-system-jpeg
CONFIGURE_ARGS += --with-system-freetype
CONFIGURE_ARGS += --with-system-curl
CONFIGURE_ARGS += --with-system-expat
CONFIGURE_ARGS += --with-system-nas
# CSW icu is outdated for now
#CONFIGURE_ARGS += --with-system-icu

# we will create the package ourself
CONFIGURE_ARGS += --enable-epm
CONFIGURE_ARGS += --with-package-format=portable

# configure script is under the subdirectory config_office
CONFIGURE_SCRIPTS = $(WORKSRC)/config_office/configure
BUILD_SCRIPTS = icu all-modules langpack
INSTALL_SCRIPTS = core-and-common langpack

include ../category.mk

# Extra libraries location to put in the RUNPATH
EXTRA_LIBS = $(prefix)/OpenOffice.org/program 
EXTRA_LIBS += $(libexecdir)/firefox
EXTRA_LIBS += $(libdir)/mozilla
EXTRA_LIBS += $(libexecdir)/thunderbird 
EXTRA_LIBS += $(libdir)/evolution/nss/lib

#
# Build environment variables
#

# some component (icu) doesn't build with make, so
# we export $(MAKE) so configure use gmake instead of make
COMMON_EXPORTS += MAKE

X_LDFLAGS = -L$(libdir)
COMMON_EXPORTS += X_LDFLAGS

# Configure need the xmkmf tool
XMKMF=/usr/openwin/bin/xmkmf
COMMON_EXPORTS += XMKMF

# There is a bug in pkg format configure option
# we need to set it manually
PKGFORMAT=pkg
COMMON_EXPORTS += PKGFORMAT

# Build instructions need bash to be used to 
# work correctly
SHELL = /opt/csw/bin/bash

# For a faster build
# (see http://wiki.services.openoffice.org/wiki/Building_OpenOffice.org)
BUILD_ENV += NO_HIDS=TRUE
BUILD_ENV += nodep=TRUE


# For now we directly use mozilla prebuilt binaries
# available http://tools.openoffice.org/moz_prebuild/$(SRCNUM)/
post-extract:
	( for FILE in $(DOWNLOADDIR)/SOLARISC52*; do \
		cp $$FILE $(WORKSRC)/moz/zipped/`basename $$FILE`.zip; \
	  done )
	@$(MAKECOOKIE)


# We need additionnal tweaks in the configure-generated Solaris$(ARCH)Env.Set:
# 1. checkdll sometimes fails because it can't find some depen 
#    so we add some path to LD_LIBRARY_PATH
# 2. By default, Sun Pango is used instead of CSW pango, to avoid this, we make
#    sure /opt/csw/lib is read before /usr/lib
# 3. We want Cairo to use CSW Xrender so we add /opt/csw/include in the include path search
# 4. We add "-I/opt/csw/include" in the CFLAGSCXX so the expat include files are found
#    when the built-in sablot is compiled (why isn't CPPFLAGS taken in account ?!)
# 5. We add "-I/opt/csw/include" in SOLARINC so the build process correctly find
#    the jpeg headers
# 6. We add "-I/opt/csw/lib" in SOLARLIB so the build process find expat lib 
#
#post-configure:
#	perl -pi -e 's,PYTHON_CFLAGS=.*,PYTHON_CFLAGS=\"-I/opt/csw/include/python2.5\",' $(WORKSRC)/Solaris*Env.Set.sh
#	perl -pi -e 's,PYTHON_LIBS=.*,PYTHON_LIBS=\"-L/opt/csw/lib -lpython2.5\",' $(WORKSRC)/Solaris*Env.Set.sh
#	perl -pi -e 's,LD_LIBRARY_PATH=\"(.*)\",LD_LIBRARY_PATH=\"$$1:$(libdir):$(CURDIR)/$(WORKSRC)/stlport/unxsoli4.pro/lib/\",' $(WORKSRC)/Solaris*Env.Set.sh
#	perl -pi -e 's,\s+(-L$(libdir)\s+)?-L/usr/lib, -L$(libdir) -L/usr/lib,' $(WORKSRC)/Solaris*Env.Set.sh
#	perl -pi -e 's,CAIRO_CFLAGS=\"(.*)\",CAIRO_CFLAGS=\"$$1 -I/opt/csw/include\",' $(WORKSRC)/Solaris*Env.Set.sh
#	perl -pi -e 's,CFLAGSCXX\s*=\s*(.*),CFLAGSCXX=$$1 -I$(includedir),' $(WORKSRC)/solenv/inc/unxsol*4.mk
#	perl -pi -e 's,SOLARINC=\"(.*)\",SOLARINC=\"$$1 -I$(includedir)\",' $(WORKSRC)/Solaris*Env.Set.sh
#	perl -pi -e 's,SOLARLIB=\"(.*)\",SOLARLIB=\"$$1 -L$(libdir)\",' $(WORKSRC)/Solaris*Env.Set.sh
#	@$(MAKECOOKIE)


#####################################################################
# Build instructions
#####################################################################

# build the dmake too used to build openoffice
bootstrap:
	cd $(WORKSRC) && ./bootstrap
	@$(MAKECOOKIE)

# we separately build icu because it needs 
build-icu: bootstrap
	( . $(WORKSRC)/Solaris*Env.Set.sh && . $(WORKDIR)/SolarisCSWEnv.Set.sh && \
	  cd $(WORKSRC)/icu && build )
	@$(MAKECOOKIE)

build-all-modules: bootstrap
	( . $(WORKSRC)/Solaris*Env.Set.sh && . $(WORKDIR)/SolarisCSWEnv.Set.sh && \
	  cd $(WORKSRC)/instsetoo_native && $(BUILD_ENV) build --dlv_switch -link --all )
	@$(MAKECOOKIE)
	
build-langpack: bootstrap
	( . $(WORKSRC)/Solaris*Env.Set.sh && . $(WORKDIR)/SolarisCSWEnv.Set.sh && \
	  cd $(WORKSRC)/instsetoo_native/util; \
       	  $(BUILD_ENV) dmake ooolanguagepack )
	@$(MAKECOOKIE)
	

#####################################################################
# Installation instructions
#####################################################################

install-core-and-common: 
	ginstall -d $(DESTDIR)$(prefix)/OpenOffice.org
	( for PKG in $(WORKSRC)/instsetoo_native/unxsol?4.pro/OpenOffice/pkg/install/en-US/packages/*; do \
		tar cf - -C $$PKG/reloc . | tar xf - -C $(DESTDIR)$(prefix)/OpenOffice.org; \
	  done)
	ginstall -D $(WORKSRC)/solver/$(SRCNUM)/unxsol?4.pro/bin/ConnectivityTools.jar \
		$(DESTDIR)$(prefix)/OpenOffice.org/program/classes/ConnectivityTools.jar
	ginstall -D $(WORKSRC)/solver/$(SRCNUM)/unxsol?4.pro/bin/smaster \
	       	$(DESTDIR)$(prefix)/OpenOffice.org/program/smaster
	ginstall -D $(WORKSRC)/solver/$(SRCNUM)/unxsol?4.pro/bin/legacy_binfilters.rdb \
	       	$(DESTDIR)$(prefix)/OpenOffice.org/program/legacy_binfilters.rdb
	ginstall -D $(WORKSRC)/solver/$(SRCNUM)/unxsol?4.pro/bin/pluginapp.bin \
	      	$(DESTDIR)$(prefix)/OpenOffice.org/program/pluginapp.bin
	cp $(WORKSRC)/solver/$(SRCNUM)/unxsol?4.pro/lib/*.so* $(DESTDIR)$(prefix)/OpenOffice.org/program/
	cp $(WORKSRC)/solver/$(SRCNUM)/unxsol?4.pro/bin/*.so* $(DESTDIR)$(prefix)/OpenOffice.org/program/
	@$(MAKECOOKIE)


install-langpack-%:
	( for PKG in $(WORKSRC)/instsetoo_native/unxsol?4.pro/OpenOffice_languagepack/pkg/install/$*/packages/*; do \
		tar cf - -C $$PKG/reloc . | tar xf - -C $(DESTDIR)$(prefix)/OpenOffice.org; \
	  done )
	@$(MAKECOOKIE)

install-langpack: $(addprefix install-langpack-,$(OOO_LANGS))

