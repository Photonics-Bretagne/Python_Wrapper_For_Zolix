from zolix.tests import test_common


def test():
    m = test_common.zolix_gateway.get_motor_cur_pos(1)
    test_common.print_result('GetMotorCurPos(1)', m)


if __name__ == '__main__':
    test()
