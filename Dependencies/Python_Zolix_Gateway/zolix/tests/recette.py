from zolix.tests import test_common
from zolix.tests import test_get_comport
from zolix.tests import test_set_comport
from zolix.tests import test_get_usb_serials
from zolix.tests import test_set_usb_serials
from zolix.tests import test_get_usb_mode
from zolix.tests import test_set_usb_mode
from zolix.tests import test_get_is_open
from zolix.tests import test_get_system_manufacturer
from zolix.tests import test_get_system_model
from zolix.tests import test_get_system_serials_number
from zolix.tests import test_get_system_factory_time
from zolix.tests import test_get_firmware_version
from zolix.tests import test_get_current_wave
from zolix.tests import test_get_synchro_mode
from zolix.tests import test_open
from zolix.tests import test_close
from zolix.tests import test_connect
from zolix.tests import test_disconnect
from zolix.tests import test_search_zolix_usb_device
from zolix.tests import test_get_zolix_usb_serial
from zolix.tests import test_get_current_grating
from zolix.tests import test_set_current_grating
from zolix.tests import test_grating_home
from zolix.tests import test_move_to_wave
from zolix.tests import test_move_wave
from zolix.tests import test_refresh_current_wave
from zolix.tests import test_stop
from zolix.tests import test_set_speed
from zolix.tests import test_get_speed
from zolix.tests import test_set_filter
from zolix.tests import test_get_filter
from zolix.tests import test_filter_home
from zolix.tests import test_set_exit_port
from zolix.tests import test_get_exit_port
from zolix.tests import test_set_exit_side_pos
from zolix.tests import test_get_exit_side_pos
from zolix.tests import test_get_port_input
from zolix.tests import test_set_port_output
from zolix.tests import test_show_port_test
from zolix.tests import test_reload_peripheral
from zolix.tests import test_get_peripheral_count
from zolix.tests import test_set_peripheral
from zolix.tests import test_add_peripheral
from zolix.tests import test_get_peripheral_name
from zolix.tests import test_set_peripheral_string
from zolix.tests import test_motor_home
from zolix.tests import test_move_motor_to
from zolix.tests import test_get_motor_cur_pos
from zolix.tests import test_set_motor_speed
from zolix.tests import test_get_motor_speed
from zolix.tests import test_set_motor_home_direction
from zolix.tests import test_get_motor_home_direction
from zolix.tests import test_show_setting_dialog
from zolix.tests import test_send_command
from zolix.tests import test_get_receive_string
from zolix.tests import test_store_data
from zolix.tests import test_load_data
from zolix.tests import test_backup
from zolix.tests import test_restore
from zolix.tests import test_initialize
from zolix.tests import test_reload_system_infor
from zolix.tests import test_set_system_infor
from zolix.tests import test_reload_total_steps
from zolix.tests import test_get_total_steps
from zolix.tests import test_set_total_steps
from zolix.tests import test_reload_turret
from zolix.tests import test_get_turret
from zolix.tests import test_set_turret
from zolix.tests import test_reload_rom_infor
from zolix.tests import test_get_zero_pos
from zolix.tests import test_set_zero_pos
from zolix.tests import test_get_adjust_coefficient
from zolix.tests import test_get_coefficient
from zolix.tests import test_get_grating_wave_range_max
from zolix.tests import test_set_adjustment
from zolix.tests import test_calibrate
from zolix.tests import test_reload_init_wave
from zolix.tests import test_reload_init_wave
from zolix.tests import test_get_init_wave
from zolix.tests import test_set_init_wave
from zolix.tests import test_reload_gratings_param
from zolix.tests import test_set_grating_param
from zolix.tests import test_get_grating_param
from zolix.tests import test_wave_to_steps
from zolix.tests import test_reload_current_grating
from zolix.tests import test_reload_power_grating
from zolix.tests import test_set_power_grating
from zolix.tests import test_get_power_grating
from zolix.tests import test_about_box
from zolix.tests import test_slit_home
from zolix.tests import test_get_slit_zero_pos
from zolix.tests import test_set_slit_zero_pos
from zolix.tests import test_set_slit_bandpass
from zolix.tests import test_get_slit_bandpass
from zolix.tests import test_set_slit_width
from zolix.tests import test_get_slit_width
from zolix.tests import test_set_slit_type
from zolix.tests import test_get_slit_type
from zolix.tests import test_set_entrance_port
from zolix.tests import test_get_entrance_port
from zolix.tests import test_set_motor_total_steps
from zolix.tests import test_get_motor_total_steps
from zolix.tests import test_set_setup_info


def test():
    # False si passage en RS232
    test_set_usb_mode.test(True)

    qte = test_search_zolix_usb_device.test()
    if qte < 1:
        test_common.print_result('recette', 'ERREUR: pas de connexion USB/RS')
        return

    serial = test_get_zolix_usb_serial.test(0)

    # RS232
    # test_set_comport.test(2)

    test_set_usb_serials.test(serial)
    test_get_is_open.test()
    test_open.test()
    test_get_is_open.test()
    test_get_system_manufacturer.test()
    test_get_system_model.test()
    test_get_system_serials_number.test()
    test_get_system_factory_time.test()
    test_get_firmware_version.test()
    test_get_current_wave.test()
    test_get_synchro_mode.test()

    test_set_current_grating.test()
    test_grating_home.test()
    test_refresh_current_wave.test()
    test_stop.test()
    test_set_speed.test()

    # Ne fonctionne pas au bureau
    # test_set_filter.test()

    test_set_exit_port.test()

if __name__ == '__main__':
    test()
    test_common.zolix_gateway.disconnect_from_server()
