from zolix.tests import test_common


def test(port):
    subtest(port)


def subtest(port):
    test_common.zolix_gateway.set_comport({port})
    m1 = test_common.zolix_gateway.get_comport()
    test_common.print_assert(f'SetComport', port, m1)


if __name__ == '__main__':
    test()
