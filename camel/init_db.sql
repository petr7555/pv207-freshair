CREATE TABLE processes_needing_adjustment
(
    id          INTEGER PRIMARY KEY,
    processName TEXT NOT NULL,
    date        TEXT NOT NULL
);

CREATE TABLE delayed_findings
(
    id          INTEGER PRIMARY KEY,
    findingName TEXT NOT NULL,
    date        TEXT NOT NULL
);
