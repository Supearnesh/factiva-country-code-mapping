from country_data_provider import CountryDictionary
from country_data_provider import CountryList

import csv
import pathlib
import re
import sys
import time

class CountryCodeMapping():
    """ CountryCodeMapping class for searching through dictionaries and 
    a list of mappings between DJII region codes and ISO Alpha 2 
    country codes to convert the passed inputs into the appropriate 
    format requested.
    
    Attributes:
        country_name_list (list of str) a list of country names
        djii_rc_list (list of str) a list of DJII region codes
        iso_alpha_2_list (list of str) a list of ISO Alpha 2 codes
    
    """
    def __init__(self):
        
        self.input_list = []
        self.country_name_list = []
        self.djii_rc_list = []
        self.iso_alpha_2_list = []


    def read_file(self, file_name):
        """Function to read in str input data from a text or csv file.
                
        Args:
            file_name (str): name of the file to read data from
        
        Returns:
            None
        
        """

        try:
            with open(file_name) as file:
                data_list = []
                line = file.readline()
                while line:
                    data_list.append(str(line).strip())
                    line = file.readline()
            file.close()

            if (re.match('^[A-Z]{2}$', data_list[1]) and data_list[1] != 'UK'):
                #Data row is ISO Alpha 2 - 'UK' is a two character DJII RC
                self.input_list = self.clean_str_list(data_list)
                self.iso_alpha_2_list = self.clean_str_list(data_list)

            elif (re.match('^[A-Z]{2,5}$', data_list[1])):
                #Data row is DJII RC
                self.input_list = self.clean_str_list(data_list)
                self.djii_rc_list = self.clean_str_list(data_list)

            else:
                #Data row is country name
                self.input_list = self.clean_str_list(data_list)
                self.country_name_list = self.clean_str_list(data_list)

        except Exception as e:
            print(f'File parsing unsuccessful: {str(e)}')


    def write_csv_file(self, file_name, data_list):
        """Function to write str output data to a CSV file.
                
        Args:
            file_name (str): name of the file to write output data to
            data_list (list of str): list of output data to write to file
        
        Returns:
            None
        
        """

        #Add a header row to the output
        temp_data_list = [file_name] + data_list

        #Append timestamp and file type to file_name
        file_name = f'process/output/{file_name}.csv'

        try:
            with open(file_name, 'w') as file:
                for line in temp_data_list:
                    file.write(f'{line}\n')
            file.close()
            print(f'File writing successful: {file_name}')

        except Exception as e:
            print(f'File writing unsuccessful: {str(e)}')


    def clean_str_list(self, str_list):
        """Function to remove unnecessary characters from lists of strings.
                
        Args:
            str_list (list of str): potentially dirty strings with bad chars
        
        Returns:
            str_list (list of str): clean strings with bad chars removed
        
        """

        #Remove header row
        str_list = str_list[1:]

        #List of chars to remove from string
        bad_chars = [';', ':', '[', "]", '"', "'", ',']

        for str_var in str_list:
            for char in bad_chars:
                str_var = str_var.strip().replace(char, '')

        return str_list


def main():
    """Main method to process files from command line input.
            
    Args:
        file_name (str): gives location of input files
        method (str): gives user option to use lists or dictionaries
        output_type (int): specifies which data output is requested
    
    Returns:
        None
    
    """

    try:

        start = time.time_ns()

        #Take input from command line
        file_name = str(sys.argv[1])
        method = str(sys.argv[2])
        output_type = int(sys.argv[3])

        #Create lists or dictionaries depending on method
        if (method == 'l'):
            country_list = CountryList()
            country_list.create_country_list()

        if (method == 'd'):
            country_dictionary = CountryDictionary()
            country_dictionary.create_country_name_dict()
            country_dictionary.create_djii_rc_dict()
            country_dictionary.create_iso_alpha_2_dict()

        factiva_country_map = CountryCodeMapping()

        factiva_country_map.read_file(f'process/input/{file_name}')

        #Return country names
        if (output_type == 0):

            file_name = f'country_name_{str(int(time.time()))}'

            #Use list method (slower)
            if (method == 'l'):
                for input_item in factiva_country_map.input_list:
                    factiva_country_map.country_name_list.append(\
                        country_list.get_country_name(\
                        input_item))

            #Use dictionaries method (faster)
            elif (method == 'd'):
                for input_item in factiva_country_map.input_list:
                    factiva_country_map.country_name_list.append(\
                        country_dictionary.get_country_name(\
                        input_item))
            
            #Write data list to output file
            factiva_country_map.write_csv_file(\
                file_name,\
                factiva_country_map.country_name_list)

        #Return DJII region codes
        elif (output_type == 1):

            file_name = f'djii_rc_{str(int(time.time()))}'

            #Use list method (slower)
            if (method == 'l'):
                for input_item in factiva_country_map.input_list:
                    factiva_country_map.iso_alpha_2_list.append(\
                        country_list.get_iso_alpha_2(\
                        input_item))

            #Use dictionaries method (faster)
            elif (method == 'd'):
                for input_item in factiva_country_map.input_list:
                    factiva_country_map.djii_rc_list.append(\
                        country_dictionary.get_djii_rc(\
                        input_item))
            
            #Write data list to output file
            factiva_country_map.write_csv_file(\
                file_name,\
                factiva_country_map.djii_rc_list)

        #Return ISO Alpha 2 country codes
        elif (output_type == 2):

            file_name = f'iso_alpha_2_{str(int(time.time()))}'

            #Use list method (slower)
            if (method == 'l'):
                for input_item in factiva_country_map.input_list:
                    factiva_country_map.iso_alpha_2_list.append(\
                        country_list.get_iso_alpha_2(\
                        input_item))

            #Use dictionaries method (faster)
            elif (method == 'd'):
                for input_item in factiva_country_map.input_list:
                    factiva_country_map.iso_alpha_2_list.append(\
                        country_dictionary.get_iso_alpha_2(\
                        input_item))
            
            #Write data list to output file
            factiva_country_map.write_csv_file(\
                file_name,\
                factiva_country_map.iso_alpha_2_list)


        file_path = f'{pathlib.Path(__file__).parent}/process/output/{file_name}.csv'

        print(f'File parsed here: {file_path}')
        print(f'Total runtime = {time.time_ns() - start} nanoseconds')

    except Exception as e:
        print(f'File parsing unsuccessful: {str(e)}')


if __name__ == '__main__':

    main()