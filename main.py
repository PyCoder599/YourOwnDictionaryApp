from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager  # To manage screen it must be imported
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.modules import inspector  # Just for development need to remove afterward


class YOB(MDApp):
    def build(self):
        self.title = "YourOwn Book"
        return Builder.load_file('main.kv')

    def on_start(self):
        inspector.create_inspector(Window, self)
        Clock.schedule_once(self.update_signup,0)
        Window.bind(on_resize=self.update_signup)

    def update_signup(self, *args):
        login_signup_screen = self.root.get_screen("login")
        info = login_signup_screen.ids.signup_info
        wel = login_signup_screen.ids.sign_wel
        header = login_signup_screen.ids.signup_info_header
        scroll = login_signup_screen.ids.signup_info_scroll
        footer = login_signup_screen.ids.signup_info_footer
        W = Window.width
        H = Window.height
        info.width = max(self.width_cal(H), 0)
        wel.center = (self.width_cal(H*0.7) + (W - self.width_cal(H*0.7)) / 2, H*0.7)
        scroll.height = min(H - header.height - footer.height, 490)

    def width_cal(self, y1):
        W = Window.width
        H = Window.height
        ans = 0.4330 * W - 0.25 * H + 0.15 * W - (y1 - (0.25 * W + 0.4330 * H + 0.3 * H)) / 1.7320
        return ans


if __name__ == "__main__":
    YOB().run()
