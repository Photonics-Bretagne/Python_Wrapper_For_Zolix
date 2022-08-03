from zolix.tests import test_common


def test():
    m = test_common.zolix_gateway.backup()
    test_common.print_result('Backup', m)


if __name__ == '__main__':
    test()
