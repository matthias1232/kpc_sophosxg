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
from datetime import datetime, timedelta



register.snmp_section(
    name="sophosxg_lic_enhancedsupport",
    fetch=SNMPTree(
        base=".1.3.6.1.4.1.2604.5.1.5.7",
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


def discover_sophosxg_lic_enhancedsupport(section):
    yield Service()


def check_sophosxg_lic_enhancedsupport(params, section):
    warn = params["warning_enhanced_support"][0]
    crit = params["warning_enhanced_support"][1]
    unlicensed = params["warning_enhanced_support"][2]
    evallicense = params["warning_enhanced_support"][3]
    deactivatedlicense = params["warning_enhanced_support"][4]
    
    licstate = section[0][0]
    licexpire = section[0][1]
     

    if licstate == "0":
        licstatename="None"
        licexpirename = "None"
    elif licstate == "1":
        licstatename="Evaluation"
        licexpirename = licexpire
    elif licstate == "2":
        licstatename="Not Subscribed"
        licexpirename = "Not Subscribed"
    elif licstate == "3":
        licstatename="Subscribed"
        licexpirename = licexpire
    elif licstate == "4":
        licstatename="Expired"
        licexpirename = licexpire
    elif licstate == "5":
        licstatename="Deactivated"
        licexpirename = licexpire
    else:
        licexpirename = "Unknown"
        licstatename = "Unknown"

    if  licstate == '1' or licstate == '3' or licstate == '4' or licstate == '5' :
         now = datetime.now()
         date = licexpire
         date = datetime.strptime(date, '%b %d %Y')
         datedifference = date - datetime.now()
         datedifference_days = int(datedifference.days)
    else:
         datedifference_days = "9999999999"



    #Testing
    #datedifference_days = 25

    if licstate == "0":
        state = State.CRIT
        summarytext = "License: " + str(licstatename)
        summarydetails = "For Support und Sales Please Contact K&P Computer! \n\n E-Mail: hds@kpc.de \n\n 24/7 Helpdesk-Support: \n International: +800 4479 3300 \n Germany: +49 6122 7071 330 \n Austria: +43 1 525 1833 \n\n Web Germany: https://www.kpc.de \n Web Austria: https://www.kpc.at \n Web International: https://www.kpc.de/en"
        summarytext = "License: " + str(licstatename) + ", Expire Date: " + str(licexpirename) + " (" + str(datedifference_days) + " days left)" 
        summarydetails = "For Support und Sales Please Contact K&P Computer! \n\n E-Mail: hds@kpc.de \n\n 24/7 Helpdesk-Support: \n International: +800 4479 3300 \n Germany: +49 6122 7071 330 \n Austria: +43 1 525 1833 \n\n Web Germany: https://www.kpc.de \n Web Austria: https://www.kpc.at \n Web International: https://www.kpc.de/en"

    if licstate == "1":
        if evallicense == "CRIT":
            state = State.CRIT
        if evallicense == "WARN":
            state = State.WARN
        if evallicense == "OK":
            state = State.OK

        if datedifference_days <= crit:
            state = State.CRIT
            summarytext = "License: " + str(licstatename) + ", Expire Date: " + str(licexpirename) + " (" + str(datedifference_days) + " days left)" 
            summarydetails = "For Support und Sales Please Contact K&P Computer! \n\n E-Mail: hds@kpc.de \n\n 24/7 Helpdesk-Support: \n International: +800 4479 3300 \n Germany: +49 6122 7071 330 \n Austria: +43 1 525 1833 \n\n Web Germany: https://www.kpc.de \n Web Austria: https://www.kpc.at \n Web International: https://www.kpc.de/en"
        elif datedifference_days <= warn:
            if state != State.CRIT:
                state = State.WARN
            summarytext = "License: " + str(licstatename) + ", Expire Date: " + str(licexpirename) + " (" + str(datedifference_days) + " days left)" 
            summarydetails = "For Support und Sales Please Contact K&P Computer! \n\n E-Mail: hds@kpc.de \n\n 24/7 Helpdesk-Support: \n International: +800 4479 3300 \n Germany: +49 6122 7071 330 \n Austria: +43 1 525 1833 \n\n Web Germany: https://www.kpc.de \n Web Austria: https://www.kpc.at \n Web International: https://www.kpc.de/en"
        else:
            if state != State.CRIT and state != State.WARN:
                state = State.OK
            summarytext = "License: " + str(licstatename) + ", Expire Date: " + str(licexpirename) + " (" + str(datedifference_days) + " days left)" 
            summarydetails = "For Support und Sales Please Contact K&P Computer! \n\n E-Mail: hds@kpc.de \n\n 24/7 Helpdesk-Support: \n International: +800 4479 3300 \n Germany: +49 6122 7071 330 \n Austria: +43 1 525 1833 \n\n Web Germany: https://www.kpc.de \n Web Austria: https://www.kpc.at \n Web International: https://www.kpc.de/en"

    if licstate == "2":
        if unlicensed == "CRIT":
            state = State.CRIT
        if unlicensed == "WARN":
            state = State.WARN
        if unlicensed == "OK":
            state = State.OK
        summarytext = "License: " + str(licstatename)
        summarydetails = "For Support und Sales Please Contact K&P Computer! \n\n E-Mail: hds@kpc.de \n\n 24/7 Helpdesk-Support: \n International: +800 4479 3300 \n Germany: +49 6122 7071 330 \n Austria: +43 1 525 1833 \n\n Web Germany: https://www.kpc.de \n Web Austria: https://www.kpc.at \n Web International: https://www.kpc.de/en"
            
    if licstate == "3" or licstate == "4":
        state = State.OK
        if licstate == "4":
            state = State.CRIT
        if datedifference_days <= crit:
            state = State.CRIT
            summarytext = "License: " + str(licstatename) + ", Expire Date: " + str(licexpirename) + " (" + str(datedifference_days) + " days left)" 
            summarydetails = "For Support und Sales Please Contact K&P Computer! \n\n E-Mail: hds@kpc.de \n\n 24/7 Helpdesk-Support: \n International: +800 4479 3300 \n Germany: +49 6122 7071 330 \n Austria: +43 1 525 1833 \n\n Web Germany: https://www.kpc.de \n Web Austria: https://www.kpc.at \n Web International: https://www.kpc.de/en"
        elif datedifference_days <= warn:
            if state != State.CRIT:
                state = State.WARN
            summarytext = "License: " + str(licstatename) + ", Expire Date: " + str(licexpirename) + " (" + str(datedifference_days) + " days left)" 
            summarydetails = "For Support und Sales Please Contact K&P Computer! \n\n E-Mail: hds@kpc.de \n\n 24/7 Helpdesk-Support: \n International: +800 4479 3300 \n Germany: +49 6122 7071 330 \n Austria: +43 1 525 1833 \n\n Web Germany: https://www.kpc.de \n Web Austria: https://www.kpc.at \n Web International: https://www.kpc.de/en"
        else:
            if state != State.CRIT and state != State.WARN:
                state = State.OK
            summarytext = "License: " + str(licstatename) + ", Expire Date: " + str(licexpirename) + " (" + str(datedifference_days) + " days left)" 
            summarydetails = "For Support und Sales Please Contact K&P Computer! \n\n E-Mail: hds@kpc.de \n\n 24/7 Helpdesk-Support: \n International: +800 4479 3300 \n Germany: +49 6122 7071 330 \n Austria: +43 1 525 1833 \n\n Web Germany: https://www.kpc.de \n Web Austria: https://www.kpc.at \n Web International: https://www.kpc.de/en"
 
    if licstate == "5":
        if deactivatedlicense == "CRIT":
            state = State.CRIT
        if deactivatedlicense == "WARN":
            state = State.WARN
        if deactivatedlicense == "OK":
            state = State.OK

        if datedifference_days <= crit:
            state = State.CRIT
            summarytext = "License: " + str(licstatename) + ", Expire Date: " + str(licexpirename) + " (" + str(datedifference_days) + " days left)" 
            summarydetails = "For Support und Sales Please Contact K&P Computer! \n\n E-Mail: hds@kpc.de \n\n 24/7 Helpdesk-Support: \n International: +800 4479 3300 \n Germany: +49 6122 7071 330 \n Austria: +43 1 525 1833 \n\n Web Germany: https://www.kpc.de \n Web Austria: https://www.kpc.at \n Web International: https://www.kpc.de/en"
        elif datedifference_days <= warn:
            if state != State.CRIT:
                state = State.WARN
            summarytext = "License: " + str(licstatename) + ", Expire Date: " + str(licexpirename) + " (" + str(datedifference_days) + " days left)" 
            summarydetails = "For Support und Sales Please Contact K&P Computer! \n\n E-Mail: hds@kpc.de \n\n 24/7 Helpdesk-Support: \n International: +800 4479 3300 \n Germany: +49 6122 7071 330 \n Austria: +43 1 525 1833 \n\n Web Germany: https://www.kpc.de \n Web Austria: https://www.kpc.at \n Web International: https://www.kpc.de/en"
        else:
            if state != State.CRIT and state != State.WARN:
                state = State.OK
            summarytext = "License: " + str(licstatename) + ", Expire Date: " + str(licexpirename) + " (" + str(datedifference_days) + " days left)" 
            summarydetails = "For Support und Sales Please Contact K&P Computer! \n\n E-Mail: hds@kpc.de \n\n 24/7 Helpdesk-Support: \n International: +800 4479 3300 \n Germany: +49 6122 7071 330 \n Austria: +43 1 525 1833 \n\n Web Germany: https://www.kpc.de \n Web Austria: https://www.kpc.at \n Web International: https://www.kpc.de/en" 
    
    if licstatename == "Unknown" or licexpirename == "Unknown" :
        state = State.CRIT
        summarytext = "Unknown Error! License: " + str(licstatename) + ", Expire Date: " + str(licexpirename)
        summarydetails = "For Support und Sales Please Contact K&P Computer! \n\n E-Mail: hds@kpc.de \n\n 24/7 Helpdesk-Support: \n International: +800 4479 3300 \n Germany: +49 6122 7071 330 \n Austria: +43 1 525 1833 \n\n Web Germany: https://www.kpc.de \n Web Austria: https://www.kpc.at \n Web International: https://www.kpc.de/en"



    yield Result(
        state=state,
        summary=f"{summarytext}",
        details = summarydetails )

register.check_plugin(
    name="sophosxg_lic_enhancedsupport",
    service_name="License Enhanced Support",
    discovery_function=discover_sophosxg_lic_enhancedsupport,
    check_function=check_sophosxg_lic_enhancedsupport,
    check_default_parameters={'warning_enhanced_support' : (40,30,"CRIT","WARN","CRIT")},
    check_ruleset_name="snmp_sophosxg_lic",
)

