import math

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
        Clock.schedule_once(self.update_login,0)
        Window.bind(on_resize=self.update_login)

    def update_signup(self, *args):
        login_signup_screen = self.root.get_screen("login")
        info = login_signup_screen.ids.signup_info
        wel = login_signup_screen.ids.sign_wel
        header = login_signup_screen.ids.signup_info_header
        scroll = login_signup_screen.ids.signup_info_scroll
        footer = login_signup_screen.ids.signup_info_footer
        W = Window.width
        H = Window.height
        info.width = max(self.width_cal(H, 's'), 0)
        wel.center = (self.width_cal(H*0.7, 's') + (W - self.width_cal(H*0.7, 's')) / 2, H*0.7)
        scroll.height = min(H - header.height - footer.height, 500)

    def update_login(self, *args):
        login_signup_screen = self.root.get_screen("login")
        info = login_signup_screen.ids.login_info
        wel = login_signup_screen.ids.login_wel
        W = Window.width
        H = Window.height
        info.width = max(W - self.width_cal(H, 'l'), 0)
        info.center = (W - info.width/2, H/2)
        wel.center = (self.width_cal(H*0.7, 'l') / 2, H*0.7)

    def width_cal(self, y1, fac):
        W = Window.width
        H = Window.height
        if fac == 'l':
            th = math.radians(-30)
            W = -W
            cx = 0.85
        elif fac == 's':
            th = math.radians(30)
            cx = 0.15
        x_prime = W / 2 * math.cos(th) - H * math.sin(th)
        y_prime = W / 2 * math.sin(th) + H * math.cos(th)
        W = abs(W)
        ans = x_prime + cx * W + (y1 - (y_prime + 0.3 * H)) / math.tan(math.pi/2 + th)
        return ans

    def switch_to_login(self):
        print("Ready to go")

    def switch_to_signup(self):
        print("Ready to go")

if __name__ == "__main__":
    YOB().run()
