from enum import Enum


class ExportBatchesExportType(str, Enum):
    CSV = "csv"
    IMAGES = "images"
    ISO20022 = "iso20022"
    ISO20022_MERGED = "iso20022_merged"
    JSON = "json"
    MERGED = "merged"
    PARSED_FILES = "parsed_files"
    PARSED_VIRTUAL_FILES = "parsed_virtual_files"
    RAW_FILES = "raw_files"
    RAW_VIRTUAL_FILES = "raw_virtual_files"

    def __str__(self) -> str:
        return str(self.value)
