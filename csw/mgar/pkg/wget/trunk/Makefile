GARNAME = wget
GARVERSION = 1.11.4
CATEGORIES = net

DESCRIPTION = A network utility to retrieve files from the Web
define BLURB
  GNU Wget is a utility for noninteractive download of files from the Web. It
  supports HTTP and FTP protocols, as well as retrieval through HTTP proxies. It
  can follow HTML links, download many pages, and convert the links for local
  viewing. It can also mirror FTP hierarchies or only those files that have
  changed. Wget has been designed for robustness over slow network connections;
  if a download fails due to a network problem, it will keep retrying until the
  whole file has been retrieved.
endef

MASTER_SITES = $(GNU_MIRROR)
DISTFILES = $(GARNAME)-$(GARVERSION).tar.bz2

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

SPKG_SOURCEURL = http://www.gnu.org/software/wget/

EXTRA_MODULATORS = STATIC
MODULATIONS_STATIC = disable enable

EXTRA_CONFIGURE_STATIC-disable = --with-ssl
EXTRA_CONFIGURE_STATIC-enable = --disable-shared
EXTRA_CONFIGURE_STATIC-enable += --enable-static
EXTRA_CONFIGURE_STATIC-enable += --without-ssl

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-ssl
CONFIGURE_ARGS += --disable-nls
CONFIGURE_ARGS += $(EXTRA_CONFIGURE_STATIC-$(STATIC))

TEST_TARGET = check
REQUIRED_PKGS = CSWosslrt

SAMPLECONF = $(sysconfdir)/wgetrc.CSW
EXTRA_PAX_ARGS = -s ",^\(.$(sysconfdir)/wgetrc\)\$$,\1.CSW,p"

MERGE_SCRIPTS_isa-sparcv8-static-disable = copy-all
 MERGE_SCRIPTS_isa-sparcv8-static-enable = copy-static-wget-only
    MERGE_DIRS_isa-sparcv8-static-enable = $(bindir)

    MERGE_SCRIPTS_isa-i386-static-disable = copy-all
     MERGE_SCRIPTS_isa-i386-static-enable = rename-wget copy-only
        MERGE_DIRS_isa-i386-static-enable = $(bindir)

merge-copy-static-wget-only:
	ginstall $(INSTALLISADIR)$(bindir)/wget $(PKGROOT)$(bindir)/wget.static
	@$(MAKECOOKIE)

include gar/category.mk
