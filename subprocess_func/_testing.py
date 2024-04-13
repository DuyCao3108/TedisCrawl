from generator import Generator, generate_section_template

def main():
    generator = Generator(input_csv_path = "storage/data.csv")
    generator.start_generate("output.html")

if __name__ == "__main__":
    main()