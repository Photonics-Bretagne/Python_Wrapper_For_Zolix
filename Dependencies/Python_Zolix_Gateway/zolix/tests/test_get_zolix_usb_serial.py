from zolix.tests import test_common


def test(qte):
    m = test_common.zolix_gateway.get_zolix_usb_serial(qte)
    test_common.print_result(f'GetZolixUSBSerial({qte})', m)
    return m


if __name__ == '__main__':
    test()
