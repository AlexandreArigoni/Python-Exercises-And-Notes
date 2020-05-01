from ex107.modules import mod
p = float(input('Enter the number: '))
print(mod.half(p, True))
print(mod.double(p, True))
print(mod.plus(p, 10, True))
print(mod.minus(p, 13, True))
mod.resume(p, 10, 13)
