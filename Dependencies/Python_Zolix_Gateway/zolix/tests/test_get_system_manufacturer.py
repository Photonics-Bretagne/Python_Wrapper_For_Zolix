from zolix.tests import test_common


def test():
    m = test_common.zolix_gateway.get_system_manufacturer()
    test_common.print_result('GetSystemManuFacturer', m)


if __name__ == '__main__':
    test()
