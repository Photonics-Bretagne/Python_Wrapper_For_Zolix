from zolix.tests import test_common


def test():
    m = test_common.zolix_gateway.get_is_open()
    test_common.print_result('GetIsOpen', m)


if __name__ == '__main__':
    test()
