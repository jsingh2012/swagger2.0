import http.client
import mimetypes
from codecs import encode

conn = http.client.HTTPConnection("10.0.2.15", 8080)
dataList = []
boundary = 'wL36Yn8afVp8Ag7AmP8qZ0SA4n1v9T'
dataList.append(encode('--' + boundary))
dataList.append(encode('Content-Disposition: form-data; name=multipages_input;'))

dataList.append(encode('Content-Type: {}'.format('text/plain')))
dataList.append(encode(''))

dataList.append(encode("id pariatur"))
dataList.append(encode('--' + boundary))
dataList.append(encode('Content-Disposition: form-data; name=images; filename={0}'.format('testetest.png')))

fileType = mimetypes.guess_type('/home/omni/Downloads/testetest.png')[0] or 'application/octet-stream'
dataList.append(encode('Content-Type: {}'.format(fileType)))
dataList.append(encode(''))

with open('/home/omni/Downloads/testetest.png', 'rb') as f:
      dataList.append(f.read())
      dataList.append(encode('--' + boundary))
      dataList.append(encode('Content-Disposition: form-data; name=images; filename={0}'.format('nn_no2_0003.png')))

      fileType = mimetypes.guess_type('/home/omni/omni/mega-server/swagger_server/test/assets/nn_no2_0003.png')[0] or 'application/octet-stream'
      dataList.append(encode('Content-Type: {}'.format(fileType)))
      dataList.append(encode(''))

      with open('/home/omni/omni/mega-server/swagger_server/test/assets/nn_no2_0003.png', 'rb') as f:
            dataList.append(f.read())
            dataList.append(encode('--'+boundary+'--'))
            dataList.append(encode(''))
            body = b'\r\n'.join(dataList)
            payload = body
            headers = {
                      'X_Client_Trace_Id': 'aute',
                        'Content-Type': 'multipart/form-data',
                          'Accept': 'application/json',
                            'Content-type': 'multipart/form-data; boundary={}'.format(boundary)
                            }
            conn.request("POST", "//multipages", payload, headers)
            res = conn.getresponse()
            data = res.read()
            print(data.decode("utf-8"))
