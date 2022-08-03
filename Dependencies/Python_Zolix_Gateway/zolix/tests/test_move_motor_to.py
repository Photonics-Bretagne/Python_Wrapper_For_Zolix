from zolix.tests import test_common


def test():
    m = test_common.zolix_gateway.move_motor_to(1, 2)
    test_common.print_result('MoveMotorTo(1, 2)', m)


if __name__ == '__main__':
    test()
