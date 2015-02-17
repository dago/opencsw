# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = check_mk
#VERSION = 1.2.0p3
VERSION = 1.2.1i3
GARTYPE = v2

DESCRIPTION = A new general purpose Nagios-plugin for retrieving data

MASTER_SITES = http://mathias-kettner.de/download/
DISTFILES += $(DISTNAME).tar.gz

PATCHFILES += 0001-Solaris-header-fixes.patch

VENDOR_URL = http://mathias-kettner.de/check_mk.html

PACKAGES += CSWnagios-plugin-mk-livestatus
SPKG_DESC_CSWnagios-plugin-mk-livestatus = A new general purpose Nagios-plugin for retrieving data
# PKGFILES is catchall

# ~/.check_mk_setup.conf

#    VARNAME=$1
#    DEF_ROOT=$2
#    DEF_USER=$3
#    DEF_OMD=$4
#    SHORT=$5
#    DESCR=$6

# ask_dir bindir /usr/bin $HOMEBASEDIR/bin $OMD_ROOT/local/bin "Executable programs" \
# ask_dir confdir /etc/$NAME $HOMEBASEDIR $OMD_ROOT/etc/check_mk "Check_MK configuration" \
# ask_dir sharedir /usr/share/$NAME $HOMEBASEDIR $OMD_ROOT/local/share/check_mk "Check_MK software" \
# ask_dir docdir /usr/share/doc/$NAME $HOMEBASEDIR/doc $OMD_ROOT/local/share/check_mk/doc "documentation" \
# ask_dir checkmandir /usr/share/doc/$NAME/checks $HOMEBASEDIR/doc/checks $OMD_ROOT/local/share/check_mk/checkman "check manuals" \
# ask_dir vardir /var/lib/$NAME $HOMEBASEDIR/var $OMD_ROOT/var/check_mk "working directory of check_mk" \
# ask_dir agentslibdir /usr/lib/check_mk_agent $HOMEBASEDIR/check_mk_agent /usr/lib/check_mk_agent "extensions for agents" \
# ask_dir agentsconfdir /etc/check_mk $HOMEBASEDIR /etc/check_mk "configuration dir for agents" \
# ask_dir -d nagiosuser nagios $(id -un) "$OMD_SITE" "Name of Nagios user" \
# ask_dir -d wwwuser www-data www-data "$OMD_SITE" "User of Apache process" \
# ask_dir -d wwwgroup nagios $(id -un) "$OMD_SITE" "Common group of Nagios+Apache" \
# ask_dir nagios_binary /usr/sbin/nagios $HOMEBASEDIR/nagios/bin/nagios $OMD_ROOT/bin/nagios "Nagios binary" \
# ask_dir nagios_config_file /etc/nagios/nagios.cfg $HOMEBASEDIR/nagios/etc/nagios.cfg $OMD_ROOT/tmp/nagios/nagios.cfg "Nagios main configuration file" \
# ask_dir nagconfdir /etc/nagios/objects $HOMEBASEDIR/nagios/etc $OMD_ROOT/etc/nagios/conf.d "Nagios object directory" \
# ask_dir nagios_startscript /etc/init.d/nagios /etc/init.d/nagios $OMD_ROOT/etc/init.d/nagios "Nagios startskript" \
# ask_dir nagpipe /var/log/nagios/rw/nagios.cmd $HOMEBASEDIR/var/nagios/rw/nagios.cmd $OMD_ROOT/tmp/run/nagios.cmd "Nagios command pipe" \
# ask_dir check_result_path /usr/local/nagios/var/spool/checkresults $HOMEBASEDIR/var/nagios/checkresults $OMD_ROOT/tmp/nagios/checkresults "Check results directory" \
# ask_dir nagios_status_file /var/log/nagios/status.dat /var/log/nagios/status.dat $OMD_ROOT/tmp/nagios/status.dat "Nagios status file" \
# ask_dir check_icmp_path /usr/lib/nagios/plugins/check_icmp $HOMEBASEDIR/libexec/check_icmp $OMD_ROOT/lib/nagios/plugins/check_icmp "Path to check_icmp" \
# ask_dir -d url_prefix / / /$OMD_SITE/ "URL Prefix for Web addons" \
# ask_dir apache_config_dir /etc/apache2/conf.d /etc/apache2/conf.d $OMD_ROOT/etc/apache/conf.d "Apache config dir" \
# ask_dir htpasswd_file /etc/nagios/htpasswd.users $HOMEBASEDIR/etc/htpasswd.users $OMD_ROOT/etc/htpasswd "HTTP authentication file" \
# ask_dir -d nagios_auth_name "Nagios Access" "Nagios Access" "OMD Monitoring Site $OMD_SITE" "HTTP AuthName" \
# ask_dir pnptemplates /usr/share/$NAME/pnp-templates $HOMEBASEDIR/pnp-templates $OMD_ROOT/local/share/check_mk/pnp-templates "PNP4Nagios templates" \
# ask_dir -d enable_livestatus yes yes yes "compile livestatus module" \
#   ask_dir libdir /usr/lib/$NAME $HOMEBASEDIR/lib $OMD_ROOT/local/lib/mk-livestatus "check_mk's binary modules" \
#   ask_dir livesock ${nagpipe%/*}/live ${nagpipe%/*}/live $OMD_ROOT/tmp/run/live "Unix socket for Livestatus" \
#   ask_dir livebackendsdir /usr/share/$NAME/livestatus $HOMEBASEDIR/livestatus $OMD_ROOT/local/share/mk-livestatus "Backends for other systems" \

GARCOMPILER = GCC4

EXTRA_LDFLAGS += -lsocket  -lnsl

# The issued command "which diet" is on Solaris /usr/bin/diet which always returns 0 and therefore always enable diet mode
REINPLACE_MATCH = .*diet.*
REINPLACE_WITH = if false; then
REINPLACE_FILES += configure

include gar/category.mk

post-extract-modulated:
	-cd $(WORKSRC) && gtar zxvf livestatus.tar.gz
	@$(MAKECOOKIE)
