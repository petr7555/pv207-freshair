DROP TABLE IF EXISTS processes_needing_adjustment;
DROP TABLE IF EXISTS delayed_findings;

CREATE TABLE processes_needing_adjustment
(
    id          INTEGER PRIMARY KEY,
    processName TEXT NOT NULL,
    description TEXT NOT NULL,
    date        TEXT NOT NULL
);

CREATE TABLE delayed_findings
(
    id          INTEGER PRIMARY KEY,
    processName TEXT NOT NULL,
    description TEXT NOT NULL,
    date        TEXT NOT NULL
);
