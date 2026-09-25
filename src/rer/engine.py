"""Exact finite engine for Repair Evidence Resolution.

No external dependencies. Deterministic by construction.
"""
from __future__ import annotations
from dataclasses import dataclass
from itertools import combinations
from typing import Callable, Hashable, Iterable, Mapping, Sequence


@dataclass(frozen=True)
class Repair:
    name: str
    outputs: tuple[Hashable, ...]


def signature(repair: Repair, evidence_indices: Sequence[int]) -> tuple[Hashable, ...]:
    return tuple(repair.outputs[i] for i in evidence_indices)


def evidence_classes(
    repairs: Sequence[Repair], evidence_indices: Sequence[int]
) -> dict[tuple[Hashable, ...], list[Repair]]:
    classes: dict[tuple[Hashable, ...], list[Repair]] = {}
    for r in repairs:
        classes.setdefault(signature(r, evidence_indices), []).append(r)
    return classes


def claim_conflict_witnesses(
    repairs: Sequence[Repair],
    evidence_indices: Sequence[int],
    claim: Callable[[Repair], Hashable],
) -> list[tuple[str, str]]:
    witnesses: list[tuple[str, str]] = []
    for cell in evidence_classes(repairs, evidence_indices).values():
        for a, b in combinations(cell, 2):
            if claim(a) != claim(b):
                witnesses.append((a.name, b.name))
    return witnesses


def rcr(
    repairs: Sequence[Repair],
    evidence_indices: Sequence[int],
    claim: Callable[[Repair], Hashable],
) -> bool:
    return not claim_conflict_witnesses(repairs, evidence_indices, claim)


def claim_boundary_complete(
    universe: Sequence[Repair],
    surrogate: Sequence[Repair],
    evidence_indices: Sequence[int],
    claim: Callable[[Repair], Hashable],
) -> bool:
    surrogate_names = {r.name for r in surrogate}
    for cell in evidence_classes(universe, evidence_indices).values():
        full_values = {claim(r) for r in cell}
        if len(full_values) > 1:
            sampled_values = {claim(r) for r in cell if r.name in surrogate_names}
            if len(sampled_values) <= 1:
                return False
    return True


def claim_resolution_profile(
    repairs: Sequence[Repair],
    evidence_indices: Sequence[int],
    claims: Mapping[str, Callable[[Repair], Hashable]],
) -> dict[str, bool]:
    return {name: rcr(repairs, evidence_indices, fn) for name, fn in claims.items()}
