from zolix.tests import test_common


def test():
    m = test_common.zolix_gateway.get_system_model()
    test_common.print_result('GetSystemModel', m)


if __name__ == '__main__':
    test()
