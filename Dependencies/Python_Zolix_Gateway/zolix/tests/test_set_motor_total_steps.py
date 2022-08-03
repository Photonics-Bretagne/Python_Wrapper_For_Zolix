from zolix.tests import test_common


def test():
    subtest(3, 5423)
    subtest(3, 5000)


def subtest(p1, p2):
    test_common.zolix_gateway.set_motor_total_steps(p1, p2)
    m1 = test_common.zolix_gateway.get_motor_total_steps(p1)
    test_common.print_assert(f'GetMotorTotalSteps', p2, m1)


if __name__ == '__main__':
    test()
