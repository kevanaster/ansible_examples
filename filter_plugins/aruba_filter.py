#!/usr/bin/python
import re

class FilterModule(object):
    def filters(self):
        return {
            'aruba_negate_logging': self.aruba_negate_logging,
            'aruba_negate_firewallcp': self.aruba_negate_firewallcp
        }

    def aruba_negate_logging(self, logging_stdout, expected_commands):
        # To be used to take logging data from "show run | include 'logging ' " stdout and negate it
        negated_commands = []
        ip_regex = re.compile(r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b')
        for item in logging_stdout.splitlines():
            if item.rstrip() not in expected_commands and 'logging level' in item:
                negated_commands.append('no ' + item)
            elif item.rstrip() not in expected_commands and ip_regex.search(item):
                negated_commands.append('no logging ' + item.split()[1])
        
        return negated_commands

    def aruba_negate_firewallcp(self, firewallcp_stdout):
        return firewallcp_stdout
