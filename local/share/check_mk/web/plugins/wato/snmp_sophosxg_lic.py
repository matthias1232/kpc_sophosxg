#!/usr/bin/env python3


################################################################################################################
#
# Author: Matthias Binder
# Date: 04/2023
#
# 
# Support: support@kpc.de
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
            ("warning_base_firewall", Tuple(
                title=_("Base Firewall"),
                elements=[
                    Integer(title=_("Warning when License expires in under X days"), default_value=40),
                    Integer(title=_("Critical when License expires in under X days"), default_value=30),
                    DropdownChoice(
                        title = _("State if Product ist not Licenced"),
                        help = _('default is CRIT'),
                        choices = [
                            ( "CRIT",  _("CRIT") ),
                            ( "WARN", _("WARN") ),
                            ( "OK", _("OK") ),                            
                        ],
                        default_value = "CRIT",
                    ),
                    DropdownChoice(
                        title = _("State if Product has only an Evaluation License installed"),
                        help = _('default is WARN'),
                        choices = [
                            ( "CRIT",  _("CRIT") ),
                            ( "WARN", _("WARN") ),
                            ( "OK", _("OK") ),                            
                        ],
                        default_value = "WARN",
                    ),
                    DropdownChoice(
                        title = _("State if Product is Deactivated"),
                        help = _('default is CRIT'),
                        choices = [
                            ( "CRIT",  _("CRIT") ),
                            ( "WARN", _("WARN") ),
                            ( "OK", _("OK") ),                            
                        ],
                        default_value = "CRIT",
                    ),
                ], 
            )),
            ("warning_central_orchestration", Tuple(
                title=_("Central Orchestration"),
                elements=[
                    Integer(title=_("Warning when License expires in under X days"), default_value=40),
                    Integer(title=_("Critical when License expires in under X days"), default_value=30),
                    DropdownChoice(
                        title = _("State if Product ist not Licenced"),
                        help = _('default is CRIT'),
                        choices = [
                            ( "CRIT",  _("CRIT") ),
                            ( "WARN", _("WARN") ),
                            ( "OK", _("OK") ),                            
                        ],
                        default_value = "CRIT",
                    ),
                    DropdownChoice(
                        title = _("State if Product has only an Evaluation License installed"),
                        help = _('default is WARN'),
                        choices = [
                            ( "CRIT",  _("CRIT") ),
                            ( "WARN", _("WARN") ),
                            ( "OK", _("OK") ),                            
                        ],
                        default_value = "WARN",
                    ),
                    DropdownChoice(
                        title = _("State if Product is Deactivated"),
                        help = _('default is CRIT'),
                        choices = [
                            ( "CRIT",  _("CRIT") ),
                            ( "WARN", _("WARN") ),
                            ( "OK", _("OK") ),                            
                        ],
                        default_value = "CRIT",
                    ),
                ], 
            )),  
            ("warning_email_protection", Tuple(
                title=_("Email Protection"),
                elements=[
                    Integer(title=_("Warning when License expires in under X days"), default_value=40),
                    Integer(title=_("Critical when License expires in under X days"), default_value=30),
                    DropdownChoice(
                        title = _("State if Product ist not Licenced"),
                        help = _('default is CRIT'),
                        choices = [
                            ( "CRIT",  _("CRIT") ),
                            ( "WARN", _("WARN") ),
                            ( "OK", _("OK") ),                            
                        ],
                        default_value = "CRIT",
                    ),
                    DropdownChoice(
                        title = _("State if Product has only an Evaluation License installed"),
                        help = _('default is WARN'),
                        choices = [
                            ( "CRIT",  _("CRIT") ),
                            ( "WARN", _("WARN") ),
                            ( "OK", _("OK") ),                            
                        ],
                        default_value = "WARN",
                    ),
                    DropdownChoice(
                        title = _("State if Product is Deactivated"),
                        help = _('default is CRIT'),
                        choices = [
                            ( "CRIT",  _("CRIT") ),
                            ( "WARN", _("WARN") ),
                            ( "OK", _("OK") ),                            
                        ],
                        default_value = "CRIT",
                    ),
                ],
            )),
            ("warning_enhanced_plus_support", Tuple(
                title=_("Enhanced Plus Support"),
                elements=[
                    Integer(title=_("Warning when License expires in under X days"), default_value=40),
                    Integer(title=_("Critical when License expires in under X days"), default_value=30),
                    DropdownChoice(
                        title = _("State if Product ist not Licenced"),
                        help = _('default is CRIT'),
                        choices = [
                            ( "CRIT",  _("CRIT") ),
                            ( "WARN", _("WARN") ),
                            ( "OK", _("OK") ),                            
                        ],
                        default_value = "CRIT",
                    ),
                    DropdownChoice(
                        title = _("State if Product has only an Evaluation License installed"),
                        help = _('default is WARN'),
                        choices = [
                            ( "CRIT",  _("CRIT") ),
                            ( "WARN", _("WARN") ),
                            ( "OK", _("OK") ),                            
                        ],
                        default_value = "WARN",
                    ),
                    DropdownChoice(
                        title = _("State if Product is Deactivated"),
                        help = _('default is CRIT'),
                        choices = [
                            ( "CRIT",  _("CRIT") ),
                            ( "WARN", _("WARN") ),
                            ( "OK", _("OK") ),                            
                        ],
                        default_value = "CRIT",
                    ),
                ],
            )),
            ("warning_enhanced_support", Tuple(
                title=_("Enhanced Support"),
                elements=[
                    Integer(title=_("Warning when License expires in under X days"), default_value=40),
                    Integer(title=_("Critical when License expires in under X days"), default_value=30),
                    DropdownChoice(
                        title = _("State if Product ist not Licenced"),
                        help = _('default is CRIT'),
                        choices = [
                            ( "CRIT",  _("CRIT") ),
                            ( "WARN", _("WARN") ),
                            ( "OK", _("OK") ),                            
                        ],
                        default_value = "CRIT",
                    ),
                    DropdownChoice(
                        title = _("State if Product has only an Evaluation License installed"),
                        help = _('default is WARN'),
                        choices = [
                            ( "CRIT",  _("CRIT") ),
                            ( "WARN", _("WARN") ),
                            ( "OK", _("OK") ),                            
                        ],
                        default_value = "WARN",
                    ),
                    DropdownChoice(
                        title = _("State if Product is Deactivated"),
                        help = _('default is CRIT'),
                        choices = [
                            ( "CRIT",  _("CRIT") ),
                            ( "WARN", _("WARN") ),
                            ( "OK", _("OK") ),                            
                        ],
                        default_value = "CRIT",
                    ),
                ], 
            )),
            ("warning_network_protection", Tuple(
                title=_("Network Protection"),
                elements=[
                    Integer(title=_("Warning when License expires in under X days"), default_value=40),
                    Integer(title=_("Critical when License expires in under X days"), default_value=30),
                    DropdownChoice(
                        title = _("State if Product ist not Licenced"),
                        help = _('default is CRIT'),
                        choices = [
                            ( "CRIT",  _("CRIT") ),
                            ( "WARN", _("WARN") ),
                            ( "OK", _("OK") ),                            
                        ],
                        default_value = "CRIT",
                    ),
                    DropdownChoice(
                        title = _("State if Product has only an Evaluation License installed"),
                        help = _('default is WARN'),
                        choices = [
                            ( "CRIT",  _("CRIT") ),
                            ( "WARN", _("WARN") ),
                            ( "OK", _("OK") ),                            
                        ],
                        default_value = "WARN",
                    ),
                    DropdownChoice(
                        title = _("State if Product is Deactivated"),
                        help = _('default is CRIT'),
                        choices = [
                            ( "CRIT",  _("CRIT") ),
                            ( "WARN", _("WARN") ),
                            ( "OK", _("OK") ),                            
                        ],
                        default_value = "CRIT",
                    ),
                ],
            )),
            ("warning_web_rotection", Tuple(
                title=_("Web Protection"),
                elements=[
                    Integer(title=_("Warning when License expires in under X days"), default_value=40),
                    Integer(title=_("Critical when License expires in under X days"), default_value=30),
                    DropdownChoice(
                        title = _("State if Product ist not Licenced"),
                        help = _('default is CRIT'),
                        choices = [
                            ( "CRIT",  _("CRIT") ),
                            ( "WARN", _("WARN") ),
                            ( "OK", _("OK") ),                            
                        ],
                        default_value = "CRIT",
                    ),
                    DropdownChoice(
                        title = _("State if Product has only an Evaluation License installed"),
                        help = _('default is WARN'),
                        choices = [
                            ( "CRIT",  _("CRIT") ),
                            ( "WARN", _("WARN") ),
                            ( "OK", _("OK") ),                            
                        ],
                        default_value = "WARN",
                    ),
                    DropdownChoice(
                        title = _("State if Product is Deactivated"),
                        help = _('default is CRIT'),
                        choices = [
                            ( "CRIT",  _("CRIT") ),
                            ( "WARN", _("WARN") ),
                            ( "OK", _("OK") ),                            
                        ],
                        default_value = "CRIT",
                    ),
                ],
            )), 
            ("warning_web_Server_rotection", Tuple(
                title=_("Web Server Protection"),
                elements=[
                    Integer(title=_("Warning when License expires in under X days"), default_value=40),
                    Integer(title=_("Critical when License expires in under X days"), default_value=30),
                    DropdownChoice(
                        title = _("State if Product ist not Licenced"),
                        help = _('default is CRIT'),
                        choices = [
                            ( "CRIT",  _("CRIT") ),
                            ( "WARN", _("WARN") ),
                            ( "OK", _("OK") ),                            
                        ],
                        default_value = "CRIT",
                    ),
                    DropdownChoice(
                        title = _("State if Product has only an Evaluation License installed"),
                        help = _('default is WARN'),
                        choices = [
                            ( "CRIT",  _("CRIT") ),
                            ( "WARN", _("WARN") ),
                            ( "OK", _("OK") ),                            
                        ],
                        default_value = "WARN",
                    ),
                    DropdownChoice(
                        title = _("State if Product is Deactivated"),
                        help = _('default is CRIT'),
                        choices = [
                            ( "CRIT",  _("CRIT") ),
                            ( "WARN", _("WARN") ),
                            ( "OK", _("OK") ),                            
                        ],
                        default_value = "CRIT",
                    ),
                ],
            )),
            ("warning_zero_day_protection", Tuple(
                title=_("Zero-Day Protection"),
                elements=[
                    Integer(title=_("Warning when License expires in under X days"), default_value=40),
                    Integer(title=_("Critical when License expires in under X days"), default_value=30),
                    DropdownChoice(
                        title = _("State if Product ist not Licenced"),
                        help = _('default is CRIT'),
                        choices = [
                            ( "CRIT",  _("CRIT") ),
                            ( "WARN", _("WARN") ),
                            ( "OK", _("OK") ),                            
                        ],
                        default_value = "CRIT",
                    ),
                    DropdownChoice(
                        title = _("State if Product has only an Evaluation License installed"),
                        help = _('default is WARN'),
                        choices = [
                            ( "CRIT",  _("CRIT") ),
                            ( "WARN", _("WARN") ),
                            ( "OK", _("OK") ),                            
                        ],
                        default_value = "WARN",
                    ),
                    DropdownChoice(
                        title = _("State if Product is Deactivated"),
                        help = _('default is CRIT'),
                        choices = [
                            ( "CRIT",  _("CRIT") ),
                            ( "WARN", _("WARN") ),
                            ( "OK", _("OK") ),                            
                        ],
                        default_value = "CRIT",
                    ),
                ],
            )),       
        ],
    )
   
        
rulespec_registry.register(
CheckParameterRulespecWithoutItem(
check_group_name="snmp_sophosxg_lic",
group=RulespecGroupCheckParametersOperatingSystem,
parameter_valuespec=_parameter_valuespec_snmp_sophosxg_lic,
title=lambda: _("Sophos XG - Levels for License Expiry Check"),
))