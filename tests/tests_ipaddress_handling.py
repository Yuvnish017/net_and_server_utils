import unittest
from ipaddress import AddressValueError, NetmaskValueError
import os

from network_utils.src.net_and_server_utils.ipaddress_handling import IPv4NetworkHandling, IPv6NetworkHandling


class TestsIPAddressHandling(unittest.TestCase):
    def setUp(self) -> None:
        self.ipaddress_ipv4_normal = '192.168.0.0/24'
        self.ipaddress_ipv4_host_bits_set = '123.45.67.89/27'
        self.ipaddress_ipv4_invalid_address = '256.0.0.0/27'
        self.ipaddress_ipv4_invalid_netmask = '192.168.0.0/33'
        self.ipaddress_ipv6_normal = '2001:db00::0/112'
        self.ipaddress_ipv6_host_bit_set = '2001:db00::0/16'
        self.filename_for_ipaddresses_ipv4 = 'ipaddresses_ipv4.txt'
        self.filename_for_ipaddresses_ipv6 = 'ipaddresses_ipv6.txt'

    def test_class_imports(self):
        IPv4NetworkHandling(self.ipaddress_ipv4_normal)

    def test_network_ip_address_ipv4(self):
        addr = IPv4NetworkHandling(self.ipaddress_ipv4_normal)
        self.assertEqual(addr.version(), 4)
        self.assertEqual(addr.max_prefixlen(), 32)
        self.assertEqual(addr.network_address(), '192.168.0.0')
        self.assertEqual(addr.netmask(), '255.255.255.0')

    def test_host_bit_set_ipv4(self):
        addr = IPv4NetworkHandling(self.ipaddress_ipv4_host_bits_set)
        self.assertEqual(addr.version(), 4)
        self.assertEqual(addr.max_prefixlen(), 32)
        self.assertEqual(addr.network_address(), '123.45.67.64')
        self.assertEqual(addr.netmask(), '255.255.255.224')

    def test_address_value_error_ipv4(self):
        with self.assertRaises(AddressValueError):
            _ = IPv4NetworkHandling(self.ipaddress_ipv4_invalid_address)

    def test_net_mask_value_error_ipv4(self):
        with self.assertRaises(NetmaskValueError):
            _ = IPv4NetworkHandling(self.ipaddress_ipv4_invalid_netmask)

    def test_write_to_file_ipv4(self):
        addr = IPv4NetworkHandling(self.ipaddress_ipv4_normal)
        addr.write_to_file_ipaddresses_included(self.filename_for_ipaddresses_ipv4)
        self.assertTrue(os.path.exists(self.filename_for_ipaddresses_ipv4))
        count = addr.count_number_of_ipaddresses()
        self.assertEqual(count, 256)

    def test_ipaddress_ipv6_ipv6_handling(self):
        addr = IPv6NetworkHandling(self.ipaddress_ipv6_normal)
        self.assertEqual(addr.version(), 6)
        self.assertEqual(addr.max_prefixlen(), 128)
        self.assertEqual(addr.network_address(), '2001:db00:0000:0000:0000:0000:0000:0000')
        self.assertEqual(addr.netmask(), 'ffff:ffff:ffff:ffff:ffff:ffff:ffff:0000')

    def test_ipaddress_ipv6_host_bits_set(self):
        addr = IPv6NetworkHandling(self.ipaddress_ipv6_host_bit_set)
        self.assertEqual(addr.version(), 6)
        self.assertEqual(addr.max_prefixlen(), 128)
        self.assertEqual(addr.network_address(), '2001:0000:0000:0000:0000:0000:0000:0000')
        self.assertEqual(addr.netmask(), 'ffff:0000:0000:0000:0000:0000:0000:0000')

    def test_ipv6_addresses_write_to_file(self):
        addr = IPv6NetworkHandling(self.ipaddress_ipv6_normal)
        addr.write_to_file_ipaddresses_included(self.filename_for_ipaddresses_ipv6)
        self.assertTrue(os.path.exists(self.filename_for_ipaddresses_ipv6))
        count = addr.count_number_of_ipaddresses()
        self.assertEqual(count, 65536)

    def test_ipaddress_ipv6_with_ipv4_handling(self):
        with self.assertRaises(AddressValueError):
            _ = IPv4NetworkHandling(self.ipaddress_ipv6_normal)

    def test_ipaddress_ipv4_with_ipv6_handling(self):
        with self.assertRaises(AddressValueError):
            _ = IPv6NetworkHandling(self.ipaddress_ipv4_normal)

    def tearDown(self) -> None:
        del self.ipaddress_ipv4_normal
        del self.ipaddress_ipv4_host_bits_set
        del self.ipaddress_ipv4_invalid_address
        del self.ipaddress_ipv4_invalid_netmask
        del self.filename_for_ipaddresses_ipv4


if __name__ == '__main__':
    unittest.main()
