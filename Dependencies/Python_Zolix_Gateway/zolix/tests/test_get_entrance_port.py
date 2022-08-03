from zolix.tests import test_common


def test():
    m = test_common.zolix_gateway.get_entrance_port()
    test_common.print_result('GetEntrancePort', m)


if __name__ == '__main__':
    test()
