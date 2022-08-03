from zolix.tests import test_common


def test():
    m = test_common.zolix_gateway.get_firmware_version()
    test_common.print_result('GetFirmwareVersion', m)


if __name__ == '__main__':
    test()
