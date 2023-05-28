## Prerequisites

- install **JBang**: https://www.jbang.dev/download/
- install **Camel** using JBang: `jbang app install camel@apache/camel`
	- verify by running `camel version`
- install **sqlite3**
	- verify by running `sqlite3 --version`

## How to run

- Start
  with `camel run integration.yaml application.properties --deps=org.xerial:sqlite-jdbc:3.41.2.1 --dev --port=8081`
  or with `camel run integration.yaml --deps=org.xerial:sqlite-jdbc:3.41.2.1 --dev` since `application.properties` are
  picked up automatically.
- Initialize database: `sqlite3 data.db < init_db.sql`

## Available endpoints

| Endpoint                            | Command                                                                                                                                                                                      | Response                                                                                               | Side-effect                                                 |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|-------------------------------------------------------------|
| Health check                        | `curl -X GET http://0.0.0.0:8081/health`                                                                                                                                                     | `Camel OK`                                                                                             | -                                                           |
| Insert process needing adjustment   | `curl -X POST http://0.0.0.0:8081/kpi/processes-needing-adjustment -H "Content-Type: application/json" -d "{\"processName\":\"Logistics\",\"description\":\"Logistics needs improvement\"}"` | `Process added successfully`                                                                           | Inserts process name, description and current date into DB. |
| Select processes needing adjustment | `curl -X GET http://0.0.0.0:8081/kpi/processes-needing-adjustment`                                                                                                                           | `[{"id":1,"processName":"Logistics","description":"Logistics needs improvement","date":"2023-05-28"}]` | -                                                           |
| Insert delayed finding              | `curl -X POST http://0.0.0.0:8081/kpi/delayed-findings -H "Content-Type: application/json" -d "{\"processName\":\"Logistics\",\"description\":\"Logistics needs improvement\"}"`             | `Delayed finding added successfully`                                                                   | Inserts process name, description and current date into DB. |
| Select delayed findings             | `curl -X GET http://0.0.0.0:8081/kpi/delayed-findings`                                                                                                                                       | `[{"id":1,"processName":"Logistics","description":"Logistics needs improvement","date":"2023-05-28"}]` | -                                                           |
