"""
Test cases for ipaddress_handling module of net_and_server_utils
"""

import unittest
from ipaddress import AddressValueError, NetmaskValueError
import os
import io
from unittest import mock
import sys
sys.path.append('../')
from ..src.net_and_server_utils.ipaddress_handling import IPv4NetworkHandling
from ..src.net_and_server_utils.ipaddress_handling import IPv6NetworkHandling


class TestsIPAddressHandling(unittest.TestCase):
    """
    Test cases class
    """
    def setUp(self) -> None:
        """
        set up fixtures for the test cases
        :return:
        """
        self.ipaddress_ipv4_normal = '192.168.0.0/24'
        self.ipaddress_ipv4_single = '192.168.0.0/32'
        self.ipaddress_ipv4_host_bits_set = '123.45.67.89/27'
        self.ipaddress_ipv4_invalid_address = '256.0.0.0/27'
        self.ipaddress_ipv4_invalid_netmask = '192.168.0.0/33'
        self.ipaddress_ipv6_normal = '2001:db00::0/112'
        self.ipaddress_ipv6_host_bit_set = '2001:db00::0/16'
        self.filename_for_ipaddresses_ipv4 = 'ipaddresses_ipv4.txt'
        self.filename_for_ipaddresses_ipv6 = 'ipaddresses_ipv6.txt'

    def test_network_ip_address_ipv4(self):
        """
        tests the ipv4 network class for normal network address
        """
        addr = IPv4NetworkHandling(self.ipaddress_ipv4_normal)
        self.assertEqual(addr.version(), 4)
        self.assertEqual(addr.max_prefixlen(), 32)
        self.assertEqual(addr.network_address(), '192.168.0.0')
        self.assertEqual(addr.netmask(), '255.255.255.0')

    def test_host_bit_set_ipv4(self):
        """
        tests the case where the address given has host bits set
        """
        addr = IPv4NetworkHandling(self.ipaddress_ipv4_host_bits_set)
        self.assertEqual(addr.version(), 4)
        self.assertEqual(addr.max_prefixlen(), 32)
        self.assertEqual(addr.network_address(), '123.45.67.64')
        self.assertEqual(addr.netmask(), '255.255.255.224')

    def test_address_value_error_ipv4(self):
        """
        tests for value error in case of wrong address given
        """
        with self.assertRaises(AddressValueError):
            _ = IPv4NetworkHandling(self.ipaddress_ipv4_invalid_address)

    def test_net_mask_value_error_ipv4(self):
        """
        tests for net mask value in case of wrong net mask
        """
        with self.assertRaises(NetmaskValueError):
            _ = IPv4NetworkHandling(self.ipaddress_ipv4_invalid_netmask)

    def test_ipv4_addresses_print(self):
        """
        tests ip addresses print function
        """
        addr = IPv4NetworkHandling(self.ipaddress_ipv4_single)
        with mock.patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            addr.print_all_ipaddress_included()
        self.assertEqual(list(fake_stdout.getvalue().split('\n'))[1], '192.168.0.0')

    def test_write_to_file_ipv4(self):
        """
        tests whether the ip addresses are written to file correctly or not
        """
        addr = IPv4NetworkHandling(self.ipaddress_ipv4_normal)
        addr.write_to_file_ipaddresses_included(self.filename_for_ipaddresses_ipv4)
        self.assertTrue(os.path.exists(self.filename_for_ipaddresses_ipv4))
        count = addr.count_number_of_ipaddresses()
        self.assertEqual(count, 256)

    def test_ipaddress_ipv6_ipv6_handling(self):
        """
        tests ipv6 network class with normal ipv6 network address
        """
        addr = IPv6NetworkHandling(self.ipaddress_ipv6_normal)
        self.assertEqual(addr.version(), 6)
        self.assertEqual(addr.max_prefixlen(), 128)
        self.assertEqual(addr.network_address(), '2001:db00:0000:0000:0000:0000:0000:0000')
        self.assertEqual(addr.netmask(), 'ffff:ffff:ffff:ffff:ffff:ffff:ffff:0000')

    def test_ipaddress_ipv6_host_bits_set(self):
        """
        tests the ipv6 class with address having hosts bit set
        """
        addr = IPv6NetworkHandling(self.ipaddress_ipv6_host_bit_set)
        self.assertEqual(addr.version(), 6)
        self.assertEqual(addr.max_prefixlen(), 128)
        self.assertEqual(addr.network_address(), '2001:0000:0000:0000:0000:0000:0000:0000')
        self.assertEqual(addr.netmask(), 'ffff:0000:0000:0000:0000:0000:0000:0000')

    def test_ipv6_addresses_write_to_file(self):
        """
        tests whether the ip addresses are written to file correctly or not
        """
        addr = IPv6NetworkHandling(self.ipaddress_ipv6_normal)
        addr.write_to_file_ipaddresses_included(self.filename_for_ipaddresses_ipv6)
        self.assertTrue(os.path.exists(self.filename_for_ipaddresses_ipv6))
        count = addr.count_number_of_ipaddresses()
        self.assertEqual(count, 65536)

    def test_ipaddress_ipv6_with_ipv4_handling(self):
        """
        tests for value error
        In case where ipv6 address is passed to ipv4 class
        """
        with self.assertRaises(AddressValueError):
            _ = IPv4NetworkHandling(self.ipaddress_ipv6_normal)

    def test_ipaddress_ipv4_with_ipv6_handling(self):
        """
        tests for value error
        In case when ipv4 address is passed to ipv6 class
        """
        with self.assertRaises(AddressValueError):
            _ = IPv6NetworkHandling(self.ipaddress_ipv4_normal)

    def tearDown(self) -> None:
        """
        tear down fixture for test cases
        """
        del self.ipaddress_ipv4_normal
        del self.ipaddress_ipv4_host_bits_set
        del self.ipaddress_ipv4_invalid_address
        del self.ipaddress_ipv4_invalid_netmask
        del self.filename_for_ipaddresses_ipv4


if __name__ == '__main__':
    unittest.main()
