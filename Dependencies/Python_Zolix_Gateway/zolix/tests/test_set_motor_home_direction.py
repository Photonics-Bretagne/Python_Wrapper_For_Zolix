from zolix.tests import test_common


def test():
    test_common.zolix_gateway.set_motor_home_direction()
    test_common.print_result('SetMotorHomeDirection(3, 0)', m)

    m = test_common.zolix_gateway.get_motor_home_direction(5)
    test_common.print_result('GetMotorHomeDirection(3)', m)

    test_common.zolix_gateway.set_motor_home_direction()
    test_common.print_result('SetMotorHomeDirection(3, 1)', m)

    m = test_common.zolix_gateway.get_motor_home_direction(5)
    test_common.print_result('GetMotorHomeDirection(3)', m)


if __name__ == '__main__':
    test()
