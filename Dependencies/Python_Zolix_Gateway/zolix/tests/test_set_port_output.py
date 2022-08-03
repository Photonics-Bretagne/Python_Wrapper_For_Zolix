from zolix.tests import test_common


def test():
    subtest(3)
    subtest(1)


def subtest(p1):
    test_common.zolix_gateway.set_port_output(p1)
    m1 = test_common.zolix_gateway.get_port_input()
    test_common.print_assert(f'GetPortInput', p1, m1)


if __name__ == '__main__':
    test()
