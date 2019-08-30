# Multipartformdata
Convert the request data to form-data.

### 
	Convert the request data to form-data.

	data:
		{
			'id': '23139j76h6t15f',
			'name': 'yhleng'
		}
	Example:
		from MultipartFormData.Multipart import MultipartFormData

		e.g.
		data_str = MultipartFormData.to_form_data(data) =>
		------WebKitFormBoundary7MA4YWxkTrZu0gW
		Content-Disposition: form-data; name="id"

		123131313
		------WebKitFormBoundary7MA4YWxkTrZu0gW
		Content-Disposition: form-data; name="name"

		yhleng
		------WebKitFormBoundary7MA4YWxkTrZu0gW--


		e.g.
		headers = {
			"content-type": "multipart/form-data; boundary=1q2w3e4r5t67u9i8u7y6t"
		}
		data_str = MultipartFormData.to_form_data(data, headers=headers)
		--1q2w3e4r5t67u9i8u7y6t
		Content-Disposition: form-data; name="id"

		123131313
		--1q2w3e4r5t67u9i8u7y6t
		Content-Disposition: form-data; name="name"

		yhleng
		--1q2w3e4r5t67u9i8u7y6t--

	"""






  
