n = float(input('How much many do you have in your wallet? R$ '))
dollar = 4.70
ex = n / dollar
print('With R${:.2f}, you can buy U${:.2f}'.format(n, ex))