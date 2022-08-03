from zolix.tests import test_common


def test():
    test_common.zolix_gateway.show_setting_dialog()
    test_common.print_result('ShowSettingDialog', m)


if __name__ == '__main__':
    test()
