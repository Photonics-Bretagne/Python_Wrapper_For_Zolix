from zolix.tests import test_common


def test():
    test_common.zolix_gateway.set_entrance_port()
    test_common.print_result('SetEntrancePort(1)', m)


if __name__ == '__main__':
    test()
