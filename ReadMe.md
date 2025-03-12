# SEARS SDK 
The purpose of this SDK is to publish code that will help data scientists to query MongoDB using python so as to bulk download data and files directly from the SEARS backend for aggregated analysis. Case studies 6.1 and 6.2 from our main paper were conducted using this SDK.


## Main SEARS platform
Please refer to our main SEARS platform repository [here](https://github.com/baskargroup/SEARS/).

## Steps to pull data.

0. Copy the `.env` file to the root directory of the project. Update the connection string to use your own MongoDB Atlas connection string. Also update the AWS S3 parameters as per your AWS settings.
1. Install all requirements using `pip3 install -r requirements.txt`
2. Run `python3 mongo_connect.py` to download data from MongoDB to a CSV file. Set `search_criteria` and `output_file_name` in the program file.
3. Run `python3 AWS_Download.py` to download files from AWS S3 to a local directory `./file_fetch/`. All files related to experiments meeting the search criteria will be downloaded.
4. Run your ML model on the downloaded data and files.
