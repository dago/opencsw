# http://jakarta.apache.org/commons

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX ?= commons-$(GARNAME)-(\d+(?:\.\d+)*)-bin.tar.gz
USTREAM_MASTER_SITE ?= $(SPKG_SOURCEURL)

# Includes the rest of gar
include gar/gar.mk
