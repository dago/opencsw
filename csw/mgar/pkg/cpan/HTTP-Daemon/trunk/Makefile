NAME = HTTP-Daemon
VERSION = 6.01
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = GAAS

DESCRIPTION = A simple http server class
define BLURB
  Instances of the HTTP::Daemon class are HTTP/1.1 servers that listen on a
  socket for incoming requests. The HTTP::Daemon is a subclass of
  IO::Socket::INET, so you can perform socket operations directly on it too.
endef

LICENSE_TEXT = This module is licensed under the perl license

PACKAGES = CSWpm-http-daemon
ARCHALL = 1
RUNTIME_DEP_PKGS += CSWpm-lwp-mediatypes
RUNTIME_DEP_PKGS += CSWpm-http-date
RUNTIME_DEP_PKGS += CSWpm-http-message

include gar/category.mk
