from zolix.tests import test_common


def test():
    test_common.zolix_gateway.set_peripheral(1, "name")
    test_common.print_result('SetPeripheral(1, "name")', m)


if __name__ == '__main__':
    test()
