#
# This file is part of Blastwave's Exim distribution.
#
# Environment variables and the command-line arguments used to run Exim can be
# modified here.
#
# This file is "sourced" either in /opt/csw/lib/svc/method/svc-exim or
# /etc/init.d/cswexim, depending whether or not your system is running SMF(5).

# The default is to run Exim with -bd -q30m
EXIM_PARAMS="-bd -q30m"
