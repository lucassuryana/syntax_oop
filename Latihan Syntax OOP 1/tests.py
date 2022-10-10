def run_tests(shoes_one, shoes_two, total_cost, total_discount):
 
    # Unit tests to check your solution
    assert shoes_one.price == 70, 'shoes_one price seharusnya 70'
    assert shoes_one.color == 'merah', ' shoes_one color seharusnya merah'
    assert shoes_one.style == 'Adidas', 'shoes_one style seharusnya Adidas'
    assert shoes_one.size == 42, 'shoes_one seharusnya 42'

    assert shoes_two.price == 60, 'shoes_two price seharusnya 60'
    assert shoes_two.color == 'biru', ' shoes_two color seharusnya biru'
    assert shoes_two.style == 'Nike', 'shoes_two style seharusnya Nike'
    assert shoes_two.size == 41, 'shoes_two seharusnya 41'

    assert total_cost == 130, 'total_cost dari shoes_one dan shoes_two seharusnya 130'
    
    assert round(total_discount) == 117, 'total_discount seharusnya 117'