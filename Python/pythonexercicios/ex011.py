largura = float(input("Largura da parede: "))
altura = float(input("Altura da parede: "))
litro = 2 #2m²
area = largura * altura
print('Sua parede tem a dimensão de {:.2f} x {:.2f} e sua área é de {:.3f}m².'.format(largura, altura, area))
print('Para pintar essa parede, você precisará de {}l de tinta.'.format(area/litro))

