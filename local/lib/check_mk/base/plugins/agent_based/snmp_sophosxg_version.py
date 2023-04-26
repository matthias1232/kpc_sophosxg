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
    name="sophosxg_version",
    fetch=SNMPTree(
        base=".1.3.6.1.4.1.2604.5.1.1",
        oids=["3"],
    ),
    detect=all_of(
        startswith(".1.3.6.1.2.1.1.2.0", ".1.3.6.1.4.1.2604.5"),
        exists(".1.3.6.1.4.1.2604.5.1.1.*"),
    ),
)


def discover_sophosxg_version(section):
    yield Service()


def check_sophosxg_version(section):
    version = section[0][0]

    summarytext = "Version: " + str(version)
    summarydetails = "For Update Support Contact K&P Computer! \n\n E-Mail: hds@kpc.de \n\n 24/7 Helpdesk-Support: \n International: +800 4479 3300 \n Germany: +49 6122 7071 330 \n Austria: +43 1 525 1833 \n\n Web Germany: https://www.kpc.de \n Web Austria: https://www.kpc.at \n Web International: https://www.kpc.de/en"

    yield Result(
        state=State.OK,
        summary=f"{version} (Check Details if you need Update Support)",
        details = summarydetails )

register.check_plugin(
    name="sophosxg_version",
    service_name="Firmware Version",
    discovery_function=discover_sophosxg_version,
    check_function=check_sophosxg_version,
)
