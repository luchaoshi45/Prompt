from .WHERE import WHERE
from .SELECT import SELECT
from .AND import AND
from .OR import OR
from .ORDER_BY import ORDER_BY
from .INSERT_INTO import INSERT_INTO
from .UPDATE import UPDATE
from .DELETE import DELETE
from .SELECT_TOP import SELECT_TOP
from .LIKE import LIKE
from .IN import IN
from .BETWEEN import BETWEEN
from .JOIN import JOIN
from .CREATE_DATABASE import CREATE_DATABASE
from .CREATE_TABLE import CREATE_TABLE
from .NOT_NULL import NOT_NULL
from .UNIQUE import UNIQUE
from .PRIMARY_KEY import PRIMARY_KEY
from .FOREIGN_KEY import FOREIGN_KEY
from .CHECK import CHECK
from .DEFAULT import DEFAULT
from .CREATE_INDEX import CREATE_INDEX
from .DROP import DROP
from .ALTER import ALTER
from .NULL import NULL
from .SET import SET
from .GROUP_BY import GROUP_BY


GRAMMAR = {
    "WHERE": WHERE,
    "SELECT TOP": SELECT_TOP,
    "SELECT": SELECT,
    "AND": AND,
    "OR": OR,
    "ORDER BY": ORDER_BY,
    "INSERT INTO": INSERT_INTO,
    "UPDATE": UPDATE,
    "DELETE": DELETE,
    "LIKE": LIKE,
    "IN": IN,
    "BETWEEN": BETWEEN,
    "JOIN": JOIN,
    "CREATE DATABASE": CREATE_DATABASE,
    "CREATE TABLE": CREATE_TABLE,
    "NOT NULL": NOT_NULL,
    "UNIQUE": UNIQUE,
    "PRIMARY KEY": PRIMARY_KEY,
    "FOREIGN KEY": FOREIGN_KEY,
    "CHECK": CHECK,
    "DEFAULT": DEFAULT,
    "CREATE INDEX": CREATE_INDEX,
    "DROP": DROP,
    "ALTER": ALTER,
    "SET": SET,
    "GROUP BY": GROUP_BY,
}