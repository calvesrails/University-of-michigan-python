from module_package.modulo import soma_do_modulo
from module_package import modulo
from module_package import *

print(soma_do_modulo(5, 5))
print(modulo.soma_do_modulo(5, 5))

import module_package

print(module_package.dobra(22))