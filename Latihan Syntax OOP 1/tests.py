def run_tests(sepatu_satu, sepatu_dua, total_harga, total_discount):
 
    # Unit tests to check your solution
    assert sepatu_satu.harga == 700000, 'harga sepatu_satu seharusnya 700000'
    assert sepatu_satu.warna == 'merah', ' warna sepatu_satu seharusnya merah'
    assert sepatu_satu.merk == 'Adidas', 'merk sepatu_satu seharusnya Adidas'
    assert sepatu_satu.ukuran == 42, 'ukuran sepatu_satu seharusnya 42'

    assert sepatu_dua.harga == 600000, 'harga sepatu_dua seharusnya 600000'
    assert sepatu_dua.warna == 'biru', 'warna sepatu_dua seharusnya biru'
    assert sepatu_dua.merk == 'Nike', 'merk sepatu_dua seharusnya Nike'
    assert sepatu_dua.ukuran == 41, 'ukuran sepatu_dua seharusnya 41'

    assert total_harga == 1300000, 'total_harga dari sepatu_satu dan sepatu_dua seharusnya 1300000'
    
    assert int(total_discount) == 1170000, 'total_discount seharusnya 1170000'