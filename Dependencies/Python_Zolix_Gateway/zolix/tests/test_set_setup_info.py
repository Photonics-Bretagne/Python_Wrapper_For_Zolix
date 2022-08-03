from zolix.tests import test_common


def test():
    test_common.zolix_gateway.set_setup_info()
    test_common.print_result('SetSetupInfo(true)', m)


if __name__ == '__main__':
    test()
