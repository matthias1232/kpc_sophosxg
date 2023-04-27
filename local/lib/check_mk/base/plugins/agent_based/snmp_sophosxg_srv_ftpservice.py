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
    name="sophosxg_srv_ftpservice",
    fetch=SNMPTree(
        base=".1.3.6.1.4.1.2604.5.1.3",
        oids = [
        "4",
        ],
    ),
    detect=all_of(
        startswith(".1.3.6.1.2.1.1.2.0", ".1.3.6.1.4.1.2604.5"),
        exists(".1.3.6.1.4.1.2604.5.1.1.*"),
    ),
)


def discover_sophosxg_srv_ftpservice(section):
    yield Service()


def check_sophosxg_srv_ftpservice(section):
    srvstate = section[0][0]
    srvstatename = "Unknown"

    if srvstate == "0":
        srvstatename="Untouched"
    if srvstate == "1":
        srvstatename="Stopped"
    if srvstate == "2":
        srvstatename="Initializing"
    if srvstate == "3":
        srvstatename="Running"
    if srvstate == "4":
        srvstatename="Exiting"
    if srvstate == "5":
        srvstatename="Dead"
    if srvstate == "6":
        srvstatename="Frozen"      
    if srvstate == "7":
        srvstatename="Unregistered"
        
    if srvstatename == "Running":
        state=State.OK
    else:
        state=State.CRIT

    summarytext = "State: " + str(srvstatename) 
    summarydetails = "For Support and Sales Please Contact K&P Computer! \n\n E-Mail: hds@kpc.de \n\n 24/7 Helpdesk-Support: \n International: +800 4479 3300 \n Germany: +49 6122 7071 330 \n Austria: +43 1 525 1833 \n\n Web Germany: https://www.kpc.de \n Web Austria: https://www.kpc.at \n Web International: https://www.kpc.de/en"

    yield Result(
        state=state,
        summary=f"{summarytext} (Check Details if you need Help)",
        details = summarydetails )

register.check_plugin(
    name="sophosxg_srv_ftpservice",
    service_name="Service FTP",
    discovery_function=discover_sophosxg_srv_ftpservice,
    check_function=check_sophosxg_srv_ftpservice,
)
