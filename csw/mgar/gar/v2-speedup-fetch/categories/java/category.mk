# http://jakarta.apache.org/commons

# We define upstream file regex so we can be notifed of new upstream software release
USTREAM_MASTER_SITE ?= $(SPKG_SOURCEURL)

# Includes the rest of gar
include gar/gar.mk
