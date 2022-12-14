from pprint import pprint


def manager(response, output):
    '''Manager for handling reponses from BE'''
    data = response.json()
    if output == '-':
        pprint(data)
    elif output != '-':
        with open(output, 'wb') as outfile:
            outfile.write(response.content)
