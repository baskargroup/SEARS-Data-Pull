from dotenv import load_dotenv, find_dotenv
import boto3
import os
import errno

if __name__ == '__main__':
    # Load .env file
    load_dotenv(find_dotenv())

    with open('./file_fetch/payload.txt', 'r') as file:
        folder_names = file.readlines()
        for folder_name in folder_names:
            folder_name = folder_name.strip()
            print(f'Experiment ID: {folder_name}')

            # Create a directory with the folder name
            os.makedirs('./file_fetch/'+folder_name, exist_ok=True)

            # Download from Digital Ocean
            try:
                session = boto3.session.Session()
                s3 = session.client('s3',
                                    endpoint_url=os.environ.get('DO_URI'),
                                    aws_access_key_id=os.environ.get('DO_KEY'),
                                    aws_secret_access_key=os.environ.get('DO_SECRET'))

                # return client
                # List all files in a bucket with a specific prefix
                response = s3.list_objects_v2(Bucket=os.environ.get(
                    'DO_SPACE_NAME'), Prefix=folder_name)
                # print(response)

                local_download_path = './file_fetch/'+folder_name

                # Download each file
                if 'Contents' in response:
                    for obj in response['Contents']:
                        file_key = obj['Key']

                        local_file_path = os.path.join(
                            local_download_path, os.path.relpath(file_key, folder_name))

                        if 'Preanneal' in file_key or 'Postanneal' in file_key or 'Postdope' in file_key:
                            print(
                                '==========================================================================')
                            print('file_key:', file_key.split('/')[-1])
                            print(
                                '==========================================================================')
                            s3.download_file(os.environ.get(
                                'DO_SPACE_NAME'), file_key, './file_fetch/' + folder_name + '/' + file_key.split('/')[-1])

            except Exception as e:
                if e.errno == errno.EBUSY:
                    print(
                        f"Error: Device or resource busy while accessing {local_file_path}")
                else:
                    print(e)

            finally:
                s3.close()
                print("\nDownload complete.")
