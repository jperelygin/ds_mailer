"""
iOS 14 Pyto widget
"""
from requests import request

import widgets as wd


BACKGROUND_COLOR = wd.Color.rgb(74/255, 82/255, 90/255)
FOREGROUND_COLOR = wd.COLOR_WHITE


def get_text(key):
    req = request("POST", "https://ds-mailer.herokuapp.com/", data={"key": key})
    return req.text


wd.wait_for_internet_connection()

text = get_text("")
text_list = text.split("\n")
widget = wd.Widget()

widget.small_layout.set_background_color(BACKGROUND_COLOR)
for i in text_list[1:3]:
    widget.small_layout.add_row(
            [wd.Text(
                i,
                color=FOREGROUND_COLOR,
                font=wd.Font.bold_system_font_of_size(9),
                padding=wd.Padding(0, 0, 0, 0)
                )])

widget.medium_layout.set_background_color(BACKGROUND_COLOR)
for i in text_list:
    widget.medium_layout.add_row(
        [wd.Text(
            i,
            color=FOREGROUND_COLOR,
            font=wd.Font.bold_system_font_of_size(10),
            padding=wd.Padding(0, 0, 0, 0)
            )])

widget.large_layout.set_background_color(BACKGROUND_COLOR)
for i in text_list:
    widget.large_layout.add_row(
        [wd.Text(
            i,
            color=FOREGROUND_COLOR,
            font=wd.Font.bold_system_font_of_size(12),
            padding=wd.Padding(5, 0, 10, 10)
            )])

wd.schedule_next_reload(60*60)
wd.show_widget(widget)
