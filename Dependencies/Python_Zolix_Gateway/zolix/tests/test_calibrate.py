from zolix.tests import test_common


def test():
    m = test_common.zolix_gateway.calibrate()
    test_common.print_result('Calibrate(1, 0, 0)', m)


if __name__ == '__main__':
    test()
