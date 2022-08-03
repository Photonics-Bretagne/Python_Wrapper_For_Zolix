from zolix.tests import test_common


def test():
    test_common.zolix_gateway.set_slit_zero_pos()
    test_common.print_result('SetSlitZeroPos(1, 1)', m)


if __name__ == '__main__':
    test()
