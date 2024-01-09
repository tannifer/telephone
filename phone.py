import phonenumbers
import csv

def convert_to_standard_format(phone_number):
    try:
        parsed_number = phonenumbers.parse(phone_number, None)
        formatted_number = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164)
        return formatted_number
    except phonenumbers.NumberParseException:
        # Handle invalid phone numbers
        return None

def process_csv(input_file, output_file):
    with open(input_file, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip header row
        data = list(reader)

    converted_data = []
    for row in data:
        name, phone_number, phone_number2 = row

        if phone_number2.strip():  # Use phone_number2 if it's not empty
            default_phone_number = phone_number2
        else:
            default_phone_number = phone_number

        formatted_number = convert_to_standard_format(default_phone_number)
        if formatted_number:
            converted_data.append([name, formatted_number])
        else:
            print(f"Invalid phone number for {name}: {default_phone_number}")

    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['name', 'converted_number'])
        writer.writerows(converted_data)

def main():
    input_file = 'student_numbers_two_columbs.csv'  # Replace with your input CSV file
    output_file = 'output.csv'  # Replace with your desired output CSV file
    process_csv(input_file, output_file)
    print(f"Conversion complete. Output saved to {output_file}")

if __name__ == "__main__":
    main()
