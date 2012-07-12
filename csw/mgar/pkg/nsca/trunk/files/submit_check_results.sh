#!/bin/sh

# Arguments:
#  $1 = host_name (Short name of host the service is
#       associated with)
#  $2 = svc_description (Description of the service)
#  $3 = state_string (A string representing the status of
#       the given service - "OK", "WARNING", "CRITICAL"
#       or "UNKNOWN")
#  $4 = plugin_output (A text string that should be used
#       as the plugin output for the service checks)
#

# Don't forget to set this variable!
CENTRAL_NAGIOS_SERVER=myhost

# Convert the state string to the corresponding return code
return_code=-1

case "$3" in
        OK)
        return_code=0
                    ;;
                WARNING)
                    return_code=1
                        ;;
                CRITICAL)
                    return_code=2
                        ;;
                UNKNOWN)
                    return_code=-1
                        ;;
        esac

# pipe the service check info into the send_nsca program, which
# in turn transmits the data to the nsca daemon on the central
# monitoring server

/usr/bin/echo "$1\t$2\t$return_code\t$4" |  /opt/csw/nagios/bin/send_nsca $CENTRAL_NAGIOS_SERVER -c /etc/opt/csw/nagios/send_nsca.cfg
