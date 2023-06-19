import ujson
import time
import sys


class WinterBoot:

    def __init__(self):           
        with open("config.json") as fp:
            data = ujson.loads(fp.read())
        
        
        for device in data["devices"]:
            print(device)
            deviceclass = device["device_class"]
            name = device["name"]
            attributes = device["attributes"]

            
            module_obj = __import__(device["module"])
            globals()[device["module"]] = module_obj
            
            module = getattr(sys.modules[__name__], device["module"])
            print(deviceclass, name, attributes, module)

            setattr(self, name, getattr(module, deviceclass)(**attributes))
            
        if data["winter_blue"]:
            import __main__
            handler_class = data['winter_blue']['handler_class']
            handler_function = data['winter_blue']['handler_function']
            print(f"{handler_class=}, {handler_function=}")
       
       
            function_name = f"{handler_class}.{handler_function}"
            function_object = eval(function_name)
            
            
            
            import winter_blue
            print(data["winter_blue"]["name"])
            self.winter_blue = winter_blue.WinterBlue(name = data["winter_blue"]["name"], handler = function_object)
    
