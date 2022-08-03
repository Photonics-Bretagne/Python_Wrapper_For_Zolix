from zolix.tests import test_common


def test():
    subtest(0)
    subtest(1)


def subtest(p1):
    test_common.zolix_gateway.set_exit_port(p1)
    m1 = test_common.zolix_gateway.get_exit_port()
    test_common.print_assert(f'GetExitPort', p1, m1)


if __name__ == '__main__':
    test()
