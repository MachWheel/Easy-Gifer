# coding=utf-8
import logging
from os.path import isfile, join, splitext

from resources.names import IGNORED_CATEGORY, LOG_NAME, OTHER_CATEGORY


class Filter:
    def __init__(self, working_dir, extensions):
        self.log = logging.getLogger(__name__)
        self.working_dir = working_dir
        self.extensions = extensions


    def category_name(self, file) -> str:
        file_extension = str.lower(splitext(file)[1])
        for category, entries in self.extensions.items():
            if file_extension in entries:
                name = category.capitalize()
                return name
        return OTHER_CATEGORY


    def ignored_file(self, file):
        file_path = join(self.working_dir, file)
        file_name = splitext(file)[0]
        return not isfile(file_path) \
               or file_name == LOG_NAME \
               or self.category_name(file) == IGNORED_CATEGORY
