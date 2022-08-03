from zolix.tests import test_common


def test():
    test_common.zolix_gateway.set_peripheral_string("string test")
    test_common.print_result('SetPeripheralString("string test")', m)


if __name__ == '__main__':
    test()
