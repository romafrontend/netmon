from django.test import TestCase

from .models import CoreNetworkObject
# Create your tests here.


class CoreNetworkObjectMethodTests(TestCase):
    def test_auto_fulfill_if_external_ipv4(self):
        ''' check what happen if web_address is https://tradeinter.dyndns.org and port='23' '''
        # create network object
        c = CoreNetworkObject(
            web_address="https://tradeinter.dyndns.org",
            cli_access_port="23",
            login="admin",
            password="Sat%io2262",
            site_name_id=1,
            spec_model_id=3,
        )

        # First we create/find pattern of one key field, and then use it to autofill another fields
        c.pattern_web_address()

        # flag and loop we need to check that everything is fine with autofullillment
        flag = False
        if c.cli_address == "tradeinter.dyndns.org:23" and c.ipv4_external_address == "" \
                and c.dns_address == "tradeinter.dyndns.org":
            flag = True

        self.assertIs(flag, True)

    def test_auto_fulfill_if_external_dns(self):
        ''' check what happen if web_address is https://1.1.1.1 and port='22' '''
        # create network object
        c = CoreNetworkObject(
            web_address="https://1.1.1.1",
            cli_access_port="22",
            login="admin",
            password="Sat%io2262",
            site_name_id=1,
            spec_model_id=3,
        )

        # First we create/find pattern of one key field, and then use it to autofill another fields
        c.pattern_web_address()

        # flag and loop we need to check that everything is fine with autofullillment
        flag = False
        if c.cli_address == "1.1.1.1:22" and c.ipv4_external_address == "1.1.1.1" and c.dns_address == "":
            flag = True

        self.assertIs(flag, True)
