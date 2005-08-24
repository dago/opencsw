# Packaging information
SPKG_VENDOR   = $(firstword $(MASTER_SITES)) packaged for CSW by Cory Omand
SPKG_EMAIL    = comand@blastwave.org
# Where to put finished packages
SPKG_EXPORT   = /export/medusa/comand/staging/build-$(shell date '+%d.%b.%Y')
# Where to put downloaded sources (make garchive)
GARCHIVEDIR   = /export/medusa/comand/src
# Where to look for DISTFILES before downloading
GARCHIVEPATH  = /export/medusa/comand/src
GARCHIVEPATH += /export/medusa/src
