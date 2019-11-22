# Soal 1
print ('Soal 1:')
def calculate_years(principal,interest,tax,desired):
    year = 0
    while principal < desired:
        bunga = principal*interest
        bunga = bunga - (bunga*tax)
        principal = principal + bunga
        year += 1
    return print(year)

calculate_years(1000,0.05,0.18,1100)
calculate_years(1200.00, 0.17, 0.05, 2000.00)
calculate_years(1500.00, 0.07, 0.6, 5000.00)