# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = ruby
SHORTVER = 2.1
VERSION = $(SHORTVER).3
API_VERSION = $(VERSION)

DESCRIPTION = An object-oriented language for quick and easy programming.
define BLURB
  Ruby is a language for quick and easy programming. Similar in scope to Perl
  and Python, it has high-level data types, automatic memory management,
  dynamic typing, a module system, exceptions, and a rich standard library.
  What sets Ruby apart is a clean and consistent language design where
  everything is an object. Other distinguishing features are CLU-style
  iterators for loop abstraction, singleton classes/methods and lexical
  closures.
endef

MASTER_SITES = ftp://ftp.ruby-lang.org/pub/ruby/$(SHORTVER)/
DISTFILES += $(DISTNAME).tar.gz

PACKAGING_PLATFORMS += solaris10-sparc solaris10-i386
PACKAGING_PLATFORMS += solaris11-sparc solaris11-i386

PACKAGES += CSWruby21
SPKG_DESC_CSWruby21 = Ruby 2.1.x
RUNTIME_DEP_PKGS_CSWruby21 += CSWlibgdbm3
RUNTIME_DEP_PKGS_CSWruby21 += CSWlibssl1-0-0
RUNTIME_DEP_PKGS_CSWruby21 += CSWlibz1
RUNTIME_DEP_PKGS_CSWruby21 += CSWlibgmp10
RUNTIME_DEP_PKGS_CSWruby21 += CSWlibtcl8-5
RUNTIME_DEP_PKGS_CSWruby21 += CSWlibtk8-5
RUNTIME_DEP_PKGS_CSWruby21 += CSWlibyaml0-2
RUNTIME_DEP_PKGS_CSWruby21 += CSWlibffi5
RUNTIME_DEP_PKGS_CSWruby21 += CSWlibreadline5

GARCOMPILER = SOS12U2
#GARCOMPILER = GNU

# Using binutils 2.24 objcopy leads to this funny corruption:
#/home/dam/mgar/pkg/ruby21/trunk/work/solaris11-i386/build-isa-pentium_pro/ruby-2.1.3
#unstable11x% /opt/solstudio12.2/bin/cc  -G -h libruby2.1.3.so.2 -R/opt/csw/lib  -m32 dln.o localeinit.o loadpath.o array.o bignum.o class.o compar.o complex.o dir.o dln_find.o encoding.o enum.o enumerator.o error.o eval.o load.o proc.o file.o gc.o hash.o inits.o io.o marshal.o math.o node.o numeric.o object.o pack.o parse.o process.o random.o range.o rational.o re.o regcomp.o regenc.o regerror.o regexec.o regparse.o regsyntax.o ruby.o safe.o signal.o sprintf.o st.o strftime.o string.o struct.o time.o transcode.o util.o variable.o version.o compile.o debug.o iseq.o vm.o vm_dump.o vm_backtrace.o vm_trace.o thread.o cont.o ascii.o us_ascii.o unicode.o utf_8.o newline.o flock.o isinf.o setproctitle.o  prelude.o dmyext.o  -lpthread -lgmp -lsocket -ldl -lcrypt -lm    -o libruby2.1.3.so.2
#unstable11x% /usr/gnu/bin/objcopy libruby2.1.3.so.2
#unstable11x% elfdump libruby2.1.3.so.2 >/dev/null
#libruby2.1.3.so.2: .SUNW_ldynsym: invalid sh_link: 0
#libruby2.1.3.so.2: .SUNW_dynsymsort: invalid sh_link: 0
#libruby2.1.3.so.2: .SUNW_ldynsym: invalid sh_link: 0
#libruby2.1.3.so.2: .SUNW_ldynsym: invalid sh_link: 0

# There is no fix for objcopy available yet and both Oracle /usr/gnu/bin/objcopy and also our own
# /opt/csw/gnu/objcopy is affected, so disable objcopy completely for now:
EXTRA_CONFIGURE_ENV += OBJCOPY=/bin/true

CONFIGURE_ARGS += $(DIRPATHS)

# Enabled DTrace support has problems during linking
CONFIGURE_ARGS += --disable-dtrace

CONFIGURE_ARGS += --program-suffix=21
CONFIGURE_ARGS += --enable-shared
CONFIGURE_ARGS += --with-soname=ruby$(API_VERSION)
#CONFIGURE_ARGS += --with-out-ext=tk


# There are tests failing
SKIPTEST ?= 1

include gar/category.mk

