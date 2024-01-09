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

from cmk.gui.i18n import _

# import required to register agent
from cmk.gui.plugins.wato import (
    rulespec_registry,
    HostRulespec,
    CheckParameterRulespecWithoutItem,
    RulespecGroupCheckParametersOperatingSystem
)

from cmk.gui.valuespec import (
    FixedValue,
    TextInput,
    Age,
    ListOfStrings,
    DropdownChoice,
    Tuple,
    Integer,
    ListChoice,
)

# import structure where special agent will be registered
from cmk.gui.plugins.wato.datasource_programs import RulespecGroupDatasourcePrograms


 
def _parameter_valuespec_snmp_sophosxg_lic():
    return Dictionary(
        elements=[
            ("warning_firmware_check", Tuple(
                title=_("Firmware Check"),
                elements=[
                    TextInput(title=_("Warning when Firmware is not this expected version"), default_value="0"),
                ], 
            )),     
        ],
    )
   
        
rulespec_registry.register(
CheckParameterRulespecWithoutItem(
check_group_name="snmp_sophosxg_version",
group=RulespecGroupCheckParametersOperatingSystem,
parameter_valuespec=_parameter_valuespec_snmp_sophosxg_lic,
title=lambda: _("Sophos XG - Device Info and Firmware"),
))
