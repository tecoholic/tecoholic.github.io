---
title: Backup all the files in a directory to Azure Cloud
date: '2020-12-24T11:53:15'
slug: backup-all-the-files-in-a-directory-to-azure-cloud
categories:
  - Coding
  - Notes
tags:
  - azure
---

I had to copy all the files from the home directory into a Azure Blob container today. All the regular folders without any of the dot files and dot folders.




Azure CLI provides [batch upload functionality](https://docs.microsoft.com/en-us/cli/azure/storage/blob?view=azure-cli-latest#az_storage_blob_upload_batch) to upload folders. But there are two issues I faced:




1. I needed to copy all the folders - and I didn't want to run the command for each folder.
2. I wanted to preserve the folder structure in the container as well.




 After some trial and error I settled on this one liner.





```
for f in */; do az storage blob upload-batch -d container-name/$f -s $f; done;
```



For loop take care of #1 and using the `/$f` takes care of creating corresponding folders to preserve the same folder structure as in my home directory.




This assumes you already have set the AZURE_STORAGE_ACCOUNT and the AZURE_STORAGE_KEY environment variables for authentication.



