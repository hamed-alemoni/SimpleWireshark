from .variables import set_check_thread


def stop_sniffing_thread(status_label):
    # exit this thread out of loop
    set_check_thread(False)

    status_label_settings(status_label)


def status_label_settings(status_label):
    # change label text and color
    status_label.setText('Stopped')
    status_label.setStyleSheet('color: red')
