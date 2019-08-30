"""
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
class MultipartFormData:
    """Convert the request data to form-data."""

    @staticmethod
    def to_form_data(data, boundary="----WebKitFormBoundary7MA4YWxkTrZu0gW", headers={}):
        """
        Convert the request data to form-data.

        Args:
            data: Request data
            {
                'id': '23139j76h6t15f',
                'name': 'yhleng'
            }
            boundary: Form - the data string segmentation.
            headers: boundary default is not specified.
        Example:
            e.g.
            data_str = MultipartFormData.to_form_data(data) =>

            ------WebKitFormBoundary7MA4YWxkTrZu0gW
            Content-Disposition: form-data; name="id"

            123131313
            ------WebKitFormBoundary7MA4YWxkTrZu0gW
            Content-Disposition: form-data; name="name"

            yhleng
            ------WebKitFormBoundary7MA4YWxkTrZu0gW--     
        """
        # 从headers中提取boundary信息
        if "content-type" in headers:
            fd_val = str(headers["content-type"])
            if "boundary" in fd_val:
                fd_val = fd_val.split(";")[1].strip()
                boundary = fd_val.split("=")[1].strip()
            else:
                raise("multipart/form-data头信息错误，请检查content-type key是否包含boundary")
        # form-data格式定式
        jion_str = '--{}\r\nContent-Disposition: form-data; name="{}"\r\n\r\n{}\r\n'
        end_str = "--{}--".format(boundary)
        args_str = ""

        if not isinstance(data, dict):
            raise("multipart/form-data参数错误，data参数应为dict类型")
        for key, value in data.items():
            args_str = args_str + jion_str.format(boundary, key, value)

        args_str = args_str + end_str.format(boundary)
        args_str = args_str.replace("\'", "\"").replace('False', 'false').replace('True', 'true')
        return args_str


if __name__ == "__main__":
    data = {
        "id": "123131313",
        "name": "yhleng"
    }
    tmp = MultipartFormData.to_form_data(data)
    print(tmp)