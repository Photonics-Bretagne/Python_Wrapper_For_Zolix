from zolix.tests import test_common


def test():
    m = test_common.zolix_gateway.move_wave(1.1)
    test_common.print_result('MoveWave(1.1)', m)


if __name__ == '__main__':
    test()
