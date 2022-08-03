from zolix.tests import test_common


def test(value):
    m = test_common.zolix_gateway.get_usb_mode()
    test_common.print_result('GetUSBMode', m)

    test_common.zolix_gateway.set_usb_mode(value)
    test_common.print_result(f'SetUSBMode({value})', m)

    m = test_common.zolix_gateway.get_usb_mode()
    test_common.print_result('GetUSBMode', m)


if __name__ == '__main__':
    test()
    test_common.zolix_gateway.disconnect_from_server()