from zolix.tests import test_common


def test():
    test_common.zolix_gateway.set_motor_speed(3, 1500)
    test_common.print_result('SetMotorSpeed(1, 1)', m)

    m = test_common.zolix_gateway.get_motor_speed(3)
    test_common.print_result('GetMotorSpeed(3)', m)

    test_common.zolix_gateway.set_motor_speed(5, 250)
    test_common.print_result('SetMotorSpeed(1, 1)', m)

    m = test_common.zolix_gateway.get_motor_speed(5)
    test_common.print_result('GetMotorSpeed(5)', m)


if __name__ == '__main__':
    test()
