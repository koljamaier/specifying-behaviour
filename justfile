set shell := ["zsh", "-cu"]
set dotenv-load := true

_default:
  @just --choose

run-python:
    python3 python/main.py

run-rust:
    cargo run --manifest-path rust/traits/Cargo.toml

run-scala:
    scala-cli run scala/TypeClasses.scala