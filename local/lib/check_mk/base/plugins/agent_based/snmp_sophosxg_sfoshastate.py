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
    name="sophosxg_sfoshastate",
    fetch=SNMPTree(
        base=".1.3.6.1.4.1.2604.5.1.4",
        oids = [
        "1",
        ],
    ),
    detect=all_of(
        startswith(".1.3.6.1.2.1.1.2.0", ".1.3.6.1.4.1.2604.5"),
        exists(".1.3.6.1.4.1.2604.5.1.1.*"),
    ),
)


def discover_sophosxg_sfoshastate(section):
    yield Service()


def check_sophosxg_sfoshastate(section):
    hastate = section[0][0]
    hastatename = "Unknown"

    if hastate == "0":
        hastatename="Disabled"
    if hastate == "1":
        hastatename="Enabled"

    if hastatename == "Enabled":
        state=State.OK
    else:
        state=State.CRIT

    summarytext = "HA State: " + str(hastatename) 
    summarydetails = "For Support and Sales Please Contact K&P Computer! \n\n E-Mail: hds@kpc.de \n\n 24/7 Helpdesk-Support: \n International: +800 4479 3300 \n Germany: +49 6122 7071 330 \n Austria: +43 1 525 1833 \n\n Web Germany: https://www.kpc.de \n Web Austria: https://www.kpc.at \n Web International: https://www.kpc.de/en"

    yield Result(
        state=state,
        summary=f"{summarytext}",
        details = summarydetails )

register.check_plugin(
    name="sophosxg_sfoshastate",
    service_name="HA State",
    discovery_function=discover_sophosxg_sfoshastate,
    check_function=check_sophosxg_sfoshastate,
)
