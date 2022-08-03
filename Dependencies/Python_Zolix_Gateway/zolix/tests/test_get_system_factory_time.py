from zolix.tests import test_common


def test():
    m = test_common.zolix_gateway.get_system_factory_time()
    test_common.print_result('GetSystemFactoryTime', m)


if __name__ == '__main__':
    test()
