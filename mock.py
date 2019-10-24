def mock_db(key_word):
    db={
        'name': 'Yajyuu',
        'age':'24',
        'is_students': True
    }
    return db.get(key_word,'')