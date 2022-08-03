from zolix.tests import test_common


def test():
    m = test_common.zolix_gateway.get_peripheral_name(1)
    test_common.print_result('GetPeripheralName(1)', m)


if __name__ == '__main__':
    test()
