# SEARS SDK 
The purpose of this SDK is to publish code that will help data scientists to query MongoDB using python so as to bulk download data and files directly from the SEARS backend for aggregated analysis. Case studies 6.1 and 6.2 from our main paper were conducted using this SDK.


## Main SEARS platform
Please refer to our main SEARS platform repository [here](https://github.com/baskargroup/SEARS/).

## Steps to pull data.

0. Copy the `.env` file to the root directory of the project. Update the connection string to use your own MongoDB Atlas connection string. Also update the AWS S3 parameters as per your AWS settings.
1. Install all requirements using `pip3 install -r requirements.txt`
2. Run `python3 mongo_connect.py` to download data from MongoDB to a CSV file. Set `search_criteria` and `output_file_name` in the program file. Please note that `mongo_connect.py` has been customized to access our own schema in SEARS. As you adapt SEARS to your own needs, you may need to modify the code to suit your schema. Therefore please use this file as a reference to write your own MongoDB query code. We encourage use of AI agents to achieve this goal.
3. Run `python3 AWS_Download.py` to download files from AWS S3 to a local directory `./file_fetch/`. All files related to experiments meeting the search criteria will be downloaded.
4. Run your ML model on the downloaded data and files.


### Process to automate the upload of experiment data to MongoDB

#Steps

1. Notice the folder ```./uploads``` in the root directory of the project. This folder is used to upload data to MongoDB.
2. Drop data for an experiment in the folder ```./uploads```. The data should be in the form of a JSON file. 
3. Run the program `python3 auto_upload.py` to upload the data to MongoDB. The program will automatically upload the data to the MongoDB collection `productData`.
