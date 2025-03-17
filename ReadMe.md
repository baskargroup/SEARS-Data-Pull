### SEARS SDK to Query MongoDB using Python to Download Data and Files from SEARS Backend.

#Steps

0. Copy the `.env` file to the root directory of the project. Update the connection string to use your own MongoDB Atlas connection string. Also update the AWS S3 parameters as per your AWS settings.
1. Install all requirements using `pip3 install -r requirements.txt`
2. Run `python3 mongo_connect.py` to download data from MongoDB to a CSV file. Set `search_criteria` and `output_file_name` in the program file.
3. Run `python3 AWS_Download.py` to download files from AWS S3 to a local directory `./file_fetch/`. All files related to experiments meeting the search criteria will be downloaded.
4. Run your ML model on the downloaded data and files.


### Process to automate the upload of experiment data to MongoDB

#Steps

1. Notice the folder ```./uploads``` in the root directory of the project. This folder is used to upload data to MongoDB.
2. Drop data for an experiment in the folder ```./uploads```. The data should be in the form of a JSON file. 
3. Run the program `python3 auto_upload.py` to upload the data to MongoDB. The program will automatically upload the data to the MongoDB collection `productData`.
