# FreshAir

[![Lint server](https://github.com/petr7555/pv207-freshair/actions/workflows/lint_backend.yml/badge.svg)](https://github.com/petr7555/pv207-freshair/actions/workflows/lint_backend.yml)

## Info

### Process 1 – DAC monitoring
- needs FastAPI server
- uses [IFTTT](https://ifttt.com/my_applets), logged in with Google account `jbpm.pv207@gmail.com`
    - https://maker.ifttt.com/use/qZjWWfvrrfR6ouZCtlnsQ
    - https://github.com/kiegroup/jbpm-work-items/blob/main/ifttt-workitem/src/main/java/org/jbpm/process/workitem/ifttt/IFTTTWorkitemHandler.java
- IFTTT creates an event in a Google Calendar for account `jbpm.pv207@gmail.com`
- an email is sent to `jbpm.pv207@gmail.com` Gmail account
