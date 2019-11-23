This repo will contain ansible examples that I have written for Aruba, Cisco, and Juniper networking devices.



filter_plugins/aruba.py
-----------------------

This is a filter written to negate commands that are gathered from a `show run`. This is built to deal with removing configurations that cannot be easily removed with a generic statement using a `before:` statement

TODO: Create the firewall cp function


