NAME = gzip
VERSION = 1.4
CATEGORIES = utils
GARTYPE = v2

DESCRIPTION = GNU zip
define BLURB
  gzip (GNU zip) is a compression utility designed to be a replacement for compress.
  Its main advantages over compress are much better compression and freedom from patented
  algorithms. It has been adopted by the GNU project and is now relatively popular on the
  Internet. gzip was written by Jean-loup Gailly (jloup@gzip.org), and Mark Adler for the
  decompression code.
endef

MASTER_SITES = $(GNU_MIRROR)
DISTFILES  = $(NAME)-$(VERSION).tar.gz
PATCHFILES = 0001-Force-ggrep-as-Solaris-grep-doesn-t-understand-the-f.patch

# From TODO:
# - Add a block size (-b) option to improve error recovery in case of
#   failure of a complete sector. Each block could be extracted
#   independently, but this reduces the compression ratio.
# 
# For one possible approach to this, please see:
#   http://www.samba.org/netfilter/diary/gzip.rsync.patch
#
# Update patch from
#  http://cvs.fedoraproject.org/viewvc/rpms/gzip/F-12/gzip-1.3.9-rsync.patch?revision=1.2&content-type=text%2Fplain&view=co
PATCHFILES += gzip-1.3.9-rsync.patch

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

PACKAGES = CSWgzip CSWgzipextras

CATALOGNAME_CSWgzip       = gzip
CATALOGNAME_CSWgzipextras = gzip_extras

SPKG_DESC_CSWgzip       = GNU zip
SPKG_DESC_CSWgzipextras = GNU zip additional tools

RUNTIME_DEP_PKGS_CSWgzipextras = CSWgzip CSWggrep

CONFIGURE_ARGS = $(DIRPATHS)

EXTRA_MERGE_EXCLUDE_FILES = $(libdir)/charset.alias

PKGFILES_CSWgzip  = $(bindir)/gzip
PKGFILES_CSWgzip += $(bindir)/gunzip
PKGFILES_CSWgzip += $(bindir)/uncompress
PKGFILES_CSWgzip += $(mandir)/man1/gzip\.1
PKGFILES_CSWgzip += $(mandir)/man1/gunzip\.1

include gar/category.mk
