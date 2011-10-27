# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
# ! Early stage recipe, doesn't build yet
#
#gmake[3]: Entering directory `/home/skayser/mgar/pkg/monit/trunk/work/solaris9-sparc/build-isa-sparcv8/monit-5.3.1/libmonit'
#/bin/bash ./libtool --tag=CC   --mode=compile /opt/SUNWspro/bin/cc -DHAVE_CONFIG_H -I. -I./src -I./src -I./src/exceptions -I./src/io -I./src/net -I./src/util -I./src/thread -I/opt/csw/include  -I/opt/csw/include  -xO3 -m32 -xarch=v8 -D_REENTRANT -D_POSIX_PTHREAD_SEMANTICS -D__EXTENSIONS__ -m64 -mtune=v9 -c -o src/Bootstrap.lo src/Bootstrap.c
#libtool: compile:  /opt/SUNWspro/bin/cc -DHAVE_CONFIG_H -I. -I./src -I./src -I./src/exceptions -I./src/io -I./src/net -I./src/util -I./src/thread -I/opt/csw/include -I/opt/csw/include -xO3 -m32 -xarch=v8 -D_REENTRANT -D_POSIX_PTHREAD_SEMANTICS -D__EXTENSIONS__ -m64 -mtune=v9 -c src/Bootstrap.c  -KPIC -DPIC -o src/.libs/Bootstrap.o
#cc: Warning: illegal option -mtune=v9
#cc: -xarch=v8 is 32-bit only
#
NAME = monit
VERSION = 5.3.1
GARTYPE = v2
CATEGORIES = utils

DESCRIPTION = Utility for monitoring and managing daemons or similar programs
define BLURB
  Long description
endef

VENDOR_URL = http://mmonit.com/monit/
MASTER_SITES = http://mmonit.com/monit/dist/
DISTFILES  = $(DISTNAME).tar.gz

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

