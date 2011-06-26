# $Id$
NAME = sipcalc
VERSION = 1.1.5
CATEGORIES = net

DESCRIPTION = Advanced console-based ip subnet calculator
define BLURB
  Sipcalc is an advanced console-based IP subnet calculator. It can take
  multiple forms of input (IPv4/IPv6/interface/hostname) and output a
  multitude of information about a given subnet.
  
  Features include:
   - IPv4
    * Retrieving of address information from interfaces.
    * Classfull and CIDR output.
    * Multiple address and netmask input and output formats (dotted
      quad, hex, number of bits).
    * Output of broadcast address, network class, Cisco wildcard, hosts/range,
      network range.
    * The ability to "split" a network based on a smaller netmask, now also with
      recursive runs on the generated subnets. (also IPv6)
   - IPv6
    * Compressed and expanded input and output addresses.
    * Standard IPv6 network output.
    * v4 in v6 output.
    * Reverse DNS address generation.
endef

MASTER_SITES = http://www.routemeister.net/projects/sipcalc/files/
DISTFILES  = $(NAME)-$(VERSION).tar.gz

# File name regex to get notifications about upstream software releases
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

RUNTIME_DEP_PKGS_CSWsipcalc += CSWlibgnugetopt

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk
