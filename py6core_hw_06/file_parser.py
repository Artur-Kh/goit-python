import sys
from pathlib import Path

JPEG_IMAGES = []
JPG_IMAGES = []
PNG_IMAGES = []
SVG_IMAGES = []
AVI_VIDEO = []  # добавил
MP4_VIDEO = []  # добавил
MOV_VIDEO = []  # добавил
MKV_VIDEO = []  # добавил
DOC_DOCS = []  # добавил
DOCX_DOCS = []  # добавил
TXT_DOCS = []  # добавил
PDF_DOCS = []  # добавил
XLSX_DOCS = []  # добавил
PPTX_DOCS = []  # добавил
MP3_AUDIO = []
OGG_AUDIO = []  # добавил
WAV_AUDIO = []  # добавил
AMR_AUDIO = []  # добавил

OTHER = []
ARCHIVES = []

REGISTER_EXTENSIONS = {
    'JPEG': JPEG_IMAGES,
    'PNG': PNG_IMAGES,
    'JPG': JPG_IMAGES,
    'SVG': SVG_IMAGES,
    'AVI': AVI_VIDEO,  # добавил
    'MP4': MP4_VIDEO,  # добавил
    'MOV': MOV_VIDEO,  # добавил
    'MKV': MKV_VIDEO,  # добавил
    'DOC': DOC_DOCS,  # добавил
    'DOCX': DOCX_DOCS,  # добавил
    'TXT': TXT_DOCS,  # добавил
    'PDF': PDF_DOCS,  # добавил
    'XLSX': XLSX_DOCS,  # добавил
    'PPTX': PPTX_DOCS,  # добавил
    'MP3': MP3_AUDIO,
    'OGG': OGG_AUDIO,  # добавил
    'WAV': WAV_AUDIO,  # добавил
    'AMR': AMR_AUDIO,  # добавил
    'ZIP': ARCHIVES,
    'GZ': ARCHIVES,  # добавил
    'TAR': ARCHIVES  # добавил
}

FOLDERS = []
EXTENSIONS = set()
UNKNOWN = set()


def get_extension(filename: str) -> str:
    # превращаем расширение файла в название папки .jpg -> JPG
    return Path(filename).suffix[1:].upper()


def scan(folder: Path) -> None:
    for item in folder.iterdir():
        # Если это папка то добавляем ее с список FOLDERS и преходим к следующему элементу папки
        if item.is_dir():
            # проверяем, чтобы папка не была той в которую мы складываем уже файлы
            if item.name not in ('archives', 'video', 'audio', 'documents', 'images', 'OTHER'):
                FOLDERS.append(item)
                #  сканируем эту вложенную папку - рекурсия
                scan(item)
            #  перейти к следующему элементу в сканируемой папке
            continue

        #  Пошла работа с файлом
        ext = get_extension(item.name)  # взять расширение
        fullname = folder / item.name  # взять полный путь к файлу
        if not ext:  # если у файла нет расширения добавить к неизвестным
            OTHER.append(fullname)
        else:
            try:
                # взять список куда положить полный путь к файлу
                container = REGISTER_EXTENSIONS[ext]
                EXTENSIONS.add(ext)
                container.append(fullname)
            except KeyError:
                # Если мы не регистрировали расширение в REGISTER_EXTENSIONS, то добавить в другое
                UNKNOWN.add(ext)
                OTHER.append(fullname)


if __name__ == '__main__':
    folder_for_scan = sys.argv[1]
    print(f'Start in folder {folder_for_scan}')

    scan(Path(folder_for_scan))
    print(f'Images jpeg: {JPEG_IMAGES}')
    print(f'Images jpg: {JPG_IMAGES}')
    print(f'Images svg: {SVG_IMAGES}')
    print(f'Video avi: {AVI_VIDEO}')  # добавил
    print(f'Video mp4: {MP4_VIDEO}')  # добавил
    print(f'Video mov: {MOV_VIDEO}')  # добавил
    print(f'Video mkv: {MKV_VIDEO}')  # добавил
    print(f'Documents doc: {DOC_DOCS}')  # добавил
    print(f'Documents docx: {DOCX_DOCS}')  # добавил
    print(f'Documents txt: {TXT_DOCS}')  # добавил
    print(f'Documents pdf: {PDF_DOCS}')  # добавил
    print(f'Documents xlsx: {XLSX_DOCS}')  # добавил
    print(f'Documents pptx: {PPTX_DOCS}')  # добавил
    print(f'Audio mp3: {MP3_AUDIO}')
    print(f'Audio ogg: {OGG_AUDIO}')  # добавил
    print(f'Audio wav: {WAV_AUDIO}')  # добавил
    print(f'Audio amr: {AMR_AUDIO}')  # добавил
    print(f'Archives: {ARCHIVES}')

    print(f'Types of files in folder: {EXTENSIONS}')
    print(f'Unknown files of types: {UNKNOWN}')

    print(FOLDERS[::-1])
