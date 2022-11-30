import asposepdfcloud 
from asposepdfcloud.apis.pdf_api import PdfApi



	# Get your ClientId and ClientSecret from https://dashboard.aspose.cloud (free registration required).
pdf_api_client = asposepdfcloud.ApiClient('MY_CLIENT_ID', 'MY_CLIENT_SECRET')

pdf_api = PdfApi(pdf_api_client)
filename = 'foo.pdf'
remote_name = 'foo.pdf'
output_file= 'foo.xml'
#upload PDF file to storage
pdf_api.upload_file(remote_name,filename)
#Covert PDF to XML and save in storage
response=pdf_api.put_pdf_in_storage_to_xml(remote_name,output_file)
print(response)

# hata veriyor deniyemedim. hatanın çözümünü bulamadım.