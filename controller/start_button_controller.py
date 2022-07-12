from threading import Thread
from .sniffing import sniffing
from .table_widget_contoller import write_info_in_table_widget_format
from .variables import set_check_thread, get_check_thread, set_packets_number, get_packet_number

is_thread_created = False
thread = None


def run_sniffing_in_thread(status_label, table_widget):
    status_label_settings(status_label)

    # make thread for sniffing live in network and run it when user push start button
    start_sniffing_thread(sniffing_loop, (table_widget,))

    set_check_thread(True)


def start_sniffing_thread(target, args):
    global thread, is_thread_created

    if not is_thread_created:
        thread = Thread(target=target, args=args)
        thread.start()
    else:
        thread.start()


def status_label_settings(status_label):
    # change label text and color
    status_label.setText('Started')
    status_label.setStyleSheet('color: green')


def sniffing_loop(table_widget):
    while get_check_thread():
        packets_number = get_packet_number()
        # get one sniffed packet
        packet = sniffing()

        packets_number += 1
        set_packets_number(packets_number)
        # write info of new packet into the table widget
        write_info_in_table_widget_format(table_widget, packet, get_packet_number())
