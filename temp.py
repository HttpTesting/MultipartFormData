from MultipartFormData.Multipart import MultipartFormData

data = {
    "id": 12313123,
    "name": "yhleng"
}

req_str = MultipartFormData.to_form_data(data)
print(req_str)