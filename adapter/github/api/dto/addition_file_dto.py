import dataclasses


@dataclasses.dataclass(frozen=True)
class AdditionFileDto:
    file_name: str
    raw_url: str

    def get_save_dir(self) -> str:
        return self.file_name.split("/")[0]

    def get_file_ext(self) -> str:
        return self.file_name.split(".")[-1]

    def get_file_name(self) -> str:
        file_path = self.file_name.split(".")[0]
        file_name = file_path.split("/")[-1]
        return file_name

    def get_raw_url(self):
        return self.raw_url
