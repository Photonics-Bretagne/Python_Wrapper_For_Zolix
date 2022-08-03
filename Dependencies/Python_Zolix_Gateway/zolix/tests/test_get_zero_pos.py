from zolix.tests import test_common


def test():
    m = test_common.zolix_gateway.get_zero_pos()
    test_common.print_result('GetZeroPos(1)', m)


if __name__ == '__main__':
    test()
