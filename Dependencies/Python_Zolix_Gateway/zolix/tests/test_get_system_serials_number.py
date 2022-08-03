from zolix.tests import test_common


def test():
    m = test_common.zolix_gateway.get_system_serials_number()
    test_common.print_result('GetSystemSerialsNumber', m)


if __name__ == '__main__':
    test()
