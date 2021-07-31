import requests
token = ""

file_list = ["d:\\temp\\file.txt", "d:\\temp\\file1.txt", "d:\\temp\\file2.txt", "d:\\temp\\file3.txt", "d:\\temp\\file4.txt"]

# Для создания файлов раскомментировать эту часть
# for newfiles in file_list:
#     my_file = open(newfiles, "w+")
#     my_file.write("Привет, файл " + newfiles)
#     my_file.close()

class YaUploader:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def get_headers(self):
        return {
                'Content-Type': 'application/json',
                'Authorization': 'OAuth '+ token
        }

    def _get_upload_link(self, disk_file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": self.file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        # pprint(response.json())
        return response.json()

    def upload(self):
        href = self._get_upload_link(disk_file_path=self.file_path).get("href")
        response = requests.put(href, data=open(files, 'rb'))
        if response.status_code == 201:
            return print('Файл', filename, ' успешно загружен')
        else:
            return print("ошибка", response.status_code)


if __name__ == '__main__':
    for files in file_list:    #Проходим по списку файлов и получаем ссылки на файлы (files) для использования в функции upload
        filename = files.split('\\')[-1] #Получаем имя файла, чтобы получить для него ссылку для загрузки
        uploader = YaUploader(filename)
        result = uploader.upload()

