from zolix.tests import test_common


def test():
    m = test_common.zolix_gateway.get_motor_home_direction(5)
    test_common.print_result('GetMotorHomeDirection(5)', m)


if __name__ == '__main__':
    test()
