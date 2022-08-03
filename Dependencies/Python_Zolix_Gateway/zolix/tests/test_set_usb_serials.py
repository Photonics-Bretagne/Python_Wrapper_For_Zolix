from zolix.tests import test_common


def test(serial):
    subtest(serial)


def subtest(serial):
    test_common.zolix_gateway.set_usb_serials(serial)
    m1 = test_common.zolix_gateway.get_usb_serials()
    test_common.print_assert(f'SetUSBSerials', serial, m1)


if __name__ == '__main__':
    test()
