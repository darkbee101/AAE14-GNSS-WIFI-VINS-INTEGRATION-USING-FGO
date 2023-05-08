import csv

# Open the CSV file for reading
with open('D:\FYP\Final\Data\Experimental Data\output3.csv', newline='') as csvfile:
    # Create a CSV reader object
    reader = csv.reader(csvfile)
    
    # Initialize variables to keep track of odd line values
    odd_first_value = None
    odd_second_value = None
    #odd_third_value = None

    # Initialize a CSV writer object to write to the output file
    with open('output4.csv', mode='w', newline='') as outfile:
        writer = csv.writer(outfile)

    # Loop through each line in the CSV file
    for i, row in enumerate(reader):
        # If the line number is odd
        if i % 2 == 0:
            # Get the first and second values of the odd line
            odd_first_value = float(row[0])
            odd_second_value = float(row[1])
            #odd_third_value = float(row[2])
        # If the line number is even
        else:
            # Get the second and third values of the even line
            even_second_value = float(row[1])
            even_third_value = float(row[2])
            
            # Calculate the products and square of the third value
            product_1 = (odd_first_value * even_second_value)*0.8
            product_2 = (odd_second_value * even_second_value)*0.8
            square_third_value = even_third_value*0.8

            # Check if the conditions are met
            if 17.1824 <= product_1 <= 27.1824 and 109.1045 <= product_2 <= 119.1045:
                # Open the output file for appending
                with open('output4.csv', mode='a', newline='') as outfile:
                    # Create a CSV writer object
                    writer = csv.writer(outfile)
                    
                    # Write the odd line values to the output file
                    writer.writerow([odd_first_value, odd_second_value])

            # Print the results
            print(product_1, product_2, square_third_value)
