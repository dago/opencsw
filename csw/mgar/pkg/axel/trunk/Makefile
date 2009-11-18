# TODO
# - Migrate configuration from /opt to /etc
GARNAME = axel
GARVERSION = 2.4
CATEGORIES = utils

DESCRIPTION = Lightweight command-line download accelerator
define BLURB
  Axel tries to accelerate downloads by using multiple connections (possibly 
  to multiple servers) for one download. Because of its size, it might be 
  very useful on bootdisks or other small systems as a wget replacement
endef

# Beware: When bumping the version, you also need to visit the download page
# and get the correct DOWNLOAD_ID for the new version. If you don't change it,
# you will get the tarball with the corrent name, but with the old content.
SPKG_SOURCEURL = http://axel.alioth.debian.org/
MASTER_SITES   = http://alioth.debian.org/frs/download.php/$(DOWNLOAD_ID)/
DOWNLOAD_ID    = 3015
DISTFILES      = $(GARNAME)-$(GARVERSION).tar.gz
UFILES_REGEX   = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

# upstream_watch currently uses lftp and lftp only lists files when
# they are offered via the SAME scheme as the requested page. The
# axel download page can be accessed via http:// and https:// but 
# the files themselves are only offered via https://, thus https://.
UPSTREAM_MASTER_SITES = https://alioth.debian.org/frs/?group_id=100070

# Make ./configure play nicely with /bin/sh and /opt/csw prefix
PATCHFILES = 0001-configure-use-backticks-and-honor-prefix-for-gettext.patch

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --i18n=0

# axel doesn't come with a test suite
TEST_SCRIPTS =

SAMPLECONF = $(sysconfdir)/axelrc

include gar/category.mk

# Get rid of hard-coded -Wall gcc'ism
pre-build-modulated:
	perl -pi -e 's/-Wall//g' $(WORKSRC)/Makefile
	@$(MAKECOOKIE)

post-install-modulated: DOCDEST=$(DESTDIR)$(docdir)/$(GARNAME)
post-install-modulated:
	ginstall -d $(DOCDEST)
	cp $(FILEDIR)/changelog.CSW $(DOCDEST)
	perl -pi -e "s#/etc/axelrc#$(sysconfdir)/axelrc#" \
		$(DESTDIR)$(mandir)/man1/axel.1 \
		$(DESTDIR)$(mandir)/zh_CN/man1/axel.1
	@$(MAKECOOKIE)
