from zolix.tests import test_common


def test():
    m = test_common.zolix_gateway.set_adjustment(1, 0)
    test_common.print_result('SetAdjustment(1, 0)', m)


if __name__ == '__main__':
    test()
