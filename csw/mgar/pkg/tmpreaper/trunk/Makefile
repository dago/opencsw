GARNAME = tmpreaper
GARVERSION = 1.6.13
CATEGORIES = apps

DESCRIPTION = Cleans up files in directories based on their age
define BLURB
  This package provides a program that can be used to clean out
  temporary-file directories. It recursively searches the directory,
  refusing to chdir() across symlinks, and removes files that haven't been
  accessed in a user-specified amount of time. You can specify a set of
  files to protect from deletion with a shell pattern. It will not remove
  files owned by the process EUID that have the `w' bit clear, unless you
  ask it to, much like `rm -f'. `tmpreaper' will not remove symlinks,
  sockets, fifos, or special files unless given a command line option
  enabling it to. 
endef

SPKG_SOURCEURL = http://packages.debian.org/sid/tmpreaper
MASTER_SITES = http://ftp.de.debian.org/debian/pool/main/t/tmpreaper/
DISTFILES  = $(GARNAME)_$(GARVERSION).tar.gz
UFILES_REGEX = $(GARNAME)_(\d+(?:\.\d+)*).tar.gz

TEST_SCRIPTS =

# getcwd() returns char*, fix return value comparison
PATCHFILES  = 0001-fix-getcwd-comparison.patch
# Studio 11 does not know about statement expressions
PATCHFILES += 0002-provide-statement-expression-workaround.patch

# Force zone-friendly dirs, while they have not yet become standard in GAR
sysconfdir=/etc/opt/csw
localstatedir=/var/opt/csw

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

post-install-modulated: DOCDEST=$(DESTDIR)$(docdir)/$(CATALOGNAME)
post-install-modulated:
	ginstall -d $(DOCDEST)
	cp $(FILEDIR)/changelog.CSW $(FILEDIR)/README.CSW $(DOCDEST)
	@$(MAKECOOKIE)
