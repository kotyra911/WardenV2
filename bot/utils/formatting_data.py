import hashlib



def formatting_data_for_message(avito_url: str, price: str, title: str, photo_url: str):

    combined_string = avito_url + price + title + photo_url

    hash_value = hashlib.sha256(combined_string.encode()).hexdigest()









    """Продумать -> что делать с объявлениями. Нужно либо сохранять в
    базу хеш и сравнивать его. Если хеш не совпадает,
    тогда отправлять объявление и сохранять его хеш в
    базу. Либо можно просто смотреть возраст объявления
    и отправлять только те, которые например младше часа"""