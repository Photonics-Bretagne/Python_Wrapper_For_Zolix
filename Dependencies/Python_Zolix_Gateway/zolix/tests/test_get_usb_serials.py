from zolix.tests import test_common


def test():
    m = test_common.zolix_gateway.get_usb_serials()
    test_common.print_result('GetUSBSerials', m)


if __name__ == '__main__':
    test()
