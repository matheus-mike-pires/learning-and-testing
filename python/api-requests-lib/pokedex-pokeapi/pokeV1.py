import requests

while True:
  while True:
    try:
      names = input('Name of the pokemon to search: ').lower()
      api_test = requests.get(f'https://pokeapi.co/api/v2/pokemon/' + names)
      dados = api_test.json()
      print('')
      break
    except requests.JSONDecodeError:
      print('not a valid name!')
      print('')
      continue

  print(f'name: {dados['name']}')
  print(f'ability: {dados['abilities'][0]['ability']['name']}')
  print(f'height: {float(dados['height']) / 10} M')
  print(f'type: {dados['types'][0]['type']['name']}')
  print(f'weight: {float(dados['weight']) / 10} kg')

  print('')
  decision = input('verify new pokemon? (Y/N): ').lower()
  if decision == 'no' or decision == 'n':
    break
  if decision == 'yes' or decision == 'y':
    print('')
    continue

print('')
print('thank you for using this pokedex!')



