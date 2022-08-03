from zolix.tests import test_common


def test():
    m = test_common.zolix_gateway.get_receive_string()
    test_common.print_result('GetReceiveString', m)


if __name__ == '__main__':
    test()
