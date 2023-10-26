#!/usr/bin/env python3
# -*- coding: utf-8 -*-
################################################################################################################
#
# Author: K&P Computer Service- und Vertriebs-GmbH
# Author: Matthias Binder
# License: GNU General Public License
# Date: 05/2023
#
# 
# For Support and Sales Please Contact K&P Computer!
#
# E-Mail: hds@kpc.de
#
# 24/7 Helpdesk-Support:
# International: +800 4479 3300
# Germany: +49 6122 7071 330
# Austria: +43 1 525 1833
#
# Web Germany: https://www.kpc.de
# Web Austria: https://www.kpc.at
# Web International: https://www.kpc.de/en
#
################################################################################################################
import time

from .agent_based_api.v1 import (
    all_of,
    startswith,
    exists,
    Metric,
    register,
    Result,
    Service,
    SNMPTree,
    State,
    get_value_store,
    render,
)



register.snmp_section(
    name="sophosxg_version",
    fetch=SNMPTree(
        base=".1.3.6.1.4.1.2604.5.1.1",
        oids = [
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        ],
    ),
    detect=all_of(
        startswith(".1.3.6.1.2.1.1.2.0", ".1.3.6.1.4.1.2604.5"),
        exists(".1.3.6.1.4.1.2604.5.1.1.*"),
    ),
)


def discover_sophosxg_version(section):
    yield Service()


def check_sophosxg_version(params, section):
    devicename = section[0][0]
    devicetype = section[0][1]
    devicefwversion = section[0][2]
    deviceappkey = section[0][3]
    webcatversion = section[0][4]
    ipsversion = section[0][5]

    warning_firmware_check = params["warning_firmware_check"][0]
    
    if devicefwversion == warning_firmware_check or warning_firmware_check == "0":
        s=State.OK
    else:
        s=State.WARN
        summarytext = "Firmware version " + str(devicefwversion) + "  is not expected version " + "(" + warning_firmware_check + ")" + " Device Name: " + str(devicename) + ", Device Type: " + str(devicetype) + " (more infos in Summary)"

    if s == State.OK:
        summarytext = "Device Name: " + str(devicename) + ", Device Type: " + str(devicetype) + ", Firmware Version: " + str(devicefwversion) + " (more infos in Summary)"
    
    summarydetails = "Device Name: " + str(devicename) + "\n" + "Device Type: " + str(devicetype) + "\n" + "Firmware Version: " + str(devicefwversion) + "\n" + "Device App Key: " + str(deviceappkey) + "\n" + "Webcat Version: " + str(webcatversion)+ "\n" + "IPS Version: " + str(ipsversion) + "\n" + "\n\n" + "This Check is always OK and just shows the Information of the Device" + "\n\n" + "For Sales and Support Contact K&P Computer! \n\n E-Mail: hds@kpc.de \n\n 24/7 Helpdesk-Support: \n International: +800 4479 3300 \n Germany: +49 6122 7071 330 \n Austria: +43 1 525 1833 \n\n Web Germany: https://www.kpc.de \n Web Austria: https://www.kpc.at \n Web International: https://www.kpc.de/en"

    yield Result(
        state=s,
        summary=f"{summarytext}",
        details = summarydetails )

register.check_plugin(
    name="sophosxg_version",
    service_name="Sophos Device Info",
    discovery_function=discover_sophosxg_version,
    check_function=check_sophosxg_version,
    check_default_parameters={'warning_firmware_check' : ("0")},
    check_ruleset_name="snmp_sophosxg_version",
)
