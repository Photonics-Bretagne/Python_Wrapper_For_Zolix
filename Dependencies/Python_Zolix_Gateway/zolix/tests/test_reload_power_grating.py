from zolix.tests import test_common


def test():
    m = test_common.zolix_gateway.reload_power_grating()
    test_common.print_result('ReloadPowerGrating', m)


if __name__ == '__main__':
    test()
