from zolix.tests import test_common


def test():
    m = test_common.zolix_gateway.reload_rom_infor()
    test_common.print_result('ReloadRomInfor', m)


if __name__ == '__main__':
    test()
