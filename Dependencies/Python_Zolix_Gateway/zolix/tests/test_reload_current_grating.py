from zolix.tests import test_common


def test():
    m = test_common.zolix_gateway.reload_current_grating()
    test_common.print_result('ReloadCurrentGrating', m)


if __name__ == '__main__':
    test()
