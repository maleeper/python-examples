def encode_name(name):
    try:
        name = name.encode('ascii')
    except UnicodeError as e:
        print(f'The name {e.object} has a character at position {e.start} that cannot be encoded in {e.encoding} due to {e.reason}')
    return name
    
encode_name('Stéfan')