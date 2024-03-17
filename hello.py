import sys
import gi

gi.require_version("Gtk", "4.0")
from gi.repository import GLib, Gtk

class MyApplication(Gtk.Application):
    def __init__(self):
        super().__init__(application_id="com.github.aamersohel.quranic-videos-audio-sync")
        GLib.set_application_name('Audio Sync')

    def do_activate(self):
        window = Gtk.ApplicationWindow(application=self, title="Audio Sync")
        window.present()
        
        


app = MyApplication()
exit_status = app.run(sys.argv)
sys.exit(exit_status)