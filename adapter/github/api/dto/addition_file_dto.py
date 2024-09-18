import dataclasses


@dataclasses.dataclass(frozen=True)
class AdditionFileDto:
    file_name: str
    raw_url: str

    def get_save_dir(self) -> str:
        return self.file_name.split("/")[0]

    def get_file_ext(self) -> str:
        return self.file_name.split(".")[-1]
