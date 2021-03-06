from .plant import Plant
from interfaces import Identifiable
from interfaces import IStagnant
from interfaces import ISunny

class BlueJade(Plant, IStagnant, ISunny, Identifiable):

    def __init__(self, name = "Blue Jade"):
        Plant.__init__(self, name)
        Identifiable.__init__(self)
        IStagnant.__init__(self)
        ISunny.__init__(self)
        self.image = """ 
                 __    __        __          __    __        __          
    (//    \\)    __(//   __    (//    \\)    __(//   __    (//    \\)  
    /"      / __  \\)"    \\)_  /"      / __  \\)"    \\)_  /"      / __
  '|-..__..-''\_''-.\__..-''  '|-..__..-''\_''-.\__..-''  '|-..__..-''\
  (\\  \_    _(\\      _/     (\\  \_    _(\\      _/     (\\  \_    //)
   ""  (\\  //)""     //)      ""  (\\  //)""     //)      ""  (\\   ""
        ""  ""        ""            ""  ""        ""            ""
        """
        