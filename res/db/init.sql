CREATE TABLE "robot"
(
    "ID"              INTEGER NOT NULL,
    "ipa"             TEXT    NOT NULL,
    "name"            TEXT    NOT NULL,
    "contactPersonID" INTEGER,
    "descr"           TEXT,
    "cost"            INTEGER NOT NULL,
    "runtime"         INTEGER NOT NULL,
    "add_time"        INTEGER,
    "comment"         TEXT,
    PRIMARY KEY ("ID" AUTOINCREMENT)
);

CREATE TABLE "contactPerson"
(
    "ID"         INTEGER NOT NULL,
    "forname"    TEXT    NOT NULL,
    "surname"    TEXT    NOT NULL,
    "department" TEXT    NOT NULL,
    "email"      TEXT    NOT NULL,
    PRIMARY KEY ("ID" AUTOINCREMENT)
);
