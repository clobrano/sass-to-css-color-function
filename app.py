#!/usr/bin/python3

from gi import require_version
require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk
import sys


class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="SASS/CSS Color Substitute")
        self.set_name('MyWindow')
        self.set_default_size(600, 300)

        self.box = Gtk.HBox()
        self.box.set_halign(Gtk.Align.CENTER)
        self.box.set_valign(Gtk.Align.CENTER)
        self.add(self.box)

        self.expected_color_lbl = Gtk.Label()
        context = self.expected_color_lbl.get_style_context()
        context.add_class("expected");
        self.expected_color_lbl.set_label("expected");
        self.box.pack_start(self.expected_color_lbl, True, True, 0)

        self.actual_color_lbl = Gtk.Label()
        self.actual_color_lbl.set_label("actual");
        context = self.actual_color_lbl.get_style_context()
        context.add_class("actual");
        self.box.pack_start(self.actual_color_lbl, True, True, 0)


def main(argv):

    def gtk_style():
        style_provider = Gtk.CssProvider()
        style_provider.load_from_path("theme.css")
        context = Gtk.StyleContext()

        context.add_provider_for_screen(
            Gdk.Screen.get_default(),
            style_provider,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )

    gtk_style()
    win = MyWindow()
    win.connect("delete-event", Gtk.main_quit)
    win.show_all()
    Gtk.main()

if __name__ == "__main__":
    main(sys.argv)
