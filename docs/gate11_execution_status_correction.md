# Gate 11 execution-status correction

## Correction

Earlier status notes treated an empty result from the connector operation
`fetch_commit_workflow_runs` as evidence that the push-triggered Gate 11
workflow had not run.

That inference is invalid. The connector operation explicitly returns
pull-request-triggered workflow runs. Gate 11 is configured for `push` and
`workflow_dispatch`. Therefore an empty connector response does **not**
establish absence of a Gate 11 run.

## Verified facts

- repository default branch: `main`;
- connected identity has admin/push permission;
- workflow exists at
  `.github/workflows/ase20-patchsim-rer.yml`;
- workflow syntax declares both `workflow_dispatch` and a path-filtered
  `push` trigger;
- the primary-artifact URL remains the Zenodo ASE20 release;
- the current chat/container download path cannot retrieve the 43.2 MB archive;
- no quantitative Gate 11 result is claimed until the produced inventory is
  actually retrieved and inspected.

## No-loop rule

Do not create further theory gates merely because CI run visibility is absent.
The next accepted scientific input is one of:

1. the Gate 11 inventory artifact;
2. an extracted local copy of `PATCH-SIM_result.zip`; or
3. another primary APCA artifact whose released data are directly readable.

Until one of those is available, the empirical status is **blocked on artifact
materialization**, not on RER theory.
