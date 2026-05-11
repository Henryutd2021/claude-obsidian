---
type: folder-about
title: "About: Parameter bank"
updated: 2026-05-11
tags:
  - meta
  - folder-about
status: living
---

# About: `banks/parameter-bank/`

_This folder is currently empty. This `_about.md` explains why and what triggers it filling._

## Purpose

Parameter values (CAPEX, OPEX, capacity factors, efficiencies, lifetimes, discount rates, learning rates, carbon prices, etc.) extracted from L2-A ingests, supplemented by manual L3 entries. One `.md` per parameter category (e.g. `electrolyzer-capex.md`, `pv-capacity-factor.md`).

## When it fills

When the first L2-A ingest produces a Parameter Card.

## Trigger

An L2-A codex run finishes and the orchestrator merges `bank-candidates.md` parameter rows into this folder. Also: Henry manually adds rows from technical-support (L3) papers.

## Source of truth

[[_meta/routing-rules]] section L2-A row.
