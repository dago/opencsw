bin_PROGRAMS=binexample
binexample_SOURCES=binexample.c libexample.1 system.h aclocal.m4 getopt.c getopt1.c getopt.h

#  uncomment the following if libexample requires the math library
#libexample_LDADD=-lm

EXTRA_DIST=libexample.lsm.in libexample.spec.in libexample.texinfo

# AUTOMAKE_OPTIONS = gnu

lib_LTLIBRARIES = libexample.la
libexample_la_SOURCES = libexample.c
libexample_la_LDFLAGS = -version-info 0:0:0

#  if you write a self-test script named `chk', uncomment the
#  following and add `chk' to the EXTRA_DIST list
#TESTS=chk

#  build and install the .info pages
info_TEXINFOS = libexample.texinfo
libexample_TEXINFOS = gpl.texinfo

#  install the man pages
man_MANS=libexample.1
