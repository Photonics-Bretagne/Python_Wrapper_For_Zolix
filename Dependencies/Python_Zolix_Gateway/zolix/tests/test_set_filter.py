from zolix.tests import test_common


def test():
    subtest(1)
    subtest(5)


def subtest(p1):
    test_common.zolix_gateway.set_filter(p1)
    m1 = test_common.zolix_gateway.get_filter()
    test_common.print_assert(f'GetFilter', p1, m1)


if __name__ == '__main__':
    test()
