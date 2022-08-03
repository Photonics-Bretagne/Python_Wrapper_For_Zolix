from zolix.tests import test_common


def test():
    m = test_common.zolix_gateway.reload_peripheral()
    test_common.print_result('ReloadPeripheral', m)


if __name__ == '__main__':
    test()
