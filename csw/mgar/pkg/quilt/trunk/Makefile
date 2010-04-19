GARNAME = quilt
GARVERSION = 0.48
CATEGORIES = utils

DESCRIPTION = A patch management tooln
define BLURB
Quilt allows you to easily manage large numbers of patches by keeping
track of the changes each patch makes. Patches can be applied,
un-applied, refreshed, and more.

Quilt originally was based on Andrew Morton's patch scripts found at
http://www.zip.com.au/~akpm/linux/patches/.
endef

MASTER_SITES = http://mirror.csclub.uwaterloo.ca/nongnu/quilt/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

CONFIGURE_ARGS =  $(DIRPATHS)
CONFIGURE_ARGS += --with-bash=/opt/csw/bin/bash
CONFIGURE_ARGS += --with-cp=/opt/csw/bin/gcp
CONFIGURE_ARGS += --with-date=/opt/csw/bin/gdate
CONFIGURE_ARGS += --with-perl=/opt/csw/bin/perl
CONFIGURE_ARGS += --with-grep=/opt/csw/bin/ggrep
CONFIGURE_ARGS += --with-tail=/opt/csw/bin/gtail
CONFIGURE_ARGS += --with-tr=/opt/csw/bin/gtr
CONFIGURE_ARGS += --with-sed=/opt/csw/bin/gsed
CONFIGURE_ARGS += --with-awk=/opt/csw/bin/gawk
CONFIGURE_ARGS += --with-column=/opt/csw/bin/column
CONFIGURE_ARGS += --with-pod2man=/opt/csw/bin/pod2man
CONFIGURE_ARGS += --with-getopt=/opt/csw/bin/ggetopt
CONFIGURE_ARGS += --with-diff=/opt/csw/bin/gdiff
CONFIGURE_ARGS += --with-mktemp=/opt/csw/bin/mktemp
CONFIGURE_ARGS += --with-patch=/opt/csw/bin/gpatch
CONFIGURE_ARGS += --with-diffstat=/opt/csw/bin/gdiffstat
CONFIGURE_ARGS += --with-find=/opt/csw/bin/gfind
CONFIGURE_ARGS += --with-sendmail=/usr/lib/sendmail

include gar/category.mk

PATH := /opt/csw/gnu:$(PATH)
