#!/usr/bin/env python3
# -*- coding: utf-8 -*-
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
    name="sophosxg_lic_webprotection",
    fetch=SNMPTree(
        base=".1.3.6.1.4.1.2604.5.1.5.3",
        oids = [
        "1",
        "2",
        ],
    ),
    detect=all_of(
        startswith(".1.3.6.1.2.1.1.2.0", ".1.3.6.1.4.1.2604.5"),
        exists(".1.3.6.1.4.1.2604.5.1.1.*"),
    ),
)


def discover_sophosxg_lic_webprotection(section):
    yield Service()


def check_sophosxg_lic_webprotection(section):
    licstate = section[0][0]
    licstatename = "Unknown"
    licexpire = section[0][1]
    licexpirename = "Unknown"

    if licstate == "0":
        licstatename="None"
        licexpirename = "None"
    if licstate == "1":
        licstatename="Evaluation"
        licexpirename = licexpire
    if licstate == "2":
        licstatename="Not Subscribed"
        licexpirename = "Not Subscribed"
    if licstate == "3":
        licstatename="Subscribed"
        licexpirename = licexpire
    if licstate == "4":
        licstatename="Expired"
        licexpirename = licexpire
    if licstate == "5":
        licstatename="Deactivated"
        licexpirename = licexpire

    summarytext = "License: " + str(licstatename) + " Expire Date: " + str(licexpirename) + " (0000 days left)" 
    summarydetails = "For Support and Sales Please Contact K&P Computer! \n\n E-Mail: hds@kpc.de \n\n 24/7 Helpdesk-Support: \n International: +800 4479 3300 \n Germany: +49 6122 7071 330 \n Austria: +43 1 525 1833 \n\n Web Germany: https://www.kpc.de \n Web Austria: https://www.kpc.at \n Web International: https://www.kpc.de/en"

    yield Result(
        state=State.OK,
        summary=f"{summarytext} (Check Details if you need Help)",
        details = summarydetails )

register.check_plugin(
    name="sophosxg_lic_webprotection",
    service_name="License Web Protection",
    discovery_function=discover_sophosxg_lic_webprotection,
    check_function=check_sophosxg_lic_webprotection,
)
