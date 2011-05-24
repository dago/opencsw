# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
# ! doesn't build yet
#   "adraw.h", line 82: warning: enumerator value overflows INT_MAX (2147483647)
#   "adraw.c", line 138: warning: implicit function declaration: round
#   "language.y", line 28: cannot find include file: <stdint.h>
#   ...
#   "language.y", line 199: warning: return value type mismatch
#   "language.y", line 200: cannot recover from previous errors
#

NAME = mscgen
VERSION = 0.20
GARTYPE = v2
CATEGORIES = utils

DESCRIPTION = Message Sequence Chart (MSC) generator
define BLURB
  Mscgen is a small program that parses Message Sequence Chart
  descriptions and produces PNG, SVG, EPS or server side image maps
  (ismaps) as the output. Message Sequence Charts (MSCs) are a way of
  representing entities and interactions over some time period and are
  often used in combination with SDL. MSCs are popular in Telecoms to
  specify how protocols operate although MSCs need not be complicated to
  create or use. Mscgen aims to provide a simple text language that is
  clear to create, edit and understand, which can also be transformed into
  common image formats for display or printing. 
endef

VENDOR_URL   = http://www.mcternan.me.uk/mscgen/
MASTER_SITES = http://www.mcternan.me.uk/mscgen/software/
DISTFILES    = $(NAME)-src-$(VERSION).tar.gz

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk
