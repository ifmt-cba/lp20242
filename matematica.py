def area(largura, profundidade):
    return largura * profundidade

def volume(largura, profundidade, altura):
    return area(largura,profundidade) * altura 

print(area(2,3))
print(volume(2,3,5))

largura = input('Forneça a largura da área: ')
profundidade = input('Forneça a profundidade da área: ')
print(area(int(largura),int(profundidade)))
