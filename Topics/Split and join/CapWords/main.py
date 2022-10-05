joiner = None
var_name = input()
var_name_parts = var_name.split('_')
class_name_parts = [v.lower().capitalize() for v in var_name_parts]
class_name = joiner.join(class_name_parts)
print(class_name)
