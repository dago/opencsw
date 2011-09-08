# TODO (release-critical prefixed with !, non release-critical with *)
# ! Make sure to honour these on an update:
#     http://www.mail-archive.com/pca@lists.univie.ac.at/msg02692.html
#     https://lists.gnu.org/archive/html/bug-wget/2011-09/msg00001.html

NAME = wget
VERSION = 1.13.3
CATEGORIES = net

DESCRIPTION = A network utility to retrieve files from the web
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
DISTFILES = $(NAME)-$(VERSION).tar.xz

# This is the reformatted patch wget-1.13.3.patch from
#    https://lists.gnu.org/archive/html/bug-wget/2011-09/msg00001.html
PATCHFILES += 0001-Features-patch.patch

# This is from
#   https://lists.gnu.org/archive/html/bug-wget/2011-09/msg00004.html
PATCHFILES += 0002-Make-sure-FIONBIO-is-defined.patch

VENDOR_URL = http://www.gnu.org/software/wget/

PACKAGES += CSWwget
SPKG_DESC_CSWwget = A network utility to retrieve files from the web
RUNTIME_DEP_PKGS_CSWwget += CSWlibintl8
RUNTIME_DEP_PKGS_CSWwget += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWwget += CSWlibgcrypt11
RUNTIME_DEP_PKGS_CSWwget += CSWlibz1
RUNTIME_DEP_PKGS_CSWwget += CSWlibgpg-error0
RUNTIME_DEP_PKGS_CSWwget += CSWlibgnutls26
RUNTIME_DEP_PKGS_CSWwget += CSWlibidn11

EXTRA_MODULATORS = STATIC
MODULATIONS_STATIC = disable enable

EXTRA_CONFIGURE_STATIC-disable += --with-ssl
# NTLM can only be enabled when used with OpenSSL instead of the defaulting GnuTLS
#EXTRA_CONFIGURE_STATIC-disable += --enable-ntlm

EXTRA_CONFIGURE_STATIC-enable += --without-ssl
EXTRA_CONFIGURE_STATIC-enable += --disable-nls
EXTRA_CONFIGURE_STATIC-enable += --disable-iri

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += $(EXTRA_CONFIGURE_STATIC-$(STATIC))

PRESERVECONF = $(sysconfdir)/wgetrc
MIGRATE_FILES = wgetrc

EXTRA_MERGE_EXCLUDE_FILES += $(libdir)/charset.alias

MERGE_SCRIPTS_isa-sparcv8-static-disable = copy-all
 MERGE_SCRIPTS_isa-sparcv8-static-enable = copy-static-wget-only
    MERGE_DIRS_isa-sparcv8-static-enable = $(bindir)

    MERGE_SCRIPTS_isa-i386-static-disable = copy-all
     MERGE_SCRIPTS_isa-i386-static-enable = rename-wget copy-only
        MERGE_DIRS_isa-i386-static-enable = $(bindir)

# This is ok, it is just one example occurrence, all others have been replaced
CHECKPKG_OVERRIDES_CSWwget += file-with-bad-content|/usr/local|root/opt/csw/share/info/wget.info

include gar/category.mk

post-extract-modulated:
	@# Make sure our perl is used as the /usr/bin/perl lacks some needed modules
	-perl -pi -e 's,#!/usr/bin/env perl,#!/opt/csw/bin/perl,' \
		$(WORKSRC)/tests/*.px \
		$(WORKSRC)/tests/run-px

merge-copy-static-wget-only:
	ginstall $(INSTALLISADIR)$(bindir)/wget $(PKGROOT)$(bindir)/wget.static
	@$(MAKECOOKIE)

post-install-modulated:
	perl -pi -e 's,/usr/local/etc,$(sysconfdir),g' \
		$(DESTDIR)$(infodir)/wget.info \
		$(DESTDIR)$(mandir)/man1/wget.1 \
		$(DESTDIR)$(sysconfdir)/wgetrc
