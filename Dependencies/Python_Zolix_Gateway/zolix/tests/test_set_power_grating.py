from zolix.tests import test_common


def test():
    test_common.zolix_gateway.set_power_grating()
    test_common.print_result('SetPowerGrating(1)', m)


if __name__ == '__main__':
    test()
