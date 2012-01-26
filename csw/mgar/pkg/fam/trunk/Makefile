NAME = fam
VERSION = 2.7.0
CATEGORIES = server
GARTYPE = v2

DESCRIPTION = File Alteration Monitor, daemon and interface library
define BLURB
  GUI tools should not mislead the user; they should display the current
  state of the system, even when changes to the system originate from outside
  of the tools themselves. FAM helps make GUI tools more usable by notifying
  them when the files they're interested in are created, modified, executed,
  and removed.
endef

MASTER_SITES = ftp://oss.sgi.com/projects/fam/download/stable/
DISTFILES  = $(NAME)-$(VERSION).tar.gz

# Taken from http://pkgbuild.svn.sourceforge.net/viewvc/pkgbuild/spec-files-extra/trunk/patches/
PATCHFILES  = fam-oss-01.patch
PATCHFILES += fam-oss-02.patch

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

SPKG_SOURCEURL = http://oss.sgi.com/projects/fam/

sysconfdir = /etc/opt/csw
sharedstatedir = /var/opt/csw
CONFIGURE_ARGS = $(DIRPATHS)

MIFRATE_FILES = fam.conf

CSWfam_etcrpc = "sgi_fam		391002"
CSWfam_inetdconf = "sgi_fam/1-2	stream	rpc/tcp	wait	root	$(bindir)/fam	fam"

include gar/category.mk
