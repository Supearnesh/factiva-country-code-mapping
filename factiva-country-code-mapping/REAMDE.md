# Factiva Country Code Mapping

This utility simplifies mapping between country names, DJII region codes, and ISO Alpha 2 country codes. The following services can be used at the moment.

Snapshots: Allows to run each snapshot creation, monitoring, download and local exploration, in an individual manner. Also allows to run the whole process within a single method.
Streams: In addition to creating and getting stream details, contains the methods to easily implement a stream listener and push the content to other locations appropriate for high-available setups.
The previous components rely on the API-Key authentication method, which is a prerequisite when using either of those services.

### Installation

To install this library, run the following commands.

*$ pip install -u factiva-country-code-mapping*

### Usage

The utility can be run by adding csv files to the 'process' folder; the input files should contain a newline ('\n') delimited list of country codes, DJII region codes, or ISO Alpha 2 country codes that are to be mapped to either of the other two data types. I've included some sample inputs and outputs in the 'process' folder - both inputs should be uploaded there and outputs will be displayed there. This utlity will output the other two data types by running the following command.

*python -m country_code_mapping input_state2.csv d 1*

### Implementation

There were two approaches explored in this implementation: the first was to create a list containing lists for each mapping of country name to DJII RC to ISO Alpha 2 code, and the second was to create three separate dictionaries with each of the various data type as keys. This was both a simple exercise to compare O(n) between searching the underlying data using lists vs dictionaries as well as to actually transform data files being used with the Factiva search engine.
