from zolix.tests import test_common


def test():
    subtest(1, 1)
    subtest(1, 2)


def subtest(p1, p2):
    test_common.zolix_gateway.set_speed(p1, p2)
    m1 = test_common.zolix_gateway.get_speed(p1)
    test_common.print_assert(f'GetSpeed', p2, m1)


if __name__ == '__main__':
    test()
