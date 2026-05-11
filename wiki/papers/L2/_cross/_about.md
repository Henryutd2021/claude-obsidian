---
type: folder-about
title: "About: L2 _cross folder"
updated: 2026-05-11
tags:
  - meta
  - folder-about
status: living
---

# About: `papers/L2/_cross/`

_This folder is currently empty. This `_about.md` explains why and what triggers it filling._

## Purpose

L2 (`applied_flagship`) papers that span 3+ subdomains as primary. Rare in practice: usually a perspective / cross-disciplinary synthesis. Most L2 papers land in a single subdomain folder.

## When it fills

When a Phase 2+ L2 ingest produces a paper with `len(subdomain_primary) >= 3` AND no subdomain is a clear dominant.

## Trigger

`scripts/codex-ingest-paper-L2.sh <KEY> <ADDR> <SLUG> A_deep _cross`.

## Source of truth

[[_meta/subdomain-vocab]] (rules for cross-subdomain papers).
