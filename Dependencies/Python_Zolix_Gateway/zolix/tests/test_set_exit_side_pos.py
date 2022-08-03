from zolix.tests import test_common


def test():
    subtest(1)
    subtest(2)


def subtest(p1):
    test_common.zolix_gateway.set_exit_side_pos(p1)
    m1 = test_common.zolix_gateway.get_exit_side_pos()
    test_common.print_assert(f'GetExitSidePos', p1, m1)


if __name__ == '__main__':
    test()
