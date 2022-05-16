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
dataList.append(encode('Content-Disposition: form-data; name=images; filename={0}'.format('testetest2.png')))

fileType = mimetypes.guess_type('/home/omni/Downloads/images/testetest2.png')[0] or 'application/octet-stream'
dataList.append(encode('Content-Type: {}'.format(fileType)))
dataList.append(encode(''))

with open('/home/omni/Downloads/images/testetest2.png', 'rb') as f:
      dataList.append(f.read())
      dataList.append(encode('--' + boundary))
      dataList.append(encode('Content-Disposition: form-data; name=images; filename={0}'.format('pic5.jpeg')))

      fileType = mimetypes.guess_type('/home/omni/Downloads/images/pic5.jpeg')[0] or 'application/octet-stream'
      dataList.append(encode('Content-Type: {}'.format(fileType)))
      dataList.append(encode(''))

      with open('/home/omni/Downloads/images/pic5.jpeg', 'rb') as f:
            dataList.append(f.read())
            dataList.append(encode('--' + boundary))
            dataList.append(encode('Content-Disposition: form-data; name=images; filename={0}'.format('pic4.jpeg')))

            fileType = mimetypes.guess_type('/home/omni/Downloads/images/pic4.jpeg')[0] or 'application/octet-stream'
            dataList.append(encode('Content-Type: {}'.format(fileType)))
            dataList.append(encode(''))

            with open('/home/omni/Downloads/images/pic4.jpeg', 'rb') as f:
                  dataList.append(f.read())
                  dataList.append(encode('--' + boundary))
                  dataList.append(encode('Content-Disposition: form-data; name=images; filename={0}'.format('pic3.jpeg')))

                  fileType = mimetypes.guess_type('/home/omni/Downloads/images/pic3.jpeg')[0] or 'application/octet-stream'
                  dataList.append(encode('Content-Type: {}'.format(fileType)))
                  dataList.append(encode(''))

                  with open('/home/omni/Downloads/images/pic3.jpeg', 'rb') as f:
                        dataList.append(f.read())
                        dataList.append(encode('--' + boundary))
                        dataList.append(encode('Content-Disposition: form-data; name=images; filename={0}'.format('pic2.jpeg')))

                        fileType = mimetypes.guess_type('/home/omni/Downloads/images/pic2.jpeg')[0] or 'application/octet-stream'
                        dataList.append(encode('Content-Type: {}'.format(fileType)))
                        dataList.append(encode(''))

                        with open('/home/omni/Downloads/images/pic2.jpeg', 'rb') as f:
                              dataList.append(f.read())
                              dataList.append(encode('--' + boundary))
                              dataList.append(encode('Content-Disposition: form-data; name=images; filename={0}'.format('pic1.jpeg')))

                              fileType = mimetypes.guess_type('/home/omni/Downloads/images/pic1.jpeg')[0] or 'application/octet-stream'
                              dataList.append(encode('Content-Type: {}'.format(fileType)))
                              dataList.append(encode(''))

                              with open('/home/omni/Downloads/images/pic1.jpeg', 'rb') as f:
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
