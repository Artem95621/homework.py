def introspection_info(obj):

    obj_type = type(obj).__name__

    attributes = [attr for attr in dir(obj) if not callable(getattr(obj, attr))]

    methods = [method for method in dir(obj) if callable(getattr(obj, method))]

    obj_module = obj.__class__.__module__


    info = f"Type: {obj_type}\n"
    info += f"Attributes: {', '.join(attributes)}\n"
    info += f"Methods: {', '.join(methods)}\n"
    info += f"Module: {obj_module}\n"


    other_properties = []

    if other_properties:
        info += "Other Properties:\n" + "\n".join(other_properties)

    if hasattr(obj, '__len__'):
        other_properties.append(f"length: {len(obj)}")

    if isinstance(obj, (int, float, complex)):
        other_properties.append(f"Is numeric: True")
        other_properties.append(f"Numeric value: {obj}")

    if isinstance(obj, str):
        other_properties.append(f"Is string: True")
        other_properties.append(f"String: {obj}")

    if other_properties:
        info += "Other Properties:\n" + "\n".join(other_properties)

    return info


class MyClass:
    def __init__(self, value):
        self.value = value

    def greet(self):
        return f"Hello, {self.value}!"


my_object = MyClass("Python")

object_info = introspection_info(my_object)
print(object_info)

number_info = introspection_info(42)
print(number_info)
