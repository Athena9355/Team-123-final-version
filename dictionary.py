import requests


def get_word(input_word):
    input_word = str(input_word)
    url = "https://dictionary-by-api-ninjas.p.rapidapi.com/v1/dictionary"

    querystring = {"word": input_word}

    headers = {
        'x-rapidapi-host': "dictionary-by-api-ninjas.p.rapidapi.com",
        'x-rapidapi-key': "53c0bdc20bmshd40bff3eddbed53p11401djsn6beee195a713"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    return response.text