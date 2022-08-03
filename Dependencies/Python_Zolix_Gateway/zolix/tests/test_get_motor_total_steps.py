from zolix.tests import test_common


def test():
    m = test_common.zolix_gateway.get_motor_total_steps()
    test_common.print_result('GetMotorTotalSteps(1)', m)


if __name__ == '__main__':
    test()
