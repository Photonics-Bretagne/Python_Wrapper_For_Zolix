from zolix.tests import test_common


def test():
    m = test_common.zolix_gateway.add_peripheral("name")
    test_common.print_result('AddPeripheral("name")', m)


if __name__ == '__main__':
    test()
