# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = nxlog-ce
VERSION = 2.5.1089
GARTYPE = v2

DESCRIPTION = A multi-platform universal log collector and forwarder
define BLURB
  nxlog is a modular, multi-threaded, high-performance log management solution with multi-platform support. In concept it is similar to syslog-ng or rsyslog but is not limited to unix/syslog only. It can collect logs from files in various formats, receive logs from the network remotely over UDP, TCP or TLS/SSL . It supports platform specific sources such as the Windows Eventlog, Linux kernel logs, Android logs, local syslog etc. Writing and reading logs to/from databases is also supported. The collected logs can be stored into files, databases or forwarded to a remote log server using various protocols. The old BSD Syslog and the newer IETF syslog standard is fully supported by nxlog in addition to XML, JSON, GELF, CSV and custom formats. A key concept in nxlog is to be able to handle and preserve structured logs. No need to convert everything to syslog and parse these logs again at the other side. It has powerful message filtering, log rewrite and conversion capabilities.
endef

VENDOR_URL   = http://nxlog-ce.sourceforge.net/
MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(DISTNAME).tar.gz

GARCOMPILER = GCC4

BUILD_DEP_PKGS += CSWlibdbi-dev
BUILD_DEP_PKGS += CSWlibapr-dev

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --enable-static=no

BUILD64 = 1
ISAEXEC = 1

include gar/category.mk

