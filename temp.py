from MultipartFormData.Multipart import MultipartFormData

data = {
    "id": 12313123,
    "name": "yhleng"
}

req_str = MultipartFormData.to_form_data(data)
print(req_str)

# result
"""
------WebKitFormBoundary7MA4YWxkTrZu0gW
Content-Disposition: form-data; name="id"

12313123
------WebKitFormBoundary7MA4YWxkTrZu0gW
Content-Disposition: form-data; name="name"

yhleng
------WebKitFormBoundary7MA4YWxkTrZu0gW--
"""
