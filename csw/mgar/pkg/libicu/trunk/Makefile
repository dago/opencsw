# $Id$
GARNAME = libicu
GARVERSION = 4.4.1
CATEGORIES = lib

DESCRIPTION = International Components for Unicode
define BLURB
endef

EXTRA_MODULATORS = GARVERSION
MODULATIONS_GARVERSION = 4.4.1 4.2.1

SKIP_MODULATIONS  = isa-sparcv9-garversion-4.2.1
SKIP_MODULATIONS += isa-amd64-garversion-4.2.1

# filename = icu4c-$(shell echo $(1) | tr '.' '_')-src.tgz
_V-4.2.1 = 4_2_1
_V-4.4.1 = 4_4_1
filename = icu4c-$(_V-$(1))-src.tgz

MASTER_SITES = $(addsuffix /,$(addprefix http://download.icu-project.org/files/icu4c/,$(MODULATIONS_GARVERSION)))
SOURCEFILES = $(foreach VERSION,$(MODULATIONS_GARVERSION), $(call filename,$(VERSION)))
DISTFILES  = $(SOURCEFILES)

NOEXTRACT = $(filter-out $(call filename,$(GARVERSION)),$(SOURCEFILES))

# File name regex to get notifications about upstream software releases
UFILES_REGEX = $(GARNAME)-(\d+(?:_\d+)*)-src.tgz

PACKAGES = CSWlibicu CSWlibicudevel

CATALOGNAME_CSWlibicu      = libicu
CATALOGNAME_CSWlibicudevel = libicu_devel

SPKG_DESC_CSWlibicu      = International Components for Unicode
SPKG_DESC_CSWlibicudevel = Development Files for libicu

RUNTIME_DEP_PKGS_CSWlibicudevel += CSWlibicu

LICENSE = license.html

VENDOR_URL = http://icu-project.org/

DISTNAME = icu
WORKSRC = $(WORKDIR)/$(DISTNAME)/source

# Using -I/opt/csw/include here puts it before the include of the newly built
# software which breaks definitions
CPPFLAGS = 
LINKER_FLAGS = -lCrun

BUILD64 = 1
NOISAEXEC = 1
NOISALIST = 1
CONFIGURE_ARGS = $(DIRPATHS)

MERGE_SCRIPTS_isa-default-garversion-4.2.1 = copy-only
MERGE_DIRS_isa-default-garversion-4.2.1 = $(libdir)

MERGE_SCRIPTS_isa-default-garversion-4.4.1 = copy-all
MERGE_SCRIPTS_isa-default64-garversion-4.4.1 = copy-relocated-only copy-config-only
MERGE_DIRS_isa-default64-garversion-4.4.1 = $(libdir)

PKGFILES_CSWlibicu = $(PKGFILES_RT)

CHECKPKG_OVERRIDES_CSWlibicu += soname-not-found|libm.so.2|is|needed|by|opt/csw/lib/amd64/libicui18n.so.44.1
CHECKPKG_OVERRIDES_CSWlibicu += soname-not-found|libm.so.2|is|needed|by|opt/csw/lib/amd64/libicule.so.44.1
CHECKPKG_OVERRIDES_CSWlibicu += soname-not-found|libm.so.2|is|needed|by|opt/csw/lib/amd64/libiculx.so.44.1
CHECKPKG_OVERRIDES_CSWlibicu += soname-not-found|libm.so.2|is|needed|by|opt/csw/lib/amd64/libicuuc.so.44.1
CHECKPKG_OVERRIDES_CSWlibicu += soname-not-found|libm.so.2|is|needed|by|opt/csw/lib/amd64/libicutu.so.44.1
CHECKPKG_OVERRIDES_CSWlibicu += soname-not-found|libm.so.2|is|needed|by|opt/csw/lib/amd64/libicuio.so.44.1
CHECKPKG_OVERRIDES_CSWlibicu += soname-not-found|libm.so.2|is|needed|by|opt/csw/lib/amd64/libicutest.so.44.1

include gar/category.mk
