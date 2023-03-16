__version__ = "0.0.1"
__appname__ = "Spell Checker"

(
    SUCCESS,
    DIR_ERROR,
    FILE_ERROR,
    JSON_ERROR,
    ID_ERROR,
) = range(5)

ERRORS = {
    DIR_ERROR: "directory error",
    FILE_ERROR: "file error",
    ID_ERROR: "to-do id error",
}
