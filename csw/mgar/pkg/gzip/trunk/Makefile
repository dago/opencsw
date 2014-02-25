# TBD:
# ! Transformation from 'z' to 'gz' prefix does not apply to invocations:
#     http://debbugs.gnu.org/cgi/bugreport.cgi?bug=16876

NAME = gzip
VERSION = 1.6
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
DISTFILES  = $(NAME)#-$(VERSION).tar.gz
PATCHFILES = 0001-Force-ggrep-as-Solaris-grep-doesn-t-understand-the-f.patch

# From TODO:
# - Add a block size (-b) option to improve error recovery in case of
#   failure of a complete sector. Each block could be extracted
#   independently, but this reduces the compression ratio.
# 
# For one possible approach to this, please see:
#   http://www.samba.org/netfilter/diar
# Reformatted version of debian_patches_rsyncable.diff
PATCHFILES += 0001-Debian-patch-for-rsyncable.patch

PACKAGES += CSWgzip
CATALOGNAME_CSWgzip = gzip
SPKG_DESC_CSWgzip = GNU zipdir)/charset.alias

PKGFILES_CSWgzip  = $(bindir)/gzip
PKGFILES_CSWgzip += $(bindir)/gunzip
PKGFILES_CSWgzip += $(bindir)/uncompress
PKGFILES_CSWgzip += $(mandir)/man1/gzip\.1
PKGFILES_CSWgzip += $(mandiPACKAGES += CSWgzip-extras
SPKG_DESC_CSWgzip-extras = GNU zip additional tools
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWgzip-extras += CSWgzip
RUNTIME_DEP_PKGS_CSWgzip-extras += CSWggrep
OBSOLETED_BY_CSWgzip-extras = CSWgzipextras
CATALOGNAME_CSWgzipextras = gzip_extras_stub

EXTRA_MERGE_EXCLUDE_FILES = $(libdir)/charset.alias

# The 'z'-prefix commands now belong to zutils whereas the gzip-commands are prefixed with 'gz' instead:
#   http://lists.nongnu.org/archive/html/zutils-bug/2012-10/msg00002.html
EXTRA_CONFIGURE_ARGS += --program-transform-name='s/^z/gz/'

include gar/category.mk
