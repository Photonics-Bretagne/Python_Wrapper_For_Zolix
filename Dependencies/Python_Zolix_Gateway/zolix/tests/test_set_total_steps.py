from zolix.tests import test_common


def test():
    test_common.zolix_gateway.set_total_steps(56245)
    test_common.print_result('SetTotalSteps(56245)', m)


if __name__ == '__main__':
    test()
