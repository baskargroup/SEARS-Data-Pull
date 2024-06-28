### How to Query MongoDB using Python to Download Data and Files

#Steps

0. Copy the `.env` file to the root directory of the project.
1. Install all requirements using `pip3 install -r requirements.txt`
2. Run `python3 mongo_connect.py` to download data from MongoDB to a CSV file. Set `search_criteria` and `output_file_name` in the program file.
3. Run `python3 DO_Download.py` to download files from Digital Ocean to a local directory `./file_fetch/`. All files related to experiments meeting the search criteria will be downloaded.
4. Run your ML model on the downloaded data and files.
