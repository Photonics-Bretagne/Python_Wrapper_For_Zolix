from zolix.tests import test_common


def test():
    m = test_common.zolix_gateway.get_port_input()
    test_common.print_result('GetPortInput', m)


if __name__ == '__main__':
    test()
