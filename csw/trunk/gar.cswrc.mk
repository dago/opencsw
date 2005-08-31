# Packaging information
SPKG_PACKAGER  ?= Cory Omand
SPKG_SOURCEURL ?= $(firstword $(MASTER_SITES))
SPKG_VENDOR     = $(SPKG_SOURCEURL) packaged for CSW by $(SPKG_PACKAGER)
SPKG_EMAIL      = comand@blastwave.org
# Where to put finished packages
SPKG_EXPORT     = /export/medusa/comand/staging/build-$(shell date '+%d.%b.%Y')
# Where to put downloaded sources (make garchive)
GARCHIVEDIR     = /export/medusa/comand/src
# Where to look for DISTFILES before downloading
GARCHIVEPATH    = /export/medusa/comand/src
GARCHIVEPATH   += /export/medusa/src
