import pytest




#testing list slicing
def test_func():

    favorite_books = [["Michael Vey", "Richard Paul Evans"], ["The Lightning Thief", "Rick Riordian"],["Going Bovine", "Libba Bray"]]

    books = []
    for i in range(0,3):
        temp = favorite_books[i][0]
        books.append(temp)
    assert books == ['Michael Vey', 'The Lightning Thief', 'Going Bovine']

def test_dict():
    students = {
        "student1" :{
            "name" : "John",
            "id" : 121
            },
        "student2" : {
            "name" : "Karl",
            "id" : 543
        },
        "student3" : {
            "name" : "Ellie",
            "id" : 239
        }
    }
    
    assert students["student3"]["id"] == 239