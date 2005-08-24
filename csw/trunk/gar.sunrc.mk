# Packager info
SPKG_VENDOR   = $(firstword $(MASTER_SITES)) packaged for CSW by Cory Omand
SPKG_EMAIL    = comand@blastwave.org
# Where to put finished packages
SPKG_EXPORT   = /export/public/csw/build-$(shell date '+%d.%b.%Y')
# Where to put downloaded sources (make garchive)
GARCHIVEDIR   = /export/garchive
# Where to look for DISTFILES before downloading
GARCHIVEPATH  = /export/garchive
GARCHIVEPATH += /net/labhome.sfbay/export/archive/software/sources
# Proxies
http_proxy = http://webcache:8080
ftp_proxy  = $(http_proxy)
export http_proxy ftp_proxy
