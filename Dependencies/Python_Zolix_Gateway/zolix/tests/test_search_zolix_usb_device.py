from zolix.tests import test_common


def test():
    m = test_common.zolix_gateway.search_zolix_usb_device()
    test_common.print_result('SearchZolixUSBDevice', m)
    return m


if __name__ == '__main__':
    test()
