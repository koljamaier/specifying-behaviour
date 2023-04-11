{ pkgs ? import <nixpkgs> {} }:
pkgs.mkShell {
  buildInputs = [
    # rust
    pkgs.rustc
    pkgs.cargo
    # python
    pkgs.python311
    # scala
    pkgs.scala-cli
    # justfile support
    pkgs.just
  ];
}