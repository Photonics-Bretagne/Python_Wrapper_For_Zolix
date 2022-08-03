from zolix.tests import test_common


def test():
    subtest(1)
    subtest(2)


def subtest(p1):
    test_common.zolix_gateway.set_current_grating(p1)
    m1 = test_common.zolix_gateway.get_current_grating()
    test_common.print_assert(f'GetCurrentGrating', p1, m1)


if __name__ == '__main__':
    test()
