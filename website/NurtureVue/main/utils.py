

menu = [
    {'title': "HOME", 'url_name': 'home'},
    {'title': "ABOUT US", 'url_name': 'about'},
    {'title': "CONTACT US", 'url_name': 'contact'},
]
"""{'title': "LOGIN", 'url_name': 'login'},
{'title': "SIGN UP", 'url_name': 'signup'},
{'title': "ADD A GREENHOUSE", 'url_name': 'addgrhs'}"""

class DataMixin:
   def get_data(self, **kwargs):
      context = kwargs
      user_menu = menu.copy()
      if self.request.user.is_authenticated:
         user_menu.pop(0)
         user_menu.pop(0)
         user_menu.pop(0)
      """elif self.request.user.is_authenticated:
          user_menu.pop(3)
          print(user_menu)"""
      context['menu'] = user_menu
      return context