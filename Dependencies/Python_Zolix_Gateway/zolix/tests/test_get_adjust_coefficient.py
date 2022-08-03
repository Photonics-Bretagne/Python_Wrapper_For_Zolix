from zolix.tests import test_common


def test():
    m = test_common.zolix_gateway.get_adjust_coefficient(1)
    test_common.print_result('GetAdjustCoefficient(1, 0, 0)', m)


if __name__ == '__main__':
    test()
