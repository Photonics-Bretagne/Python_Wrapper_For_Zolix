from zolix.tests import test_common


def test():
    m = test_common.zolix_gateway.get_peripheral_count()
    test_common.print_result('GetPeripheralCount', m)


if __name__ == '__main__':
    test()
