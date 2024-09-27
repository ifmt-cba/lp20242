def area(largura, profundidade):
    return largura * profundidade

def volume(largura, profundidade, altura):
    return area(largura,profundidade) * altura 

print(area(2,3))
print(volume(2,3,5))