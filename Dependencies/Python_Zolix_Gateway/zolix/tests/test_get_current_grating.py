from zolix.tests import test_common


def test():
    m = test_common.zolix_gateway.get_current_grating()
    test_common.print_result('GetCurrentGrating', m)


if __name__ == '__main__':
    test()
