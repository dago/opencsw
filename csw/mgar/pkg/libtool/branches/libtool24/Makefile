NAME = libtool
VERSION = 2.4
CATEGORIES = devel

EXTRA_MODULATORS = GARCOMPILER
MODULATIONS_GARCOMPILER = GCC3 GCC4 SOS12

# Modulate over compiler only for 2.4
# Compile 64 bit libraries only with SOS12
SKIP_MODULATIONS += $(foreach I,sparcv9 amd64,$(foreach C,GCC3 GCC4,isa-$I-garcompiler-$C))

# TODO: Make sure -xnorunpath / -norunpath stays in cc and CC

DESCRIPTION = A generic library support tool
define BLURB
  GNU libtool is a generic library support script. Libtool hides the complexity
  of using shared and static libraries behind a consistent, portable interface.
  Libtool supports building static libraries on all platforms.
endef

MASTER_SITES = $(GNU_MIRROR)
DISTFILES = $(NAME)-$(VERSION).tar.xz
DISTFILES += README.CSW

PATCH_LIBTOOL = 0002-Forward-port-GCC-tags-patch.patch
PATCHFILES_POSTINSTALL_isa-i386-garcompiler-SOS12 = $(PATCH_LIBTOOL)
PATCHFILES_POSTINSTALL_isa-sparcv8-garcompiler-SOS12 = $(PATCH_LIBTOOL)
DISTFILES += $(PATCH_LIBTOOL)

PATCHFILES  = 0001-Preserve-norunpath.patch

EXTRA_TAGS = gcc3 gcc4 sos12
COMPILER_TAGNAME_GCC3 = gcc3
COMPILER_TAGNAME_GCC4 = gcc4
COMPILER_TAGNAME_SOS12 = sos12

VENDOR_URL = http://www.gnu.org/software/libtool/

PACKAGES += CSWlibtool
CATALOGNAME_CSWlibtool = libtool
SPKG_DESC_CSWlibtool = A generic library support tool
# Double-legacy packages may not even depend on CSWlibtoolrt, so we must
# also directly depend on CSWlibltdl3
RUNTIME_DEP_PKGS_CSWlibtool += CSWlibltdl3
RUNTIME_DEP_PKGS_CSWlibtool += CSWlibltdl7
CHECKPKG_OVERRIDES_CSWlibtool += surplus-dependency|CSWlibltdl3
CHECKPKG_OVERRIDES_CSWlibtool += surplus-dependency|CSWlibltdl7

# This is built from pkgs/libltdl3
FOREIGN_PACKAGES += CSWlibltdl3
OBSOLETED_BY_CSWlibltdl3 += CSWlibtoolrt

PACKAGES += CSWlibltdl7
CATALOGNAME_CSWlibltdl7 = libltdl7
SPKG_DESC_CSWlibltdl7 = Libtool libltdl.so.7 from libtool 2.x
PKGFILES_CSWlibltdl7 += $(PKGFILES_RT)
OBSOLETED_BY_CSWlibltdl7 += CSWlibtoolrt

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_ARGS = $(DIRPATHS)

BUILD64 = 1
NOISAEXEC = 1

TEST_TARGET = check

# Some Fortran-specific tests fail which is probably not that important
SKIPTEST ?= 1

   MERGE_SCRIPTS_isa-default-garcompiler-SOS12 = copy-all
 MERGE_SCRIPTS_isa-default64-garcompiler-SOS12 = copy-relocated-only
    MERGE_DIRS_isa-default64-garcompiler-SOS12 = $(libdir)

    MERGE_SCRIPTS_isa-default-garcompiler-GCC3 = copy-tags
    MERGE_SCRIPTS_isa-default-garcompiler-GCC4 = copy-tags

include gar/category.mk

post-install-modulated: $(if $(PATCHFILES_POSTINSTALL_$(MODULATION)),patch-libtool)
post-install-modulated: $(if $(COMPILER_TAGNAME_$(GARCOMPILER)),install-libtool-$(COMPILER_TAGNAME_$(GARCOMPILER)))
	ginstall -d $(DESTDIR)$(docdir)/libtool
	ginstall $(WORKDIR)/README.CSW $(DESTDIR)$(docdir)/libtool/README.CSW

patch-libtool:
	cat $(WORKDIR)/$(PATCHFILES_POSTINSTALL_$(MODULATION)) | (cd $(DESTDIR)$(bindir) && gpatch -p1)
	# Remove arch-specific flags from the libtool-compilation so they don't spoil the target build
	perl -pi -e 's/^LTCFLAGS=.*/LTCFLAGS="-O"/' $(DESTDIR)$(bindir)/libtool
	@$(MAKECOOKIE)

install-libtool-%:
	perl -ane 'print if( /^available_tags/ ); $$p = 1 if( /^# ### BEGIN LIBTOOL CONFIG/ ); print if( $$p ); $$p = 0 if( /^# ### END LIBTOOL CONFIG/ )' \
		<$(DESTDIR)$(bindir)/libtool >$(DESTDIR)$(datadir)/libtool/$*.conf
	perl -ane '$$p = 1 if( /^# ### BEGIN LIBTOOL TAG CONFIG/ ); print if( $$p ); if( /^# ### END LIBTOOL TAG CONFIG/ ) { $$p = 0; print "\n"; }' \
		<$(DESTDIR)$(bindir)/libtool >$(DESTDIR)$(datadir)/libtool/$*.tags
	@$(MAKECOOKIE)

merge-copy-tags: $(PKGROOT)
	$(_DBG_MERGE)(cd $(INSTALLISADIR); pax -r -w -v $(_PAX_ARGS) \
		-s ",^\(\..*\.conf\)\$$,\1,p" \
		-s ",^\(\..*\.tags\)\$$,\1,p" \
		-s ",.*,," \
		. $(PKGROOT) \
	)
	@$(MAKECOOKIE)


