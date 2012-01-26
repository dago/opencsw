NAME = Net-Syslog
VERSION = 0.04
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = LHOWARD

DESCRIPTION = Perl extension for sending syslog messages directly to a remote syslogd
define BLURB
  Net::Syslog implements the intra-host syslog forwarding protocol. It is not intended 
  to replace the Sys::Syslog or Unix::Syslog modules, but instead to provide a method 
  of using syslog when a local syslogd is unavailable or when you don't want to write 
  syslog messages to the local syslog.
endef

PACKAGES = CSWpmnetsyslog
CATALOGNAME = pm_netsyslog

ARCHALL = 1

# No license specified by author for this perl module
LICENSE = 

CHECKPKG_OVERRIDES_CSWpmnetsyslog += license-missing|/opt/csw/share/doc/pm_netsyslog/license

include gar/category.mk
