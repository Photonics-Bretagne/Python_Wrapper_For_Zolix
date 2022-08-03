from zolix.tests import test_common


def test():
    m = test_common.zolix_gateway.motor_home(1)
    test_common.print_result('MotorHome(1)', m)


if __name__ == '__main__':
    test()
