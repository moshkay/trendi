import kivy
kivy.require("1.9.1")
from kivy.app import App 
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.clock import Clock
from kivymd.theming import ThemeManager
from kivymd.navigationdrawer import NavigationDrawer
from kivy.properties import StringProperty,ListProperty,ObjectProperty
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivymd.list import ILeftBody
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivymd.card import MDCard
from kivymd.button import MDIconButton
from kivy.storage.jsonstore import JsonStore


class AdvertCard(MDCard):
	header=StringProperty("")
	company_name=StringProperty("")
	goods=StringProperty("")
	def __init__(self,**opt):
		super().__init__(**opt)

class Manager(ScreenManager):
	def __init__(self,**opt):
		super().__init__(**opt)
		Clock.schedule_once(self.move,10)
	def move(self,*args):
		state=users_state.get('status')['value']
		print(state)
		if state==False:
			self.switch_to(Login())
			users_state.put('status',value=True)
		else:
			
			self.switch_to(Home())

class AdvertLayout(FloatLayout):
	image=StringProperty("")
	name=StringProperty("")
	def __init__(self,**opt):
		super().__init__(**opt)
class IconLayout(FloatLayout):
	image=StringProperty("")
	text=StringProperty("")
	def __init__(self,**opt):
		super().__init__(**opt)
		
class ToolbarScreen(Screen):
	left_item=ListProperty([])
	right_item=ListProperty([])
	page_title=StringProperty("")
	def _init__(self,**opt):
		super().__init__(**opt)

class Splash(Screen):
	def __init__(self,**opt):
		super().__init__(**opt)

class Home(ToolbarScreen):
	#layout=ObjectProperty(None)#layout that holds different screens
	layout_man=ObjectProperty(None)
	image_carousel=ObjectProperty(None)
	state=True
	
	def __init__(self,**opt):
		super().__init__(**opt)
		self.bind(on_enter=Clock.schedule_interval(self.moving_image,7))
		self.bind(on_pre_enter=self.add_images)
		

	def next_page(self,*args):
			print("next")
	def moving_image(self,*args):	
		self.image_carousel.load_next(mode="next")
	def add_images(self,*args):
		if self.state==True:
			for i in range(1,14):
				ad=AdvertLayout()
				ad.image="images/%s.jpg"%i
				ad.name=str(i)
				self.image_carousel.add_widget(ad)
			self.state=False
	
class Login(ToolbarScreen):
	username=ObjectProperty(None)
	password=ObjectProperty(None)

	
	def __init__(self,**opt):
		super().__init__(**opt)
	def next_page(self,*args):
		if (not(self.validate())):
			pass
		else:
			app.root.current="home"
	def validate(self,*args):
		if (self.username.text=="") or (self.password.text==""):
			return False
		else:	
			return True
class Navigation(NavigationDrawer):
	def __init__(self,**opt):
		super().__init__(**opt)
class RoundLabel(Label):
	image=StringProperty("")
	def __init__(self,**opt):
		super().__init__(**opt)
class ImageBoxLayout(BoxLayout):
	image=StringProperty("")
	text=StringProperty("")
	def __init__(self,**opt):
		super().__init__(**opt)
class ListImage(ILeftBody,Image):
	def __init__(self,**opt):
		super().__init__(**opt)
class ListIcon(ILeftBody,MDIconButton):
	def __init__(self,**opt):
		super().__init__(**opt)

class TrendiApp(App):
	use_kivy_settings=False
	theme_cls=ThemeManager()

	nav_bar=ObjectProperty()#the navigation drawer
	def build(self):
		self.nav_bar=Navigation()
		return Manager()
users_state=JsonStore("state.json")
try:
	users_state.get('status')['value']

except:
	users_state.put('status',value=False)
Window.system_size=(300,400)
app=TrendiApp()
app.run()
